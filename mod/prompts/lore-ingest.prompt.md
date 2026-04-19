---
name: lore-ingest
description: "Ingesta el pack de lore completo y genera/actualiza el corpus. Punto de entrada para el ciclo lore → corpus → grafo → universo → obra."
argument-hint: "[full | diff | status]"
agent: Archivero Lore
tools: [vscode, execute, read, agent, edit, search, todo]
---

# /lore-ingest — Ingesta del pack de lore

Invoca el protocolo de `@Archivero Lore` para procesar el pack de piezas tipadas y generar o actualizar el corpus.

## Modos

1. **`/lore-ingest`** o **`/lore-ingest full`** — ingesta completa. Lee todas las piezas + LORE_F, pasa por Bartleby, genera CORPUS_PREVIEW.
2. **`/lore-ingest diff`** — solo detecta piezas nuevas o modificadas desde la última ingesta. Presenta delta sin editar.
3. **`/lore-ingest status`** — reporta estado del corpus, conteos, piezas no integradas.

## Flujo típico

```
/ingest-lore          → corpus actualizado
  ↓ (handoff)
@Grafista             → grafo de bifurcación
  ↓ (handoff)
@Dramaturgo Cortos    → obra desde una rama
```
