# TASK-07 — Validación de la cadena completa

> **Estado:** pendiente
> **Agente recomendado:** `Pipeline`
> **Dependencias:** CA-06
> **Entrega esperada:** `DRAFTS2/cristalizacion-cadena-agentica/ENTREGA_CA-07_VALIDACION.md`

## Lee primero

- Todos los agentes del mod tras los refactors
- [pipeline.agent.md](../../../mod/agents/pipeline.agent.md) — con handoffs actualizados
- [FEAT-06_PIPELINE_REFRESH.md](../../FEAT-06_PIPELINE_REFRESH.md) — protocolo vinculante

## Objetivo

Verificar que la cadena de 5 agentes funciona end-to-end: cada handoff conecta, no hay roles duplicados, no hay huecos.

## Secuencia de validación

1. `@Pipeline /refresh status` — debe listar los 5 agentes como nodos del grafo de dependencias.
2. Verificar que Puzzle puede inventariar las 51 piezas.
3. Verificar que Archivero Lore recibe pack y no re-valida.
4. Verificar que Grafista genera grafo sin instanciar universos.
5. Verificar que Demiurgo puede leer el grafo y presentar ramas.
6. Verificar que Dramaturgo Cortos recibe universo del Demiurgo (no del Grafista).
7. Documentar resultado en ENTREGA.

## Criterio de aceptación

Ningún agente mezcla dos transformaciones. Todos los handoffs conectan. El refresh recorre la cadena en orden sin saltar eslabones.
