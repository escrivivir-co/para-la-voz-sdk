---
name: ingest-lore
description: "Ingesta el pack de lore completo y genera/actualiza el corpus. Punto de entrada para el ciclo lore → corpus → grafo → universo → obra."
argument-hint: "[full | diff | status]"
agent: Archivero Lore
tools: [vscode, execute, read, agent, edit, search, todo]
---

# /ingest-lore — Ingesta del pack de lore

Invoca el protocolo de `@Archivero Lore` para procesar el pack de piezas tipadas y generar o actualizar el corpus.

## Modos

1. **`/ingest-lore`** o **`/ingest-lore full`** — ingesta completa. Lee todas las piezas + LORE_F, pasa por Bartleby, genera CORPUS_PREVIEW.
2. **`/ingest-lore diff`** — solo detecta piezas nuevas o modificadas desde la última ingesta. Presenta delta sin editar.
3. **`/ingest-lore status`** — reporta estado del corpus, conteos, piezas no integradas.

## Flujo típico

```
/ingest-lore          → corpus actualizado
  ↓ (handoff)
@Grafista             → grafo de bifurcación
  ↓ (handoff)
@Dramaturgo Cortos    → obra desde una rama
```
