# TASK-03 — Actualizar refs de consumidores del grafo migrado

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** GL-01, GL-02
> **Entrega esperada:** consumidores del grafo e instructions sin refs obsoletas a `DRAFTS2/`

## Lee primero

- [Plan §5.3](../PLAN.md)
- `mod/agents/grafista.agent.md`
- `mod/agents/archivero-lore.agent.md`
- `mod/instructions/lore-estado.instructions.md`

## Objetivo

Actualizar los consumidores del **grafo** para que lean desde `lore/derivados/` en vez de `DRAFTS2/`. Las refs de universo instanciado se resuelven en `universos-legislativa` y las de cortos en `cortos-legislativa`.

## Cambios esperados

1. Actualizar refs de Grafista
2. Actualizar Archivero en la ruta vigente (`archivero-lore` o `archivero-legislativa`, según estado de LP-05)
3. Ajustar cabecera de `gramatica.md`, `index.json` y cualquier instruction del mod que siga apuntando a `DRAFTS2/` para el grafo

## Criterio de aceptación

Los consumidores del grafo no contienen rutas obsoletas a `DRAFTS2/` para assets ya migrados.