# TASK-01 — Materializar la capa corpus

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CP-00, CS-01†, LP-01b‡
> **Entrega esperada:** `corpus/` canónico y no solo de redirección

> † CS-01 es del dossier `corpus-sdk`.
> ‡ LP-01b es del dossier `lore-db-legislativa`.

## Objetivo

Convertir `corpus/` en capa pública real del mod y dejar de depender públicamente de `DRAFTS2/CORPUS_PREVIEW.md`.

## Debe resolver

1. Qué pasa con `DRAFTS2/CORPUS_PREVIEW.md`.
2. Qué contenido pasa a `corpus/corpus.md`.
3. Cómo se reescribe `corpus/README.md` una vez que deje de ser shim.

## Criterio de aceptación

- El corpus del mod tiene ya ruta canónica pública.