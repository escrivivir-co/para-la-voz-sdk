# TASK-01 — Migrar los 3 universos existentes a `lore/derivados/universo/`

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** UL-00, LP-01b, GL-01, GL-02
> **Entrega esperada:** `lore/derivados/universo/` con 3 universos migrados

## Lee primero

- [Plan §5.1](../PLAN.md)
- `DRAFTS2/universo/`
- `DRAFTS2/LORE_F-02_UNIVERSO.md`

## Objetivo

Mover los universos instanciados a la estructura canónica de la lore-db sin perder historial.

## Cambios esperados

1. `git mv DRAFTS2/universo/ lore/derivados/universo/`
2. Verificar que se conservan `universo-1.md`, `universo-1-r1.md`, `universo-1-r2.md`
3. Ajustar refs internas si alguno de esos ficheros apunta a rutas antiguas

## Criterio de aceptación

Los 3 universos viven en `lore/derivados/universo/` con historial preservado.