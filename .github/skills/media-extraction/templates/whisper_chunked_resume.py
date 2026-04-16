from __future__ import annotations

import argparse
import json
import os
import site
import sys
import time
from pathlib import Path

import av
from faster_whisper import WhisperModel


def ts() -> str:
    return time.strftime("%H:%M:%S")


def log(message: str) -> None:
    print(f"[{ts()}] {message}", flush=True)


def hhmmss(seconds: float) -> str:
    total = int(seconds)
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def bootstrap_windows_nvidia_runtime() -> list[str]:
    if sys.platform != "win32":
        return []

    candidates: list[Path] = []
    user_site = Path(site.getusersitepackages())
    candidates.extend(
        [
            user_site / "nvidia" / "cublas" / "bin",
            user_site / "nvidia" / "cudnn" / "bin",
        ]
    )

    for env_name, env_value in sorted(os.environ.items()):
        if env_name.startswith("CUDA_PATH") and env_value:
            candidates.append(Path(env_value) / "bin")

    added: list[str] = []
    seen: set[str] = set()
    for path in candidates:
        key = str(path).lower()
        if key in seen or not path.exists():
            continue
        seen.add(key)
        try:
            os.add_dll_directory(str(path))
        except (AttributeError, FileNotFoundError, OSError):
            pass
        os.environ["PATH"] = str(path) + os.pathsep + os.environ.get("PATH", "")
        added.append(str(path))

    return added


def audio_duration_seconds(audio_path: Path) -> float:
    with av.open(str(audio_path)) as container:
        if container.duration is None:
            raise RuntimeError("Audio duration is not available; pass --end-seconds explicitly")
        return container.duration / 1_000_000.0


def load_state(state_path: Path) -> dict:
    if not state_path.exists():
        return {}
    return json.loads(state_path.read_text(encoding="utf-8"))


def save_state(state_path: Path, payload: dict) -> None:
    state_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Chunked faster-whisper transcription with resume support")
    parser.add_argument("audio", help="Audio or video file to transcribe")
    parser.add_argument("--tag", required=True, help="Logical tag used in logs and headers")
    parser.add_argument("--model", default="small", help="Whisper model size")
    parser.add_argument("--device", default="cpu", choices=["cpu", "cuda", "auto"], help="Execution device")
    parser.add_argument("--compute-type", default="int8", help="Compute type for the selected device")
    parser.add_argument("--language", default="es", help="Language code")
    parser.add_argument("--beam-size", type=int, default=5, help="Beam size")
    parser.add_argument("--chunk-seconds", type=float, default=60.0, help="Chunk size in seconds")
    parser.add_argument("--start-seconds", type=float, default=0.0, help="Initial start offset")
    parser.add_argument("--end-seconds", type=float, default=None, help="Optional end offset")
    parser.add_argument("--output", required=True, help="Transcript output path")
    parser.add_argument("--state", required=True, help="JSON state path for resume")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    audio_path = Path(args.audio)
    output_path = Path(args.output)
    state_path = Path(args.state)

    if sys.platform == "win32" and args.device in {"cuda", "auto"}:
        added = bootstrap_windows_nvidia_runtime()
        if added:
            log("Added DLL directories:")
            for path in added:
                log(f"  {path}")

    total_seconds = args.end_seconds
    if total_seconds is None:
        total_seconds = audio_duration_seconds(audio_path)

    state = load_state(state_path)
    next_start = max(args.start_seconds, float(state.get("next_start", args.start_seconds)))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.parent.mkdir(parents=True, exist_ok=True)

    mode = "a" if output_path.exists() and next_start > args.start_seconds else "w"
    log(f"=== TRANSCRIPTION START {args.tag} ===")
    log(f"Audio: {audio_path}")
    log(f"Window: {hhmmss(next_start)} -> {hhmmss(total_seconds)}")
    log(f"Model: {args.model} on {args.device} ({args.compute_type})")

    t0 = time.perf_counter()
    model = WhisperModel(args.model, device=args.device, compute_type=args.compute_type)
    load_seconds = time.perf_counter() - t0
    log(f"Model loaded in {load_seconds:.2f}s")

    with output_path.open(mode, encoding="utf-8") as transcript:
        if mode == "w":
            transcript.write(f"# {args.tag}\n")
            transcript.write(f"# audio={audio_path}\n")
            transcript.write(
                f"# model={args.model} device={args.device} compute_type={args.compute_type} "
                f"chunk_seconds={args.chunk_seconds}\n\n"
            )

        chunk_index = int(state.get("completed_chunks", 0))
        while next_start < total_seconds:
            chunk_index += 1
            chunk_end = min(next_start + args.chunk_seconds, total_seconds)
            log(f"Chunk {chunk_index}: {hhmmss(next_start)} -> {hhmmss(chunk_end)}")
            t1 = time.perf_counter()

            segments, info = model.transcribe(
                str(audio_path),
                language=args.language,
                beam_size=args.beam_size,
                vad_filter=True,
                vad_parameters=dict(min_silence_duration_ms=500),
                clip_timestamps=[next_start, chunk_end],
                condition_on_previous_text=False,
            )

            segment_count = 0
            transcript.write(f"## chunk {chunk_index} {hhmmss(next_start)}-{hhmmss(chunk_end)}\n")
            for segment in segments:
                segment_count += 1
                abs_start = next_start + float(segment.start)
                abs_end = next_start + float(segment.end)
                if segment.avg_logprob >= -0.5:
                    confidence = "HIGH"
                elif segment.avg_logprob >= -1.0:
                    confidence = "OK"
                else:
                    confidence = "LOW"
                transcript.write(
                    f"[{abs_start:.1f}-{abs_end:.1f}] ({confidence} {segment.avg_logprob:.2f}) "
                    f"{segment.text.strip()}\n"
                )
            transcript.write("\n")
            transcript.flush()

            chunk_seconds = time.perf_counter() - t1
            log(
                f"Chunk {chunk_index} done: segments={segment_count} "
                f"language={info.language} prob={info.language_probability:.2f} "
                f"time={chunk_seconds:.2f}s"
            )

            next_start = chunk_end
            save_state(
                state_path,
                {
                    "tag": args.tag,
                    "audio": str(audio_path),
                    "model": args.model,
                    "device": args.device,
                    "compute_type": args.compute_type,
                    "language": args.language,
                    "beam_size": args.beam_size,
                    "chunk_seconds": args.chunk_seconds,
                    "next_start": next_start,
                    "completed_chunks": chunk_index,
                    "load_seconds": load_seconds,
                    "updated_at": ts(),
                },
            )

    log(f"Transcript: {output_path}")
    log(f"State: {state_path}")
    log(f"=== TRANSCRIPTION DONE {args.tag} ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
