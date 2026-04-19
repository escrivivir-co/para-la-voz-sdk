# Backlog — grafo-sdk

> **Última actualización:** 19-abr-2026 — Claude Opus 4.6

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| GS-00 | cerrada | Claude Opus 4.6 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| GS-01 | libre | — | GS-00 | `.github/instructions/grafo-schema.instructions.md` | [TASK-01](./tasks/TASK-01_SCHEMA_GRAFO.md) |
| GS-02 | libre | — | GS-00 | `.github/templates/grafo-gramatica.template.md` | [TASK-02](./tasks/TASK-02_TEMPLATE_GRAMATICA.md) |
| GS-03 | libre | — | GS-01 | Edición de `.github/agents/dramaturgo.agent.md` | [TASK-03](./tasks/TASK-03_AMPLIAR_DRAMATURGO.md) |
| GS-04 | libre | — | GS-01, GS-02 | Edición de `.github/copilot-instructions.md` | [TASK-04](./tasks/TASK-04_DOCUMENTAR_SDK.md) |

## Criterio de cierre

- [ ] `.github/instructions/grafo-schema.instructions.md` existe con protocolo genérico (nodos, arcos, huecos)
- [ ] `.github/templates/grafo-gramatica.template.md` existe
- [ ] `@Dramaturgo` SDK referencia el concepto de grafo sin asumir tipos concretos
- [ ] `.github/copilot-instructions.md` documenta la convención `{{LORE_DIR}}/derivados/grafo/`
- [ ] `mod/legislativa` sigue funcionando sin rotura (gramática existente no se toca)
