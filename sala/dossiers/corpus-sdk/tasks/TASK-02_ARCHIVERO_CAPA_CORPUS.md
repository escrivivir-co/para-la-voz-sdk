# TASK-02 — Archivero como capa corpus

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CS-01
> **Entrega esperada:** edición de `.github/agents/archivero.agent.md`

## Objetivo

Reformular el `@Archivero` del SDK como agente de corpus en dos modos compatibles:

- curación incremental (`diff`, `merge`, `status`)
- corpuseado batch (`ingest` o equivalente)

## Cambios esperados

1. Mantener intacto el principio: el Archivero nunca analiza directamente; delega a `@Bartleby`.
2. Dejar explícito que **no** gestiona piezas ni inventario de lore-db.
3. Añadir el modo batch solo dentro del dominio corpus.
4. Mantener los handoffs existentes y añadir los necesarios sin romper el flujo clásico.

## Criterio de aceptación

- El Archivero queda mejor definido y no invada el dominio de `@Loreador`.