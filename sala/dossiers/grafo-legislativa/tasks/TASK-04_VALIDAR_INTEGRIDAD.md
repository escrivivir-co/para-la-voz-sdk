# TASK-04 — Validar integridad del grafo tras la migración

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** GL-03
> **Entrega esperada:** informe de validación de integridad

## Lee primero

- [Plan §5.4](../PLAN.md)
- `lore/derivados/grafo/nodos.json`
- `corpus/corpus.md`

## Objetivo

Verificar que la migración no rompe el grafo ni sus anclas documentales.

## Cambios esperados

1. Comprobar que `piezas_ancla` siguen resolviendo contra el corpus en su ruta nueva
2. Verificar que los agentes leen sin error las nuevas rutas
3. Dejar un informe breve con incidencias, si las hay

## Criterio de aceptación

Existe informe de validación y no quedan inconsistencias críticas entre grafo, corpus y agentes.