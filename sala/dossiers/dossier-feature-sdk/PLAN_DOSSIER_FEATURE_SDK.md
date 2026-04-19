# PLAN INICIAL — dossier-feature-sdk

> **Fecha:** 19-abr-2026
> **Modelo:** `Claude Opus 4.6`
> **Estado:** abierto
> **Prioridad:** media
> **Anclas:** `mod/prompts/dossier.prompt.md`, `mod/skills/cristalizacion-feature/SKILL.md`, `.github/copilot-instructions.md`

### [Claude Opus 4.6] Inicialización del plan base

#### 1. Contexto DRY

El patrón "dossier de feature" (PLAN + BACKLOG + RESPUESTAS + tasks/ + activacion.prompt.md) fue desarrollado en `mod/legislativa` y se usó para 5 features en el sprint cristalizacion-v1. Es completamente genérico: cualquier mod puede necesitar gestionar features con dossiers.

Dos artefactos son portables al SDK:

| Artefacto | Ubicación actual | Tipo |
|-----------|-----------------|------|
| `dossier.prompt.md` | `mod/prompts/` | Prompt `/dossier` — crea, continúa, lista dossiers |
| `cristalizacion-feature/SKILL.md` | `mod/skills/` | Protocolo completo de ciclo de vida del dossier |

Contexto adicional ya en el SDK:
- La estructura `{{SALA_DIR}}/dossiers/` ya está formalizada en `.github/copilot-instructions.md`
- `sala/plantilla-dossier/` ya existe con scaffold vacío
- `/sala-archivar` ya maneja el archivado de dossiers cerrados

#### 2. Agente ejecutor

Cualquier agente de sala. Las 3 tasks son independientes (DF-01 y DF-02 paralelas; DF-03 depende de ambas).

#### 3. Restricciones

- Las tasks escriben en `.github/` (SDK main) — requiere rama `feat/dossier-sdk` y merge por Aleph.
- El prompt y el SKILL deben ser **genéricos**: sin refs a lore legislativa, DRAFTS2, ni rutas hardcoded. Usar `{{SALA_DIR}}` donde corresponda.
- R4 del SKILL no aplica: este dossier promueve a `.github/` por diseño.

#### 4. Generalización de `dossier.prompt.md`

- Rutas: ya usa `sala/dossiers/` y `sala/tablero.md` — verificar que no quede ningún `DRAFTS2/` ni `mod/legislativa`.
- Refs cruzadas: la ref a `mod/skills/cristalizacion-feature/SKILL.md` debe actualizarse a `.github/skills/cristalizacion-feature/SKILL.md`.
- Fronmatter: OK tal cual.

#### 5. Generalización de `cristalizacion-feature/SKILL.md`

- Ubicación canónica: actualizar de `mod/skills/` a `.github/skills/`.
- Rutas de ejemplo: actualizar refs a dossiers archivados.
- R4: relajar restricción "Los artefactos propuestos van en `mod/`" → "Los artefactos propuestos van en `mod/` (o `.github/` si son promociones al SDK)."
- Refs a `DRAFTS2/`: eliminar (ya no quedan tras migraciones anteriores, pero verificar).

#### 6. Actualizar `.github/copilot-instructions.md`

Añadir `/dossier` a la tabla de comandos de sala con descripción breve.

## Salida operativa

- Tracking: [BACKLOG](./BACKLOG_DOSSIER_FEATURE_SDK.md)
- Tasks: carpeta [tasks](./tasks)
