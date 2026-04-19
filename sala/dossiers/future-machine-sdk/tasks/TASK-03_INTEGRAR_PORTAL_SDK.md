# TASK-03 — Integrar Portal SDK con la future-machine

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** FS-01, FS-05, FS-06
> **Entrega esperada:** edición de `.github/agents/portal.agent.md`

## Lee primero

1. `.github/agents/portal.agent.md` — Portal SDK actual
2. `.github/instructions/future-machine-schema.instructions.md` (FS-01) — schema de slots
3. `.github/agents/pipeline.agent.md` (FS-05) — Pipeline SDK
4. Los 3 prompts de entrypoint (FS-06)
5. `mod/agents/portal.agent.md` en mod/legislativa — override rico de referencia

## Objetivo

Permitir que el Portal SDK reconozca una machine declarada por el mod y la presente como ciclo completo cuando exista. Debe delegar la navegación a los entrypoints (`/machine-start`, `/machine-status`, `/machine-refresh`) y al `@Pipeline`.

## Debe cubrir

1. Detección de `FUTURE_MACHINE.md` — si existe, Portal está en modo "machine completa"
2. Presentación resumida del ciclo completo leyendo slots del manifest
3. Handoff a `@Pipeline` para refresh y a los prompts de entrypoint para navegación
4. Compatibilidad con mods que no tengan future-machine: degrade a modo básico (corpus-only)

## Criterio de aceptación

- Portal SDK puede navegar la machine sin imponer nombres concretos de prompt al mod
- Portal degrada graceful cuando no hay machine (sigue ofreciendo corpus-based Q&A)
- Portal usa `@Pipeline` como fuente de verdad para el estado del ciclo