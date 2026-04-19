# TASK-03 — Compatibilidad de prompts y flujos

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CS-02
> **Entrega esperada:** edición de prompts/templates SDK de corpus

## Objetivo

Documentar sin ambigüedad que el SDK soporta:

1. El flujo clásico:
   `/feed -> Bartleby -> /diff-corpus -> /merge-corpus`
2. El flujo batch:
   `Loreador -> Archivero ingest -> corpus/corpus.md`

## Ficheros objetivo

- `.github/prompts/feed.prompt.md`
- `.github/prompts/diff-corpus.prompt.md`
- `.github/prompts/merge-corpus.prompt.md`
- `.github/prompts/status.prompt.md`
- `.github/templates/guion-ciclo.template.md`

## Criterio de aceptación

- Ningún prompt pierde compatibilidad con el flujo clásico y el batch queda reconocido.