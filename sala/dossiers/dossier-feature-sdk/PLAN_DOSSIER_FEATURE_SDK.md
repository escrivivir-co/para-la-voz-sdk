# Dossier — dossier-feature-sdk

> **Prioridad:** media
> **Tasks estimadas:** 3
> **Rama:** `feat/dossier-sdk` (desde main)

## Contexto

El patrón "dossier de feature" (PLAN + BACKLOG + RESPUESTAS + tasks/ + activacion.prompt.md) fue desarrollado en `mod/legislativa` y se usó para 5 features en el sprint cristalizacion-v1. Es completamente genérico: cualquier mod puede necesitar gestionar features con dossiers.

Dos artefactos clave son 100% portables sin cambios:
- `mod/prompts/dossier.prompt.md` — crea/continúa dossiers
- `mod/skills/cristalizacion-feature/SKILL.md` — protocolo de ciclo de vida

## Inventario

### Artefactos a promover

| Origen (mod/) | Destino (.github/) | Cambios |
|---|---|---|
| `mod/prompts/dossier.prompt.md` | `.github/prompts/dossier.prompt.md` | Mínimos: eliminar refs a DRAFTS2 si las hay |
| `mod/skills/cristalizacion-feature/SKILL.md` | `.github/skills/cristalizacion-feature/SKILL.md` | Verificar que no hay refs a lore legislativa |

### Cambios adicionales

- Actualizar `.github/copilot-instructions.md` con `/dossier` en la tabla de comandos
- Actualizar `mod/` para que herede del SDK tras merge

## Operación

1. Crear rama `feat/dossier-sdk` desde main
2. Copiar + generalizar los 2 artefactos
3. Actualizar copilot-instructions.md
4. Merge a main
5. En mod/legislativa: merge main → limpiar duplicados
