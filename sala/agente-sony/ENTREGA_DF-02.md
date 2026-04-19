# ENTREGA — DF-02

> **Task:** DF-02 — Promover `cristalizacion-feature/SKILL.md` a `.github/skills/`
> **Agente:** Sony (Claude Sonnet 4.6)
> **Fecha:** 2026-04-19

## Resultado

Candidato generalizado y verificado. Listo para que Aleph copie a `.github/skills/cristalizacion-feature/SKILL.md`.

## Ficheros producidos

| Fichero | Ruta en carpeta | Destino final |
|---------|-----------------|---------------|
| `candidato-SKILL.md` | `sala/agente-sony/candidato-SKILL.md` | `.github/skills/cristalizacion-feature/SKILL.md` |

## Cambios respecto al original (`mod/skills/cristalizacion-feature/SKILL.md`)

El fichero original no existe en este workspace (no hay carpeta `mod/`). El candidato fue sintetizado desde:
- `sala/dossiers/dossier-feature-sdk/TASK-02_PROMOVER_SKILL.md` (cambios requeridos)
- `sala/dossiers/dossier-feature-sdk/PLAN.md` (contexto y criterios)
- Skills existentes en `.github/skills/` (formato YAML frontmatter + secciones)
- `sala/plantilla-dossier/PLAN.md` (scaffold canónico actual)

### Cambios implementados

1. **Ubicación canónica:** `.github/skills/cristalizacion-feature/SKILL.md` (no `mod/`).
2. **Estructura del dossier:** describe el formato actual: `PLAN.md`, `BACKLOG.md`, `RESPUESTAS.md`, `activacion.prompt.md`, `tasks/`. Incluye plantillas completas de cada fichero.
3. **Relación con `sala`:** explícita — los dossiers viven en `{{SALA_DIR}}/dossiers/`, sobreviven al sprint y son la capa de diseño que activa `/dossier`.
4. **R4 (restricción de escritura):** reescrita para promociones al SDK: el agente deja candidatos en su carpeta, Aleph copia al destino final. Incluye también el caso de promociones a `.github/`.
5. **Referencias de ejemplo:** sin rutas hardcoded ni paths de archivo. Usa `{{SALA_DIR}}` en todas las rutas relativas.
6. **Consumidores:** "cualquier agente que gestione features o abra dossiers" — eliminada referencia a `@Cristalizador`.
7. **R5 (absorción en main):** nueva regla explícita: protocolo y scaffold rico pertenecen al SDK base; mods solo añaden delta local.
8. **Sin lore específico:** cero referencias a `legislativa`, `DRAFTS2`, rutas hardcoded o taxonomías de corpus.

### Verificación de criterios de aceptación

| Criterio | Estado |
|----------|--------|
| SKILL funciona sin presuponer ningún mod | ✓ |
| SKILL describe formato actual del dossier (no legado) | ✓ |
| Rescata material portable del archivo (scaffold rico: `activacion.prompt.md`, `RESPUESTAS.md` con efecto operativo, `Lee primero`, `Criterio de aceptación`) | ✓ |
| Grep `DRAFTS2\|legislativa\|PLAN_<\|BACKLOG_<\|RESPUESTAS_USUARIO_<\|mod/skills` = 0 hits | ✓ (verificado) |
| R4 permite promociones al SDK explícitamente | ✓ |

## Pasos que Aleph debe ejecutar

1. **Copiar** `sala/agente-sony/candidato-SKILL.md` → `.github/skills/cristalizacion-feature/SKILL.md` (crear directorio si no existe).
2. **Verificar** grep de exclusiones en el destino final.
3. **Actualizar** tablero: DF-02 → `entregada:sony` → `cerrada`.
4. **Actualizar** `sala/agente-sony/estado.md`: `Estado: entregada`.
5. Si DF-01 también está entregada: desbloquear DF-03.
