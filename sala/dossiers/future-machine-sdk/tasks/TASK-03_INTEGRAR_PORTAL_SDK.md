# TASK-03 — Integrar Portal SDK con la future-machine

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** FS-01
> **Entrega esperada:** edición de `.github/agents/portal.agent.md`

## Objetivo

Permitir que el Portal SDK reconozca una machine declarada por el mod y la presente como ciclo completo cuando exista.

## Debe cubrir

1. Detección de entrypoints declarados por la machine.
2. Presentación resumida del ciclo completo cuando el mod tenga future-machine.
3. Compatibilidad con mods que no tengan esta capa aún.

## Criterio de aceptación

- Portal SDK puede navegar la machine sin imponer nombres concretos de prompt al mod.