# TASK-01 — Schema genérico de piezas

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** PS-00
> **Entrega esperada:** `.github/instructions/pieza-schema.instructions.md` + `.github/templates/pieza-schema.template.md`

## Lee primero

- [Plan §4.1](../PLAN.md)
- `mod/instructions/lore-schema.instructions.md` — el schema concreto de legislativa (referencia)
- `.github/instructions/bartleby-voice.instructions.md` — cómo funcionan las instructions del SDK

## Objetivo

Crear el schema genérico de piezas del SDK. Define **qué es un tipo de pieza** y **qué campos mínimos tiene**, sin fijar tipos concretos.

## Cambios esperados

1. **`.github/instructions/pieza-schema.instructions.md`** — instruction genérica:
   - Qué es una pieza (unidad atómica del lore con marca estable)
   - Qué es un tipo de pieza (prefijo + nombre + campos)
   - Campos mínimos obligatorios para cualquier tipo: `Marca`, `Tipo`, `Estado`, `Bloque principal`
   - Cómo se define DoR / DoD por tipo
   - Regla de conteo (qué suma al total, qué no)
   - Referencia a que el mod concreto define sus tipos en `mod/instructions/`

2. **`.github/templates/pieza-schema.template.md`** — plantilla rellenable:
   - Tabla de ontología vacía (Tipo | Qué es | Fichero propio | ...)
   - Sección por tipo con campos obligatorios/opcionales
   - Sección DoR/DoD
   - Sección reglas de conteo

## Qué NO se toca

- `mod/instructions/lore-schema.instructions.md` no se modifica aquí (se adaptará en el dossier `lore-pipeline-legislativa`)
- No se crean tipos concretos

## Criterio de aceptación

Un mod nuevo puede copiar la template, rellenar sus tipos, y tener un schema funcional sin leer nada de legislativa.
