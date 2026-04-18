# TASK-05 — Validación del pipeline

> **Estado:** pendiente
> **Agente recomendado:** `Pipeline`
> **Dependencias:** PO-01, PO-02, PO-03, PO-04
> **Entrega esperada:** `DRAFTS2/cristalizacion-pipeline-operativo/ENTREGA_PO-05_VALIDACION.md`

## Lee primero

- [Plan local §6 — Validación](../PLAN_PIPELINE_OPERATIVO.md)
- [Agente pipeline](../../../mod/agents/pipeline.agent.md)
- [Protocolo refresh](../../FEAT-06_PIPELINE_REFRESH.md)
- Los 4 artefactos nuevos:
  - [lore-schema.instructions.md](../../../mod/instructions/lore-schema.instructions.md)
  - [lore-estado.instructions.md](../../../mod/instructions/lore-estado.instructions.md)
  - [lore-routing.instructions.md](../../../mod/instructions/lore-routing.instructions.md)
  - [legislativa-universo.instructions.md](../../../mod/instructions/legislativa-universo.instructions.md) (actualizado)

## Objetivo

Verificar que `@Pipeline` puede operar con los nuevos artefactos sin workarounds manuales.

## Secuencia de validación

1. Invocar `@Pipeline /refresh status`.
2. Verificar que el inventario (Paso 0) usa el esquema de `lore-schema` para tipar piezas.
3. Verificar que los conteos reportados coinciden con `lore-estado` (piezas + grafo + universos).
4. Verificar que las rutas se resuelven desde `lore-routing` sin consultar `corpus/corpus.md`.
5. Verificar que `legislativa-universo.instructions.md` no contiene conteos propios.
6. Verificar que los 4 agentes restantes (`@Puzzle`, `@Archivero Lore`, `@Grafista`, `@Demiurgo`) pueden resolver rutas desde `lore-routing`. (Añadido 19-abr-2026.)
7. Documentar resultado: qué funcionó, qué no, qué requiere ajuste.

## Criterio de aceptación

Pipeline completa su Paso 0 (inventario) sin ambigüedad en tipos, conteos ni rutas. Los 5 agentes de la cadena resuelven rutas desde `lore-routing`. Si cualquiera detecta desync, lo señala con referencia a la fuente canónica correcta.
