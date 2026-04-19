# TASK-03 — Integrar en SDK y limpiar mod

> **Estado:** libre
> **Agente recomendado:** Aleph (requiere merge a main)
> **Dependencias:** DF-01, DF-02
> **Entrega esperada:** `.github/copilot-instructions.md` actualizado, consumidores de `sala` alineados, merge main → mod, cleanup controlado

## Lee primero

1. `.github/copilot-instructions.md` — tabla de comandos actual
2. `sala/README.md` — flujo real de `dossier` + `sala`
3. `mod/README_MOD.md` — consumidor vivo de la ruta antigua
4. `mod/prompts/lore-status.prompt.md` — consumidor vivo del formato antiguo
5. Entregas de DF-01 y DF-02 (candidatos aprobados)

## Objetivo

Cerrar la extracción de la capa de diseño de `sala`: publicar prompt + SKILL, alinear la superficie y los triggers que los consumen, y cerrar el puente `main -> mod` sin dejar dependencias vivas en el formato o la ruta antigua.

## Pasos

1. Crear rama `feat/dossier-sdk` desde main (o commit directo si Aleph tiene confianza).
2. Colocar los candidatos aprobados de DF-01 y DF-02 en `.github/prompts/` y `.github/skills/`.
3. En `.github/copilot-instructions.md`, añadir `/dossier` a la superficie de `sala` como comando de diseño persistente:
   ```
   | `/dossier` | Crear, continuar o listar dossiers de feature |
   ```
4. Publicar `sala/archivo/sprint-extraccion-sala-v2/` en `main` si aún no está allí. Se trata como archivo histórico SDK, no como artefacto exclusivo del mod.
5. Revisar y actualizar los consumidores vivos no archivados que sigan anclados a la ruta o al formato antiguo. Mínimo: `mod/README_MOD.md` y `mod/prompts/lore-status.prompt.md`. Si aparece algún otro hit no archivado en el grep final, se corrige en esta misma task.
6. Commit + merge a main.
7. En mod/legislativa: `git merge main`.
8. Eliminar o puentear `mod/prompts/dossier.prompt.md` y `mod/skills/cristalizacion-feature/` solo si no queda ningún consumidor vivo dependiendo de esas rutas. Si se mantiene puente temporal, documentarlo explícitamente y mantenerlo sin drift.
9. Commit de cleanup o bridge en mod.

## Salida mínima esperada

1. `/dossier` aparece en la documentación de `sala` del SDK.
2. `sala/archivo/sprint-extraccion-sala-v2/` queda visible en `main` como archivo histórico del SDK.
3. Los consumidores vivos del formato o la ruta antigua quedan migrados o con puente explícito.
4. `mod/legislativa` hereda `dossier.prompt.md` y `SKILL.md` de `.github/`.

## Criterio de aceptación

- `git diff main..mod/legislativa -- .github/prompts/dossier.prompt.md` = vacío (hereda de main).
- `git diff main..mod/legislativa -- .github/skills/cristalizacion-feature/SKILL.md` = vacío (hereda de main).
- `git ls-tree -r --name-only main -- sala/archivo | grep sprint-extraccion-sala-v2` devuelve el archivo publicado.
- Grep de `BACKLOG_\*|PLAN_\*|RESPUESTAS_USUARIO_\*|mod/skills/cristalizacion-feature/SKILL.md|mod/prompts/dossier.prompt.md` en rutas no archivadas = 0 hits, salvo puente temporal documentado.
