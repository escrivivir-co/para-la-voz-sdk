---
description: "Estado canónico del lore activo. Fuente única de verdad para conteos y estado del pipeline."
applyTo: "DRAFTS2/**"
---

# Estado canónico del lore — mod legislativa

> **Baseline:** caso Zoowoman / Feo
> **Fecha de corte:** 19-abr-2026
> **Quién actualiza:** `@Pipeline` (Paso 5) · `@Archivero` (tras merge) · manual si hay piezas fuera de pipeline

---

## 1. Conteo de piezas por tipo

| Tipo | Total | Marcas | Emergencias (+) |
|------|-------|--------|-----------------|
| `P-*` | 9 | P-01 … P-09 | — |
| `S-*` | 13 | S-01 … S-13 | S-04 · S-09 · S-10 · S-11 · S-12 · S-13 |
| `N-*` | 5 | N-01 … N-05 | N-04 · N-05 |
| `T-*` | 14 | T-01 … T-14 | — |
| `R-*` | 10 | R-01 … R-10 | R-09 · R-10 |
| **Total** | **51** | | |

> La regla de conteo y qué suma o no suma está en `lore-schema.instructions.md §6`.

---

## 2. Nodos del grafo

| Métrica | Valor |
|---------|-------|
| Nodos totales (universo-1) | 19 |
| Ramas activas | 4 (R1, R2, R3, R4) |
| Universos instanciados | 1 (universo-1) |
| Huecos abiertos | 4 (H2, H3, H4, H5) |
| Huecos resueltos | 2 (H1 por `[S-10]`, H6 parcial por `[N-05]`) |

> Detalle de nodos y huecos en `DRAFTS2/LORE_F-02_UNIVERSO.md`.

---

## 3. Estado de universos

| Universo | Ramas con nodos propios | Cortos generados | Última actualización |
|----------|-------------------------|------------------|----------------------|
| universo-1 | R4 (6 nodos) | 4 | 18-abr-2026 |

> Los cortos están en `DRAFTS2/LORE_F-02_CORTO-universo-1-*.md`.

---

## 4. Estado de nodos derivados

| Artefacto | Fichero | Fecha de corte | Estado |
|-----------|---------|----------------|--------|
| Hilo narrativo (1ª mitad) | `DRAFTS2/LORE_F.md` | 18-abr-2026 | activo — pendiente refactor editorial |
| Hilo narrativo v2 | `DRAFTS2/LORE_F-02_CORTO.md` | 18-abr-2026 | activo — *Tres Lunes Para Una Misma Sala* |
| Corpus preview | `DRAFTS2/CORPUS_PREVIEW.md` | 18-abr-2026 | activo — 51 piezas procesadas |
| Artefacto grafo | `DRAFTS2/LORE_F-02_ARTEFACTO.md` | 17-abr-2026 | activo |
| Universo-1 | `DRAFTS2/LORE_F-02_UNIVERSO.md` | 18-abr-2026 | activo — R4 expandida |

---

## 5. Piezas pendientes de integrar

| Pieza | Fichero | Estado |
|-------|---------|--------|
| `[S-12]`, `[S-13]` | `LORE_S-12.md`, `LORE_S-13.md` | Emergencias (+) creadas — pendientes de pasar por Bartleby |
| `[R-10]` | `LORE_R-10.md` | Emergencia (+) creada — pendiente de pasar por Bartleby |
| `LORE_F.md` | — | Pendiente refactor editorial (ver `LORE_DRAFT_CORE.md`) |

---

## 6. Cómo actualizar este fichero

### Tras un merge de Archivero

1. Actualizar §1 (conteo por tipo y total).
2. Añadir emergencias (+) si las hay.
3. Actualizar `Fecha de corte`.

### Tras un refresh de Pipeline

1. Actualizar §4 (estado de nodos derivados).
2. Actualizar §5 si hay piezas nuevas pendientes de integrar.

### Tras diseño de universo nuevo

1. Añadir fila en §3 (universos).
2. Actualizar §2 (nodos totales, ramas activas, universos instanciados).

### Tras resolución de hueco

1. Mover hueco de "abiertos" a "resueltos" en §2.
2. Anotar qué pieza lo resuelve.
