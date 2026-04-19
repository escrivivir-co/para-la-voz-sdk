---
description: "Mapa temporal de rutas canónicas del SDK hacia DRAFTS2. Caduca cuando el lore se mueva a su ubicación definitiva."
applyTo: "mod/**,corpus/**"
---

# Mapa de rutas canónicas — mod legislativa

> **Estado:** workaround activo mientras el lore viva en `DRAFTS2/`.
> **Condición de expiración:** este fichero se elimina cuando el lore migre a su ubicación definitiva fuera de `DRAFTS2/`.
> **Instrucción operativa:** cuando un agente necesite leer una ruta canónica del SDK, consulta esta tabla primero. Si la ruta buscada no aparece, es un bug de este fichero — repórtalo.

---

## Tabla de routing

| Ruta canónica SDK | Ruta real actual | Notas |
|-------------------|-----------------|-------|
| `corpus/corpus.md` | `DRAFTS2/CORPUS_PREVIEW.md` | Mapa acumulativo: 51 piezas, taxonomía y linajes |
| `corpus/documentos/` | `DRAFTS2/LORE_*.md` | Piezas numeradas (A…F, P-*, S-*, N-*, T-*, R-*) |
| `corpus/analisis/` | *(no existe todavía)* | Pendiente: informes Bartleby por pieza |
| `mod/universos/` | `DRAFTS2/universo/` | Ramas expandidas (universo-1-r1.md, universo-1-r2.md, universo-1.md) — `mod/universos/` tiene README de redirección |
| `mod/universos/universo-1` | `DRAFTS2/LORE_F-02_UNIVERSO.md` | Grafo maestro: 19 nodos, 4 ramas, huecos |
| `grafo/` (JSON) | `DRAFTS2/grafo/` | **Pendiente — no existe todavía.** Se creará en Track GJ (`cristalizacion-grafo-json/`) |
| `artefacto` | `DRAFTS2/LORE_F-02_ARTEFACTO.md` | Spec de construcción del grafo y universo |
| `hilo narrativo (1ª mitad)` | `DRAFTS2/LORE_F.md` | T-∞ → T=0. Pendiente refactor editorial |
| `hilo narrativo (corto)` | `DRAFTS2/LORE_F-02_CORTO.md` | *Tres Lunes Para Una Misma Sala* |
| `hilo narrativo (cortos por modelo)` | `DRAFTS2/LORE_F-02_CORTO-universo-1-*.md` | 4 versiones generadas por modelo |
| `índice del lore` | `DRAFTS2/LORE_INDEX.md` | Inventario de marcas, conteos y convenciones |
| `plan de producción` | `DRAFTS2/LORE_PLAN.md` | Guía de trabajo, tipos, DoR/DoD, carriles |
| `mod/instructions/lore-schema` | `mod/instructions/lore-schema.instructions.md` | Esquema de tipos de pieza (generado PO-01) |
| `mod/instructions/lore-estado` | `mod/instructions/lore-estado.instructions.md` | Estado canónico y conteos (generado PO-02) |

---

## Rutas del SDK base que el mod extiende

| Ruta SDK | Ruta mod | Notas |
|----------|----------|-------|
| `.github/agents/` | `mod/agents/` | Agentes del mod (archivero-lore, grafista, etc.) |
| `.github/skills/` | `mod/skills/` | Skills del mod (cristalizacion-feature, etc.) |
| `.github/prompts/` | `mod/prompts/` | Prompts del mod (sala-entrar, sala-aleph, etc.) |
| `.github/instructions/` | `mod/instructions/` | Instructions del mod (lore-schema, lore-estado, lore-routing, etc.) |

---

## Notas de migración

Cuando el lore salga de `DRAFTS2/`:

1. `corpus/documentos/` pasa a contener los ficheros `LORE_*.md` directamente.
2. `corpus/analisis/` pasa a contener los informes Bartleby.
3. `corpus/corpus.md` pasa a ser el corpus real (no el workaround actual).
4. `mod/universos/` pasa a contener los ficheros de universo directamente.
5. `grafo/` pasa a ser la ruta canónica del grafo JSON.
6. Este fichero se elimina.
