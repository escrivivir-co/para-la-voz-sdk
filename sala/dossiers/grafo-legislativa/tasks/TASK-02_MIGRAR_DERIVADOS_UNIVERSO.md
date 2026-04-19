# TASK-02 — Migrar artefacto, universo y cortos a `lore/derivados/`

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** GL-00, LP-01b
> **Entrega esperada:** derivados del universo migrados a `lore/derivados/`

## Lee primero

- [Plan §5.2](../PLAN.md)
- [BACKLOG](../BACKLOG.md)
- `DRAFTS2/LORE_F-02_ARTEFACTO.md`
- `DRAFTS2/LORE_F-02_UNIVERSO.md`

## Objetivo

Mover los derivados del grafo y las ramas instanciadas desde `DRAFTS2/` a la estructura canónica de la lore-db.

## Cambios esperados

1. `git mv` de `LORE_F-02_ARTEFACTO.md`, `LORE_F-02_UNIVERSO.md`, `LORE_F-02_CORTO*.md`
2. `git mv DRAFTS2/universo/ lore/derivados/universo/`
3. Verificar que no se pierde ninguna rama ni ningún corto

## Criterio de aceptación

Los derivados del universo viven en `lore/derivados/` y las ramas en `lore/derivados/universo/`, con historial preservado.