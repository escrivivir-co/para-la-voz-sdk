# Dossier — gap-corto-universo

> **Origen:** BL-01 del sprint-cristalizacion-v1
> **Prioridad:** media
> **Tasks estimadas:** 1

## Contexto

FM-05 detectó que `mod/prompts/corto-universo.prompt.md` no existe. El flujo `/corto-universo` funciona por invocación directa del agente Dramaturgo Cortos, pero no hay prompt formal que lo encapsule. Los 4 cortos ya generados demuestran que la cadena es funcional.

## Objetivo

Crear `mod/prompts/corto-universo.prompt.md` que formalice el flujo de generación de cortos desde un universo.

## Referencia

- `mod/prompts/dramaturgo-editar-universo.prompt.md` (prompt existente, posible base)
- `mod/agents/dramaturgo.agent.md` (agente que ejecuta)
- `DRAFTS2/LORE_F-02_CORTO*.md` (4 cortos como evidencia de output esperado)
- `mod/instructions/legislativa-universo.instructions.md` (reglas del lore)
