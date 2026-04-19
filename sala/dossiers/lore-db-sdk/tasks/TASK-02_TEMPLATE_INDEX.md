# TASK-02 — Template de inventario de piezas

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** PS-00
> **Entrega esperada:** `.github/templates/pieza-index.template.md`

## Lee primero

- [Plan §4.2](../PLAN.md)
- `DRAFTS2/LORE_INDEX.md` — el inventario concreto de legislativa (referencia)

## Objetivo

Crear la plantilla genérica de inventario de piezas que cualquier mod pueda usar.

## Cambios esperados

1. **`.github/templates/pieza-index.template.md`** — plantilla rellenable:
   - Cabecera con metadata (estado, fecha de corte, total de piezas)
   - Tabla índice de bloques (Bloque | Título | Piezas | Fichero)
   - Sección de ficheros de soporte por pieza
   - Convenciones de marcas (formato `[X-NN]`, estabilidad de marcas)
   - Variable `{{PIEZA_DIR}}` para la ruta base

## Qué NO se toca

- `DRAFTS2/LORE_INDEX.md` se queda tal cual
- No se migran piezas existentes

## Criterio de aceptación

Un mod nuevo puede copiar la template y rellenar su inventario de piezas sin leer el LORE_INDEX de legislativa.
