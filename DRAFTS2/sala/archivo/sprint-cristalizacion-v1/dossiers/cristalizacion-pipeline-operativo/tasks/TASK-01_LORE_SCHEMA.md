# TASK-01 — Esquema de tipos de pieza del lore

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** PO-00
> **Entrega esperada:** `mod/instructions/lore-schema.instructions.md`

## Lee primero

- [Plan local §4 — Diálogo simulado](../PLAN_PIPELINE_OPERATIVO.md)
- [LORE_PLAN.md §3.1](../../LORE_PLAN.md) — regla por formato (tabla de tipos)
- [LORE_PLAN.md §5](../../LORE_PLAN.md) — Definition of Ready
- [LORE_PLAN.md §6](../../LORE_PLAN.md) — Definition of Done
- [LORE_INDEX.md](../../LORE_INDEX.md) — inventario actual y convenciones
- [COPILOT/instructions.instructions.md](../../../COPILOT/instructions.instructions.md) — referencia de instructions files

## Objetivo

Crear un fichero de instrucciones que defina el esquema normativo de tipos de pieza del lore legislativa como ontología del mod, no del caso.

## Contenido esperado

1. **Tabla de tipos** — cada tipo de pieza (P-\*, S-\*, N-\*, T-\*, R-\*, F) con:
   - Descripción funcional
   - Campos obligatorios del frontmatter o cabecera
   - Campos opcionales
   - Regla de soporte (¿fichero propio? ¿raw `.txt`? ¿investigación externa?)
   - Ejemplo mínimo

2. **Convenciones de nombrado** — `LORE_<TIPO>-<NN>.md`, marcas estables, sufijo (+) para emergencias.

3. **Definition of Ready operativa** — derivada de LORE_PLAN.md §5, adaptada para consumo agéntico (condiciones verificables por un agente, no solo por humano).

4. **Definition of Done operativa** — derivada de LORE_PLAN.md §6, misma adaptación.

5. **Regla de conteo** — qué suma al total, qué no (soportes no suman salvo que sean piezas nuevas marcadas con (+)).

## Frontmatter sugerido

```yaml
---
description: "Esquema normativo de tipos de pieza del lore legislativa. Define ontología, campos obligatorios, DoR/DoD y reglas de conteo."
applyTo: "DRAFTS2/LORE_*.md"
---
```

## Restricciones

- No copiar la tabla de LORE_PLAN.md verbatim: transformarla en spec consumible por agentes.
- El esquema es genérico del mod legislativa. Los datos concretos del caso Feo no aparecen aquí.
- No inventar campos que el lore actual no use. Formalizar lo que ya existe.

## Criterio de aceptación

Un agente que lea este fichero puede responder sin ambigüedad: "¿esta pieza tiene formato válido?", "¿cumple DoR?", "¿qué campos le faltan?".
