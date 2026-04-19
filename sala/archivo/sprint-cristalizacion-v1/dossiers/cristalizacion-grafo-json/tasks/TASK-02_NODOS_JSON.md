# TASK-02 — Nodos JSON

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** GJ-01
> **Entrega esperada:** `DRAFTS2/grafo/nodos.json`

## Lee primero

- [Plan local §4.3 — Schema de nodos](../PLAN_GRAFO_JSON.md)
- [LORE_F-02_UNIVERSO.md](../../LORE_F-02_UNIVERSO.md) — fuente Markdown a migrar
- [gramatica.md](../../grafo/gramatica.md) — reglas de formato (debe existir)

## Objetivo

Migrar todos los nodos del grafo Markdown a `nodos.json`. Incluye: 8 nodos T0, 4 direcciones X, nodos de las 4 ramas.

## Plan de migración

1. Extraer nodos T0 (§T=0 de UNIVERSO.md): IDs 0.1–0.8.
2. Extraer pivote X: IDs X-A, X-B, X-C, X-D.
3. Extraer nodos de ramas R1–R4: IDs según detalle de cada rama.
4. Para cada nodo: verificar que las piezas ancla existen como marcas válidas.
5. Asignar tipo (`estado`, `bifurcacion`, `rama`) según estrato.

## Criterio de aceptación

`nodos.json` contiene al menos 19 nodos. Todas las piezas ancla son marcas válidas del corpus. El formato cumple `gramatica.md`.
