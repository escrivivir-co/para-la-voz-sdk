from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import site
import subprocess
import sys
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Escribiente environment precheck")
    parser.add_argument("--sessions-root", default=os.environ.get("ESCRIBIENTE_SESSIONS_ROOT", ""))
    parser.add_argument("--queue-root", default=os.environ.get("ESCRIBIENTE_QUEUE_ROOT", ""))
    parser.add_argument("--ffmpeg-command", default=os.environ.get("ESCRIBIENTE_FFMPEG", "ffmpeg"))
    return parser.parse_args()


def total_ram_gib() -> float | None:
    if sys.platform == "win32":
        import ctypes

        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]

        memory_status = MEMORYSTATUSEX()
        memory_status.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory_status)):
            return round(memory_status.ullTotalPhys / (1024 ** 3), 2)
        return None

    try:
        pages = os.sysconf("SC_PHYS_PAGES")
        page_size = os.sysconf("SC_PAGE_SIZE")
        return round((pages * page_size) / (1024 ** 3), 2)
    except (ValueError, OSError, AttributeError):
        return None


def run_nvidia_smi() -> dict[str, Any]:
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
        return {"available": False, "raw": None}

    output = (result.stdout or result.stderr).strip()
    if not output:
        return {"available": False, "raw": None}

    first_line = output.splitlines()[0]
    parts = [part.strip() for part in first_line.split(",")]
    memory_total = None
    if len(parts) > 1:
        memory_digits = "".join(ch for ch in parts[1] if ch.isdigit() or ch == ".")
        if memory_digits:
            memory_total = float(memory_digits)

    return {
        "available": result.returncode == 0,
        "raw": output,
        "name": parts[0] if parts else None,
        "memoryMiB": memory_total,
        "driver": parts[2] if len(parts) > 2 else None,
        "computeCapability": parts[3] if len(parts) > 3 else None,
    }


def ctranslate2_info() -> dict[str, Any]:
    try:
        import ctranslate2  # type: ignore

        cpu_types = sorted(ctranslate2.get_supported_compute_types("cpu"))
        try:
            cuda_types = sorted(ctranslate2.get_supported_compute_types("cuda"))
        except Exception as exc:
            cuda_types = []
            return {
                "version": ctranslate2.__version__,
                "cpuTypes": cpu_types,
                "cudaTypes": cuda_types,
                "cudaError": str(exc),
            }

        return {
            "version": ctranslate2.__version__,
            "cpuTypes": cpu_types,
            "cudaTypes": cuda_types,
        }
    except Exception as exc:
        return {
            "version": None,
            "cpuTypes": [],
            "cudaTypes": [],
            "error": str(exc),
        }


def recommended_profile(ram_gib: float | None, gpu: dict[str, Any], ct2: dict[str, Any]) -> tuple[str, int, str, str, list[str]]:
    warnings: list[str] = []
    gpu_available = bool(gpu.get("available")) and bool(ct2.get("cudaTypes"))

    if gpu_available:
        memory_mib = float(gpu.get("memoryMiB") or 0)
        if memory_mib >= 12000:
            return ("small", 90, "cuda", "int8_float32", warnings)
        if memory_mib >= 6000:
            return ("small", 60, "cuda", "int8_float32", warnings)
        warnings.append("GPU detectada pero con poca VRAM: usar chunks conservadores.")
        return ("base", 45, "cuda", "int8_float32", warnings)

    if ram_gib is None:
        warnings.append("No pude leer la RAM total del sistema; uso perfil CPU conservador.")
        return ("base", 30, "cpu", "int8", warnings)

    if ram_gib < 12:
        warnings.append("RAM ajustada: conviene usar modelo base y chunks cortos.")
        return ("base", 20, "cpu", "int8", warnings)
    if ram_gib < 24:
        return ("small", 45, "cpu", "int8", warnings)
    return ("small", 60, "cpu", "int8", warnings)


def main() -> int:
    args = parse_args()
    sessions_root = Path(args.sessions_root).expanduser() if args.sessions_root else None
    queue_root = Path(args.queue_root).expanduser() if args.queue_root else None

    warnings: list[str] = []
    info: dict[str, Any] = {
        "platform": platform.platform(),
        "pythonVersion": platform.python_version(),
        "pythonExecutable": sys.executable,
        "userSite": site.getusersitepackages(),
    }

    if sessions_root is not None:
        sessions_root.mkdir(parents=True, exist_ok=True)
        info["sessionsRoot"] = str(sessions_root.resolve())
    if queue_root is not None:
        queue_root.mkdir(parents=True, exist_ok=True)
        info["queueRoot"] = str(queue_root.resolve())

    ffmpeg_path = shutil.which(args.ffmpeg_command)
    if not ffmpeg_path:
        warnings.append("ffmpeg no está en PATH: el troceado de mp3 caerá a modo chunk único.")

    gpu = run_nvidia_smi()
    ct2 = ctranslate2_info()
    ram_gib = total_ram_gib()
    model, chunk_sec, device, compute_type, profile_warnings = recommended_profile(ram_gib, gpu, ct2)
    warnings.extend(profile_warnings)

    if gpu.get("available") and not ct2.get("cudaTypes"):
        warnings.append("nvidia-smi responde, pero CTranslate2 no expone tipos CUDA; revisa cublas/cudnn.")

    ready = ffmpeg_path is not None and not ct2.get("error")
    payload = {
        "ready": ready,
        "recommendedModel": model,
        "recommendedChunkSec": chunk_sec,
        "recommendedDevice": device,
        "recommendedComputeType": compute_type,
        "ffmpegAvailable": ffmpeg_path is not None,
        "gpuAvailable": bool(gpu.get("available")) and bool(ct2.get("cudaTypes")),
        "pythonExecutable": sys.executable,
        "sessionsRoot": str(sessions_root.resolve()) if sessions_root else None,
        "queueRoot": str(queue_root.resolve()) if queue_root else None,
        "warnings": warnings,
        "info": {
            **info,
            "ramGiB": ram_gib,
            "ffmpegPath": ffmpeg_path,
            "gpu": gpu,
            "ctranslate2": ct2,
        },
    }

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
