# TASK-04 — Formalizar grafo de dependencias del pipeline

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** LP-02
> **Entrega esperada:** `mod/instructions/lore-pipeline.instructions.md`

## Lee primero

- [Plan §4.4, §4.6](../PLAN.md)
- `DRAFTS2/FEAT-06_PIPELINE_REFRESH.md` — grafo de dependencias original
- `mod/agents/pipeline.agent.md` — orquestador actual
- `mod/instructions/lore-estado.instructions.md` — estado de nodos derivados

## Objetivo

Crear `mod/instructions/lore-pipeline.instructions.md` que documente el pipeline completo de legislativa: piezas → corpus → grafo → universos → cortos.

## Contenido esperado

1. **Grafo de dependencias** — el ASCII art de FEAT-06 pero formalizado:
   ```
   piezas ({{PIEZA_DIR}}/LORE_*.md)
      ↓
   ┌──────────────────────┐
   │ CORPUS_PREVIEW (∥)   │ ← Archivero Lore + Bartleby
   │ LORE_F (∥)           │ ← hilo narrativo
   └──────────────────────┘
      ↓ (join)
   ARTEFACTO              ← spec de grafo
      ↓
   UNIVERSO               ← grafo de bifurcación
      ↓
   ramas expandidas       ← universo/universo-1.md
      ↓
   cortos                 ← Dramaturgo Cortos
   ```

2. **Tabla agente → nodo** — qué agente produce cada nodo del grafo

3. **Condiciones de refresh** — cuándo se refresca cada nodo (de FEAT-06 §Paso 1-4)

4. **Handoffs entre agentes** — quién pasa a quién y con qué input

5. **Regla de paralelismo** — CORPUS_PREVIEW y LORE_F son hermanos, se refrescan en paralelo

## Criterio de aceptación

Un agente que lea esta instruction entiende cómo se conecta todo el pipeline sin leer FEAT-06 ni los agentes individuales.
