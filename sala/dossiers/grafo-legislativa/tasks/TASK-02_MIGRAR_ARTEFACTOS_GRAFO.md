# TASK-02 — Migrar artefacto y universo markdown legacy a `lore/derivados/`

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** GL-00, LP-01b, CP-01
> **Entrega esperada:** `LORE_F-02_ARTEFACTO.md` + `LORE_F-02_UNIVERSO.md` migrados a `lore/derivados/`

## Lee primero

- [Plan §5.2](../PLAN.md)
- [BACKLOG](../BACKLOG.md)
- `DRAFTS2/LORE_F-02_ARTEFACTO.md`
- `DRAFTS2/LORE_F-02_UNIVERSO.md`

## Objetivo

Mover los dos artefactos markdown del grafo a la estructura canónica de la lore-db. Este dossier **no** mueve ramas instanciadas ni cortos: eso pasa a `universos-legislativa` y `cortos-legislativa`.

## Cambios esperados

1. `git mv DRAFTS2/LORE_F-02_ARTEFACTO.md lore/derivados/`
2. `git mv DRAFTS2/LORE_F-02_UNIVERSO.md lore/derivados/`
3. Verificar que ambos ficheros siguen referenciando el grafo correcto

## Criterio de aceptación

`LORE_F-02_ARTEFACTO.md` y `LORE_F-02_UNIVERSO.md` viven en `lore/derivados/` con historial preservado.