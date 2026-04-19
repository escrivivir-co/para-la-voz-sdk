# TASK-04 — Huecos JSON

> **Estado:** pendiente
> **Agente recomendado:** `Cristalizador`
> **Dependencias:** GJ-01
> **Entrega esperada:** `DRAFTS2/grafo/huecos.json`

## Lee primero

- [Plan local §4.5 — Schema de huecos](../PLAN_GRAFO_JSON.md)
- [LORE_F-02_UNIVERSO.md](../../LORE_F-02_UNIVERSO.md) — buscar `[?]` y `H*`
- [LORE_F-02_ARTEFACTO.md](../../LORE_F-02_ARTEFACTO.md) — huecos declarados en ficha técnica

## Objetivo

Extraer todos los huecos no resueltos del grafo a `huecos.json`. Los huecos son preguntas abiertas o incertidumbres que afectan a nodos del grafo.

## Criterio de aceptación

Cada `[?]` o `H*` del Markdown tiene entrada en `huecos.json` con nodos afectados que existen en `nodos.json`.
