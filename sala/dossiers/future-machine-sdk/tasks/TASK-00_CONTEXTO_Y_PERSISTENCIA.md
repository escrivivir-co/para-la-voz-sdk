# TASK-00 — Contexto y persistencia

> **Estado:** cerrada
> **Agente recomendado:** GPT-5.4
> **Entrega esperada:** contexto congelado en `PLAN.md` + `BACKLOG.md`

## Hallazgos fijados

- `future-machine-universo-1` ya intuía el cierre del ciclo, pero estaba pegada al caso y luego quedó absorbida por dossiers hermanos.
- Hoy ya existe el corte por capas: `lore-db`, `corpus`, `grafo`, `universos`, `cortos`.
- Lo que falta no es otra capa de datos, sino una estructura compositiva con slots y entrypoints.
- `Portal` y `Pipeline` son las dos superficies naturales de esa composición.

## Anclas mínimas

- `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/PLAN_FUTURE_MACHINE_UNIVERSO1.md`
- `.github/agents/portal.agent.md`
- `sala/dossiers/lore-db-sdk/PLAN.md`
- `sala/dossiers/corpus-sdk/PLAN.md`
- `sala/dossiers/grafo-sdk/PLAN.md`
- `sala/dossiers/universos-sdk/PLAN.md`
- `sala/dossiers/cortos-sdk/PLAN.md`

## Criterio de aceptación

- El problema queda fijado como composición y no como nueva capa técnica aislada.