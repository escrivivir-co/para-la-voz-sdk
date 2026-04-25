# LORE — conversación Liria / Castro

> **Estado:** draft de trabajo derivado de STT local + edición manual.
> **Carpeta:** `DRAFT2/`
> **Fuente primaria preservada:** [`../tmp/media-cache/S-01-liria-rojipardismo-full.mp3`](../tmp/media-cache/S-01-liria-rojipardismo-full.mp3)
> **Transcripción STT preservada:** [`../tmp/media-cache/S-01-liria-rojipardismo-GPU-small-int8_float32.txt`](../tmp/media-cache/S-01-liria-rojipardismo-GPU-small-int8_float32.txt)

---

## Índice de bloques

| Bloque | Título | Piezas | Fichero |
|--------|--------|--------|---------|
| B | Conversaciones / entrevistas | `[S-01]` | [LORE_B.md](LORE_B.md) |
| S | Expansión speaker-attributed | `[S-01]` | [LORE_S-01.md](LORE_S-01.md) |
| R | Review pack + segunda pasada | `[S-01]` | [LORE_S-01_REVIEW.md](LORE_S-01_REVIEW.md) |

---

## Convenciones de marcas

- `[S-01]` = pieza social / conversación preservada.
- `[CFL]` = **Carlos Fernández Liria**.
- `[EC]` = **Ernesto Castro**.
- `[CFL?]` / `[EC?]` = atribución editorial probable, no cerrada por diarización automática.
- `[VOZ?]` = frontera de voz no resuelta o intervención de moderación / público filtrado.

Importante: las marcas de hablante de este draft **no las produce Whisper**. Son una **capa editorial** montada sobre el transcript STT a partir de:

1. llamadas nominales internas (`"Hola, Ernesto"`, `"Hola, ¿qué tal, Carlos?"`),
2. continuidad temática de turnos,
3. auto-referencias biográficas distinguibles,
4. zonas de pregunta / respuesta claramente encadenadas.

---

## Criterio operativo

Este lore ya permite dos usos distintos:

- **Uso de archivo / navegación:** bloques temáticos, citas de trabajo, núcleos conceptuales, rutas de revisión.
- **Uso de verbatim casi cerrado:** pasar por el review pack y escuchar solo los cortes priorizados.

Si más adelante se quiere un **verbatim línea a línea con hablante automático**, hará falta añadir una etapa de **diarización**. Con el stack actual, lo razonable es:

- usar Whisper para transcripción,
- usar atribución editorial en bloques y extractos,
- reservar la diarización automática para una fase posterior específica.
