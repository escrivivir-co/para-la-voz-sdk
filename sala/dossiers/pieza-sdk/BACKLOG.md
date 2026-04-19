# Backlog — pieza-sdk

> **Última actualización:** 19-abr-2026 — Claude Opus 4.6

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| PS-00 | cerrada | Claude Opus 4.6 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| PS-01 | libre | — | PS-00 | `.github/instructions/pieza-schema.instructions.md` + template | [TASK-01](./tasks/TASK-01_SCHEMA_GENERICO.md) |
| PS-02 | libre | — | PS-00 | `.github/templates/pieza-index.template.md` | [TASK-02](./tasks/TASK-02_TEMPLATE_INDEX.md) |
| PS-03 | libre | — | PS-01 | Edición de `.github/agents/archivero.agent.md` | [TASK-03](./tasks/TASK-03_AMPLIAR_ARCHIVERO.md) |
| PS-04 | libre | — | PS-01, PS-02 | Edición de `.github/copilot-instructions.md` | [TASK-04](./tasks/TASK-04_DOCUMENTAR_SDK.md) |

## Criterio de cierre

- [ ] `.github/instructions/pieza-schema.instructions.md` existe con protocolo genérico
- [ ] `.github/templates/pieza-index.template.md` existe
- [ ] `.github/templates/pieza-schema.template.md` existe
- [ ] `@archivero` SDK referencia el concepto de piezas sin asumir tipos concretos
- [ ] `.github/copilot-instructions.md` documenta `{{PIEZA_DIR}}` y estructura de piezas
- [ ] `mod/legislativa` sigue funcionando sin rotura (validar que lore-schema, puzzle, archivero-lore siguen operativos)
