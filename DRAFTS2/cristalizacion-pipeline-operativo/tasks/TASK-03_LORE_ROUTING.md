# TASK-03 — Mapa de rutas canónicas

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** PO-02
> **Entrega esperada:** `mod/instructions/lore-routing.instructions.md`

## Lee primero

- [Plan local §4 — Propuesta P2](../PLAN_PIPELINE_OPERATIVO.md)
- [corpus/corpus.md](../../../corpus/corpus.md) — workaround actual
- [mod/universos/README.md](../../../mod/universos/README.md) — si existe, redirección
- [mod/skills/README.md](../../../mod/skills/README.md) — si existe, redirección

## Objetivo

Crear un mapa explícito de rutas canónicas del SDK hacia las rutas reales en DRAFTS2 mientras dure el workaround.

## Contenido esperado

1. **Tabla de routing** — dos columnas: ruta canónica SDK → ruta real actual.

   | Ruta canónica | Ruta real | Notas |
   |---------------|-----------|-------|
   | `corpus/corpus.md` | `DRAFTS2/CORPUS_PREVIEW.md` | mapa acumulativo |
   | `corpus/documentos/` | `DRAFTS2/LORE_*.md` | piezas numeradas |
   | `mod/universos/` | `DRAFTS2/universo/` | ramas expandidas |
   | (grafo principal) | `DRAFTS2/LORE_F-02_UNIVERSO.md` → `DRAFTS2/grafo/` | Pendiente migración a JSON |
   | (grafo JSON) | `DRAFTS2/grafo/` | Cuando exista (ver dossier `cristalizacion-grafo-json/`) |
   | (artefacto) | `DRAFTS2/LORE_F-02_ARTEFACTO.md` | spec de construcción |
   | (hilo narrativo) | `DRAFTS2/LORE_F.md` | primera mitad |
   | (índice del lore) | `DRAFTS2/LORE_INDEX.md` | inventario de piezas |

2. **Condición de expiración** — este fichero se elimina cuando el lore salga de DRAFTS2.

3. **Instrucción operativa** — "cuando un agente necesite leer una ruta canónica, consulta esta tabla primero".

## Frontmatter sugerido

```yaml
---
description: "Mapa temporal de rutas canónicas del SDK hacia DRAFTS2. Caduca cuando el lore se mueva a su ubicación definitiva."
applyTo: "mod/**,corpus/**"
---
```

## Restricciones

- Solo routing. No estado, no esquema, no reglas de universo.
- Debe ser completo: si un agente busca una ruta canónica y no la encuentra aquí, es un bug de este fichero.

## Criterio de aceptación

Se puede eliminar `corpus/corpus.md` como workaround y usar este fichero como fuente. Todos los agentes del mod resuelven rutas desde aquí.
