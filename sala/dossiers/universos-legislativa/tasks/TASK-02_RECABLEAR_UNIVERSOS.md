# TASK-02 — Recablear Demiurgo y Pipeline a la capa universo migrada

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** UL-01, GL-01, GL-02
> **Entrega esperada:** Demiurgo y Pipeline leen universos desde `lore/derivados/universo/`

## Lee primero

- [Plan §5.2](../PLAN.md)
- `mod/agents/demiurgo.agent.md`
- `mod/agents/pipeline.agent.md`

## Objetivo

Actualizar la fase `grafo -> universo` para que Demiurgo y Pipeline trabajen ya sobre `lore/` y entreguen el handoff correcto a la capa de cortos.

## Cambios esperados

1. Actualizar rutas en `mod/agents/demiurgo.agent.md`
2. Ajustar `mod/agents/pipeline.agent.md` para que la etapa `universo` apunte a la ruta nueva y el siguiente nodo sea `cortos`
3. Verificar handoffs y descripciones de la fase

## Criterio de aceptación

La fase universo ya no depende de rutas antiguas y queda lista para entregar a `cortos-legislativa`.