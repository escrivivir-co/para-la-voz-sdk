# Backlog — cortos-sdk

> **Última actualización:** 19-abr-2026 — GPT-5.4

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| CS-00 | cerrada | GPT-5.4 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| CS-01 | libre | — | CS-00 | `.github/instructions/corto-schema.instructions.md` | [TASK-01](./tasks/TASK-01_SCHEMA_CORTO.md) |
| CS-02 | libre | — | CS-00 | `.github/templates/corto.template.md` | [TASK-02](./tasks/TASK-02_TEMPLATE_CORTO.md) |
| CS-03 | libre | — | CS-01 | Edición de `.github/agents/dramaturgo.agent.md` | [TASK-03](./tasks/TASK-03_AMPLIAR_DRAMATURGO.md) |
| CS-04 | libre | — | CS-01, CS-02 | Edición de `.github/copilot-instructions.md` | [TASK-04](./tasks/TASK-04_DOCUMENTAR_SDK.md) |

## Criterio de cierre

- [ ] `.github/instructions/corto-schema.instructions.md` existe con contrato portable de obra derivada
- [ ] `.github/templates/corto.template.md` existe
- [ ] `@Dramaturgo` SDK documenta la persistencia por modelo en `{{LORE_DIR}}/derivados/cortos/`
- [ ] `.github/copilot-instructions.md` documenta la fase `cortos`