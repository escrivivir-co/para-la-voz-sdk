# TASK-02 — Documentos y análisis de corpus

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CP-01, LP-01b†
> **Entrega esperada:** definición operativa de `corpus/documentos/` y `corpus/analisis/`

> † LP-01b es del dossier `lore-db-legislativa`.

## Objetivo

Resolver la relación entre:

- `lore/piezas/` como base de datos del lore
- `corpus/documentos/` como superficie pública del corpus
- `corpus/analisis/` como persistencia analítica Bartleby

## Debe fijar

1. Si `corpus/documentos/` es mirror, routing o materialización selectiva.
2. Si el batch de legislativa persiste análisis individuales o deja constancia documentada de por qué no.
3. Qué espera leer el SDK base cuando entre por `corpus/`.

## Criterio de aceptación

- No queda duplicación muda ni ambigüedad sobre dónde están documentos y análisis.