# TASK ES-04 — Crear templates de sala

- **Estado:** libre
- **Agente sugerido:** cualquiera

## Descripción

Crear plantillas reutilizables en `.github/templates/` para los artefactos de sala:

1. **sala-tablero.template.md** — estructura base del tablero (tracks, resumen, backlog)
2. **sala-dossier.template.md** — estructura de carpeta dossier (PLAN, BACKLOG, RESPUESTAS, activacion.prompt.md, tasks/)
3. **sala-agente.template.md** — estructura de carpeta agente (estado.md)

## Criterios de aceptación

1. Los 3 templates existen en `.github/templates/`
2. Usan placeholders tipo `{{NOMBRE_SPRINT}}`, `{{AGENTE}}`, etc.
3. Son autocontenidos — no requieren contexto del lore para instanciarse
