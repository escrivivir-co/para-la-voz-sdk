# ENTREGA: TASK-03_INTEGRAR_SDK_Y_LIMPIAR

**Agente:** Gemy (Gemini 3.1 Pro)
**Task:** DF-03
**Fecha:** 2026-04-19

## Resumen de cambios

1. **Rama generada:** se creó `feat/dossier-sdk`, se portó `dossier.prompt.md` a `.github/prompts/` y `SKILL.md` a `.github/skills/dossier-feature/`.
2. **Superficie de comandos:** `copilot-instructions.md` ahora incluye explícitamente el comando `/dossier`.
3. **Scaffold rico:** se alineó el SDK portando `sala/plantilla-dossier/` a `.github/templates/sala-dossier/` en lugar del antiguo `.github/templates/sala-dossier.template.md`.
4. **Archivo recuperado:** se recuperó y restauró `sala/archivo/sprint-extraccion-sala-v2/` desde la rama `mod/legislativa` hacia `main` como archivo del SDK.
5. **Merge y migración:** se hizo merge de la feature en `main` y luego `main` → `mod/legislativa`.
6. **Limpieza mod:** se eliminó `mod/prompts/dossier.prompt.md` y `mod/skills/cristalizacion-feature/`.
7. **Migración consumidores:** se actualizó `mod/prompts/lore-status.prompt.md` y `mod/README_MOD.md` para deshacerse del antiguo formato `<NOMBRE>.md` y referir al `.github/skills/dossier-feature/SKILL.md`.

## Verificación

- `git diff main..mod/legislativa -- .github/prompts/dossier.prompt.md` = vacío
- `git diff main..mod/legislativa -- .github/skills/dossier-feature/SKILL.md` = vacío
- `git ls-tree -r --name-only main -- sala/archivo | grep sprint-extraccion-sala-v2` = devuelve el archivo publicado.
- Grep de los formatos antiguos en consumidores vivos = 0 (migrados exitosamente en `mod/legislativa`).

El Criterio de Aceptación se cumple íntegramente.