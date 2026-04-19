# Tablero de tareas — LoreSDK

> **Sprint:** sprint-lore-db-grafo-v1
> **Última actualización:** 19-abr-2026 — orquestador (GPT-5.4)
> **Agentes activos:** 0 slots ocupados; sala lista para entradas
> **Estados:** `libre` · `propuesta:{alias}` · `en-curso:{alias}` · `entregada:{alias}` · `cerrada` · `no-aplica`
>
> **Orquestador:** si acabas de llegar a una ventana nueva, usa `/sala-aleph` o lee `sala/activacion-orquestador.md` para levantarte con todo el contexto.

### Glosario de estados

| Estado | Significado |
|--------|-------------|
| `libre` | Disponible. Cualquier agente puede proponerla si las dependencias están resueltas. |
| `propuesta:{alias}` | Un agente la propuso en su `estado.md`. Esperando que Aleph apruebe o redirija. |
| `en-curso:{alias}` | Aleph aprobó. El agente está trabajando. Tiene carpeta temporal en `sala/agente-{alias}/`. |
| `entregada:{alias}` | El agente terminó. Hay entrega en su carpeta. El orquestador debe revisar. |
| `cerrada` | Revisada y aceptada por el orquestador. Copiada al dossier si aplica. |
| `no-aplica` | No se ejecuta. |

---

## Tracks recomendados

```text
Regla operativa de este sprint:
- SS, DF, PS y GS son tracks SDK: producen artefactos para `main`.
- LP y GL son tracks mod: producen artefactos para `mod/legislativa`.
- Aleph no desbloquea tareas mod dependientes hasta verificar el merge `main -> mod/legislativa` cuando corresponda.

Camino recomendado:
1. Abrir en paralelo DF-01 + DF-02, PS-01 + PS-02, GS-01 + GS-02.
2. Cerrar base SDK: PS-03, PS-04, PS-05, GS-03, GS-04, DF-03.
3. Cerrar unidad `sala-sdk`: SS-01.
4. Tras PS-05 mergeado a mod: LP-01 -> LP-01b -> LP-03 -> LP-02 -> LP-04 -> LP-05.
5. Tras LP-01b y GS-01: GL-02 + GL-01 -> GL-03 -> GL-04.
6. Cerrar sprint revisando coherencia final main/mod y dejar backlog de protocolo branch-aware si sigue pendiente.
```

---

## Track SS — sala-sdk (2 tareas, target `main`)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| SS-00 | Contexto y especificación de la unidad `sala-sdk` | — | `cerrada` |
| SS-01 | Cerrar unidad `sala-sdk` y publicar archivo histórico en `main` | DF-03 | `libre` |

> Dossier: `sala/dossiers/sala-sdk/`

---

## Track DF — dossier-feature-sdk (3 tareas, target `main`)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| DF-01 | Promover dossier.prompt.md al SDK | — | `libre` |
| DF-02 | Promover cristalizacion-feature/SKILL.md al SDK | — | `libre` |
| DF-03 | Integrar en SDK y limpiar mod | DF-01, DF-02 | `libre` |

> Dossier: `sala/dossiers/dossier-feature-sdk/`

---

## Track PS — lore-db-sdk (5 tareas, target `main`)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| PS-01 | Schema genérico de piezas | — | `libre` |
| PS-02 | Template de inventario de piezas | — | `libre` |
| PS-03 | Crear @Loreador SDK | PS-01 | `libre` |
| PS-04 | Documentar piezas en copilot-instructions.md | PS-01, PS-02 | `libre` |
| PS-05 | Scaffold lore-db en main + inicialización automática | PS-01, PS-02 | `libre` |

> Dossier: `sala/dossiers/lore-db-sdk/`

---

## Track GS — grafo-sdk (4 tareas, target `main`)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| GS-01 | Crear schema genérico de grafo | — | `libre` |
| GS-02 | Crear template de gramática de grafo | — | `libre` |
| GS-03 | Ampliar Dramaturgo SDK para leer grafo | GS-01 | `libre` |
| GS-04 | Documentar el grafo en el SDK | GS-01, GS-02 | `libre` |

> Dossier: `sala/dossiers/grafo-sdk/`

---

## Track LP — lore-db-legislativa (6 tareas, target `mod/legislativa`)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| LP-01 | Crear lore-db: estructura canónica de la base de datos de piezas | PS-05 | `libre` |
| LP-01b | Migrar piezas de DRAFTS2/ a lore/ | LP-01 | `libre` |
| LP-02 | Adaptar lore-schema para heredar del SDK | LP-01b, PS-01 | `libre` |
| LP-03 | Adaptar lore-routing con {{LORE_DIR}} | LP-01b | `libre` |
| LP-04 | Formalizar grafo de dependencias del pipeline | LP-02 | `libre` |
| LP-05 | Nuevo mapa agéntico del mod: Loreador Legislativa + Archivero Legislativa + Pipeline | LP-02, LP-04, PS-03 | `libre` |

> Dossier: `sala/dossiers/lore-db-legislativa/`

---

## Track GL — grafo-legislativa (4 tareas, target `mod/legislativa`)

| Task | Título | Deps | Estado |
|------|--------|------|--------|
| GL-01 | Migrar el grafo JSON a `lore/derivados/grafo/` | LP-01b, GS-01 | `libre` |
| GL-02 | Migrar artefacto, universo y cortos a `lore/derivados/` | LP-01b | `libre` |
| GL-03 | Actualizar refs de agentes e instructions al grafo migrado | GL-01, GL-02 | `libre` |
| GL-04 | Validar integridad del grafo tras la migración | GL-03 | `libre` |

> Dossier: `sala/dossiers/grafo-legislativa/`

---

## Backlog post-sprint

| ID | Título | Prioridad | Notas |
|----|--------|-----------|-------|
| BL-01 | Protocolo branch-aware de sala | media | Evaluar promoción al protocolo general tras comprobar este sprint mixto main/mod |

---

## Tareas cerradas (referencia)

| Task | Dossier | Estado |
|------|---------|--------|
| SS-00 | sala-sdk | `cerrada` |

---

> **⚠️ Aleph:** actualiza esta tabla cada vez que cierres una task. Si no, se desincroniza.

| Track | Total | Cerradas | Libres | En curso | Primeras libres (sin deps) |
|-------|-------|----------|--------|----------|----------------------------|
| SS | 2 | 1 | **1** | 0 | — (espera DF-03) |
| DF | 3 | 0 | **3** | 0 | DF-01, DF-02 |
| PS | 5 | 0 | **5** | 0 | PS-01, PS-02 |
| GS | 4 | 0 | **4** | 0 | GS-01, GS-02 |
| LP | 6 | 0 | **6** | 0 | — (espera PS-05) |
| GL | 4 | 0 | **4** | 0 | — (espera LP-01b y GS-01) |
| **Total** | **24** | **1** | **23** | **0** | — |