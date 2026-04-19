# TASK-01 — Promover dossier.prompt.md al SDK

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** —
> **Entrega esperada:** `.github/prompts/dossier.prompt.md` generalizado

## Lee primero

1. `sala/archivo/sprint-extraccion-sala-v2/dossiers/extraccion-sala-sdk/PLAN_EXTRACCION_SALA_SDK.md` — extracción previa de `sala`
2. `sala/README.md` — flujo real entre `/dossier` y `/sala-*`
3. `mod/prompts/dossier.prompt.md` — versión actual
4. `.github/copilot-instructions.md` — estructura del SDK (sección Sala)
5. `sala/plantilla-dossier/` — scaffold existente

## Objetivo

Promover `mod/prompts/dossier.prompt.md` a `.github/prompts/dossier.prompt.md` como comando de diseño de `sala`, no como prompt aislado.

## Cambios requeridos

1. **Rutas:** reemplazar `sala/dossiers/` → `{{SALA_DIR}}/dossiers/`, `sala/tablero.md` → `{{SALA_DIR}}/tablero.md` y `sala/plantilla-dossier/` → `{{SALA_DIR}}/plantilla-dossier/`.
2. **Formato del scaffold:** actualizar la descripción del dossier a `PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`, `activacion.prompt.md`, `tasks/`.
3. **Relación con `sala`:** explicar que `/dossier` abre o mantiene tracks que después ejecuta `/sala-*`.
4. **Ref al SKILL:** cambiar `mod/skills/cristalizacion-feature/SKILL.md` → `.github/skills/cristalizacion-feature/SKILL.md`.
5. **Continuar y listar:** dejar de asumir `BACKLOG_{NOMBRE_UPPER}.md` y usar `BACKLOG.md`.
6. **Frontmatter:** mantener `name`, `description`, `argument-hint` y `tools` salvo delta imprescindible.
7. **No añadir** refs a ningún lore específico.

## Salida mínima esperada

1. Fichero candidato en carpeta del agente: `agente-{alias}/candidato-dossier.prompt.md`
2. ENTREGA con diff de cambios respecto al original.

## Criterio de aceptación

- El prompt funciona sin presuponer ningún mod.
- El prompt describe el formato actual del dossier y no el legado `PLAN_*` / `BACKLOG_*` / `RESPUESTAS_USUARIO_*`.
- Grep de `DRAFTS2|legislativa|PLAN_\{|BACKLOG_\{|RESPUESTAS_USUARIO_\{|mod/skills` = 0 hits en el candidato.
