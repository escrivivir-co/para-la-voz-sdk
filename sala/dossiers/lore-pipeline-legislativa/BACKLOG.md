# Backlog — lore-pipeline-legislativa

> **Última actualización:** 19-abr-2026 — Claude Opus 4.6

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| LP-00 | cerrada | Claude Opus 4.6 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| LP-01 | libre | — | LP-00 | Decisión de ubicación + migración de piezas | [TASK-01](./tasks/TASK-01_UBICACION_PIEZAS.md) |
| LP-02 | libre | — | LP-00, PS-01† | Edición de `lore-schema.instructions.md` | [TASK-02](./tasks/TASK-02_ADAPTAR_SCHEMA.md) |
| LP-03 | libre | — | LP-01 | Edición de `lore-routing.instructions.md` | [TASK-03](./tasks/TASK-03_ADAPTAR_ROUTING.md) |
| LP-04 | libre | — | LP-02 | `mod/instructions/lore-pipeline.instructions.md` | [TASK-04](./tasks/TASK-04_FORMALIZAR_PIPELINE.md) |
| LP-05 | libre | — | LP-02, LP-04 | Ediciones de agentes del mod | [TASK-05](./tasks/TASK-05_ADAPTAR_AGENTES.md) |

> † PS-01 es del dossier `pieza-sdk`. LP-02 puede empezar cuando PS-01 esté cerrada o en paralelo si se asume el schema genérico como estable.

## Criterio de cierre

- [ ] Ubicación definitiva de piezas decidida e implementada
- [ ] `lore-schema` hereda del SDK genérico
- [ ] `lore-routing` usa `{{PIEZA_DIR}}` y refleja ubicación definitiva
- [ ] `mod/instructions/lore-pipeline.instructions.md` documenta el grafo de dependencias
- [ ] Agentes del mod (archivero-lore, puzzle, pipeline) referencian el SDK genérico
- [ ] Pipeline piezas → corpus → grafo → universos → cortos está documentado y cableado
