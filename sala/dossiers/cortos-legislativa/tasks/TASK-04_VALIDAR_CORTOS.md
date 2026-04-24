# TASK-04 — Validar naming y trazabilidad de los cortos

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CL-02, CL-03
> **Entrega esperada:** informe de validación

## Lee primero

- [Plan §6.4](../PLAN.md)
- `mod/agents/dramaturgo.agent.md`
- `mod/agents/pipeline.agent.md`

## Objetivo

Verificar que la fase de cortos conserva universo fuente, modelo y trazabilidad documental tras la migración.

## Cambios esperados

1. Revisar naming por universo + modelo
2. Comprobar que las referencias a universo y artefacto siguen resolviendo
3. Verificar que nuevas versiones no sobreescriben las anteriores

## Criterio de aceptación

Existe un informe de validación y la fase `cortos` queda operativa sin pérdida de trazabilidad.