from __future__ import annotations

import argparse
import json
import os
import site
import sys
import time
from pathlib import Path
from typing import Any

from faster_whisper import WhisperModel


def ts() -> str:
    return time.strftime("%H:%M:%S")


def log(message: str) -> None:
    print(f"[{ts()}] {message}", flush=True)


def bootstrap_windows_nvidia_runtime() -> list[str]:
    if sys.platform != "win32":
        return []

    candidates: list[Path] = []
    user_site = Path(site.getusersitepackages())
    candidates.extend([
        user_site / "nvidia" / "cublas" / "bin",
        user_site / "nvidia" / "cudnn" / "bin",
    ])

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AlephScript Escribiente faster-whisper queue worker")
    parser.add_argument("--inbox-root", default=os.environ.get("ESCRIBIENTE_INBOX", ""), help="Root inbox directory")
    parser.add_argument("--outbox-root", default=os.environ.get("ESCRIBIENTE_OUTBOX", ""), help="Root outbox directory")
    parser.add_argument("--model", default=os.environ.get("ESCRIBIENTE_MODEL", "small"), help="Default Whisper model")
    parser.add_argument("--device", default=os.environ.get("ESCRIBIENTE_DEVICE", "cpu"), help="cpu | cuda | auto")
    parser.add_argument("--compute-type", default=os.environ.get("ESCRIBIENTE_COMPUTE_TYPE", "int8"), help="Compute type")
    parser.add_argument("--language", default=os.environ.get("ESCRIBIENTE_LANGUAGE", "es"), help="Language code")
    parser.add_argument("--beam-size", type=int, default=int(os.environ.get("ESCRIBIENTE_BEAM_SIZE", "5")), help="Beam size")
    parser.add_argument("--poll-interval", type=float, default=float(os.environ.get("ESCRIBIENTE_POLL_INTERVAL", "1.5")), help="Polling interval in seconds")
    parser.add_argument("--once", action="store_true", help="Process the queue once and exit")
    return parser.parse_args()


def list_job_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(
        file_path
        for file_path in root.rglob("*.job.json")
        if not file_path.name.endswith(".done.job.json") and not file_path.name.endswith(".failed.job.json")
    )


def confidence(avg_logprob: float) -> str:
    if avg_logprob >= -0.5:
        return "HIGH"
    if avg_logprob >= -1.0:
        return "OK"
    return "LOW"


class ModelCache:
    def __init__(self) -> None:
        self.model: WhisperModel | None = None
        self.model_name: str | None = None
        self.device: str | None = None
        self.compute_type: str | None = None

    def get(self, model_name: str, device: str, compute_type: str) -> WhisperModel:
        if device == "auto":
            device = "cuda" if self._cuda_available() else "cpu"
        if device in {"cuda", "auto"} and sys.platform == "win32":
            bootstrap_windows_nvidia_runtime()

        if (
            self.model is None
            or self.model_name != model_name
            or self.device != device
            or self.compute_type != compute_type
        ):
            log(f"Loading model={model_name} device={device} compute_type={compute_type}")
            self.model = WhisperModel(model_name, device=device, compute_type=compute_type)
            self.model_name = model_name
            self.device = device
            self.compute_type = compute_type
        return self.model

    @staticmethod
    def _cuda_available() -> bool:
        try:
            import ctranslate2  # type: ignore

            ctranslate2.get_supported_compute_types("cuda")
            return True
        except Exception:
            return False


def load_json(file_path: Path) -> dict[str, Any]:
    return json.loads(file_path.read_text(encoding="utf-8"))


def write_json(file_path: Path, payload: dict[str, Any]) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def process_job(job_file: Path, outbox_root: Path, defaults: argparse.Namespace, cache: ModelCache) -> None:
    processing_file = job_file.with_name(job_file.name.replace(".job.json", ".processing.json"))
    try:
        job_file.rename(processing_file)
    except OSError:
        return

    try:
        job = load_json(processing_file)
        session_id = str(job["sessionId"])
        chunk_id = str(job["chunkId"])
        outbox_dir = outbox_root / session_id
        result_path = outbox_dir / f"{chunk_id}.result.json"
        error_path = outbox_dir / f"{chunk_id}.error.json"

        if result_path.exists():
            processing_file.rename(processing_file.with_name(processing_file.name.replace(".processing.json", ".done.json")))
            return

        model_name = str(job.get("model") or defaults.model)
        device = str(job.get("device") or defaults.device)
        compute_type = str(job.get("computeType") or defaults.compute_type)
        language = str(job.get("language") or defaults.language)
        beam_size = int(job.get("beamSize") or defaults.beam_size)

        model = cache.get(model_name, device, compute_type)

        audio_path = str(job["audioPath"])
        t0 = time.perf_counter()
        segments, info = model.transcribe(
            audio_path,
            language=language,
            beam_size=beam_size,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500),
            condition_on_previous_text=False,
        )
        processing_seconds = time.perf_counter() - t0

        serialized_segments: list[dict[str, Any]] = []
        text_parts: list[str] = []
        for segment in segments:
            clean_text = segment.text.strip()
            text_parts.append(clean_text)
            serialized_segments.append(
                {
                    "start": float(segment.start) + float(job.get("startSec", 0.0)),
                    "end": float(segment.end) + float(job.get("startSec", 0.0)),
                    "text": clean_text,
                    "avgLogprob": float(segment.avg_logprob),
                    "confidence": confidence(float(segment.avg_logprob)),
                }
            )

        payload: dict[str, Any] = {
            "sessionId": session_id,
            "sessionDir": job["sessionDir"],
            "chunkId": chunk_id,
            "chunkIndex": int(job.get("chunkIndex", 0)),
            "audioPath": audio_path,
            "source": job.get("source", "mixed"),
            "startSec": float(job.get("startSec", 0.0)),
            "endSec": float(job.get("endSec", 0.0)),
            "language": info.language,
            "languageProbability": float(info.language_probability),
            "text": " ".join(part for part in text_parts if part).strip(),
            "segments": serialized_segments,
            "processingSeconds": processing_seconds,
            "model": model_name,
            "device": cache.device,
            "computeType": cache.compute_type,
            "createdAt": job.get("createdAt"),
            "completedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "originalFileName": job.get("originalFileName"),
            "mimeType": job.get("mimeType"),
        }

        write_json(result_path, payload)
        done_file = processing_file.with_name(processing_file.name.replace(".processing.json", ".done.json"))
        processing_file.rename(done_file)
        log(f"Processed {chunk_id} ({processing_seconds:.2f}s, lang={info.language}, prob={info.language_probability:.2f})")
    except Exception as exc:
        try:
            job = load_json(processing_file)
        except Exception:
            job = {"sessionId": "unknown", "chunkId": processing_file.stem}

        error_payload = {
            "sessionId": job.get("sessionId", "unknown"),
            "chunkId": job.get("chunkId", processing_file.stem),
            "error": str(exc),
            "failedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "audioPath": job.get("audioPath"),
        }
        error_path = outbox_root / str(error_payload["sessionId"]) / f"{error_payload['chunkId']}.error.json"
        write_json(error_path, error_payload)
        failed_file = processing_file.with_name(processing_file.name.replace(".processing.json", ".failed.json"))
        try:
            processing_file.rename(failed_file)
        except OSError:
            pass
        log(f"Failed {error_payload['chunkId']}: {exc}")


def main() -> int:
    args = parse_args()
    inbox_root = Path(args.inbox_root).expanduser().resolve()
    outbox_root = Path(args.outbox_root).expanduser().resolve()
    inbox_root.mkdir(parents=True, exist_ok=True)
    outbox_root.mkdir(parents=True, exist_ok=True)

    if sys.platform == "win32" and args.device in {"cuda", "auto"}:
        added = bootstrap_windows_nvidia_runtime()
        if added:
            log("Added DLL directories:")
            for directory in added:
                log(f"  {directory}")

    log(f"Escribiente worker inbox={inbox_root}")
    log(f"Escribiente worker outbox={outbox_root}")
    cache = ModelCache()

    while True:
        job_files = list_job_files(inbox_root)
        if job_files:
            for job_file in job_files:
                process_job(job_file, outbox_root, args, cache)
        elif args.once:
            break

        if args.once:
            break
        time.sleep(max(0.25, args.poll_interval))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
