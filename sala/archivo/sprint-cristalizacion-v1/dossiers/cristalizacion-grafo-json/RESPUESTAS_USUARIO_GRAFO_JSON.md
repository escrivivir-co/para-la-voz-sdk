# Respuestas del usuario — Cristalización del grafo JSON

> **Fecha:** 19-abr-2026
> **Registradas por:** `Claude Opus 4.6`
> **Propósito:** fijar las decisiones de PO, scrum master y cliente en disco.

## Punto 1 — Grafo en formato JSON (cliente)

- **Decisión del cliente:** El grafo pasa de Markdown narrativo a una gramática JSON estructurada. Los agentes necesitan consumir nodos, arcos y huecos de forma programática, no parseando prosa.
- **Efecto operativo:** Se crea `DRAFTS2/grafo/` con 4 ficheros JSON + 1 spec legible.

## Punto 2 — Vocabulario cerrado al corpus (cliente)

- **Decisión del cliente:** El grafo solo acepta como piezas ancla términos que existan en `CORPUS_PREVIEW.md`. Si un nodo cita `[S-99]` y esa pieza no existe, es error.
- **Efecto operativo:** La validación de vocabulario es un step explícito (GJ-06). El Grafista debe validar al escribir.

## Punto 3 — Markdown legacy se preserva (PO)

- **Decisión del PO:** `LORE_F-02_UNIVERSO.md` no se elimina. Se marca como legacy y referencia. El JSON es la fuente de verdad hacia adelante.
- **Efecto operativo:** El routing tendrá dos entradas: legacy (Markdown) y canónica (JSON).

## Punto 4 — Gramática genérica del mod, datos del caso (PO + cliente)

- **Decisión compartida:** La gramática (tipos de nodo, reglas de arcos, formato de huecos) es del mod legislativa. Los datos concretos (los 19 nodos, las 4 ramas) son del caso Feo.
- **Efecto operativo:** La spec `gramatica.md` es reutilizable para otro caso legislativa. Los JSON son instancia.
