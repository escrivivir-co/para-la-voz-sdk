# TASK-05 — Nuevo mapa agéntico del mod: Loreador Legislativa + Archivero Legislativa + Pipeline

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** LP-02, LP-04, PS-03† (Loreador SDK)
> **Entrega esperada:** 3 acciones en `mod/agents/`: crear, renombrar, eliminar + actualizar Pipeline

> † PS-03 es del dossier `lore-db-sdk` — provee `@Loreador` SDK que el mod extiende.

## Lee primero

- [Plan §4.5](../PLAN.md) — mapa de cambios (antes/después)
- `.github/agents/loreador.agent.md` — el Loreador SDK que se extiende (cuando exista, PS-03)
- `mod/agents/archivero-lore.agent.md` — se renombra a archivero-legislativa
- `mod/agents/puzzle.agent.md` — se elimina
- `mod/agents/pipeline.agent.md` — se actualiza la cadena

## Decisión del PO (19-abr-2026)

- Puzzle **desaparece** — su función se absorbe en Loreador Legislativa
- Archivero Lore → **Archivero Legislativa** — hace corpus específico del mod
- Pipeline incorpora a **Loreador Legislativa** como primer eslabón

## Cambios esperados

### 1. CREAR: `mod/agents/loreador-legislativa.agent.md`

Extiende `@Loreador` SDK con:
- Validación contra `lore-schema.instructions.md` (tipos P, S, N, T, R, F)
- Campos obligatorios por tipo
- DoR/DoD por tipo
- Operación `ingest` → delega a Archivero Legislativa para generar corpus
- Handoffs: → `@Archivero Legislativa`, → `@Pipeline`

### 2. RENOMBRAR: `archivero-lore.agent.md` → `archivero-legislativa.agent.md`

Cambios:
- name: `Archivero Legislativa`
- description: clarificar que genera corpus **específico del mod** (ingest batch → Bartleby → CORPUS_PREVIEW)
- Eliminar referencia a Puzzle en handoffs (ya no existe)
- Añadir handoff desde Loreador Legislativa
- Fuentes: referenciar `pieza-schema.instructions.md` SDK + `lore-schema.instructions.md` mod

### 3. ELIMINAR: `mod/agents/puzzle.agent.md`

Su función de validación (inventario ↔ disco, campos obligatorios) está ahora en `@Loreador Legislativa`.

### 4. ACTUALIZAR: `mod/agents/pipeline.agent.md`

Nueva cadena:
```
Loreador Legislativa → Archivero Legislativa → Grafista → Demiurgo → Dramaturgo Cortos
```

Cambios:
- agents: reemplazar `Puzzle` y `Archivero Lore` por `Loreador Legislativa` y `Archivero Legislativa`
- handoffs: actualizar labels y prompts
- Paso 0 (inventario): ahora delega a `@Loreador Legislativa` en vez de a `@Puzzle`
- Paso 1 (ingest): delega a `@Archivero Legislativa` (antes "Archivero Lore")

## Qué NO se toca

- Agentes SDK (`.github/agents/`) — eso es PS-03
- `@Grafista`, `@Demiurgo`, `@Dramaturgo Cortos` — no cambian en esta task
- El contenido de las piezas — solo infraestructura agéntica

## Criterio de aceptación

- `@Loreador Legislativa` existe con operaciones: validar (tipos concretos), pieza (campos obligatorios), ingest (handoff a Archivero Legislativa)
- `@Archivero Legislativa` existe (renombrado, limpio)
- `@Puzzle` eliminado
- `@Pipeline` usa la cadena nueva con handoffs actualizados
- La cadena completa funciona: Loreador Legislativa → Archivero Legislativa → Grafista → Demiurgo → Dramaturgo Cortos
