# TASK-00 — Contexto y persistencia

> **Estado:** cerrada
> **Agente recomendado:** GPT-5.4
> **Entrega esperada:** contexto congelado en `PLAN.md` + `BACKLOG.md`

## Hallazgos fijados

- El SDK ya tiene una capa corpus operativa vía `corpus/`, `/feed`, `@Archivero`, `/diff-corpus`, `/merge-corpus` y `/status`.
- El mod legislativa ya tiene una variante batch vía `@Archivero Lore` + `/lore-ingest`.
- `corpus/` en legislativa hoy es un workaround explícito, no la fuente viva.
- `lore-db-sdk` ya separó la gestión de piezas; lo que faltaba separar era la transformación **a corpus**.

## Anclas mínimas

- `.github/agents/archivero.agent.md`
- `.github/prompts/feed.prompt.md`
- `.github/prompts/diff-corpus.prompt.md`
- `.github/prompts/merge-corpus.prompt.md`
- `.github/prompts/status.prompt.md`
- `.github/templates/guion-ciclo.template.md`
- `mod/agents/archivero-lore.agent.md`
- `corpus/README.md`
- `corpus/corpus.md`

## Criterio de aceptación

- El problema y el corte de responsabilidad quedan fijados antes de tocar prompts o agentes.