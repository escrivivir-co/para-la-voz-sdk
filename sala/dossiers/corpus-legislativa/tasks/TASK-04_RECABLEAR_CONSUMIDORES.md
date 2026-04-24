# TASK-04 — Recablear consumidores del corpus

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CP-03
> **Entrega esperada:** refs downstream del corpus actualizadas

## Objetivo

Actualizar agentes, prompts e instructions del mod para que dejen de leer `DRAFTS2/CORPUS_PREVIEW.md` como ruta dura.

## Ficheros objetivo mínimos

- `mod/agents/grafista.agent.md`
- `mod/agents/demiurgo.agent.md`
- `mod/agents/dramaturgo.agent.md`
- `mod/agents/pipeline.agent.md`
- `mod/instructions/lore-routing.instructions.md`
- `mod/instructions/onboarding-map.instructions.md`

## Criterio de aceptación

- Downstream consume corpus canónico o routing explícito hacia él.