# TASK-00 — Contexto y persistencia

> **Estado:** cerrada
> **Agente recomendado:** GPT-5.4
> **Entrega esperada:** contexto congelado en `PLAN.md` + `BACKLOG.md`

## Hallazgos fijados

- El mod ya tiene `Portal`, `Pipeline`, `user-empieza-aqui`, `lore-status` y la cadena agéntica.
- La separación en capas resolvió responsabilidades, pero aún no existe un manifest que las vuelva máquina.
- El usuario quiere que esta capa sea el cierre del ciclo y que aproveche los entrypoints ya definidos.
- La machine debe operar sobre el ecosistema exportado a `lore/`, no sobre una dependencia implícita de `DRAFTS2/`.

## Anclas mínimas

- `mod/agents/portal.agent.md`
- `mod/prompts/user-empieza-aqui.prompt.md`
- `mod/prompts/lore-status.prompt.md`
- `mod/agents/pipeline.agent.md`
- `mod/instructions/onboarding-map.instructions.md`
- `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/PLAN_FUTURE_MACHINE_UNIVERSO1.md`

## Criterio de aceptación

- El problema queda fijado como integración del ciclo completo y no como nueva capa paralela.