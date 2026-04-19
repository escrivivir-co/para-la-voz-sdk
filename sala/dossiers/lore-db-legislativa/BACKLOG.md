# Backlog — lore-pipeline-legislativa

> **Última actualización:** 19-abr-2026 — Claude Opus 4.6

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| LP-00 | cerrada | Claude Opus 4.6 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| LP-01 | libre | — | LP-00, PS-05† | `lore/` inicializado + routing actualizado | [TASK-01](./tasks/TASK-01_LORE_DB.md) |
| LP-01b | libre | — | LP-01 | 40+ ficheros migrados, refs actualizadas | [TASK-01b](./tasks/TASK-01b_MIGRAR_PIEZAS.md) |
| LP-02 | libre | — | LP-01b, PS-01† | Edición de `lore-schema.instructions.md` | [TASK-02](./tasks/TASK-02_ADAPTAR_SCHEMA.md) |
| LP-03 | libre | — | LP-01b | Edición de `lore-routing.instructions.md` | [TASK-03](./tasks/TASK-03_ADAPTAR_ROUTING.md) |
| LP-04 | libre | — | LP-02 | `mod/instructions/lore-pipeline.instructions.md` | [TASK-04](./tasks/TASK-04_FORMALIZAR_PIPELINE.md) |
| LP-05 | libre | — | LP-02, LP-04 | Mapa agéntico: Loreador Legislativa + Archivero Legislativa + Pipeline | [TASK-05](./tasks/TASK-05_ADAPTAR_AGENTES.md) |

> † PS-05 y PS-01 son del dossier `pieza-sdk`. LP-01 depende del scaffold lore/ en main (PS-05). LP-02 depende del schema genérico (PS-01).

## Criterio de cierre

- [ ] `lore/` creado con estructura canónica (piezas/, derivados/, drafts/)
- [ ] 40+ ficheros migrados de DRAFTS2 con `git mv` (historial preservado)
- [ ] `{{LORE_DIR}}` definido en routing, tabla actualizada
- [ ] `lore-schema` hereda del SDK genérico
- [ ] `mod/instructions/lore-pipeline.instructions.md` documenta el grafo de dependencias
- [ ] Agentes del mod actualizados: `@Loreador Legislativa` (nuevo), `@Archivero Legislativa` (renombrado), `@Puzzle` eliminado
- [ ] Pipeline piezas → corpus → grafo → universos → cortos está documentado y cableado
- [ ] Cadena Pipeline: Loreador Legislativa → Archivero Legislativa → Grafista → Demiurgo → Dramaturgo Cortos
