# TASK-01 — Reconciliar PBIs contra disco

> **Estado:** pendiente
> **Agente recomendado:** `Archivero Lore`
> **Dependencias:** LP-00
> **Entrega esperada:** edición de `LORE_PLAN.md` §8 + informe de delta

## Lee primero

- [LORE_PLAN.md §8](../LORE_PLAN.md) — tabla actual de PBIs
- [LORE_INDEX.md](../../LORE_INDEX.md) — inventario de ficheros reales
- Disco: listar `DRAFTS2/LORE_*.md` para verificar existencia

## Objetivo

Contrastar cada PBI de la tabla §8 contra la realidad del disco:
- ¿El fichero de entrega existe?
- ¿El estado marcado es correcto?
- ¿Hay ficheros en disco que no aparecen en la tabla?

## Secuencia

1. Listar todos los `LORE_*.md` en disco.
2. Para cada PBI: verificar si su entrega existe como fichero.
3. Marcar estado real: Hecho (fichero existe y es sustancial), Pendiente (no existe), Bloqueado (existe pero incompleto o dependencia faltante).
4. Identificar PBIs no previstos (piezas en disco sin PBI en la tabla).
5. Producir tabla corregida.

## Criterio de aceptación

La tabla §8 refleja la realidad del disco sin ambigüedad. Cada estado es verificable.
