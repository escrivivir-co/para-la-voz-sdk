# TASK-03 — Actualizar refs de agentes e instructions al grafo migrado

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** GL-01, GL-02
> **Entrega esperada:** agentes e instructions sin refs a `DRAFTS2/` para el grafo

## Lee primero

- [Plan §5.3](../PLAN.md)
- `mod/agents/grafista.agent.md`
- `mod/agents/demiurgo.agent.md`
- `mod/agents/dramaturgo.agent.md`

## Objetivo

Actualizar los consumidores del grafo para que lean desde `lore/derivados/` en vez de `DRAFTS2/`.

## Cambios esperados

1. Actualizar refs de Grafista, Demiurgo y Dramaturgo
2. Actualizar Archivero en la ruta vigente (`archivero-lore` o `archivero-legislativa`, según estado de LP-05)
3. Ajustar cabecera de `gramatica.md` y cualquier instruction del mod que siga apuntando a `DRAFTS2/`

## Criterio de aceptación

Los agentes consumidores del grafo no contienen rutas obsoletas a `DRAFTS2/` para assets ya migrados.