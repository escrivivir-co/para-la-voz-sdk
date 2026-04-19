# Backlog — universos-sdk

> **Última actualización:** 19-abr-2026 — GPT-5.4

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| US-00 | cerrada | GPT-5.4 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| US-01 | libre | — | US-00 | `.github/instructions/universo-schema.instructions.md` | [TASK-01](./tasks/TASK-01_SCHEMA_UNIVERSO.md) |
| US-02 | libre | — | US-00 | `.github/templates/universo.template.md` | [TASK-02](./tasks/TASK-02_TEMPLATE_UNIVERSO.md) |
| US-03 | libre | — | US-01, US-02 | Edición de `.github/copilot-instructions.md` | [TASK-03](./tasks/TASK-03_DOCUMENTAR_SDK.md) |

## Criterio de cierre

- [ ] `.github/instructions/universo-schema.instructions.md` existe con contrato portable de universo persistido
- [ ] `.github/templates/universo.template.md` existe
- [ ] `.github/copilot-instructions.md` documenta `{{LORE_DIR}}/derivados/universo/`
- [ ] No se crea `@Demiurgo` SDK en esta iteración; el mod sigue especializándolo

## Downstream: future-machine-sdk

> US-01 (schema) → FS-01 (`slot_universos`). US-03 (docs) → FS-02 (template/manifest).