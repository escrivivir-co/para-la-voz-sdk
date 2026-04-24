# Backlog — Future-machine para universo-1

> **Fecha de apertura:** 18-abr-2026
> **Estado:** abierto
> **Modelo de inicialización:** `GPT-5.4`
> **Anclas:** `universo-1` + `PLAN_UNIVERSO1_V2.md`

## Contexto compartido

Todos los tasks de esta carpeta heredan este contexto y no deben repetirlo salvo que añadan delta local:

- [Plan inicial local](./PLAN_FUTURE_MACHINE_UNIVERSO1.md)
- [Respuestas del usuario](./RESPUESTAS_USUARIO_FUTURE_MACHINE_UNIVERSO1.md)
- [Plan madre del sprint](../PLAN_UNIVERSO1_V2.md)
- [Skill core futures-engine](../../.github/skills/futures-engine/SKILL.md)
- [Agente base Dramaturgo](../../.github/agents/dramaturgo.agent.md)
- [Dramaturgo del mod](../../mod/agents/dramaturgo.agent.md)
- [Instrucciones del mod](../../mod/instructions/legislativa-universo.instructions.md)

## Regla DRY del backlog

- El backlog hace de índice, tracking y criterio de cierre.
- El detalle operativo vive en los archivos `tasks/`.
- No se duplican reglas ya fijadas en `.github/` o `mod/`; cada task añade solo overrides, wiring o decisiones locales.

## Tracking

| Task | Estado | Agente recomendado | Modelo | Dependencias | Entrega | Brief |
|---|---|---|---|---|---|---|
| FM-00 | **Completado** | `GPT-5.4` | `GPT-5.4` | — | plan inicial + respuestas persistidas | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| FM-01 | **Completado** | `GPT-5.4` | `GPT-5.4` | FM-00 | rutas oficiales temporales inicializadas | [TASK-01](./tasks/TASK-01_REDIRECCIONES_OFICIALES_TEMPORALES.md) |
| FM-02 | **Superseded** | — | — | — | resuelto por 4 dossiers de cristalización (19-abr) | [TASK-02](./tasks/TASK-02_CRISTALIZADOR_MISION_INTERVENCION.md) |
| FM-03 | **Superseded** | — | — | — | resuelto por `cristalizacion-feature/SKILL.md` + cadena-agéntica | [TASK-03](./tasks/TASK-03_SKILL_MOD_FUTURE_MACHINE.md) |
| FM-04 | **Superseded** | — | — | — | resuelto por dossiers cadena-agéntica + pipeline-operativo | [TASK-04](./tasks/TASK-04_SUPERFICIE_AGENTICA_MOD.md) |
| FM-05 | **Reescrito** | `Pipeline` + `Explore` | modelo activo | dossiers hermanos | validación de cadena completa + lore migrado | [TASK-05](./tasks/TASK-05_VALIDACION_UNIVERSO1_PLAN_V2.md) |
| FM-06 | Condicional | `Explore` o `Cristalizador` | cualquiera | evidencia de fallo real | warning para equipo main | [TASK-06](./tasks/TASK-06_WARNING_MAIN_SI_APLICA.md) |

> **[Claude Opus 4.6] Nota 19-abr-2026:** FM-02, FM-03 y FM-04 se marcan como **Superseded** (no Cancelado). El trabajo que proponían se ha diseñado en detalle en los dossiers `cristalizacion-pipeline-operativo/`, `cristalizacion-cadena-agentica/` y `cristalizacion-grafo-json/`. FM-05 se reescribe para validar contra la cadena de 5 agentes, no solo contra Dramaturgo.

## Criterio de cierre del feature

1. ~~Existe una `future-machine` operativa en `mod/` o un override local de `futures-engine` que cubre el caso legislativa.~~ **Superseded:** la superficie agéntica se diseña en `cadena-agentica/`.
2. Las rutas canónicas del SDK tienen workaround temporal documentado hacia `DRAFTS2/`. ✔️ FM-01
3. ~~La intervención está validada contra `universo-1` y el sprint [PLAN_UNIVERSO1_V2.md](../PLAN_UNIVERSO1_V2.md).~~ **Reescrito en FM-05:** validación contra la cadena completa de 5 agentes.
4. El backlog sigue siendo índice y tracking; no reabsorbe los briefs de las tasks.

**Criterio de cierre actualizado (19-abr-2026):**

1. FM-00 y FM-01 completados. ✔️
2. Los dossiers hermanos (`pipeline-operativo`, `cadena-agentica`, `grafo-json`, `finalizacion-lore-plan`) cubren el scope de FM-02..FM-04.
3. FM-05 (validación reescrita) se ejecuta y pasa.
4. FM-06 se ejecuta si hay evidencia, o se marca como no-aplica.