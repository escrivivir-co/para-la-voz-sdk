# Plan — lore-pipeline-legislativa

> **Fecha:** 19-abr-2026
> **Autor:** Claude Opus 4.6
> **Dossier:** `sala/dossiers/lore-pipeline-legislativa/`

## 1. Contexto

Una vez que el SDK defina el protocolo genérico de piezas (dossier `pieza-sdk`), mod/legislativa necesita:

1. **Adaptar sus artefactos** para que hereden del SDK en vez de reinventar el concepto
2. **Formalizar el pipeline específico** de cómo las piezas se conectan con corpus → grafo → universos → cortos
3. **Mover las piezas de DRAFTS2/** a una ubicación canónica (o formalizar DRAFTS2 como `{{PIEZA_DIR}}` definitivo)

Hoy la cadena existe de facto pero está codificada en documentos dispersos:

```
Piezas (LORE_*.md)
   ↓
┌──────────────────┐
│ CORPUS_PREVIEW.md │ (← Archivero Lore + Bartleby)
│ LORE_F.md         │ (← hilo narrativo)
└──────────────────┘
   ↓ (join)
LORE_F-02_ARTEFACTO.md  (← spec de grafo)
   ↓
LORE_F-02_UNIVERSO.md   (← grafo 19 nodos, 4 ramas)
   ↓
universo/universo-1.md   (← rama expandida R4)
   ↓
LORE_F-02_CORTO-*.md    (← relatos generados)
```

Este pipeline está descrito en FEAT-06 pero no está formalizado como estructura del mod. El lore-routing lo mapea parcialmente pero mezcla workarounds temporales con decisiones de diseño.

## 2. Anclas

| Artefacto | Ubicación | Relación |
|-----------|-----------|----------|
| Dossier pieza-sdk | `sala/dossiers/pieza-sdk/` | Dependencia: provee el protocolo genérico |
| lore-schema | `mod/instructions/lore-schema.instructions.md` | Se adapta para heredar del SDK |
| lore-estado | `mod/instructions/lore-estado.instructions.md` | Se revisa para mapear al nuevo esquema |
| lore-routing | `mod/instructions/lore-routing.instructions.md` | Se actualiza con `{{PIEZA_DIR}}` y rutas definitivas |
| FEAT-06 | `DRAFTS2/FEAT-06_PIPELINE_REFRESH.md` | Grafo de dependencias que se formaliza |
| Cadena agéntica | `sala/archivo/sprint-cristalizacion-v1/dossiers/cristalizacion-cadena-agentica/` | 5 agentes ya diseñados |
| Archivero Lore | `mod/agents/archivero-lore.agent.md` | Se adapta para referenciar SDK |
| Puzzle | `mod/agents/puzzle.agent.md` | Se adapta para referenciar SDK |
| Pipeline | `mod/agents/pipeline.agent.md` | Se revisa para formalizar grafo de deps |

## 3. Restricciones

- **Depende de pieza-sdk:** las tasks LP-01 y LP-02 pueden empezar en paralelo con pieza-sdk, pero LP-03+ requieren que el SDK ya tenga el protocolo genérico.
- Todo en `mod/` y `DRAFTS2/` — no toca `.github/`
- No se reescribe el contenido de las piezas — solo se mueve/reorganiza
- El pipeline de FEAT-06 es referencia pero no se implementa como agente aquí (ya está en `mod/agents/pipeline.agent.md`)

## 4. Propuesta

### 4.1. Decidir ubicación definitiva de piezas

Hoy `DRAFTS2/` es un cajón de sastre. Opciones:

- **A)** `corpus/piezas/` — canónico según estructura del SDK (corpus/documentos → corpus/piezas)
- **B)** `DRAFTS2/` se renombra a `lore/` y se formaliza como `{{PIEZA_DIR}}`
- **C)** Se queda en `DRAFTS2/` y se actualiza el routing

**Pendiente de decisión del PO.**

### 4.2. Adaptar lore-schema para heredar de pieza-schema SDK

`mod/instructions/lore-schema.instructions.md` hoy define todo desde cero. Debe:
- Referenciar `pieza-schema.instructions.md` del SDK como base
- Definir solo lo que es específico de legislativa: los 6 tipos concretos, los campos concretos, las reglas específicas del caso

### 4.3. Adaptar lore-routing con {{PIEZA_DIR}}

- Añadir `{{PIEZA_DIR}}` como variable
- Simplificar la tabla de routing ahora que el SDK define el protocolo base
- Eliminar el carácter de "workaround temporal" si se decide ubicación definitiva

### 4.4. Formalizar grafo de dependencias del pipeline

Tomar el grafo de FEAT-06 y codificarlo como instruction del mod:
```
piezas → {CORPUS_PREVIEW ∥ LORE_F} → ARTEFACTO → UNIVERSO → cortos
```
Esto es lo que mod/legislativa añade sobre el SDK genérico.

### 4.5. Adaptar agentes del mod para referenciar SDK

- `archivero-lore.agent.md` → referenciar `pieza-schema.instructions.md` del SDK + `lore-schema.instructions.md` del mod
- `puzzle.agent.md` → igual
- `pipeline.agent.md` → incluir referencia al grafo de deps formalizado

### 4.6. Vincular corpus → grafo → universos → cortos

La capa que el usuario pide: cómo las piezas alimentan toda la cadena. Hoy está implícito. Se documenta como `mod/instructions/lore-pipeline.instructions.md`:
- Grafo de dependencias (de FEAT-06)
- Qué agente produce cada nodo
- Qué condiciones de refresh existen
- Handoffs entre agentes

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)
