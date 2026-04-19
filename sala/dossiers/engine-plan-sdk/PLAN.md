# Plan — engine-plan-sdk

> **Fecha:** 20-abr-2026
> **Autor:** Claude Opus 4.6 (Cristalizador + Aleph)
> **Dossier:** `sala/dossiers/engine-plan-sdk/`

## 1. Contexto

El SDK tiene un prompt (`/engine-plan`) y un skill (`engine-plan`) que juntos forman una **consola de simulación del pipeline E2E**. La consola permite arrancar la future-machine como servicio virtual, diagnosticar integración entre capas, inspeccionar nodos, detectar gaps y generar patches cross-branch.

El prompt ya existe y funciona. El skill ya existe con su SKILL.md completo. Lo que falta es:
- Promover el skill a estado operativo verificado (hoy es diseño especulativo)
- Implementar los tiers del backlog como tasks formales
- Conectar con `@Pipeline` real cuando FS-05 se cierre

### Artefactos existentes

| Artefacto | Ruta | Estado |
|-----------|------|--------|
| Prompt `/engine-plan` | `.github/prompts/engine-plan.prompt.md` | Operativo |
| Skill `engine-plan` | `.github/skills/engine-plan/SKILL.md` | Diseño — backlog especulativo |
| Ejemplo de sesión | `tmp/engine-log-2026-04-20-001032.md` | Referencia |
| Patch de ejemplo | `tmp/lore-f-patch-2026-04-20.md` | Referencia |

### Relación con otros dossiers

| Dossier | Relación |
|---------|----------|
| `future-machine-sdk` | Upstream — el skill consume la arquitectura que FS define |
| `lore-db-sdk` .. `cortos-sdk` | Laterales — el skill inspecciona/diagnostica cada capa |
| `dossier-feature-sdk` | Infraestructura — el dossier usa el scaffold que DF definió |

## 2. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| SKILL.md operativo | `.github/skills/engine-plan/SKILL.md` | 15 secciones, backlog incluido |
| Prompt operativo | `.github/prompts/engine-plan.prompt.md` | Boot + run + inspect + log/log-std |
| Pipeline SDK (futuro) | `future-machine-sdk` FS-05 | Libre — el skill evoluciona con él |

## 3. Restricciones

- El skill es **protocolo puro** — no define datos de ningún mod
- El skill funciona sin `@Pipeline` real (modo simulación)
- Los patches cross-branch van a `tmp/`, nunca se escriben en rama ajena directamente
- El skill no duplica los dossiers de capas — los referencia

## 4. Propuesta

### Tier 1 — Protocolo base verificado (EP-01 a EP-06)

Verificar que las 15 secciones del SKILL.md funcionan end-to-end con datos reales de mod/legislativa. Añadir los 6 comandos nuevos del tier 1 del backlog: `diff`, `history`, `validate`, `trace`, `coverage`, `plan`.

### Tier 2 — Integración con sala (EP-07 a EP-09)

Conectar el diagnóstico del pipeline con la generación de tasks y la planificación de sprints. `task-suggest`, `sprint-scope`, `dossier-sync`.

### Tier 3 — Machine real (EP-10 a EP-14)

Transicionar de simulación a operación real cuando `@Pipeline` exista. Hooks, MCP, plugin packaging. Cada uno con gate operativo explícito.

### Tier 4-5 — Observabilidad e inteligencia (EP-15 a EP-18)

Dashboard persistente, métricas, detección de patrones, simulación de futuros del propio pipeline.

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)
