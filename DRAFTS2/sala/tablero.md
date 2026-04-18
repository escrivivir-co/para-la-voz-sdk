# Tablero de tareas — mod/legislativa

> **Última actualización:** 19-abr-2026 — orquestador (Claude Opus 4.6)
> **Agentes activos:** 3 slots disponibles
> **Estados:** `libre` · `asignada:{modelo}` · `en-curso:{modelo}` · `entregada:{modelo}` · `cerrada` · `superseded` · `condicional`
>
> **Orquestador:** si acabas de llegar a una ventana nueva, usa `/eres-aleph` o lee `DRAFTS2/sala/activacion-orquestador.md` para levantarte con todo el contexto.

---

## Tracks recomendados para 3 agentes

```
Agente 1 ──▶ Track PO (pipeline-operativo) ──▶ luego Track LP (finalizacion-lore-plan)
Agente 2 ──▶ Track CA (cadena-agentica)
Agente 3 ──▶ Track GJ (grafo-json)

FM-05 ──▶ último, cuando los 4 tracks estén cerrados
```

Esto es una sugerencia. Cualquier agente puede tomar cualquier tarea libre cuyas dependencias estén resueltas.

---

## Track PO — pipeline-operativo (5 tareas activas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| PO-01 | Crear `lore-schema.instructions.md` | — | `libre` |
| PO-02 | Crear `lore-estado.instructions.md` | PO-01 | `libre` |
| PO-03 | Crear `lore-routing.instructions.md` | PO-02 | `libre` |
| PO-04 | Actualizar `legislativa-universo.instructions.md` | PO-02 | `libre` |
| PO-05 | Validar @Pipeline /refresh status | PO-01..PO-04 | `libre` |

## Track CA — cadena-agentica (7 tareas activas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| CA-01 | Crear `puzzle.agent.md` | — | `libre` |
| CA-02 | Refactor `archivero-lore.agent.md` | CA-01 | `libre` |
| CA-03 | Refactor `grafista.agent.md` | — | `libre` |
| CA-04 | Crear `demiurgo.agent.md` | CA-03 | `libre` |
| CA-05 | Recablear `dramaturgo.agent.md` | CA-04 | `libre` |
| CA-06 | Actualizar `pipeline.agent.md` | CA-01..CA-05 | `libre` |
| CA-07 | Validar cadena agéntica | CA-06 | `libre` |

> **Nota:** CA-01 y CA-03 pueden ejecutarse en paralelo si tienes dos agentes libres.

## Track GJ — grafo-json (7 tareas activas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| GJ-01 | Crear `gramatica.md` | — | `libre` |
| GJ-02 | Crear `nodos.json` | GJ-01 | `libre` |
| GJ-03 | Crear `arcos.json` | GJ-01 | `libre` |
| GJ-04 | Crear `huecos.json` | GJ-01 | `libre` |
| GJ-05 | Crear `index.json` | GJ-02..GJ-04 | `libre` |
| GJ-06 | Validar vocabulario JSON | GJ-05 | `libre` |
| GJ-07 | Update `grafista.agent.md` con JSON | GJ-06 + **CA-03** | `libre` |

> **Cross-dep:** GJ-07 depende de CA-03 (refactor del Grafista). No empezar hasta que ambas estén cerradas.
> **Paralelo:** GJ-02, GJ-03, GJ-04 pueden ejecutarse simultáneamente tras GJ-01.

## Track LP — finalizacion-lore-plan (8 tareas activas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| LP-01 | Reconciliar PBIs §8 | — | `libre` |
| LP-02 | Cerrar sprints §9 | LP-01 | `libre` |
| LP-03 | Eliminar redundancias §10 | LP-01 | `libre` |
| LP-04 | Sección features agénticos §7 | — | `libre` |
| LP-05 | Preparar DRY schema §5-§6 | — | `libre` |
| LP-06 | Actualizar conteos | LP-01 | `libre` |
| LP-07 | Marcar como v1.0 final | LP-01..LP-06 | `libre` |
| LP-08 | Validar plan ↔ disco | LP-07 | `libre` |

> **Paralelo:** LP-01, LP-04 y LP-05 pueden empezar a la vez.

## Track FM — future-machine (2 tareas residuales)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| FM-05 | Validar cadena completa + lore migrado | **Todos los tracks** | `libre` |
| FM-06 | Warning main si aplica | Evidencia de fallo | `condicional` |

> FM-05 es la tarea de cierre global. Solo se ejecuta cuando PO, CA, GJ y LP estén cerrados.

---

## Tareas cerradas (referencia)

| Task | Dossier | Estado |
|------|---------|--------|
| PO-00 | pipeline-operativo | `cerrada` |
| CA-00 | cadena-agentica | `cerrada` |
| GJ-00 | grafo-json | `cerrada` |
| LP-00 | finalizacion-lore-plan | `cerrada` |
| FM-00 | future-machine | `cerrada` |
| FM-01 | future-machine | `cerrada` |
| FM-02 | future-machine | `superseded` |
| FM-03 | future-machine | `superseded` |
| FM-04 | future-machine | `superseded` |

---

## Resumen

| Track | Activas | Primeras libres (sin deps) |
|-------|---------|---------------------------|
| PO | 5 | PO-01 |
| CA | 7 | CA-01, CA-03 |
| GJ | 7 | GJ-01 |
| LP | 8 | LP-01, LP-04, LP-05 |
| FM | 1+1 | — (espera a los demás) |
| **Total** | **29** | **6 arrancables ya** |
