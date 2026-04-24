# TASK-07 — Actualizar Grafista para leer JSON

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** GJ-06 + dossier `cristalizacion-cadena-agentica/` CA-03
> **Entrega esperada:** edición de `mod/agents/grafista.agent.md`

## Lee primero

- [grafista.agent.md refactorizado](../../../mod/agents/grafista.agent.md) — tras CA-03 (solo grafo, sin universos)
- [gramatica.md](../../grafo/gramatica.md) — formato que debe consumir
- Los ficheros JSON en `DRAFTS2/grafo/`

## Objetivo

Añadir al Grafista la capacidad de leer y escribir el grafo en formato JSON además del Markdown legacy.

## Cambios esperados

1. **Fuentes que lees** — añadir `DRAFTS2/grafo/` como fuente preferente. Si existe, leer JSON. Si no, fallback a `LORE_F-02_UNIVERSO.md`.
2. **Output** — al generar o actualizar el grafo, escribir en formato JSON (los 4 ficheros) además de actualizar el Markdown legacy si existe.
3. **Validación** — al escribir nodos/arcos, validar vocabulario contra corpus.

## Dependencia cruzada

Este task depende de:
- **GJ-06** (que los ficheros JSON existan y estén validados)
- **CA-03** (que el Grafista ya esté refactorizado para solo hacer grafo)

Si CA-03 no está completado, esta task se bloquea.

## Criterio de aceptación

Grafista puede leer `DRAFTS2/grafo/nodos.json` + `arcos.json` y operar con ellos. Al generar, escribe JSON validado.
