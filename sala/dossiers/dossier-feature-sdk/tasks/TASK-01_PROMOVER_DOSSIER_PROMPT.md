# TASK-01 — Promover dossier.prompt.md al SDK

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** —
> **Entrega esperada:** `.github/prompts/dossier.prompt.md` generalizado

## Lee primero

1. `mod/prompts/dossier.prompt.md` — versión actual
2. `.github/copilot-instructions.md` — estructura del SDK (sección Sala)
3. `sala/plantilla-dossier/` — scaffold existente

## Objetivo

Copiar `mod/prompts/dossier.prompt.md` a `.github/prompts/dossier.prompt.md`, generalizando:

## Cambios requeridos

1. **Rutas:** reemplazar `sala/dossiers/` → `{{SALA_DIR}}/dossiers/` y `sala/tablero.md` → `{{SALA_DIR}}/tablero.md` y `sala/plantilla-dossier/` → `{{SALA_DIR}}/plantilla-dossier/`.
2. **Ref al SKILL:** cambiar `mod/skills/cristalizacion-feature/SKILL.md` → `.github/skills/cristalizacion-feature/SKILL.md`.
3. **Frontmatter:** mantener tal cual (name, description, argument-hint, tools).
4. **No añadir** refs a ningún lore específico.

## Salida mínima esperada

1. Fichero candidato en carpeta del agente: `agente-{alias}/candidato-dossier.prompt.md`
2. ENTREGA con diff de cambios respecto al original.

## Criterio de aceptación

- El prompt funciona sin presuponer ningún mod.
- Grep de `DRAFTS2|legislativa|mod/skills|mod/prompts` = 0 hits.
