# TASK-04 — Documentar la capa corpus

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CS-01, CS-03
> **Entrega esperada:** edición de `.github/copilot-instructions.md`

## Objetivo

Volver explícita la capa `corpus/` en la arquitectura del SDK.

## Debe dejar claro

- que `lore-db` y `corpus` son capas distintas
- que `corpus/` es la superficie pública canónica
- que un mod puede resolver sus piezas desde `{{LORE_DIR}}/piezas/` sin perder compatibilidad con el SDK
- que downstream (`grafo`, `universos`, `cortos`) consumen corpus, no la lore-db directamente

## Criterio de aceptación

- El mapa arquitectónico ya no mezcla piezas con corpus.