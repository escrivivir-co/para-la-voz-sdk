# TASK-03 — Integrar en SDK y limpiar mod

> **Estado:** libre
> **Agente recomendado:** Aleph (requiere merge a main)
> **Dependencias:** DF-01, DF-02
> **Entrega esperada:** `.github/copilot-instructions.md` actualizado, merge main → mod, duplicados eliminados

## Lee primero

1. `.github/copilot-instructions.md` — tabla de comandos actual
2. Entregas de DF-01 y DF-02 (candidatos aprobados)

## Objetivo

Cerrar el ciclo: commit en main, actualizar copilot-instructions, merge a mod, limpiar duplicados.

## Pasos

1. Crear rama `feat/dossier-sdk` desde main (o commit directo si Aleph tiene confianza).
2. Colocar los candidatos aprobados de DF-01 y DF-02 en `.github/prompts/` y `.github/skills/`.
3. En `.github/copilot-instructions.md`, añadir `/dossier` a la tabla de comandos de sala:
   ```
   | `/dossier` | Crear, continuar o listar dossiers de feature |
   ```
4. Commit + merge a main.
5. En mod/legislativa: `git merge main`.
6. Eliminar duplicados: `mod/prompts/dossier.prompt.md` y `mod/skills/cristalizacion-feature/`.
7. Commit de cleanup en mod.

## Salida mínima esperada

1. `/dossier` aparece en copilot-instructions.md
2. mod/legislativa hereda `dossier.prompt.md` y `SKILL.md` de `.github/`
3. 0 duplicados en mod/

## Criterio de aceptación

- `git diff main..mod/legislativa -- .github/prompts/dossier.prompt.md` = vacío (hereda de main)
- `mod/prompts/dossier.prompt.md` no existe
- `mod/skills/cristalizacion-feature/` no existe
