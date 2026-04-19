# TASK-02 — Promover cristalizacion-feature/SKILL.md al SDK

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** —
> **Entrega esperada:** `.github/skills/cristalizacion-feature/SKILL.md` generalizado

## Lee primero

1. `sala/archivo/sprint-extraccion-sala-v2/dossiers/extraccion-sala-sdk/PLAN_EXTRACCION_SALA_SDK.md` — extracción previa de `sala`
2. `sala/archivo/sprint-extraccion-sala-v2/CIERRE.md` — backlog transferido a este dossier
3. `sala/README.md` — flujo real de diseño y ejecución
4. `mod/skills/cristalizacion-feature/SKILL.md` — versión actual
5. `.github/copilot-instructions.md` — sección Sala (estructura dossiers)
6. `.github/instructions/sala-protocolo.instructions.md` — protocolo transversal
7. `sala/plantilla-dossier/PLAN.md` — formato canónico actual
8. `sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-pipeline-operativo/PLAN_PIPELINE_OPERATIVO.md`, `.../cristalizacion-cadena-agentica/BACKLOG_CADENA_AGENTICA.md` y `.../future-machine-universo-1/tasks/TASK-02_CRISTALIZADOR_MISION_INTERVENCION.md` — material portable a rescatar

## Objetivo

Promover `mod/skills/cristalizacion-feature/SKILL.md` a `.github/skills/cristalizacion-feature/SKILL.md` como protocolo de la capa de diseño de `sala`.

## Cambios requeridos

1. **Ubicación canónica:** cambiar `mod/skills/cristalizacion-feature/SKILL.md` → `.github/skills/cristalizacion-feature/SKILL.md`.
2. **Estructura del dossier:** describir el formato actual (`PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`, `activacion.prompt.md`, `tasks/`).
3. **Relación con `sala`:** explicitar que los dossiers viven en `{{SALA_DIR}}/dossiers/`, persisten entre sprints y son la capa de diseño que activa `/dossier`.
4. **R4 (restricción de escritura):** reescribirla para promociones al SDK: el agente deja candidatos en su carpeta y Aleph copia al destino final.
5. **Refs al ejemplo:** actualizar la ruta del dossier de referencia a `{{SALA_DIR}}/archivo/` o eliminar cualquier ejemplo que dependa del formato viejo.
6. **Consumidores:** cambiar de `@Cristalizador` a "cualquier agente que gestione features o abra dossiers".
7. **Absorción máxima en `main`:** el SKILL debe decir que el protocolo y el scaffold rico del dossier pertenecen al SDK base y se heredan desde `main`, dejando al mod solo el delta local.
8. **No añadir** refs a ningún lore específico.

## Salida mínima esperada

1. Fichero candidato en carpeta del agente: `agente-{alias}/candidato-SKILL.md`
2. ENTREGA con lista de cambios respecto al original.

## Criterio de aceptación

- El SKILL funciona sin presuponer ningún mod.
- El SKILL describe el formato actual del dossier y no el legado `PLAN_*` / `BACKLOG_*` / `RESPUESTAS_USUARIO_*`.
- El SKILL rescata lo portable del archivo viejo y no deja el scaffold rico como conocimiento implícito del mod.
- Grep de `DRAFTS2|legislativa|PLAN_<|BACKLOG_<|RESPUESTAS_USUARIO_<|mod/skills` = 0 hits en el candidato.
- R4 permite promociones al SDK explícitamente.
