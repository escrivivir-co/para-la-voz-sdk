# TASK-00 — Contexto y persistencia

> **Estado:** cerrada
> **Agente recomendado:** GPT-5.4
> **Entrega esperada:** contexto congelado en `PLAN.md` + `BACKLOG.md`

## Hallazgos fijados

- `corpus/README.md` y `corpus/corpus.md` son redirects temporales, no capa viva.
- `DRAFTS2/CORPUS_PREVIEW.md` es el mapa real del corpus del caso.
- `@Archivero Lore` ya opera como Archivero batch de corpus.
- `grafo`, `demiurgo` y `dramaturgo` siguen leyendo el corpus por rutas `DRAFTS2/` duras.

## Anclas mínimas

- `corpus/README.md`
- `corpus/corpus.md`
- `DRAFTS2/CORPUS_PREVIEW.md`
- `mod/agents/archivero-lore.agent.md`
- `mod/prompts/lore-ingest.prompt.md`
- `mod/agents/pipeline.agent.md`
- `mod/instructions/lore-routing.instructions.md`

## Criterio de aceptación

- La separación de responsabilidad queda fijada antes de mover ni recablear corpus.