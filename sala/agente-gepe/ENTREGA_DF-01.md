# ENTREGA_DF-01

> **Task:** DF-01
> **Alias:** Gepe
> **Modelo:** GPT-5.4
> **Fecha:** 2026-04-19T10:02:06+02:00

## Resumen

Se preparó un candidato de `/dossier` orientado a SDK y a `sala`, no a un mod concreto.
El prompt ya usa `{{SALA_DIR}}`, adopta el formato vigente del dossier (`PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`) y preserva el scaffold rico en lugar de volver al esquema legacy.
La relación con `sala` queda explícita: `/dossier` diseña y mantiene tracks; `/sala-*` los ejecuta.

## Artefactos producidos

- `sala/agente-gepe/candidato-dossier.prompt.md`
- `sala/agente-gepe/ENTREGA_DF-01.md`

## Diff respecto al prompt original

- Rutas generalizadas: `sala/...` pasa a `{{SALA_DIR}}/...` en dossiers, tablero y scaffold.
- Referencia canónica al protocolo: `.github/skills/cristalizacion-feature/SKILL.md` sustituye a la ruta antigua fuera del SDK.
- El scaffold deja de asumir nombres legacy y adopta `PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`, `activacion.prompt.md` y `tasks/`.
- `/dossier` deja de presentarse como prompt aislado y se define como capa de diseño persistente de `sala`.
- `continuar` y `listar` trabajan con `BACKLOG.md`, no con variantes derivadas del nombre del dossier.
- El registro en tablero se alinea con el funcionamiento actual: tasks ejecutables en el track y `TASK-00_CONTEXTO_Y_PERSISTENCIA` como referencia cerrada.

## Validación

- El candidato no contiene hits de `DRAFTS2`, `legislativa`, `PLAN_{`, `BACKLOG_{`, `RESPUESTAS_USUARIO_{` ni `mod/skills`.
- La fuente legacy `mod/prompts/dossier.prompt.md` y parte de las anclas del brief no están en el checkout actual; se recuperaron desde el historial git para comparar contra una base real.
- El contenido se contrastó con `sala/README.md`, `sala/plantilla-dossier/`, `.github/templates/sala-dossier.template.md` y el dossier vivo `dossier-feature-sdk`.

## Pasos para Aleph

1. Revisar `candidato-dossier.prompt.md`.
2. Si la propuesta es válida, marcar DF-01 como cerrada y dejar este candidato como insumo aprobado para DF-03.
3. No copiar aún a `.github/prompts/` desde esta task si se quiere mantener la integración junto con DF-02 y DF-03.