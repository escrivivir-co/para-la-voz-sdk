from __future__ import annotations

import argparse
import os
import site
import subprocess
import sys
import time
from pathlib import Path


def ts() -> str:
    return time.strftime("%H:%M:%S")


def log(message: str) -> None:
    print(f"[{ts()}] {message}", flush=True)


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


def maybe_print_nvidia_smi() -> None:
    try:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=name,memory.total,driver_version,compute_cap",
                "--format=csv,noheader",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        log("nvidia-smi not available")
        return

    output = (result.stdout or result.stderr).strip()
    if output:
        log(f"nvidia-smi: {output}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Probe faster-whisper GPU on Windows")
    parser.add_argument("audio", help="Audio/video file to probe")
    parser.add_argument("--model", default="tiny", help="Whisper model size")
    parser.add_argument("--language", default="es", help="Language code")
    parser.add_argument("--compute-type", default="int8", help="CUDA compute type")
    parser.add_argument("--seconds", type=float, default=30.0, help="Seconds to transcribe")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    log("=== GPU PROBE START ===")
    if sys.platform == "win32":
        added = bootstrap_windows_nvidia_runtime()
        if added:
            log("Added DLL directories:")
            for path in added:
                log(f"  {path}")
        else:
            log("No DLL directories added")

    maybe_print_nvidia_smi()

    import ctranslate2
    from faster_whisper import WhisperModel

    log(f"CTranslate2 {ctranslate2.__version__}")
    log(f"CPU compute types: {sorted(ctranslate2.get_supported_compute_types('cpu'))}")
    try:
        cuda_types = sorted(ctranslate2.get_supported_compute_types("cuda"))
        log(f"CUDA compute types: {cuda_types}")
    except Exception as exc:
        log(f"CUDA probe failed: {exc}")
        return 1

    t0 = time.perf_counter()
    log(f"Loading model {args.model} on cuda ({args.compute_type})")
    try:
        model = WhisperModel(args.model, device="cuda", compute_type=args.compute_type)
    except Exception as exc:
        log(f"Model load failed: {exc}")
        log("If the error mentions cublas64_12.dll or cudnn64_9.dll, install:")
        log("  python -m pip install --user nvidia-cublas-cu12 nvidia-cudnn-cu12")
        return 1
    load_seconds = time.perf_counter() - t0
    log(f"Model loaded in {load_seconds:.2f}s")

    clip_end = max(1.0, args.seconds)
    log(f"Transcribing first {clip_end:.0f}s from {args.audio}")
    t1 = time.perf_counter()
    try:
        segments, info = model.transcribe(
            args.audio,
            language=args.language,
            beam_size=5,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500),
            clip_timestamps=[0.0, clip_end],
            condition_on_previous_text=False,
        )
        count = 0
        for segment in segments:
            count += 1
            if count <= 5:
                log(
                    f"[{segment.start:.1f}-{segment.end:.1f}] "
                    f"{segment.avg_logprob:.2f} {segment.text.strip()}"
                )
        infer_seconds = time.perf_counter() - t1
    except Exception as exc:
        log(f"Transcription failed: {exc}")
        return 1

    log(
        f"Done: language={info.language} prob={info.language_probability:.2f} "
        f"segments={count} infer={infer_seconds:.2f}s"
    )
    log("=== GPU PROBE DONE ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
