# TASK-01 — Migrar el grafo JSON a `lore/derivados/grafo/`

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** GL-00, LP-01b, GS-01
> **Entrega esperada:** `lore/derivados/grafo/` con 5 ficheros + `index.json` actualizado

## Lee primero

- [Plan §5.1](../PLAN.md)
- [BACKLOG](../BACKLOG.md)
- `DRAFTS2/grafo/gramatica.md`
- `DRAFTS2/grafo/index.json`

## Objetivo

Mover el grafo JSON completo desde `DRAFTS2/grafo/` a `lore/derivados/grafo/` preservando historial y actualizando las rutas internas de `index.json`.

## Cambios esperados

1. Ejecutar `git mv DRAFTS2/grafo/ lore/derivados/grafo/`
2. Actualizar en `index.json` los campos `corpus_ref`, `artefacto_ref`, `hilo_ref`, `universo_ref`
3. Verificar que los 5 ficheros siguen presentes tras el movimiento

## Criterio de aceptación

`lore/derivados/grafo/` contiene `gramatica.md`, `index.json`, `nodos.json`, `arcos.json`, `huecos.json`; `index.json` ya apunta a rutas `lore/`.