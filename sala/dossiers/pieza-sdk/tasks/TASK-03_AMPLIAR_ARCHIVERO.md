# TASK-03 — Ampliar @archivero SDK con concepto de piezas

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** PS-01
> **Entrega esperada:** edición de `.github/agents/archivero.agent.md`

## Lee primero

- [Plan §4.4](../PLAN.md)
- `.github/agents/archivero.agent.md` — estado actual del archivero SDK
- `mod/agents/archivero-lore.agent.md` — cómo lo extiende legislativa
- `mod/agents/puzzle.agent.md` — validador de piezas (referencia de qué extraer)

## Objetivo

El @archivero SDK hoy solo sabe de `corpus/corpus.md` y análisis individuales. Ampliar para que sepa que un mod puede tener piezas tipadas:

1. **Nueva sección "Piezas del lore"** — explica que un mod puede definir piezas con inventario en `{{PIEZA_DIR}}/INDEX.md` y schema en `mod/instructions/`
2. **Operación `status` ampliada** — si existe un inventario de piezas, incluirlo en el reporte
3. **Handoff a Puzzle** — si el mod define un agente de validación, referenciarlo
4. **No se añade `ingest`** — eso lo aporta el mod con su extensión del archivero

## Qué NO se toca

- Las operaciones diff/merge no cambian
- No se crean tipos concretos
- No se importa lógica de `archivero-lore`

## Criterio de aceptación

El `@archivero` SDK entiende que pueden existir piezas, puede reportar su estado, y delega al mod la definición concreta de tipos y la ingesta.
