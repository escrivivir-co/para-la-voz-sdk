# TASK-04 — Actualizar instrucciones de universo

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** PO-02
> **Entrega esperada:** edición de `mod/instructions/legislativa-universo.instructions.md`

## Lee primero

- [Plan local §4 — Propuesta P4](../PLAN_PIPELINE_OPERATIVO.md)
- [legislativa-universo.instructions.md](../../../mod/instructions/legislativa-universo.instructions.md) — fichero actual
- [lore-estado.instructions.md](../../../mod/instructions/lore-estado.instructions.md) — fuente de verdad de conteos (debe existir)

## Objetivo

Eliminar conteos y estado duplicados de `legislativa-universo.instructions.md`. Dejar solo lo específico de universos.

## Cambios esperados

1. **Eliminar §"Estado del corpus"** — los conteos (48 piezas, tabla de piezas añadidas) se mueven a `lore-estado.instructions.md`. Este fichero referencia al estado canónico en lugar de mantener cifras propias.

2. **Mantener sin cambios:**
   - Estructura temporal del universo (T=0, X, T+∞)
   - El corto original vs el universo
   - Huecos del universo-1
   - Datos duros que el corto debe poder usar
   - Consignas del corpus
   - Nota sobre metáforas drenadas

3. **Añadir referencia:** una línea al inicio que diga "Para conteos y estado del lore, ver `lore-estado.instructions.md`".

## Restricciones

- No reescribir secciones que funcionan. Solo eliminar duplicación de conteos.
- Los datos duros se quedan aquí porque son instrucciones específicas de universo, no de estado general.

## Criterio de aceptación

El fichero no contiene ningún conteo de piezas que pueda quedar desactualizado. Todo conteo se lee desde `lore-estado.instructions.md`.
