# TASK-03 — Refactor Grafista

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** CA-00
> **Entrega esperada:** edición de `mod/agents/grafista.agent.md`

## Lee primero

- [Plan local §4.3 — Grafista](../PLAN_CADENA_AGENTICA.md)
- [grafista.agent.md](../../../mod/agents/grafista.agent.md) — estado actual (mezcla grafo + universo)
- [futures-engine SKILL.md](../../../.github/skills/futures-engine/SKILL.md) — Fases 1-3 son las del Grafista

## Objetivo

Refactorizar el Grafista para que **solo construya el grafo**. Toda la lógica de generación de universos se mueve al Demiurgo (CA-04).

## Cambios esperados

1. **description** en frontmatter — cambiar "genera el artefacto de construcción y el grafo de universo" → "genera el grafo de bifurcación dramatúrgica".
2. **handoffs** — eliminar handoff directo a "Dramaturgo Cortos". Añadir handoff a "Demiurgo":
   ```yaml
   - label: Diseñar universo desde grafo
     agent: Demiurgo
     prompt: El grafo está listo. Diseña el universo seleccionando ramas.
     send: false
   ```
3. **agents** — añadir `Demiurgo` (cuando exista). Eliminar referencia directa a Dramaturgo Cortos.
4. **Skill base** — mantener futures-engine Fases 1-3. Eliminar cualquier referencia a Fases 4-5.
5. **Operación principal** — el output es solo el grafo (UNIVERSO.md o JSON). No instancia universos.
6. **Sección de pasos** — eliminar pasos de generación de ramas expandidas. Solo: detectar nodos, clasificar, estructurar grafo, presentar.

## Qué se preserva

- Lectura de CORPUS_PREVIEW + LORE_F + ARTEFACTO.
- Detección de nodos de bifurcación (Fase 3 futures-engine).
- Metadatos del grafo (huecos, plausibilidades, estatuto dato/relato).
- Handoffs a Archivero Lore y Pipeline.

## Criterio de aceptación

Grafista no contiene la palabra "universo" como cosa que él genera. Solo construye y estructura el grafo. El handoff a Demiurgo es explícito.
