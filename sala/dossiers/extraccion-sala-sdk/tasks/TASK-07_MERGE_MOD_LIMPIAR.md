# TASK ES-07 — Merge main → mod/legislativa + limpiar duplicados

- **Estado:** libre
- **Agente sugerido:** orquestador (manual)

## Descripción

En la rama `mod/legislativa`:
1. `git merge main` — hereda los artefactos de sala del SDK
2. Eliminar los ficheros duplicados en `mod/` que ahora vienen de `.github/`
3. Si `sala-aleph.prompt.md` es lore-specific, mantenerlo en `mod/prompts/` como override
4. Actualizar `mod/copilot-instructions.md` si es necesario

## Criterios de aceptación

1. `mod/legislativa` hereda sala de `.github/`
2. No hay duplicados entre `.github/` y `mod/`
3. Los overrides lore-specific (si los hay) están en `mod/`
4. El pipeline completo sigue funcionando
