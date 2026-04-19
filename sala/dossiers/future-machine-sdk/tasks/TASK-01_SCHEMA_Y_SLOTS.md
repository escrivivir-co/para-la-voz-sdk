# TASK-01 — Schema y slots de la future-machine

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** FS-00, PS-01 (lore-db-sdk), CS-01 (corpus-sdk), GS-01 (grafo-sdk), US-01 (universos-sdk), COS-01 (cortos-sdk)
> **Entrega esperada:** `.github/instructions/future-machine-schema.instructions.md`

## Lee primero

1. Sección 0 de `sala/dossiers/future-machine-sdk/PLAN.md` — tabla del pipeline completo
2. Sección 2 del PLAN — el ciclo contado por sus agentes
3. Los schemas de cada capa cuando existan (PS-01, CS-01, GS-01, US-01, COS-01)

## Objetivo

Definir el contrato portable de la machine como ensamblaje de slots. El schema es lo que `@Pipeline`, `@Portal` y los prompts de entrypoint leen para saber qué existe y qué falta.

## Debe cubrir

1. Slots de capas de datos:
   - `slot_lore_db` — piezas + LORE_F (`@Loreador`)
   - `slot_corpus` — mapa analítico acumulativo (`@Archivero`)
   - `slot_grafo` — grafo de bifurcación (`@Grafista`)
   - `slot_universos` — concreción del grafo: variables + inicializaciones (`@Demiurgo`)
   - `slot_obras` — producciones literarias en lenguaje natural (`@Dramaturgo`)
2. Slots de agentes orquestadores:
   - `slot_pipeline` — `@Pipeline`
   - `slot_portal` — `@Portal`
3. Slots de entrypoints de usuario:
   - `slot_entry_start` — big picture
   - `slot_entry_status` — dashboard
   - `slot_entry_refresh` — trigger de refresh
4. Cada slot declara: ruta canónica, agente propietario, dependencia upstream/downstream, estado
5. El grafo de dependencias entre slots (upstream → downstream)

## Criterio de aceptación

- Existe un contrato portable y reutilizable para declarar una future-machine
- El schema es suficiente para que `@Pipeline` sepa recorrer la cadena sin hardcodear agentes
- El schema es suficiente para que `@Portal` sepa qué presentar al usuario