# Backlog — dossier-feature-sdk

> **Última actualización:** 19-abr-2026 — GPT-5.4

## Contexto compartido

- `sala/archivo/sprint-extraccion-sala-v2/dossiers/extraccion-sala-sdk/PLAN_EXTRACCION_SALA_SDK.md` — antecedente directo de la extracción de `sala`
- `sala/archivo/sprint-extraccion-sala-v2/CIERRE.md` — confirma que este dossier es el backlog del sprint siguiente
- `sala/README.md` — flujo real: el dossier diseña y la sala ejecuta
- `.github/copilot-instructions.md` — estructura del SDK y comandos de sala
- `.github/templates/sala-dossier.template.md` — template SDK hoy demasiado esquelético
- `mod/prompts/dossier.prompt.md` — prompt actual a generalizar
- `mod/skills/cristalizacion-feature/SKILL.md` — SKILL actual a generalizar
- `mod/README_MOD.md` y `mod/prompts/lore-status.prompt.md` — consumidores vivos a migrar
- `sala/plantilla-dossier/` — scaffold canónico actual
- `sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-pipeline-operativo/` y `.../cristalizacion-cadena-agentica/` — mejores ejemplos del scaffold rico

## Regla DRY del backlog

- El backlog es índice y tracking. El detalle vive en `tasks/`.
- No se duplican reglas de `.github/`, `sala/` o `mod/`.

## Tracking

| Task | Estado | Agente | Dependencias | Entrega | Brief |
|------|--------|--------|--------------|---------|-------|
| DF-00 | cerrada | Claude Opus 4.6 | — | contexto congelado | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| DF-01 | libre | — | — | `.github/prompts/dossier.prompt.md` | [TASK-01](./tasks/TASK-01_PROMOVER_DOSSIER_PROMPT.md) |
| DF-02 | libre | — | — | `.github/skills/cristalizacion-feature/SKILL.md` | [TASK-02](./tasks/TASK-02_PROMOVER_SKILL.md) |
| DF-03 | libre | — | DF-01, DF-02 | superficie `sala` alineada + scaffold rico en `main` + merge main → mod + cleanup controlado | [TASK-03](./tasks/TASK-03_INTEGRAR_SDK_Y_LIMPIAR.md) |

## Criterio de cierre del feature

- [ ] `.github/prompts/dossier.prompt.md` existe, usa `{{SALA_DIR}}` y refleja el formato actual del dossier
- [ ] `.github/skills/cristalizacion-feature/SKILL.md` existe, define `dossier` como capa de diseño de `sala` y permite promociones al SDK
- [ ] `.github/templates/sala-dossier.template.md` y `sala/plantilla-dossier/` reflejan el scaffold rico y portable que cualquier rama puede heredar
- [ ] `.github/copilot-instructions.md` documenta `/dossier` dentro de la superficie de `sala`
- [ ] `sala/archivo/sprint-extraccion-sala-v2/` queda publicado en `main` como archivo histórico del SDK
- [ ] No queda ningún consumidor vivo no archivado dependiendo de `BACKLOG_*`, `PLAN_*`, `RESPUESTAS_USUARIO_*` o de rutas `mod/...` sin puente explícito
- [ ] `mod/legislativa` hereda la versión de `main`, y los duplicados en `mod/` se eliminan o quedan solo como puente deliberado y sin drift
