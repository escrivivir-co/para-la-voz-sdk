# TASK-04 — Documentar piezas en copilot-instructions.md

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** PS-01, PS-02
> **Entrega esperada:** edición de `.github/copilot-instructions.md`

## Lee primero

- [Plan §4.5](../PLAN.md)
- `.github/copilot-instructions.md` — estado actual

## Objetivo

Documentar el concepto de piezas en las instrucciones generales del SDK.

## Cambios esperados

1. **Nueva sección "Piezas del lore"** en `copilot-instructions.md`:
   - Qué es una pieza
   - Variable `{{LORE_DIR}}` y dónde se resuelve
   - Estructura esperada: `{{LORE_DIR}}/INDEX.md`, ficheros de pieza `LORE_{tipo}-{NN}.md`
   - Referencia a `pieza-schema.instructions.md` para el protocolo de tipos
   - Referencia a `pieza-index.template.md` para crear inventarios nuevos
   - Referencia a `pieza-schema.template.md` para definir tipos nuevos

2. **Actualizar la tabla "Capas del repositorio"** si es necesario para reflejar la nueva estructura.

## Criterio de aceptación

Un agente que lea copilot-instructions.md entiende qué son las piezas, dónde viven, y cómo un mod las define.
