# Backlog — corpus-sdk

> **Última actualización:** 19-abr-2026 — GPT-5.4

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| CS-00 | cerrada | GPT-5.4 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| CS-01 | libre | — | CS-00 | `.github/instructions/corpus-schema.instructions.md` | [TASK-01](./tasks/TASK-01_SCHEMA_CORPUS.md) |
| CS-02 | libre | — | CS-01 | Edición de `.github/agents/archivero.agent.md` | [TASK-02](./tasks/TASK-02_ARCHIVERO_CAPA_CORPUS.md) |
| CS-03 | libre | — | CS-02 | Prompts/templates SDK de corpus actualizados | [TASK-03](./tasks/TASK-03_COMPAT_PROMPTS_Y_FLUJOS.md) |
| CS-04 | libre | — | CS-01, CS-03 | Edición de `.github/copilot-instructions.md` | [TASK-04](./tasks/TASK-04_DOCUMENTAR_CAPA_CORPUS.md) |

## Criterio de cierre

- [ ] `.github/instructions/corpus-schema.instructions.md` existe con contrato portable de la capa corpus
- [ ] `@Archivero` documenta explícitamente la dualidad incremental + batch dentro del dominio corpus
- [ ] `/feed`, `/diff-corpus`, `/merge-corpus`, `/status` siguen siendo válidos sin ruptura
- [ ] Los prompts y templates SDK documentan también el camino `Loreador -> Archivero ingest -> corpus`
- [ ] `.github/copilot-instructions.md` trata `corpus/` como capa canónica entre `lore-db` y `grafo`