# TASK-00 — Contexto y persistencia del dossier cortos-sdk

> **Estado:** cerrada
> **Agente:** GPT-5.4
> **Fecha:** 19-abr-2026

## Contexto congelado

- El Dramaturgo SDK ya contempla la operación `generar obra`, pero no fija todavía una convención portable de persistencia por modelo.
- El mod legislativa ya tiene 5 cortos persistidos en `DRAFTS2/LORE_F-02_CORTO*.md`.
- La separación pedida por el usuario es explícita: universo y corto no comparten dossier.

## Decisión de corte

- `universos-sdk` cristaliza la persistencia de ramas/universos.
- `cortos-sdk` cristaliza la persistencia de obras derivadas por modelo.
- `cortos-legislativa` migra los cortos concretos del caso y recablea a `@Dramaturgo Cortos`.