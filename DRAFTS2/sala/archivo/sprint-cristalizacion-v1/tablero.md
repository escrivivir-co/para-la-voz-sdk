# Tablero de tareas — mod/legislativa

> **Última actualización:** 19-abr-2026 — orquestador (Claude Opus 4.6)
> **Agentes activos:** 3 slots disponibles (se identifican por alias, no por modelo)
> **Estados:** `libre` · `propuesta:{alias}` · `en-curso:{alias}` · `entregada:{alias}` · `cerrada` · `superseded` · `condicional`
>
> **Orquestador:** si acabas de llegar a una ventana nueva, usa `/sala-aleph` o lee `DRAFTS2/sala/activacion-orquestador.md` para levantarte con todo el contexto.

### Glosario de estados

| Estado | Significado |
|--------|-------------|
| `libre` | Disponible. Cualquier agente puede proponerla si las dependencias están resueltas. |
| `propuesta:{alias}` | Un agente la propuso en su `estado.md`. Esperando que Aleph apruebe o redirija. |
| `en-curso:{alias}` | Aleph aprobó. El agente está trabajando. Tiene carpeta temporal en `sala/agente-{alias}/`. |
| `entregada:{alias}` | El agente terminó. Hay entrega en su carpeta. El orquestador debe revisar. |
| `cerrada` | Revisada y aceptada por el orquestador. Copiada al dossier si aplica. |
| `superseded` | El trabajo que proponía **ya se diseñó en otro dossier**. No cancelada: absorbida. No bloquea nada. |
| `condicional` | Solo se ejecuta si aparece **evidencia real** de un problema específico. Si no hay evidencia, no se ejecuta nunca. |

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
| PO-01 | Crear `lore-schema.instructions.md` | — | `cerrada` |
| PO-02 | Crear `lore-estado.instructions.md` | PO-01 | `cerrada` |
| PO-03 | Crear `lore-routing.instructions.md` | PO-02 | `cerrada` |
| PO-04 | Actualizar `legislativa-universo.instructions.md` | PO-02 | `cerrada` |
| PO-05 | Validar @Pipeline /refresh status | PO-01..PO-04 | `cerrada` |

## Track CA — cadena-agentica (7 tareas activas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| CA-01 | Crear `puzzle.agent.md` | — | `cerrada` |
| CA-02 | Refactor `archivero-lore.agent.md` | CA-01 | `cerrada` |
| CA-03 | Refactor `grafista.agent.md` | — | `cerrada` |
| CA-04 | Crear `demiurgo.agent.md` | CA-03 | `cerrada` |
| CA-05 | Recablear `dramaturgo.agent.md` | CA-04 | `cerrada` |
| CA-06 | Actualizar `pipeline.agent.md` | CA-01..CA-05 | `cerrada:boris` |
| CA-07 | Validar cadena agéntica | CA-06 | `cerrada:boris` |

> **Nota:** CA-01 y CA-03 pueden ejecutarse en paralelo si tienes dos agentes libres.

## Track GJ — grafo-json (7 tareas activas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| GJ-01 | Crear `gramatica.md` | — | `cerrada` |
| GJ-02 | Crear `nodos.json` | GJ-01 | `cerrada` |
| GJ-03 | Crear `arcos.json` | GJ-01 | `cerrada` |
| GJ-04 | Crear `huecos.json` | GJ-01 | `cerrada` |
| GJ-05 | Crear `index.json` | GJ-02..GJ-04 | `cerrada` |
| GJ-06 | Validar vocabulario JSON | GJ-05 | `cerrada:luna` |
| GJ-07 | Update `grafista.agent.md` con JSON | GJ-06 + **CA-03** | `cerrada` |

> **Cross-dep:** GJ-07 depende de CA-03 (refactor del Grafista). No empezar hasta que ambas estén cerradas.
> **Paralelo:** GJ-02, GJ-03, GJ-04 pueden ejecutarse simultáneamente tras GJ-01.

## Track LP — finalizacion-lore-plan (8 tareas activas)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| LP-01 | Reconciliar PBIs §8 | — | `cerrada:lai` |
| LP-02 | Cerrar sprints §9 | LP-01 | `cerrada:lai` |
| LP-03 | Eliminar redundancias §10 | LP-01 | `cerrada:boris` |
| LP-04 | Sección features agénticos §7 | — | `cerrada` |
| LP-05 | Preparar DRY schema §5-§6 | — | `cerrada` |
| LP-06 | Actualizar conteos | LP-01 | `cerrada:luna` |
| LP-07 | Marcar como v1.0 final | LP-01..LP-06 | `cerrada:boris` |
| LP-08 | Validar plan ↔ disco | LP-07 | `cerrada:lai` |

> **Paralelo:** LP-01, LP-04 y LP-05 pueden empezar a la vez.

## Track FM — future-machine (2 tareas residuales)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| FM-05 | Validar cadena completa + lore migrado | **Todos los tracks** | `cerrada:boris` |
| FM-06 | Warning main si aplica | Evidencia de fallo | `no-aplica` |

> FM-05 cerrada. Cadena funcional. Gap `corto-universo.prompt.md` registrado como backlog del mod (no afecta a SDK main).
> FM-06 no aplica: la validación no detectó fallos de SDK. El gap es deuda del mod.

---

## Backlog post-sprint

| ID | Título | Prioridad | Notas |
|----|--------|-----------|-------|
| BL-01 | Crear `mod/prompts/corto-universo.prompt.md` | media | Gap detectado en FM-05. El flujo funciona por invocación directa, falta el prompt formal. |
| BL-02 | Extraer "sala" a SDK main | alta | Promover sala-protocolo, sala-*.prompt.md, plantilla de tablero/carpetas a `.github/`. Luego mod/legislativa hace pull de main y hereda la sala como SDK. |

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
| PO-01 | pipeline-operativo | `cerrada` |
| PO-02 | pipeline-operativo | `cerrada` |
| PO-03 | pipeline-operativo | `cerrada` |
| PO-04 | pipeline-operativo | `cerrada` |
| CA-03 | cadena-agentica | `cerrada` |
| CA-04 | cadena-agentica | `cerrada` |
| GJ-01 | grafo-json | `cerrada` |
| PO-05 | pipeline-operativo | `cerrada` |
| CA-05 | cadena-agentica | `cerrada` |
| CA-01 | cadena-agentica | `cerrada` |
| GJ-02 | grafo-json | `cerrada` |
| GJ-04 | grafo-json | `cerrada` |
| LP-04 | finalizacion-lore-plan | `cerrada` |
| CA-02 | cadena-agentica | `cerrada` |
| GJ-03 | grafo-json | `cerrada` |
| CA-06 | cadena-agentica | `cerrada` |
| LP-05 | finalizacion-lore-plan | `cerrada` |
| GJ-05 | grafo-json | `cerrada` |
| GJ-06 | grafo-json | `cerrada` |
| LP-01 | finalizacion-lore-plan | `cerrada` |
| CA-07 | cadena-agentica | `cerrada` |
| LP-02 | finalizacion-lore-plan | `cerrada` |
| LP-03 | finalizacion-lore-plan | `cerrada` |
| LP-07 | finalizacion-lore-plan | `cerrada` |
| LP-06 | finalizacion-lore-plan | `cerrada` |
| LP-08 | finalizacion-lore-plan | `cerrada` |
| FM-05 | future-machine-universo-1 | `cerrada` |
| FM-06 | future-machine-universo-1 | `no-aplica` |

---

> **⚠️ Aleph:** actualiza esta tabla cada vez que cierres una task. Si no, se desincroniza.

| Track | Total | Cerradas | Libres | En curso | Primeras libres (sin deps) |
|-------|-------|----------|--------|----------|----------------------------|
| PO | 5 | **5** | 0 | 0 | — (track cerrado) |
| CA | 7 | **7** | 0 | 0 | — (track cerrado ✅) |
| GJ | 7 | **7** | 0 | 0 | — (track cerrado ✅) |
| LP | 8 | **8** | 0 | 0 | — (track cerrado ✅) |
| FM | 1+1 | **1** | 0 | 0 | — (track cerrado ✅, FM-06 no-aplica) |
| **Total** | **29** | **28+1na** | **0** | **0** | **🎉 Sprint cerrado — 29/29. Backlog post-sprint registrado.** |
