# REVISION — REV-DF-01

> **Task original:** DF-01 — Promover `dossier.prompt.md` a `.github/prompts/`
> **Agente entregador:** Gepe (GPT-5.4)
> **Revisor:** aleph-review (Claude Opus 4.6)
> **Fecha:** 2026-04-19

## Veredicto: **aprobada**

## Artefacto revisado

`sala/agente-gepe/candidato-dossier.prompt.md`

## Revisión contra criterios de aceptación

| Criterio (TASK-01) | Resultado | Notas |
|---------------------|-----------|-------|
| El prompt funciona sin presuponer ningún mod | ✓ | Cero refs a lore, corpus o mod. Usa `{{SALA_DIR}}` en todas las rutas. |
| Describe formato actual (`PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`, `activacion.prompt.md`, `tasks/`) y no el legado | ✓ | Scaffold en Paso 1 usa nombres canónicos. `continuar` y `listar` usan `BACKLOG.md`, no `BACKLOG_{NOMBRE}`. |
| No contradice absorción de scaffold rico en `main` | ✓ | "No rebajes el dossier a un esqueleto mínimo. Parte del scaffold vivo de `{{SALA_DIR}}/plantilla-dossier/`..." |
| Grep `DRAFTS2\|legislativa\|PLAN_\{\|BACKLOG_\{\|RESPUESTAS_USUARIO_\{\|mod/skills` = 0 hits | ✓ | Verificado por revisor: 0 hits. |

## Revisión de cambios requeridos (TASK-01)

| Cambio requerido | Implementado | Notas |
|------------------|-------------|-------|
| 1. Rutas `sala/...` → `{{SALA_DIR}}/...` | ✓ | Todas las rutas usan variable. |
| 2. Formato scaffold actualizado | ✓ | `PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`, `activacion.prompt.md`, `tasks/`. |
| 3. Relación con `sala` explícita | ✓ | Intro: "abren o mantienen tracks que después ejecuta `/sala-aleph`, `/sala-entrar`, `/sala-seguir` y `/sala-archivar`". |
| 4. Ref al SKILL: `.github/skills/cristalizacion-feature/SKILL.md` | ✓ | Línea 12: "El protocolo de diseño vive en `.github/skills/cristalizacion-feature/SKILL.md`." |
| 5. `continuar` y `listar` usan `BACKLOG.md` | ✓ | Ambas operaciones leen `BACKLOG.md` directamente. |
| 6. Frontmatter preservado | ✓ | `name`, `description`, `argument-hint`, `tools` presentes. |
| 7. Scaffold rico heredable | ✓ | Paso 1 y Paso 3 exigen scaffold completo, no mínimo. |
| 8. Sin refs a lore específico | ✓ | Limpio. |

## Observaciones

1. El candidato referencia `.github/skills/cristalizacion-feature/SKILL.md` que aún no existe en disco — es output de DF-02. Esto es correcto: ambos artefactos son insumos de DF-03, que hará la integración conjunta.
2. La ENTREGA de gepe recomienda no copiar a `.github/prompts/` hasta DF-03. Decisión acertada per PLAN §4.4.
3. Paso 4 (registro en tablero) es una mejora sobre el brief original: formaliza la coordinación prompt → tablero, que estaba implícita. No contradice nada.

## Conclusión

El candidato cumple todos los criterios de aceptación y todos los cambios requeridos del brief. Aprobada sin devoluciones.
