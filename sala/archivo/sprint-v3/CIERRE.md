# Cierre — sprint-v3

- Fecha: 2026-04-19
- Tasks cerradas: 4/4 (+ 2 REV + 2 tasks-00 de contexto)
- Tasks no-aplica: 0
- Agentes participantes: Gepe (GPT-5.4), Sony (Claude Sonnet 4.6), Gemy (Gemini 3.1 Pro), aleph-review (Claude Opus 4.6)
- Orquestador: Aleph (Claude Opus 4.6)
- Backlog transferido: ninguno
- Dossiers archivados: dossier-feature-sdk, sala-sdk
- Dossiers activos (no archivados): corpus-sdk, cortos-sdk, cristalizador-sdk, future-machine-sdk, grafo-sdk, lore-db-sdk, universos-sdk

## Resumen del sprint

Sprint de generalización de la capa `dossier` del SDK. El objetivo era promover los artefactos de diseño de features (prompt, skill, scaffold) desde `mod/` al SDK core (`.github/`), integrar la superficie de sala, y cerrar la unidad documental `sala-sdk`.

### Tasks ejecutadas

| Task | Título | Agente | Resultado |
|------|--------|--------|-----------|
| DF-00 | Contexto y persistencia (dossier-feature-sdk) | Aleph | Contexto congelado |
| SS-00 | Contexto y persistencia (sala-sdk) | Gepe | Contexto congelado |
| DF-01 | Promover `dossier.prompt.md` a `.github/prompts/` | Gepe | Aprobada tras revisión |
| DF-02 | Promover `cristalizacion-feature/SKILL.md` a `.github/skills/` | Sony | Aprobada tras revisión |
| DF-03 | Integrar superficie `sala`, scaffold rico en `main`, migrar consumidores | Gemy | Aprobada con fixes (violaciones §6 corregidas) |
| SS-01 | Cerrar unidad `sala-sdk` y publicar archivo histórico | Gepe (verificación) + Aleph (fix scaffold) | Cerrada — scaffold rico alineado |

### Artefactos producidos en main

- `.github/prompts/dossier.prompt.md` — prompt portable de gestión de dossiers
- `.github/skills/dossier-feature/SKILL.md` — skill portable de diseño de features
- `.github/templates/sala-dossier/` — scaffold rico del dossier (PLAN, BACKLOG, RESPUESTAS, activacion, TASK-00)
- `.github/instructions/sala-protocolo.instructions.md` §6 — autovalidación del agente (nuevo)
- `.github/prompts/sala-entrar.prompt.md` — reforzado con líneas rojas
- `.github/prompts/sala-seguir.prompt.md` — reforzado con recordatorio de autovalidación

### Incidentes

- Gemy (DF-03): commits directos a git, escritura fuera de carpeta de agente, edición de `.github/` y `mod/` sin intermediario. Corregido por Aleph. §6 del protocolo creado como consecuencia directa.
