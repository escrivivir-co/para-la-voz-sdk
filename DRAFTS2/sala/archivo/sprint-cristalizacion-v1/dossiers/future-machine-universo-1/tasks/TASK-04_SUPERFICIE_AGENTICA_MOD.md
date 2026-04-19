# TASK-04 — Superficie agéntica completa en mod/

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** FM-02, FM-03
> **Entrega esperada:** artefactos nuevos o ampliados dentro de `mod/`

## Lee primero

- [Propuesta del Cristalizador](../BACKLOG_FUTURE_MACHINE_UNIVERSO1.md)
- [Dramaturgo del mod](../../../mod/agents/dramaturgo.agent.md)
- [Pipeline del mod](../../../mod/agents/pipeline.agent.md)
- [Prompt corto-universo](../../../mod/prompts/corto-universo.prompt.md)
- [Instrucciones del mod](../../../mod/instructions/legislativa-universo.instructions.md)

## Objetivo

Implementar la superficie agéntica que el feature necesite en `mod/`: agentes, prompts, instructions, hooks, handoffs o subagentes internos, siempre que aporten valor real a la future-machine.

## Alcance permitido

- `mod/agents/`
- `mod/prompts/`
- `mod/instructions/`
- `mod/hooks/` si el diseño lo justifica
- `mod/skills/`
- `mod/universos/` si la intervención necesita una vista canónica adicional

## Restricciones

- No tocar `.github/`.
- No crear artefactos por simetría o decoración.
- Todo artefacto debe justificar su utilidad en la intervención.
- Si se usan subagentes internos, preferir `user-invocable: false` cuando aplique.

## Criterio de aceptación

Existe una superficie nueva o ampliada en `mod/` que hace operable la future-machine sin obligar a reescribir manualmente el workflow cada vez.