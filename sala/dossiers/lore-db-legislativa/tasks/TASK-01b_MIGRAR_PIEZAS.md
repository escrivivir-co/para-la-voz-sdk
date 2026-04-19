# TASK-01b — Migrar piezas de DRAFTS2/ a lore/

> **Estado:** libre
> **Agente recomendado:** cualquiera (mecánico, sin decisiones de diseño)
> **Dependencias:** LP-01
> **Entrega esperada:** Todos los ficheros LORE_* migrados a `lore/`, refs actualizadas, DRAFTS2 limpio de piezas

## Lee primero

- [TASK-01 (lore-db)](./TASK-01_LORE_DB.md) — estructura destino
- `DRAFTS2/LORE_INDEX.md` — inventario actual
- `mod/instructions/lore-routing.instructions.md` — rutas que apuntan a DRAFTS2

## Objetivo

Migrar todos los ficheros del lore de `DRAFTS2/` a `lore/` usando `git mv` para preservar historial. **Cero pérdida de datos.**

## Plan de migración

### Grupo 1 — INDEX

```bash
git mv DRAFTS2/LORE_INDEX.md lore/INDEX.md
```

### Grupo 2 — Piezas (bloques temáticos + soportes)

```bash
# Bloques A-E
git mv DRAFTS2/LORE_A.md lore/piezas/
git mv DRAFTS2/LORE_B.md lore/piezas/
git mv DRAFTS2/LORE_C.md lore/piezas/
git mv DRAFTS2/LORE_D.md lore/piezas/
git mv DRAFTS2/LORE_E.md lore/piezas/

# Soportes por pieza
git mv DRAFTS2/LORE_P-*.md lore/piezas/
git mv DRAFTS2/LORE_S-*.md lore/piezas/
git mv DRAFTS2/LORE_N-*.md lore/piezas/
git mv DRAFTS2/LORE_T-*.md lore/piezas/
git mv DRAFTS2/LORE_R-*.md lore/piezas/
```

### Grupo 3 — Derivados

```bash
git mv DRAFTS2/CORPUS_PREVIEW.md lore/derivados/
git mv DRAFTS2/LORE_F.md lore/derivados/
git mv DRAFTS2/LORE_F-02_ARTEFACTO.md lore/derivados/
git mv DRAFTS2/LORE_F-02_UNIVERSO.md lore/derivados/
git mv DRAFTS2/LORE_F-02_CORTO*.md lore/derivados/
git mv DRAFTS2/universo/ lore/derivados/universo/
git mv DRAFTS2/grafo/ lore/derivados/grafo/  # si existe
```

### Grupo 4 — Drafts y material de trabajo

```bash
git mv DRAFTS2/LORE_DRAFT.md lore/drafts/
git mv DRAFTS2/LORE_DRAFT_CORE.md lore/drafts/
git mv DRAFTS2/LORE_PLAN.md lore/drafts/
git mv DRAFTS2/00__logs.json lore/drafts/
git mv DRAFTS2/01__logs.json lore/drafts/
```

### Grupo 5 — Actualizar refs internas

Ficheros que referencian rutas `DRAFTS2/LORE_*` y necesitan actualización:

| Fichero | Tipo de ref |
|---------|-------------|
| `lore/INDEX.md` (ex LORE_INDEX.md) | Links relativos a piezas — ajustar paths |
| `mod/instructions/lore-routing.instructions.md` | Tabla de routing completa |
| `mod/instructions/lore-estado.instructions.md` | Refs a ficheros |
| `mod/instructions/lore-schema.instructions.md` | Ejemplos con rutas |
| `mod/instructions/legislativa-universo.instructions.md` | Refs a piezas |
| `mod/agents/archivero-lore.agent.md` | Sección "Fuentes que lees" |
| `mod/agents/puzzle.agent.md` | Sección "Fuentes que lees" |
| `mod/agents/pipeline.agent.md` | Refs a derivados |
| `mod/agents/grafista.agent.md` | Refs a grafo/universo |
| `mod/agents/dramaturgo.agent.md` | Refs a cortos |
| `DRAFTS2/FEAT-06_PIPELINE_REFRESH.md` | Grafo de deps (si se mantiene en DRAFTS2) |
| `DRAFTS2/INDICE_DRY_SDK_MOD_LORE.md` | Índice general |
| `.github/templates/sala-tablero.template.md` | Si tiene refs |

### Grupo 6 — Verificar integridad

- [ ] `git status` no muestra ficheros LORE_* en DRAFTS2/
- [ ] `lore/INDEX.md` tiene links válidos
- [ ] `@Puzzle validar` pasa sin errores (lee lore-routing → resuelve → encuentra piezas)
- [ ] Ningún fichero del lore se ha perdido: comparar conteo pre/post migración

## Qué NO se migra (se queda en DRAFTS2/)

- `mod_legislativa_*.md` — especificación del mod, no piezas del lore
- `FEAT-*.md` — features de cristalización
- `INDICE_DRY_SDK_MOD_LORE.md` — índice meta
- `PLAN_UNIVERSO1_V2.md` — plan específico
- `DIARIO_*.png` — imágenes del diario
- `sala/` — ya migrada a raíz

## Criterio de aceptación

40 ficheros LORE_* + CORPUS_PREVIEW + universo/ migrados a `lore/`. Git historial preservado. Todas las refs actualizadas. `@Puzzle validar` funciona.
