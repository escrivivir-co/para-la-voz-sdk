# TASK-01 — Cerrar unidad `sala-sdk` y publicar archivo histórico

> **Estado:** libre
> **Agente recomendado:** Aleph
> **Dependencias:** DF-03
> **Entrega esperada:** `sala-sdk` cerrado como unidad, scaffold rico absorbido en `main` y `sala/archivo/sprint-extraccion-sala-v2/` publicado en `main`

## Lee primero

1. `sala/dossiers/sala-sdk/PLAN.md`
2. `sala/dossiers/dossier-feature-sdk/PLAN.md`
3. `sala/dossiers/dossier-feature-sdk/tasks/TASK-03_INTEGRAR_SDK_Y_LIMPIAR.md`
4. `sala/archivo/sprint-extraccion-sala-v2/CIERRE.md`
5. `.github/copilot-instructions.md`
6. `.github/templates/sala-dossier.template.md` y `sala/plantilla-dossier/`

## Objetivo

Cerrar `sala-sdk` como unidad documental y operativa cuando la capa `dossier` ya esté exportada al SDK.

## Restricciones

- No duplicar trabajo de DF-03.
- Esta task solo se cierra cuando el archivo histórico de `sala` ya está en `main`.

## Salida mínima esperada

1. `DF-03` está cerrada.
2. El scaffold rico de `dossier` está absorbido en `main` y listo para herencia por ramas.
3. `sala/archivo/sprint-extraccion-sala-v2/` existe en `main`.
4. La documentación puede referirse a `sala-sdk` como unidad del SDK.

## Criterio de aceptación

- `git ls-tree -r --name-only main -- sala/archivo | grep sprint-extraccion-sala-v2` devuelve el archivo publicado.
- `.github/templates/sala-dossier.template.md` ya recoge el scaffold rico portable y no deja esa carga en el mod.
- `dossier-feature-sdk` ya no queda como pieza huérfana, sino como cierre hijo de `sala-sdk`.