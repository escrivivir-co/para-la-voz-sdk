# TASK-05 — Scaffold lore-db en main + inicialización automática

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** PS-01, PS-02
> **Entrega esperada:** `lore/` en main con scaffold + lógica de init en `sala-aleph`

## Lee primero

- [Plan §4](../PLAN.md) — propuesta general
- `sala/README.md` — referencia de cómo se hizo con `sala/` (scaffold genérico + init en sala-aleph)
- `.github/prompts/sala-aleph.prompt.md` — Paso 0 como modelo de inicialización
- `.github/templates/sala-activacion.template.md` — modelo de template

## Objetivo

Crear el scaffold `lore/` en main — exactamente como se hizo con `sala/`: carpeta con README genérico, .gitkeep stubs, y templates. Más la lógica de inicialización que lo pone en marcha cuando un mod lo necesita.

## Cambios esperados

### 1. Scaffold `lore/` en main

```
lore/
├── README.md              ← genérico: "qué es la lore-db, cómo se usa"
├── piezas/.gitkeep        ← ficheros de pieza (mod los rellena)
├── derivados/.gitkeep     ← artefactos generados (corpus, hilo, grafo, etc.)
└── drafts/.gitkeep        ← borradores y material de trabajo
```

`lore/README.md` debe ser genérico (sin refs a legislativa ni a DRAFTS2). Explica:
- Qué es la lore-db
- Estructura esperada
- Variable `{{LORE_DIR}}` y dónde se resuelve
- Que el schema lo define cada mod en `mod/instructions/`
- Que el INDEX se genera desde template

### 2. Templates para inicialización

| Template | Ruta | Para qué |
|----------|------|----------|
| `lore-index.template.md` | `.github/templates/` | Inventario de piezas vacío (se rellena cuando el mod define sus tipos) |
| `lore-readme.template.md` | `.github/templates/` | README de la lore-db (si el mod quiere regenerar) |

> Las templates `pieza-index.template.md` y `pieza-schema.template.md` de PS-01/PS-02 se renombran o se referencian como `lore-*` para consistencia. Decisión del agente.

### 3. Lógica de inicialización en `/sala-aleph`

Ampliar el Paso 0 de `.github/prompts/sala-aleph.prompt.md` para que **además de verificar la sala**, verifique la lore-db:

```markdown
### Paso 0b — Verificar lore-db

Comprueba si `{{LORE_DIR}}/` existe y tiene al menos `INDEX.md`.

**Si la lore-db está vacía** (no existe `INDEX.md`):

1. Informa: "La lore-db existe pero no está inicializada."
2. Crea `{{LORE_DIR}}/INDEX.md` desde `.github/templates/lore-index.template.md`.
3. Asegura que existan `{{LORE_DIR}}/piezas/`, `{{LORE_DIR}}/derivados/`, `{{LORE_DIR}}/drafts/`.
4. Continúa.

**Si `{{LORE_DIR}}/` no existe en absoluto**, informa y continúa (la lore-db es opcional — no todos los mods la usan).
```

### 4. Variable `{{LORE_DIR}}` en copilot-instructions.md

Documentar la variable junto a `{{SALA_DIR}}` en la sección de variables del SDK.

## Qué NO se toca

- No se migran piezas existentes (eso es LP-01b del otro dossier)
- No se crean tipos concretos
- `mod/legislativa` no se toca aquí

## Criterio de aceptación

- `lore/` existe en main con scaffold genérico
- Un `git merge main` en cualquier mod trae `lore/` listo
- `/sala-aleph` inicializa la lore-db si está vacía
- `{{LORE_DIR}}` documentado en copilot-instructions.md
