# TASK-04 — Validar la cadena `grafo -> universo` y el handoff a cortos

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** UL-02, UL-03
> **Entrega esperada:** informe de validación de la cadena

## Lee primero

- [Plan §5.4](../PLAN.md)
- `mod/agents/grafista.agent.md`
- `mod/agents/demiurgo.agent.md`
- `mod/agents/pipeline.agent.md`

## Objetivo

Verificar que, tras la migración, la secuencia `grafo -> universos` es coherente y que el handoff hacia la fase `cortos` queda bien definido.

## Cambios esperados

1. Revisar que Grafista entrega un grafo legible por Demiurgo
2. Revisar que Demiurgo localiza universos persistidos en `lore/derivados/universo/`
3. Comprobar que Pipeline refleja la etapa `universo` sin nombres ni handoffs obsoletos
4. Confirmar que el siguiente tramo queda delegado a `cortos-legislativa`

## Criterio de aceptación

Existe un informe de validación y no quedan roturas críticas en la cadena `grafo -> universo` ni en el handoff a cortos.