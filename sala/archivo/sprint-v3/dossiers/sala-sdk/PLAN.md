# Plan — sala-sdk

> **Fecha:** 19-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/sala-sdk/`

## 1. Contexto

La extracción de `sala` al SDK ya ocurrió operativamente en el sprint archivado `extraccion-sala-sdk`: prompts `sala-*`, instructions, templates y sección específica en `.github/copilot-instructions.md`.

Quedó, sin embargo, una fragmentación de lectura:

- el archivo histórico de la extracción vive hoy en `sala/archivo/sprint-extraccion-sala-v2/`
- la capa de diseño persistente (`/dossier` + `cristalizacion-feature/SKILL.md`) se sigue cerrando en `dossier-feature-sdk`
- el scaffold rico de `dossier` sigue estando mejor expresado en el archivo viejo y en `sala/plantilla-dossier/` que en la plantilla SDK actual
- al listar dossiers activos no existe todavía una unidad visible llamada `sala-sdk`

Abrir `sala-sdk` tiene sentido como dossier paraguas: deja una unidad reconocible para documentación, listado y cierre histórico, sin reabrir la implementación que ya está separada en subtracks.

## 2. Anclas

| Artefacto | Ubicación | Papel |
|-----------|-----------|-------|
| Dossier archivado de extracción | `sala/archivo/sprint-extraccion-sala-v2/dossiers/extraccion-sala-sdk/` | Antecedente operativo de `sala` en SDK |
| Cierre del sprint | `sala/archivo/sprint-extraccion-sala-v2/CIERRE.md` | Confirma que `dossier-feature-sdk` era el siguiente backlog |
| Protocolo vivo de sala | `sala/README.md` | Define que el dossier diseña y la sala ejecuta |
| Superficie SDK ya publicada | `.github/prompts/sala-*.prompt.md`, `.github/instructions/sala-protocolo.instructions.md`, `.github/templates/sala-*.template.md` | Núcleo operativo ya exportado |
| Dossier hijo | `sala/dossiers/dossier-feature-sdk/` | Cierra la capa de diseño persistente de `sala` |
| Documentación SDK | `.github/copilot-instructions.md` | Punto de consolidación documental |

## 3. Restricciones

- Este dossier no duplica las tasks implementativas de `dossier-feature-sdk`.
- `sala-sdk` sirve como unidad paraguas y documental; el trabajo fino de `/dossier` sigue viviendo en el track DF.
- El cierre de `sala-sdk` depende de que `dossier-feature-sdk` cierre DF-03.
- El archivo `sprint-extraccion-sala-v2` debe terminar publicado en `main`, no solo en `mod/legislativa`.

## 4. Propuesta

### 4.1. Tratar `sala` como unidad visible del SDK

El dossier `sala-sdk` agrupa conceptualmente tres piezas:

1. superficie operativa ya exportada (`/sala-*`, instructions, templates)
2. capa de diseño persistente que se está cerrando en `dossier-feature-sdk`
3. archivo histórico de la extracción, que debe quedar accesible en `main`
4. scaffold rico de dossier que `main` debe absorber para que cualquier rama lo herede

### 4.2. Relación con `dossier-feature-sdk`

`dossier-feature-sdk` se mantiene como dossier hijo, porque ahí vive el backlog accionable de la capa `dossier`.

`sala-sdk` no lo sustituye; lo encapsula para que la lista de dossiers del sprint tenga una unidad legible equivalente a `lore-db-sdk`, `grafo-sdk`, `corpus-sdk`, `universos-sdk`, `cortos-sdk` o `future-machine-sdk`.

### 4.3. Cierre esperado

Cuando DF-03 cierre:

- `/dossier` y `cristalizacion-feature/SKILL.md` estarán publicados en `.github/`
- el scaffold rico de dossier estará absorbido por `main`, no retenido como saber tácito del mod
- el archivo `sala/archivo/sprint-extraccion-sala-v2/` estará publicado en `main`
- la documentación podrá referirse a `sala-sdk` como unidad y a `dossier-feature-sdk` como subdossier de cierre

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)