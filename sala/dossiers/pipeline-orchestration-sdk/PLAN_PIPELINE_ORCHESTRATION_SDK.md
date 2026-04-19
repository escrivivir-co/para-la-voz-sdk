# Dossier — pipeline-orchestration-sdk

> **Prioridad:** media
> **Tasks estimadas:** 5
> **Rama:** `feat/pipeline-sdk` (desde main)

## Contexto

El mod/legislativa desarrolló un patrón de orquestación multi-agente con pipeline configurable: un agente Pipeline detecta cambios upstream y propaga downstream a través de una cadena de agentes. El protocolo de ingesta (full/diff/status) y refresh (status/--desde) son genéricos.

Los artefactos actuales están hardcodeados a la cadena legislativa (Puzzle→Archivero Lore→Grafista→Demiurgo→Dramaturgo Cortos). El SDK necesita la versión parametrizable.

## Inventario

### Artefactos híbridos a extraer

| Origen (mod/) | Destino SDK (.github/) | Núcleo genérico | Lo que se queda en mod/ |
|---|---|---|---|
| `mod/agents/pipeline.agent.md` | `.github/agents/pipeline.agent.md` | Detección de cambios, propagación por cadena, `--desde`, delta reporting | Cadena concreta de 5 agentes, handoff messages específicos |
| `mod/prompts/pipeline-refresh.prompt.md` | `.github/prompts/pipeline-refresh.prompt.md` | Protocolo refresh (status/refresh/--desde) | Refs a agentes específicos |
| `mod/prompts/lore-ingest.prompt.md` | `.github/prompts/lore-ingest.prompt.md` | Protocolo ingesta (full/diff/status) | Refs a @Puzzle + @Archivero Lore |
| `mod/agents/portal.agent.md` | `.github/agents/portal.agent.md` (actualizar) | Perfiles nuevos (cliente, producción) + routing a sala | Mapping perfil→agente específico del lore |

### Lo que NO se extrae

Los agentes de la cadena (puzzle, archivero-lore, grafista, demiurgo, dramaturgo) son lore-específicos. El schema de tipos (P/S/N/T/R/F), el grafo JSON, y las reglas de universo también.

## Operación

1. Crear rama `feat/pipeline-sdk` desde main
2. Crear `pipeline.agent.md` genérico — cadena como parámetro, no hardcoded
3. Crear `pipeline-refresh.prompt.md` genérico
4. Crear `lore-ingest.prompt.md` genérico (renombrar a `/ingest` o mantener `/lore-ingest`)
5. Actualizar `portal.agent.md` del SDK con perfiles extendidos
6. Actualizar copilot-instructions.md
7. Merge a main
8. En mod/legislativa: merge main → mod/ hereda SDK genérico y especializa

## Decisiones pendientes

- ¿Renombrar `/lore-ingest` a `/ingest` en SDK? "lore" es término del SDK (`corpus/` = lore), no solo del mod.
- ¿El portal SDK ya tiene perfiles visitor/team/editor — añadir client/production o dejarlos como extensión del mod?
