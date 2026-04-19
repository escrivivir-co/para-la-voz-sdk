# TASK-01 — Migrar los cortos existentes a `lore/derivados/cortos/`

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CL-00, LP-01b, UL-01
> **Entrega esperada:** `lore/derivados/cortos/` con 5 cortos migrados

## Lee primero

- [Plan §6.1](../PLAN.md)
- `DRAFTS2/LORE_F-02_CORTO*.md`

## Objetivo

Mover las obras derivadas existentes a una carpeta propia dentro de `lore/`, preservando historial y sufijos de modelo.

## Cambios esperados

1. Crear/usar `lore/derivados/cortos/`
2. `git mv DRAFTS2/LORE_F-02_CORTO*.md lore/derivados/cortos/`
3. Verificar que no hay colisiones ni pérdida de trazabilidad

## Criterio de aceptación

Los cortos existentes viven en `lore/derivados/cortos/` con historial preservado.