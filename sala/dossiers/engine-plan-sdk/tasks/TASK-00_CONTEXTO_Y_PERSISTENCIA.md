# TASK-00 — Contexto y persistencia del dossier engine-plan-sdk

> **Estado:** cerrada
> **Agente:** Claude Opus 4.6 (Cristalizador + Aleph)
> **Dependencias:** —
> **Entrega esperada:** SKILL.md + prompt + ejemplo de sesión + scaffold de dossier

## Objetivo

Crear los artefactos fundacionales del skill `engine-plan`: el SKILL.md con protocolo completo, el prompt `/engine-plan`, un ejemplo de sesión real, y el scaffold del dossier con backlog especulativo.

## Artefactos producidos

1. `.github/skills/engine-plan/SKILL.md` — 15 secciones, backlog especulativo de 5 tiers
2. `.github/prompts/engine-plan.prompt.md` — prompt con modos: big picture, foco por capa, log, log-std
3. `tmp/engine-log-2026-04-20-001032.md` — sesión real log-std (boot + loadMOCK + snapshot + update + writing)
4. `tmp/lore-f-patch-2026-04-20.md` — patch cross-branch generado en sesión
5. `sala/dossiers/engine-plan-sdk/` — scaffold completo del dossier

## Criterio de aceptación

- [x] SKILL.md cubre boot, run, inspect, gaps, data, spec, docs, patch, log format
- [x] Prompt funciona en modo log-std con datos reales
- [x] Ejemplo de sesión demuestra el protocolo end-to-end
- [x] Dossier tiene PLAN, BACKLOG, RESPUESTAS y activacion.prompt.md
