# Plan — dossier-feature-sdk

> **Fecha:** 19-abr-2026
> **Autor:** Claude Opus 4.6 + GPT-5.4
> **Dossier:** `sala/dossiers/dossier-feature-sdk/`
> **Anclas:** `sala/archivo/sprint-extraccion-sala-v2/dossiers/extraccion-sala-sdk/`, `sala/archivo/sprint-extraccion-sala-v2/CIERRE.md`, `sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-pipeline-operativo/`, `sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-cadena-agentica/`, `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/`, `sala/README.md`, `mod/prompts/dossier.prompt.md`, `mod/skills/cristalizacion-feature/SKILL.md`, `sala/plantilla-dossier/`, `.github/templates/sala-dossier.template.md`, `.github/copilot-instructions.md`

### [GPT-5.4] Adenda — `dossier` como subcomponente de `sala` (19-abr-2026)

`dossier` no se trata ya como feature paralelo a `sala`. Es la capa de diseño persistente de `sala`: `/dossier` crea o mantiene el track, escribe en `{{SALA_DIR}}/dossiers/`, y deja listo el trabajo que luego ejecutan `/sala-aleph`, `/sala-entrar`, `/sala-seguir` y `/sala-archivar`.

### [GPT-5.4] Adenda — publicar el archivo SDK en `main` (19-abr-2026)

El archivo `sala/archivo/sprint-extraccion-sala-v2/` funciona como antecedente canónico de la extracción de `sala`, pero hoy vive solo en `mod/legislativa`. El cierre correcto de este dossier debe publicarlo también en `main` para que la historia del SDK quede archivada donde pertenece.

## 1. Contexto

El sprint archivado `extraccion-sala-sdk` ya exportó al SDK la superficie operativa de `sala`: 7 prompts `sala-*`, 2 instructions, 3 templates y la sección correspondiente en `.github/copilot-instructions.md`. El cierre de ese sprint dejó `dossier-feature-sdk` como backlog del siguiente paso.

La relación correcta entre ambos es:

- `sala` = protocolo de coordinación y ejecución
- `dossier` = capa de diseño persistente dentro de `{{SALA_DIR}}/dossiers/`
- `/dossier` = trigger de apertura y continuidad de tracks
- `cristalizacion-feature/SKILL.md` = protocolo interno de esa capa

El problema actual no es solo de promoción a `.github/`. El prompt y el SKILL del mod siguen describiendo un formato viejo (`PLAN_<NOMBRE>`, `BACKLOG_<NOMBRE>`, `RESPUESTAS_USUARIO_<NOMBRE>`), mientras que la sala viva y `sala/plantilla-dossier/` ya usan `PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`. Además hay consumidores vivos del formato y la ruta antigua (`mod/README_MOD.md`, `mod/prompts/lore-status.prompt.md`), así que el cierre requiere migración de superficie, no solo copiar dos ficheros y borrar duplicados.

Además, el scaffold realmente bueno no está hoy en `.github/`: sigue repartido entre el archivo de `mod/legislativa` y la práctica viva de `sala/plantilla-dossier/`. Si `main` debe absorber el máximo de `sala` y `dossier`, el cierre correcto no es promover una versión mínima del prompt y del SKILL, sino llevar a `main` el **scaffold rico y portátil** que cualquier rama pueda heredar y luego especializar con delta local.

## 2. Ejecución

Cualquier agente puede preparar DF-01 y DF-02 en paralelo. DF-03 integra ambas entregas, alinea la superficie de `sala`, migra consumidores vivos y solo entonces cierra el puente `main -> mod`.

## 3. Restricciones

- Este dossier continúa `extraccion-sala-sdk`; no abre una línea de producto separada.
- El prompt y el SKILL deben ser genéricos: sin refs a lore legislativa, `DRAFTS2/` ni rutas hardcoded. Usar `{{SALA_DIR}}`.
- El formato canónico del dossier es el actual de `sala/plantilla-dossier/`: `PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`, `activacion.prompt.md`, `tasks/`.
- `main` debe absorber el máximo de la capa `dossier`: prompt, SKILL, template y contrato del scaffold. En `mod/` solo deben quedar overrides o delta local justificado.
- No prometer borrado de duplicados en `mod/` hasta que no queden consumidores vivos del formato o la ruta antigua.
- La integración en `.github/` sigue requiriendo publicación en `main` y herencia posterior desde `mod/legislativa`.

## 4. Propuesta

### 4.1. Reencuadre de producto

Promover `/dossier` y `cristalizacion-feature/SKILL.md` como parte de la superficie de `sala`, no como feature independiente. La cadena de activación queda:

1. `/dossier crear|continuar|listar` -> diseña o reactiva dossiers
2. `{{SALA_DIR}}/dossiers/` -> persiste plan, backlog y tasks
3. `{{SALA_DIR}}/tablero.md` -> registra track y estados
4. `/sala-aleph`, `/sala-entrar`, `/sala-seguir`, `/sala-archivar` -> ejecutan y cierran el track

### 4.2. Generalización de `dossier.prompt.md`

- Adoptar `{{SALA_DIR}}` en todas las rutas.
- Describir el formato vigente del scaffold (`PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`).
- Tratar `/dossier` como comando de diseño de `sala`, no como utilidad aislada.
- Actualizar referencias cruzadas al SKILL canónico en `.github/skills/`.
- Ajustar `continuar` y `listar` al nombre real de `BACKLOG.md`.

### 4.3. Generalización de `cristalizacion-feature/SKILL.md`

- Mover la ubicación canónica a `.github/skills/cristalizacion-feature/SKILL.md`.
- Reescribir la estructura del dossier al formato actual.
- Explicitar que los dossiers viven dentro de `{{SALA_DIR}}/dossiers/` y sobreviven a la sala o sprint que los ejecutó.
- Reescribir R4 para promociones al SDK: el agente deja candidatos en su carpeta y Aleph copia al destino final.
- Actualizar el ejemplo de referencia para que no dependa de rutas o convenciones obsoletas.

### 4.4. Superficie, triggers, archivo y migración

- `main` debe absorber el máximo de `sala` y `dossier`, incluyendo el scaffold rico portable: no solo `/dossier` y el SKILL, también la plantilla/contrato que cualquier rama pueda traer sin reabrir arqueología del mod.
- Alinear `.github/templates/sala-dossier.template.md` con `sala/plantilla-dossier/` y con lo mejor del archivo viejo: `Contexto compartido`, `Regla DRY`, `Tracking` con entrega/dependencias, tasks con `Lee primero`, `Salida mínima esperada` y `Criterio de aceptación`, y `RESPUESTAS` con `Efecto operativo`.
- Dejar el scaffold rico como superficie heredable por cualquier rama; las ramas solo añaden delta local, no reconstruyen el protocolo base.
- Añadir `/dossier` a la documentación de `sala` en `.github/copilot-instructions.md` como comando de diseño persistente.
- Publicar `sala/archivo/sprint-extraccion-sala-v2/` en `main` junto con el cierre de la capa `dossier`, para que el antecedente de extracción de `sala` no quede solo en la rama del mod.
- Revisar consumidores vivos del formato antiguo o de las rutas `mod/...` y actualizarlos o puentearlos: al menos `mod/README_MOD.md` y `mod/prompts/lore-status.prompt.md`.
- Tratar el cleanup en `mod/` como paso final de migración: se elimina si no queda ningún consumidor vivo; si hace falta puente temporal, debe quedar explícito y sin drift.

## Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)
