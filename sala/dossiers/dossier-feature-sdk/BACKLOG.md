# Backlog — dossier-feature-sdk

> **Última actualización:** 19-abr-2026 — Claude Opus 4.6

## Contexto compartido

- `.github/copilot-instructions.md` — estructura del SDK y tabla de comandos
- `mod/prompts/dossier.prompt.md` — prompt actual a generalizar
- `mod/skills/cristalizacion-feature/SKILL.md` — SKILL actual a generalizar
- `sala/plantilla-dossier/` — scaffold existente

## Regla DRY del backlog

- El backlog es índice y tracking. El detalle vive en `tasks/`.
- No se duplican reglas de `.github/` o `mod/`.

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| DF-00 | cerrada | Claude Opus 4.6 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| DF-01 | libre | — | — | `.github/prompts/dossier.prompt.md` | [TASK-01](./tasks/TASK-01_PROMOVER_DOSSIER_PROMPT.md) |
| DF-02 | libre | — | — | `.github/skills/cristalizacion-feature/SKILL.md` | [TASK-02](./tasks/TASK-02_PROMOVER_SKILL.md) |
| DF-03 | libre | — | DF-01, DF-02 | `.github/copilot-instructions.md` + merge main → mod + cleanup | [TASK-03](./tasks/TASK-03_INTEGRAR_SDK_Y_LIMPIAR.md) |

## Criterio de cierre del feature

- [ ] `dossier.prompt.md` vive en `.github/prompts/` y no tiene refs a lore específico
- [ ] `cristalizacion-feature/SKILL.md` vive en `.github/skills/` y no tiene refs a lore específico
- [ ] `.github/copilot-instructions.md` incluye `/dossier` en tabla de comandos de sala
- [ ] `mod/legislativa` hereda ambos de `.github/` tras merge main → mod
- [ ] Los duplicados en `mod/prompts/` y `mod/skills/` se eliminan
