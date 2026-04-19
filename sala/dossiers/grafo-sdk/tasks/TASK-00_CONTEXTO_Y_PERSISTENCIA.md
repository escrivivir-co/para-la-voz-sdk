# TASK-00 — Contexto y persistencia

> **Estado:** cerrada
> **Agente:** Claude Opus 4.6
> **Fecha:** 19-abr-2026

## Contexto congelado

### Estado del grafo hoy

El grafo de bifurcación del mod legislativa:
- **Gramática JSON:** `DRAFTS2/grafo/gramatica.md` — 4 tipos de nodo (estado, bifurcacion, rama, hueco), arcos dirigidos con peso, huecos explícitos
- **Datos:** `DRAFTS2/grafo/` — index.json, nodos.json (19 nodos), arcos.json, huecos.json
- **Grafo Markdown (legacy):** `DRAFTS2/LORE_F-02_UNIVERSO.md` — 19 nodos, 4 ramas, pivote X
- **Agentes consumidores:** `@Grafista` (construye), `@Demiurgo` (instancia), `@Dramaturgo Cortos` (genera obras)

### Qué ya es SDK genérico

- `futures-engine` skill — Fases 1-5, bifurcación dramatúrgica portable
- `@Dramaturgo` — diseñador de universos, usa futures-engine
- `@Archivero` SDK — gestiona corpus (input del grafo)

### Qué queda en el mod

- Tipos de nodo concretos (estado, bifurcacion, rama, hueco)
- Campos concretos por nodo (plausibilidad, piezas_ancla, metadatos)
- Reglas de validación (nodo solo acepta piezas del corpus)
- Cadena Grafista → Demiurgo → Dramaturgo Cortos
- Los datos del caso

### Dossier archivado de referencia

`sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-grafo-json/` — 7 tasks completadas que crearon la gramática JSON y migraron el grafo de Markdown a JSON. Ese dossier fue mod-specific; este dossier extrae el concepto genérico al SDK.

### Decisión del PO

"Sacar la feature a main-sdk, y traer aquí, y entonces homogeneizar." — patrón idéntico a lore-db-sdk.
