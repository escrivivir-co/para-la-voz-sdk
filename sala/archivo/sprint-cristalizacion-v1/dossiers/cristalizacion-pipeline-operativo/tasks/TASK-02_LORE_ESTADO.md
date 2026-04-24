# TASK-02 — Estado canónico del lore

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** PO-01
> **Entrega esperada:** `mod/instructions/lore-estado.instructions.md`

## Lee primero

- [Plan local §4 — Propuesta P3](../PLAN_PIPELINE_OPERATIVO.md)
- [LORE_INDEX.md](../../LORE_INDEX.md) — conteos actuales
- [legislativa-universo.instructions.md](../../../mod/instructions/legislativa-universo.instructions.md) — conteos duplicados
- [lore-schema.instructions.md](../../../mod/instructions/lore-schema.instructions.md) — esquema (debe existir cuando se ejecute esta task)

## Objetivo

Crear el fichero de estado canónico del lore activo: la fuente única de verdad para conteos, fecha de corte y baseline.

## Contenido esperado

1. **Conteo por tipo** — tabla con totales por P, S, N, T, R. Incluye marca de emergencia (+).
2. **Total de piezas** — número canónico.
3. **Fecha de corte** — cuándo se actualizó por última vez.
4. **Baseline del caso** — nombre del caso activo (e.g., "Zoowoman / caso Feo").
5. **Piezas pendientes de integrar** — lista de piezas que existen como fichero pero no están incorporadas al pipeline (CORPUS_PREVIEW, LORE_F).
6. **Estado de nodos derivados** — tabla tipo: CORPUS_PREVIEW (fecha), LORE_F (fecha), ARTEFACTO (fecha), UNIVERSO (fecha).
7. **Estado del grafo** — nodos totales, ramas activas, universos instanciados, huecos abiertos. (Añadido 19-abr-2026 tras decisión de cadena de 5 agentes y grafo JSON.)
8. **Estado de universos** — tabla: universo-N (ramas seleccionadas, cortos generados, fecha). (Añadido 19-abr-2026.)

## Frontmatter sugerido

```yaml
---
description: "Estado canónico del lore activo. Fuente única de verdad para conteos y estado del pipeline."
applyTo: "DRAFTS2/**"
---
```

## Quién actualiza este fichero

- `@Pipeline` en su Paso 5 (resumen y handoff) — actualiza conteos y estado de nodos.
- `@Archivero` tras un merge — actualiza conteos de piezas.
- Manualmente si se añaden piezas fuera de pipeline.

## Restricciones

- Solo datos. No reglas, no esquema, no instrucciones de universo.
- El fichero arranca con los valores actuales del caso Feo (51 piezas, 19 nodos, etc.) pero su estructura es genérica.

## Criterio de aceptación

`legislativa-universo.instructions.md` puede eliminar sus conteos propios y referenciar este fichero. Pipeline puede leer conteos sin ambigüedad.
