---
name: lore-status
description: "Estado completo del lore cargado: piezas por tipo, grafo, universos, cortos, dossiers activos y salud del pipeline."
agent: Portal
tools: [vscode, read, search]
---

# /lore-status — Estado del lore legislativa

Produce el informe de estado específico del lore cargado. Extiende el `/status` del SDK (que muestra el corpus Bartleby) con la capa de datos concretos del caso.

## Qué haces

1. Lee `mod/instructions/onboarding-map.instructions.md` — para presentar el mismo mapa como cabecera.
2. Lee las fuentes de estado en este orden:
   - `mod/instructions/lore-estado.instructions.md` (si existe) — fuente canónica
   - Si no existe: `DRAFTS2/LORE_INDEX.md` + exploración de disco como fallback
3. Produce el informe completo.

## Formato del informe

```markdown
# Estado del Lore — mod/legislativa
**Fecha:** [hoy]
**Caso:** Zoowoman / caso Feo

─────────────────────────────────────

## Piezas del lore

| Tipo | Conteo | Marcas |
|------|--------|--------|
| P-* (personajes) | N | P-01..P-09 |
| S-* (social) | N | S-01..S-13 |
| N-* (noticias) | N | N-01..N-05 |
| T-* (fases) | N | T-01..T-14 |
| R-* (recursos) | N | R-01..R-10 |
| **Total** | **N** | |

**Hilo narrativo:** LORE_F.md — [estado: absorbe N piezas]
**Corpus:** CORPUS_PREVIEW.md — [fecha de última generación]

─────────────────────────────────────

## Grafo de bifurcación

| Métrica | Valor |
|---------|-------|
| Nodos totales | N |
| Ramas activas | R1, R2, R3, R4 |
| Pivote X | [N direcciones] |
| Huecos abiertos | N (H1..HN) |
| Formato | [Markdown / JSON / ambos] |

─────────────────────────────────────

## Universos instanciados

| Universo | Rama | Estado | Cortos generados |
|----------|------|--------|------------------|
| universo-1 | R4 | activo | N modelos |
| universo-1-r1 | R1 | activo | — |
| universo-1-r2 | R2 | activo | — |

─────────────────────────────────────

## Cortos generados

| Fichero | Universo | Modelo |
|---------|----------|--------|
| LORE_F-02_CORTO.md | original | — |
| LORE_F-02_CORTO-universo-1-*.md | universo-1 | [modelo] |

─────────────────────────────────────

## Dossiers de cristalización activos

| Dossier | Estado | Tasks completadas/total |
|---------|--------|------------------------|
| pipeline-operativo | abierto | N/N |
| cadena-agentica | abierto | N/N |
| grafo-json | abierto | N/N |
| finalizacion-lore-plan | abierto | N/N |
| future-machine-universo-1 | abierto | N/N |

─────────────────────────────────────

## Salud del pipeline

| Nodo | Estado |
|------|--------|
| Piezas → Corpus | [sincronizado / desfasado] |
| Corpus → Grafo | [sincronizado / desfasado / no migrado] |
| Grafo → Universos | [sincronizado / pendiente] |
| Universos → Cortos | [sincronizado / pendiente] |
```

## Cómo calculas cada bloque

### Piezas
Lee `DRAFTS2/LORE_INDEX.md` o `lore-estado`. Lista ficheros `LORE_*.md` por tipo.

### Grafo
Lee `DRAFTS2/grafo/index.json` (si existe) o `DRAFTS2/LORE_F-02_UNIVERSO.md`. Cuenta nodos, ramas, huecos.

### Universos
Lee `DRAFTS2/universo/`. Lista ficheros `universo-*.md`.

### Cortos
Lee `DRAFTS2/LORE_F-02_CORTO*.md`. Extrae modelo del nombre de fichero.

### Dossiers
Lee cada `DRAFTS2/cristalizacion-*/BACKLOG_*.md` y `DRAFTS2/finalizacion-*/BACKLOG_*.md`. Cuenta tasks completadas vs total.

### Salud del pipeline
Compara fechas de modificación de los nodos principales. Si CORPUS_PREVIEW es más antiguo que las piezas, está desfasado.

## Tono

Limpio, tabular, sin opinión. Es un dashboard, no un ensayo. Ofrece al final: "¿Quieres profundizar en algún bloque?" con handoffs al agente apropiado.
