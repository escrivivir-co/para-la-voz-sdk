# TASK-01 — Schema y slots de la future-machine

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** FS-00
> **Entrega esperada:** `.github/instructions/future-machine-schema.instructions.md`

## Objetivo

Definir el contrato portable de la machine como ensamblaje de slots.

## Debe cubrir

1. Slots de capas:
   - `slot_lore_db`
   - `slot_corpus`
   - `slot_grafo`
   - `slot_universos`
   - `slot_obras`
2. Slots de superficies:
   - `slot_portal`
   - `slot_pipeline`
   - `slot_entry_start`
   - `slot_entry_status`
   - `slot_entry_refresh`
3. Estados y dependencias entre slots.

## Criterio de aceptación

- Existe un contrato portable y reutilizable para declarar una future-machine.