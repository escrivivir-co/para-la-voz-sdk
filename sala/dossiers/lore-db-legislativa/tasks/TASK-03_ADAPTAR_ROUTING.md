# TASK-03 — Adaptar lore-routing con {{LORE_DIR}}

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** LP-01
> **Entrega esperada:** edición de `mod/instructions/lore-routing.instructions.md`

## Lee primero

- [Plan §4.3](../PLAN.md)
- `mod/instructions/lore-routing.instructions.md` — estado actual

## Objetivo

Actualizar el routing para usar `{{LORE_DIR}}` y reflejar la ubicación definitiva de las piezas (decidida en LP-01).

## Cambios esperados

1. **Variable nueva:** `{{LORE_DIR}}` → ruta decidida en LP-01
2. **Tabla de routing:** actualizar todas las filas que usan `DRAFTS2/` → `{{LORE_DIR}}/`
3. **Eliminar workaround:** si la ubicación es definitiva, eliminar el carácter temporal del fichero
4. **Condición de expiración:** actualizar o eliminar según decisión

## Criterio de aceptación

Todos los agentes que lean lore-routing pueden resolver `{{LORE_DIR}}` y llegar a las piezas.
