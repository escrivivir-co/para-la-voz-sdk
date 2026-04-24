# TASK-06 — Actualizar Pipeline handoffs

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** CA-01..CA-05
> **Entrega esperada:** edición de `mod/agents/pipeline.agent.md`

## Lee primero

- [Plan local §4 — cadena completa](../PLAN_CADENA_AGENTICA.md)
- [pipeline.agent.md](../../../mod/agents/pipeline.agent.md) — estado actual
- Todos los agentes tras sus respectivos refactors

## Objetivo

Asegurar que Pipeline tiene handoffs a los 5 agentes de la cadena y que su refresh refleja la secuencia correcta.

## Cambios esperados

1. **agents** en frontmatter — añadir `Puzzle` y `Demiurgo`. Lista final: `[Bartleby, Archivero, Puzzle, Archivero Lore, Grafista, Demiurgo, Dramaturgo Cortos]`.
2. **handoffs** — añadir:
   ```yaml
   - label: Validar pack de lore
     agent: Puzzle
     prompt: Valida las piezas del lore antes de re-ingestar.
     send: true
   - label: Diseñar universo
     agent: Demiurgo
     prompt: Diseña un universo desde el grafo actual.
     send: false
   ```
3. **Protocolo de refresh** — el Paso 0 (inventario) puede delegar a Puzzle en lugar de inventariar por cuenta propia.

## Criterio de aceptación

Pipeline recorre toda la cadena: Puzzle → Archivero Lore → Grafista → Demiurgo → Dramaturgo Cortos. Cada handoff es funcional.
