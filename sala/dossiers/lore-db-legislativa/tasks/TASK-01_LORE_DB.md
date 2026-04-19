# TASK-01 — Crear lore-db: estructura canónica de la base de datos de piezas

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** LP-00, PS-05† (scaffold lore/ en main)
> **Entrega esperada:** `lore/` inicializado con estructura canónica + `lore-routing` actualizado

> † PS-05 es del dossier `lore-db-sdk` — provee el scaffold `lore/` en main.

## Lee primero

- [Plan §4.1](../PLAN.md)
- `mod/instructions/lore-routing.instructions.md` — mapa actual (workaround DRAFTS2)
- `DRAFTS2/LORE_INDEX.md` — inventario de 51 piezas
- `sala/dossiers/lore-db-sdk/tasks/TASK-05_SCAFFOLD_LORE_DB.md` — scaffold SDK

## Objetivo

Establecer `lore/` como la **base de datos canónica de piezas** del mod. La estructura:

```
lore/
├── INDEX.md              ← inventario de piezas (antes LORE_INDEX.md)
├── piezas/               ← ficheros de pieza LORE_*.md (bloques + soportes)
│   ├── LORE_A.md
│   ├── LORE_B.md
│   ├── ...
│   ├── LORE_P-01.md
│   └── ...
├── derivados/            ← artefactos generados desde piezas
│   ├── CORPUS_PREVIEW.md
│   ├── LORE_F.md         ← hilo narrativo
│   ├── LORE_F-02_ARTEFACTO.md
│   ├── LORE_F-02_UNIVERSO.md
│   ├── LORE_F-02_CORTO*.md
│   └── universo/         ← ramas expandidas
├── drafts/               ← borradores, logs, material no formal
│   ├── LORE_DRAFT.md
│   ├── LORE_DRAFT_CORE.md
│   ├── LORE_PLAN.md
│   └── *.json            ← logs
└── README.md             ← generado desde template SDK
```

## Decisión del PO (19-abr-2026)

**"lore-db"**: las piezas viven en `lore/`, no en `DRAFTS2/`. Se migra con `git mv` para preservar historial. La variable `{{LORE_DIR}}` reemplaza a `{{PIEZA_DIR}}`.

`DRAFTS2/` se vacía progresivamente: lo que es pieza o derivado va a `lore/`, lo que es especificación del mod (mod_legislativa_*.md, FEAT-*, INDICE_DRY) se queda o se mueve a `mod/docs/` en otra task.

## Checklist de ejecución

### Fase 1 — Crear estructura

- [ ] Asegurar que `lore/` existe (viene del scaffold SDK vía merge main)
- [ ] Crear subcarpetas: `lore/piezas/`, `lore/derivados/`, `lore/drafts/`
- [ ] Copiar `lore/README.md` desde template SDK si no existe

### Fase 2 — Definir `{{LORE_DIR}}`

- [ ] Actualizar `lore-routing.instructions.md`: nueva variable `{{LORE_DIR}}` = `lore/`
- [ ] Actualizar tabla de routing con rutas nuevas:
  - `corpus/documentos/` → `lore/piezas/`
  - `índice del lore` → `lore/INDEX.md`
  - `corpus/corpus.md` → `lore/derivados/CORPUS_PREVIEW.md`
  - `hilo narrativo` → `lore/derivados/LORE_F.md`
  - etc.

### Fase 3 — Verificar

- [ ] Todos los agentes (puzzle, archivero-lore, pipeline) resuelven las rutas nuevas vía lore-routing
- [ ] LORE_INDEX refs internas siguen funcionando (paths relativos)

**La migración de ficheros es LP-01b** — esta task crea la estructura y actualiza el routing.

## Criterio de aceptación

`lore/` existe con subdirectorios, `{{LORE_DIR}}` definido en routing, tabla de routing actualizada. Los agentes saben dónde buscar.
