---
name: media-extraction
description: Skill portable para extraer clips de audio/video de fuentes remotas (YouTube, Twitch VODs, URLs HLS), transcribirlos a texto con STT local, y archivar el resultado como pieza de lore. Se activa cuando se pide obtener, transcribir o archivar un fragmento de medio audiovisual remoto dado un timestamp y una URL.
---

# Skill: media-extraction — Extracción y transcripción de medios remotos

Esta skill implementa el pipeline completo: **URL + timestamps → clip local → transcripción STT → pieza archivada en lore**. Es agnóstica de plataforma (YouTube, Twitch, cualquier HLS/DASH) y de OS.

## Cuándo activar esta skill

- Cuando el usuario proporciona una **URL de vídeo** + **timestamps** y pide extraer, transcribir o archivar el fragmento
- Cuando se necesita obtener el texto hablado de un clip para registrarlo como pieza de lore
- Cuando se quiere preservar el contenido de un vídeo efímero (stream VOD, vídeo que puede desaparecer)

**NO activar si:**
- El usuario proporciona texto ya transcrito manualmente (solo archivar)
- Se pide analizar un documento escrito (usar `documental-analysis`)
- Se pide generar contenido (usar `voice-crystallization`)

---

## Dependencias del pipeline

| Herramienta | Rol | Instalación |
|---|---|---|
| `yt-dlp` | Descarga de clips YouTube y otras plataformas | `pip install --user yt-dlp` |
| `streamlink` | Extracción de tramos de Twitch VODs (HLS nativo) | `pip install --user streamlink` |
| `faster-whisper` | Transcripción STT local (modelo Whisper CTranslate2) | `pip install --user faster-whisper` |
| `ffmpeg` | (Opcional) Recorte y conversión de audio. Requerido por yt-dlp `--download-sections`. Si no disponible, descargar audio completo + recortar con `av` en Python (ver fallback abajo). | Paquete de sistema: `apt install ffmpeg` / `brew install ffmpeg` / `choco install ffmpeg` |

### Verificación de dependencias

```bash
# Verificar todo el stack
python --version
python -m yt_dlp --version        # o: yt-dlp --version
python -m streamlink --version     # o: streamlink --version
python -c "from faster_whisper import WhisperModel; print('faster-whisper OK')"
ffmpeg -version                    # opcional
```

Si alguna herramienta falta, instalar antes de continuar. Todas se instalan a nivel `--user`, no requieren privilegios.

---

## Directorios de trabajo

El pipeline usa dos carpetas bajo `tmp/`, ambas en `.gitignore`:

### `tmp/media/` — zona de trabajo temporal

Aquí se descargan y procesan los clips durante la sesión activa.
- Nombres con marca de lore: `{marca}-{descriptor}.{ext}`
- Se limpia **solo tras confirmación del usuario** (ver protocolo abajo)

### `tmp/media-cache/` — caché de referencia entre sesiones

Cuando el usuario decide conservar piezas, se mueven aquí. Esto permite:
- Retomar trabajo sin re-descargar clips ya obtenidos
- Re-transcribir con otro modelo o parámetros sin repetir la extracción
- Tener referencia del audio original si se necesita verificar una cita

Nombres con marca + fuente: `{marca}-{descriptor}-{fuente}.{ext}`

```
tmp/
├── media/                  ← zona de trabajo (efímera)
│   ├── .gitkeep
│   ├── S-01-feo-cierre.wav
│   └── S-02-feo-cierre.wav
│
└── media-cache/            ← caché persistente entre sesiones
    ├── .gitkeep
    ├── S-01-feo-detencion-full-yt.webm
    ├── S-05-facu-bustinduy-twitch.aac
    └── ...
```

### Protocolo de cierre de sesión

Al terminar cada extracción:
1. Verificar que la transcripción está archivada en el fichero de lore correspondiente
2. Listar archivos en `tmp/media/`
3. **Preguntar al usuario** qué quiere hacer con cada pieza:
   - **Archivar en caché** → mover a `tmp/media-cache/` (conserva para reuso)
   - **Eliminar** → borrar del workspace
   - **Mantener en media/** → dejar para seguir trabajando en la sesión
4. Si `tmp/media/` queda vacío, mantener la carpeta (`.gitkeep`)

El agente **nunca borra sin preguntar**. Si el usuario va a seguir trabajando con esas piezas, le conviene conservarlas en caché.

---

## Pipeline paso a paso

### Paso 1 — Seleccionar herramienta según plataforma

| Plataforma | Herramienta | Notas |
|---|---|---|
| **YouTube** | `yt-dlp` | Soporta `--download-sections` para recortar por timestamp |
| **Twitch VOD** | `streamlink` | Usa `--hls-start-offset` y `--hls-duration` para extraer tramos |
| **Otra URL HLS/DASH** | `streamlink` o `yt-dlp` | Intentar `yt-dlp` primero; fallback a `streamlink` |

### Paso 2 — Extraer el clip

#### YouTube (yt-dlp)

**Con ffmpeg instalado** (preferente):

```bash
# Extraer tramo de audio entre dos timestamps
# Formato: *HH:MM:SS-HH:MM:SS
python -m yt_dlp \
  --download-sections "*00:05:30-00:06:00" \
  -x --audio-format mp3 \
  -o "tmp/media/{marca}-{descriptor}.%(ext)s" \
  "URL_DEL_VIDEO"
```

**Sin ffmpeg** (fallback con av):

```bash
# 1. Descargar audio completo (bestaudio, ~10 MB por 10 min)
python -m yt_dlp -f bestaudio \
  -o "tmp/media/{marca}-{descriptor}-full.%(ext)s" \
  "URL_DEL_VIDEO"

# 2. Recortar con Python av (viene con faster-whisper)
python -c "
import av, wave, struct
container = av.open('tmp/media/{marca}-{descriptor}-full.webm')
stream = container.streams.audio[0]
sr = stream.rate or 16000
samples = []
for frame in container.decode(audio=0):
    arr = frame.to_ndarray()
    if arr.ndim > 1: arr = arr.mean(axis=0)
    samples.extend(arr.flatten().tolist())
container.close()
start = int(START_SECONDS * sr)
trimmed = samples[start:]
with wave.open('tmp/media/{marca}-{descriptor}.wav', 'w') as wf:
    wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr)
    mx = max(abs(s) for s in trimmed) or 1
    scale = 32767.0 / mx if mx > 1 else 32767.0
    wf.writeframes(struct.pack('<'+'h'*len(trimmed), *[int(s*scale) for s in trimmed]))
print(f'Trimmed: {len(trimmed)/sr:.1f}s')
"
```

**Notas por OS:**
- **Linux/macOS:** El comando funciona tal cual. Usa comillas dobles para la URL.
- **Windows (PowerShell):** Reemplazar `\` por `` ` `` para continuación de línea, o escribir en una sola línea. Las comillas simples dentro de dobles funcionan.
- **Windows (cmd):** Usar `^` para continuación de línea. No usar comillas simples.

#### Twitch VOD (streamlink)

```bash
# Extraer tramo de vídeo (HLS offset + duration)
python -m streamlink \
  --hls-start-offset HH:MM:SS \
  --hls-duration HH:MM:SS \
  "https://www.twitch.tv/videos/VIDEOID" \
  best \
  -o "tmp/media/{marca}-{descriptor}.ts"

# Solo audio (más rápido, menor tamaño)
python -m streamlink \
  --hls-start-offset HH:MM:SS \
  --hls-duration HH:MM:SS \
  "https://www.twitch.tv/videos/VIDEOID" \
  audio \
  -o "tmp/media/{marca}-{descriptor}.aac"
```

**Notas por OS:**
- **Linux/macOS:** `$PWD` funciona en la ruta de `-o`. Usar comillas dobles para URLs con `?` y `&`.
- **Windows:** Usar `%cd%` (cmd) o `$PWD` (PowerShell). Las rutas usan `\` pero streamlink acepta `/`.

### Paso 3 — Transcribir con STT local

```bash
python - <<'PY'
from faster_whisper import WhisperModel

model = WhisperModel("small", device="cpu", compute_type="int8")
segments, info = model.transcribe(
    "tmp/media/{marca}-{descriptor}.ts",   # o .aac, .mp3
    language="es",                          # forzar idioma si se conoce
    beam_size=5,
    vad_filter=True,                        # filtrar silencios
    vad_parameters=dict(min_silence_duration_ms=500)
)

print(f"Idioma detectado: {info.language} (prob: {info.language_probability:.2f})\n")
for seg in segments:
    conf = "LOW" if seg.avg_logprob < -1.0 else "OK"
    print(f"[{seg.start:.1f}–{seg.end:.1f}] ({conf}) {seg.text.strip()}")
PY
```

**Notas por OS:**
- **Linux/macOS:** El heredoc `<<'PY'` funciona en bash/zsh.
- **Windows (PowerShell):** No soporta heredoc. Usar un fichero `.py` temporal:
  ```powershell
  # Escribir script temporal
  @"
  from faster_whisper import WhisperModel
  model = WhisperModel("small", device="cpu", compute_type="int8")
  segments, info = model.transcribe("tmp/media/{marca}-{descriptor}.ts", language="es", beam_size=5, vad_filter=True)
  for seg in segments:
      conf = "LOW" if seg.avg_logprob < -1.0 else "OK"
      print(f"[{seg.start:.1f}-{seg.end:.1f}] ({conf}) {seg.text.strip()}")
  "@ | Out-File -Encoding utf8 tmp/media/_stt_tmp.py
  python tmp/media/_stt_tmp.py
  Remove-Item tmp/media/_stt_tmp.py
  ```
- **Windows (Git Bash / WSL):** El heredoc funciona igual que en Linux.

### Paso 4 — Clasificar la confianza

| `avg_log_prob` | Etiqueta | Criterio de archivo |
|---|---|---|
| ≥ −0.5 | **ALTA** | Cita cerrada literal → usar `>` blockquote |
| −1.0 … −0.5 | **OK** | Transcripción de trabajo → usar `>` con nota "(STT)" |
| < −1.0 | **LOW** | Solo sentido verificado → marcar como "sentido de trabajo, no cita cerrada" |

### Paso 5 — Archivar en lore

Insertar la transcripción en el fichero de lore correspondiente (`LORE_B.md` para piezas sociales) bajo la marca `[S-XX]`:

```markdown
### Detalle `[S-XX]`

**Fuente:** <URL_COMPLETA_CON_TIMESTAMP>

- Tramo relevante: desde `HH:MM:SS` hasta `HH:MM:SS` aprox.
- Situación archivada: [descripción breve de qué ocurre en el clip]
- Efecto archivado: [qué produce esta pieza en el lore]

**Transcripción de trabajo** (STT local sobre clip extraído; revisar contra audio si se quiere cita literal):

> "[fragmento alta confianza]"
>
> "[fragmento OK]"

- Fragmento de baja confianza: **"[texto]"** — conservado como sentido verificado de trabajo.
```

### Paso 6 — Cierre: preguntar al usuario y gestionar piezas

**Antes de borrar nada**, listar los archivos y preguntar al usuario:

```
Archivos en tmp/media/:
  S-01-feo-detencion-full.webm (9.1 MB)
  S-01-feo-detencion-cierre.wav (2.8 MB)
  S-02-feo-juicio-full.webm (15.5 MB)
  S-02-feo-juicio-cierre.wav (2.9 MB)

¿Qué hago con ellos?
  1. Mover a caché (tmp/media-cache/) para reuso futuro
  2. Eliminar todos
  3. Mantener en tmp/media/ para seguir trabajando
```

Según respuesta:

```bash
# Opción 1 — Mover a caché
mv tmp/media/*.webm tmp/media/*.wav tmp/media-cache/
# Windows: move tmp\media\*.webm tmp\media-cache\

# Opción 2 — Eliminar
rm tmp/media/*.webm tmp/media/*.wav 2>/dev/null
# Windows (PowerShell): Remove-Item tmp/media/*.webm, tmp/media/*.wav -ErrorAction SilentlyContinue

# Opción 3 — No hacer nada
```

Si en una sesión futura el usuario pide trabajar con un clip que ya está en `tmp/media-cache/`, **copiar al media/ de trabajo** en vez de re-descargar:

```bash
cp tmp/media-cache/S-01-feo-detencion-full-yt.webm tmp/media/
```

---

## Refinamiento iterativo

Si un fragmento tiene baja confianza y es relevante:

1. **Recortar más estrecho** — extraer solo los 20-30 segundos del fragmento problemático
2. **Usar stream `audio`** en vez de `best` (menos ruido de vídeo en el decode)
3. **Subir modelo** — usar `medium` o `large-v3` en vez de `small` (más lento, más preciso)
4. **Ajustar VAD** — reducir `min_silence_duration_ms` si hay cortes en medio de frases
5. Si sigue low-confidence: marcar como "sentido de trabajo" y verificar manualmente

---

## Modelo Whisper: selección por recurso

| Modelo | VRAM/RAM | Velocidad CPU | Precisión | Cuándo usar |
|---|---|---|---|---|
| `tiny` | ~1 GB | Muy rápido | Baja | Previsualización rápida |
| `small` | ~2 GB | Rápido | Buena | **Default para lore** — equilibrio velocidad/calidad |
| `medium` | ~5 GB | Medio | Alta | Fragmentos problemáticos o idiomas mixtos |
| `large-v3` | ~10 GB | Lento | Muy alta | Cuando se necesita cita literal verificada |

---

## Ejemplos rápidos

### YouTube — últimos 30 segundos de un vídeo

```bash
# Averiguar duración
python -m yt_dlp --print duration "URL"

# Si dura 5:42 (342s), extraer desde 5:12
python -m yt_dlp \
  --download-sections "*00:05:12-00:05:42" \
  -x --audio-format mp3 \
  -o "tmp/media/S-01-feo-detencion-cierre.mp3" \
  "URL"

# Transcribir
python -c "
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8')
segs, info = m.transcribe('tmp/media/S-01-feo-detencion-cierre.mp3', language='es', beam_size=5, vad_filter=True)
for s in segs:
    conf = 'LOW' if s.avg_logprob < -1.0 else 'OK'
    print(f'[{s.start:.1f}-{s.end:.1f}] ({conf}) {s.text.strip()}')
"
```

### Twitch VOD — tramo con timestamps conocidos

```bash
python -m streamlink \
  --hls-start-offset 02:01:19 \
  --hls-duration 00:03:41 \
  "https://www.twitch.tv/videos/XXXXX" \
  audio \
  -o "tmp/media/S-05-facu-bustinduy.aac"

python -c "
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8')
segs, info = m.transcribe('tmp/media/S-05-facu-bustinduy.aac', language='es', beam_size=5, vad_filter=True)
for s in segs:
    conf = 'LOW' if s.avg_logprob < -1.0 else 'OK'
    print(f'[{s.start:.1f}-{s.end:.1f}] ({conf}) {s.text.strip()}')
"
```
