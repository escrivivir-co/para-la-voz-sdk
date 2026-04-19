# TASK-05 — Recablear Dramaturgo Cortos

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** CA-04
> **Entrega esperada:** edición de `mod/agents/dramaturgo.agent.md`

## Lee primero

- [Plan local §4.5 — Dramaturgo Cortos](../PLAN_CADENA_AGENTICA.md)
- [dramaturgo.agent.md](../../../mod/agents/dramaturgo.agent.md) — estado actual
- [TASK-04 (Demiurgo)](./TASK-04_DEMIURGO.md) — para entender el nuevo proveedor de universos

## Objetivo

Recablear el Dramaturgo Cortos para que reciba universos del Demiurgo en lugar del Grafista.

## Cambios esperados

1. **agents** en frontmatter — sustituir `Grafista` por `Demiurgo`.
2. **handoffs** — cambiar:
   - "Actualizar grafo antes de generar → Grafista" → "Pedir universo actualizado → Demiurgo"
3. **Fuentes que lees** — sin cambios (sigue leyendo los mismos ficheros).
4. **Operación principal** — sin cambios funcionales. Solo la procedencia del universo es distinta.

## Qué NO se toca

- El protocolo de generación de cortos.
- El skill base (futures-engine Fase 5, voice-crystallization).
- La regla de desincronización.
- El handoff a Pipeline.

## Criterio de aceptación

Dramaturgo Cortos no referencia al Grafista como proveedor directo. El handoff de "actualizar" apunta a Demiurgo.
