# Backlog — Cristalización del grafo JSON

> **Fecha de apertura:** 19-abr-2026
> **Estado:** abierto
> **Modelo de inicialización:** `Claude Opus 4.6`
> **Anclas:** `DRAFTS2/LORE_F-02_UNIVERSO.md`, `DRAFTS2/LORE_F-02_ARTEFACTO.md`

## Contexto compartido

Todos los tasks heredan este contexto:

- [Plan local](./PLAN_GRAFO_JSON.md)
- [Respuestas del usuario](./RESPUESTAS_USUARIO_GRAFO_JSON.md)
- [Skill cristalización-feature](../../mod/skills/cristalizacion-feature/SKILL.md)
- [LORE_F-02_UNIVERSO.md](../LORE_F-02_UNIVERSO.md) — grafo Markdown a migrar
- [LORE_F-02_ARTEFACTO.md](../LORE_F-02_ARTEFACTO.md) — reglas de construcción
- [CORPUS_PREVIEW.md](../CORPUS_PREVIEW.md) — fuente de vocabulario válido

## Regla DRY del backlog

- El backlog es índice y tracking.
- El detalle vive en `tasks/`.
- No se duplican reglas de `.github/`, `mod/` ni del plan.

## Tracking

| Task | Estado | Agente recomendado | Modelo | Dependencias | Entrega | Brief |
|---|---|---|---|---|---|---|
| GJ-00 | **Completado** | `Claude Opus 4.6` | `Claude Opus 4.6` | — | plan + backlog + respuestas | [TASK-00](./tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md) |
| GJ-01 | Pendiente | `Cristalizador` | modelo activo | GJ-00 | `DRAFTS2/grafo/gramatica.md` | [TASK-01](./tasks/TASK-01_GRAMATICA.md) |
| GJ-02 | Pendiente | `Cristalizador` | modelo activo | GJ-01 | `DRAFTS2/grafo/nodos.json` | [TASK-02](./tasks/TASK-02_NODOS_JSON.md) |
| GJ-03 | Pendiente | `Cristalizador` | modelo activo | GJ-01 | `DRAFTS2/grafo/arcos.json` | [TASK-03](./tasks/TASK-03_ARCOS_JSON.md) |
| GJ-04 | Pendiente | `Cristalizador` | modelo activo | GJ-01 | `DRAFTS2/grafo/huecos.json` | [TASK-04](./tasks/TASK-04_HUECOS_JSON.md) |
| GJ-05 | Pendiente | `Cristalizador` | modelo activo | GJ-02..GJ-04 | `DRAFTS2/grafo/index.json` | [TASK-05](./tasks/TASK-05_INDEX_JSON.md) |
| GJ-06 | Pendiente | `Grafista` | modelo activo | GJ-05 | informe de validación | [TASK-06](./tasks/TASK-06_VALIDACION_VOCABULARIO.md) |
| GJ-07 | Pendiente | `Cristalizador` | modelo activo | GJ-06 + dossier cadena-agéntica | update `grafista.agent.md` | [TASK-07](./tasks/TASK-07_UPDATE_GRAFISTA_JSON.md) |

## Dependencias entre tasks

```
GJ-00 (contexto)
  └── GJ-01 (gramática)
        ├── GJ-02 (nodos) ─┐
        ├── GJ-03 (arcos) ─┤──→ GJ-05 (index) ──→ GJ-06 (validación) ──→ GJ-07 (update grafista)
        └── GJ-04 (huecos) ┘
```

GJ-02, GJ-03 y GJ-04 pueden ejecutarse **en paralelo** tras GJ-01.

## Criterio de cierre del feature

1. Existen los 5 ficheros JSON en `DRAFTS2/grafo/` con los datos del caso actual.
2. La gramática (`gramatica.md`) está documentada y es legible.
3. Todas las piezas ancla referenciadas existen en `CORPUS_PREVIEW.md`.
4. Grafista puede leer el grafo JSON (además de Markdown legacy).
5. El routing (`lore-routing.instructions.md`) incluye `DRAFTS2/grafo/` como ruta canónica.
