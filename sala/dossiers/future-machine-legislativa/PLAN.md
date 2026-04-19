# Plan — future-machine-legislativa

> **Fecha:** 19-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/future-machine-legislativa/`

## 1. Contexto

Una vez separado el pipeline en capas (`lore-db`, `corpus`, `grafo`, `universos`, `cortos`), mod/legislativa necesita volver a juntarlo como **máquina operable** del caso Feo.

Eso no significa reabsorber los dossiers anteriores. Significa instanciar la `future-machine` sobre el ecosistema nuevo para que:

- `Portal` la presente como fábrica completa
- `/user-empieza-aqui` la muestre como big picture real
- `/lore-status` la lea como dashboard de la máquina
- `Pipeline` ocupe el slot técnico de refresh
- el export de `lore/` pueda levantar ya los datos que hoy existen

Este dossier es la contraparte mod de `future-machine-sdk`.

Relación con otros dossiers:

| Dossier | Branch | Qué hace | Relación |
|---------|--------|----------|----------|
| `lore-db-legislativa` | mod/legislativa | Migra piezas y crea `lore/` | Slot upstream |
| `corpus-legislativa` | mod/legislativa | Materializa `corpus/` | Slot upstream |
| `grafo-legislativa` | mod/legislativa | Migra grafo y artefactos | Slot intermedio |
| `universos-legislativa` | mod/legislativa | Migra universos | Slot downstream |
| `cortos-legislativa` | mod/legislativa | Migra obras derivadas | Slot downstream |
| `future-machine-sdk` | main | Contrato portable de la machine | Provee el shape |
| **future-machine-legislativa** | mod/legislativa | **Instancia la machine del caso Feo** | Este dossier |

## 2. Inventario de slots a levantar

| Slot | Fuente prevista |
|------|-----------------|
| `slot_lore_db` | `lore/INDEX.md` + `lore/piezas/` |
| `slot_corpus` | `corpus/corpus.md` + `corpus/documentos/` + `corpus/analisis/` |
| `slot_grafo` | `lore/derivados/grafo/` + artefactos markdown del grafo |
| `slot_universos` | `lore/derivados/universo/` |
| `slot_obras` | `lore/derivados/cortos/` |
| `slot_portal` | `mod/agents/portal.agent.md` |
| `slot_pipeline` | `mod/agents/pipeline.agent.md` |
| `slot_entry_start` | `/user-empieza-aqui` |
| `slot_entry_status` | `/lore-status` |
| `slot_entry_refresh` | `/pipeline-refresh` |

## 3. Refs a actualizar

| Fichero | Qué cambiar |
|---------|-------------|
| `mod/agents/portal.agent.md` | Leer y presentar la machine del mod |
| `mod/prompts/user-empieza-aqui.prompt.md` | Presentar el cierre de ciclo desde la machine |
| `mod/prompts/lore-status.prompt.md` | Dashboard como estado de machine, no solo de lore |
| `mod/agents/pipeline.agent.md` | Posición explícita como slot técnico de refresh |
| `mod/instructions/onboarding-map.instructions.md` | Pasar de mapa ad hoc a mapa de machine |
| `mod/instructions/lore-pipeline.instructions.md` | Coherencia con la machine si existe |

## 4. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Portal del mod | `mod/agents/portal.agent.md` | Operativo |
| Start here | `mod/prompts/user-empieza-aqui.prompt.md` | Operativo |
| Dashboard | `mod/prompts/lore-status.prompt.md` | Operativo |
| Pipeline | `mod/agents/pipeline.agent.md` | Operativo pero aún no presentado como machine |
| Mapa visual | `mod/instructions/onboarding-map.instructions.md` | Operativo |
| Future-machine archivada | `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/` | Referencia histórica |

## 5. Restricciones

- Depende del export real del lore hacia `lore/` y de las capas ya separadas
- No debe reabsorber decisiones de `lore-db`, `corpus`, `grafo`, `universos` o `cortos`
- Debe aprovechar los prompts y agentes ya definidos en el mod, no crear duplicados gratuitos
- Tiene que servir como cierre del ciclo completo y como punto de entrada para usuario
- No se añade al sprint activo por defecto

## 6. Propuesta

### 6.1. Instanciar la machine del mod (FL-01)

Crear `lore/FUTURE_MACHINE.md` desde el template SDK y llenarlo con los slots reales del caso Feo una vez completado el export.

### 6.2. Conectar Pipeline como slot técnico (FL-02)

Actualizar `Pipeline` y la instruction de pipeline para que el refresh se entienda como operación de la machine, no como agente suelto.

### 6.3. Conectar Portal + start here + status (FL-03)

Actualizar Portal y los prompts de entrada para que presenten la máquina completa al usuario.

### 6.4. Levantar los datos actuales en la machine (FL-04)

Mapear corpus, grafo, universos, cortos y entrypoints actuales en el manifest para no perder lo ya existente del caso.

### 6.5. Validar el cierre completo del ciclo (FL-05)

Comprobar que el usuario puede entrar por Portal, ver el mapa, ver el status y recorrer el ciclo hasta refresh/universo/obra sin saltos conceptuales.

## 7. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)