# TASK-02 — Refactor Archivero Lore

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** CA-01
> **Entrega esperada:** edición de `mod/agents/archivero-lore.agent.md`

## Lee primero

- [Plan local §4.2 — Archivero Lore](../PLAN_CADENA_AGENTICA.md)
- [archivero-lore.agent.md](../../../mod/agents/archivero-lore.agent.md) — estado actual
- [TASK-01 (Puzzle)](./TASK-01_PUZZLE.md) — para entender qué asume del input

## Objetivo

Refactorizar el Archivero Lore para que asuma input pre-verificado por Puzzle. Eliminar la lógica de inventario/validación de su operación `ingest`.

## Cambios esperados

1. **Paso 1 de `ingest`** — actualmente "Inventariar": reducir a "Recibir pack del Puzzle". No re-verifica tipos ni conteos, asume validado.
2. **agents** en frontmatter — añadir `Puzzle` como agente referenciado.
3. **handoffs** — añadir handoff inverso: "Pedir validación de piezas" → Puzzle.
4. **Descripción** — actualizar para reflejar que el inventario lo hace Puzzle.

## Qué NO se toca

- Las operaciones `diff`, `merge`, `status` no cambian.
- Los handoffs a Grafista, Bartleby y Pipeline no cambian.
- El paso 2 (análisis batch con Bartleby) no cambia.

## Criterio de aceptación

Archivero Lore no duplica la validación de Puzzle. Su `ingest` empieza directo con el análisis Bartleby.
