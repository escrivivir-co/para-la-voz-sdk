# Plan: Feature "Guiones" — carpeta de trabajo + generación desde plantilla

## Qué es un guion

Un guion es un **roadmap ejecutable** para procesar una editorial por el pipeline Bartleby. Es un documento markdown con checkboxes que una persona de la editorial sigue paso a paso en VS Code. No es un artefacto agéntico — es un documento humano.

**Momento en el flujo:** el guion se crea **antes** de activar ningún agente. Es lo primero que hace el usuario cuando llega una nueva editorial. Después, sigue las instrucciones del guion para ejecutar `/feed`, `/diff-corpus`, `/merge-corpus`, etc.

```
usuario crea guion  →  usuario sigue guion  →  agentes ejecutan pasos
         ↑                     ↑                        ↑
    pre-pipeline          el roadmap              /feed /diff /merge
```

## Estado actual

- 3 guiones manuales en la raíz: `GUION_2024-11-20_materialismo.md`, `GUION_2025-04-30_arte.md`, `GUION_2025-12-11_guerra_y_capital.md`
- 2 editoriales nuevas sin trackear por git: `corpus/editoriales/2025-04-30_arte.md`, `corpus/editoriales/2025-12-11_guerra_y_capital.md`
- Todo en `mod/restitutiva`, comiteado y pusheado (commit `0c9c1fd`)

## Qué hay que hacer

### Fase 1 — `main` (SDK): plantilla + prompt + docs

#### 1.1 Crear `.github/templates/guion-ciclo.template.md`

Plantilla parametrizada del guión estándar. Variables con `{{PLACEHOLDER}}`:

| Variable | Qué es | Ejemplo |
|----------|--------|---------|
| `{{EDITORIAL_FECHA}}` | Fecha de publicación | `2024-11-20` |
| `{{EDITORIAL_TITULO}}` | Título legible | *Materialismo militante* |
| `{{EDITORIAL_ARCHIVO}}` | Ruta en corpus | `corpus/editoriales/2024-11-20_materialismo.md` |
| `{{EDITORIAL_NUMERO}}` | Número de publicación | `PARA LA VOZ 2(2)` |
| `{{CORPUS_PROCESADAS}}` | Editoriales en corpus antes | `1` |
| `{{CORPUS_PROCESADAS_DESPUES}}` | Editoriales en corpus después | `2` |
| `{{GUION_ANTERIOR}}` | Guion previo (encadenar) | `2024-05-01_primero-de-mayo.guion.md` |
| `{{GUION_SIGUIENTE}}` | Guion siguiente | `2025-04-30_arte.guion.md` o "flujo rutinario" |
| `{{INCLUIR_DESIGN}}` | ¿Incluir paso /design? | `sí` / `no` |
| `{{INCLUIR_PUSH}}` | ¿Incluir push o acumular? | `sí` / `no` |

**Contenido:** extraer de los 3 guiones actuales la estructura común y parametrizarla. Secciones:

1. **Cabecera** — rama, editorial, título, número, prerrequisitos
2. **Qué vas a hacer** — diagrama resumen del ciclo
3. **Paso 1 · Análisis — `/feed`** — qué escribir en Copilot Chat, qué sucede, checkboxes de verificación
4. **Paso 2 · Comparación — `/diff-corpus`** — tabla NUEVO/CONFIRMA/DISCREPA/EVOLUCIONA, checkboxes, decisión
5. **Paso 3 · Integración — `/merge-corpus`** — qué sucede, checkboxes
6. **Paso 4 · Cristalización — `/design`** *(condicional: solo si `{{INCLUIR_DESIGN}}` es sí)*
7. **Paso 5 · Guardar — commit/push** *(push condicional según `{{INCLUIR_PUSH}}`)*
8. **Resumen visual** — diagrama ASCII del ciclo
9. **Siguiente paso** — enlace al siguiente guion o nota de flujo rutinario

#### 1.2 Crear `.github/prompts/guion.prompt.md`

Nuevo comando `/guion`. **Sin agent asignado** — es una utilidad de scaffolding, no una operación de análisis ni de corpus.

```yaml
name: guion
description: Genera un guión de ciclo editorial a partir de la plantilla SDK. El guion es un roadmap paso a paso para que una persona del equipo editorial procese una nueva editorial por el pipeline Bartleby.
argument-hint: "[ruta a editorial en corpus/editoriales/]"
tools: ['search/codebase', 'file-create']
```

Lógica del prompt:

1. Lee la plantilla `.github/templates/guion-ciclo.template.md`
2. Lee `corpus/corpus.md` → extrae `Editoriales procesadas: N`
3. Lee la editorial indicada → extrae título, fecha de publicación, número
4. Lee `guiones/` → identifica el guion más reciente (para encadenar con `{{GUION_ANTERIOR}}`)
5. Decide si incluir `/design` y push según contexto (o pregunta al usuario)
6. Rellena las variables y genera `guiones/YYYY-MM-DD_slug.guion.md`
7. Informa al usuario: "Guion creado en `guiones/...`. Ábrelo y sigue los pasos."

**No tiene `agent:` en el frontmatter.** El prompt se ejecuta como Copilot genérico. Crear un guion no es trabajo de ningún agente del pipeline — es preparación previa del usuario.

#### 1.3 Editar `.github/prompts/feed.prompt.md`

Añadir al final del bloque de pasos (antes del recordatorio del hook):

```markdown
10. Si no existe guion para esta editorial en `guiones/`, informa al usuario:
    "No hay guion de seguimiento para esta editorial. Puedes generar uno con `/guion [ruta]` para tener un roadmap del ciclo completo."
```

No genera el guion automáticamente — solo sugiere. El guion es decisión del usuario.

#### 1.4 Editar `.github/copilot-instructions.md`

Dos cambios:

**Tabla de comandos** — añadir fila:

```
| `/guion` | Generar guion de ciclo editorial desde plantilla |
```

**Capas del repositorio** — añadir `guiones/` y `templates/`:

```
.github/
  ...
  templates/      → plantillas de documentos (guion de ciclo, etc.)

guiones/          → roadmaps de ciclo editorial (.guion.md) — uno por editorial
```

#### 1.5 Editar `README.md`

Añadir sección **"Guiones de ciclo"** (después de "Ciclo operativo" o similar):

- Qué son los guiones
- Dónde viven (`guiones/`)
- Cómo se generan (`/guion` o manual desde plantilla)
- Convención de nombres: `YYYY-MM-DD_slug.guion.md`
- Son documentos vivos: los checkboxes se marcan durante la ejecución
- Relación con el pipeline: el guion se crea antes, los agentes se invocan durante

Actualizar el diagrama de estructura de directorios para incluir `guiones/` y `.github/templates/`.

#### 1.6 Editar `proyecto.config.template.md`

Añadir sección:

```yaml
## Guiones

ruta-guiones: "guiones/"
plantilla: ".github/templates/guion-ciclo.template.md"
formato-nombre: "YYYY-MM-DD_slug.guion.md"
```

---

### Fase 2 — `mod/restitutiva`: migrar guiones + pull de main

#### 2.1 Hacer pull de main en mod/restitutiva

```bash
git pull origin main
```

Así el mod hereda la plantilla, el prompt `/guion`, y los docs actualizados.

#### 2.2 Crear carpeta `guiones/`

```bash
mkdir guiones
```

#### 2.3 Mover y renombrar los 3 guiones existentes

```bash
git mv GUION_2024-11-20_materialismo.md guiones/2024-11-20_materialismo.guion.md
git mv GUION_2025-04-30_arte.md guiones/2025-04-30_arte.guion.md
git mv GUION_2025-12-11_guerra_y_capital.md guiones/2025-12-11_guerra_y_capital.guion.md
```

Los 3 guiones mantienen su contenido íntegro. Solo cambian de ubicación y extensión.

#### 2.4 Editar `proyecto.config.md`

Añadir la misma sección de guiones que en el template, rellenada para restitutiva.

#### 2.5 Commit y push

```bash
git add guiones/ proyecto.config.md
git commit -m "feat: migrar guiones a guiones/ + pull SDK con plantilla y /guion"
git push origin mod/restitutiva
```

---

### Fase 3 — Verificación

| Check | Esperado |
|-------|----------|
| `main` tiene `.github/templates/guion-ciclo.template.md` | ✓ plantilla parametrizada |
| `main` tiene `.github/prompts/guion.prompt.md` | ✓ sin `agent:` |
| `main` NO tiene `guiones/` | ✓ es carpeta de mod |
| `main` NO tiene editoriales ni análisis | ✓ SDK puro |
| `mod/restitutiva` tiene `guiones/` con 3 `.guion.md` | ✓ migrados |
| `mod/restitutiva` NO tiene `GUION_*.md` en raíz | ✓ borrados por git mv |
| `mod/restitutiva` conserva `corpus/editoriales/` con 4 archivos | ✓ intactos |
| `mod/restitutiva` conserva `corpus/analisis/` con 1 análisis | ✓ intacto |
| `/guion corpus/editoriales/2024-05-01_primero-de-mayo.md` funciona | ✓ genera guion coherente |
| Los 3 guiones migrados conservan todo su contenido | ✓ solo cambia path |

---

## Archivos afectados

### En `main`:

| Operación | Archivo |
|-----------|---------|
| CREAR | `.github/templates/guion-ciclo.template.md` |
| CREAR | `.github/prompts/guion.prompt.md` |
| EDITAR | `.github/prompts/feed.prompt.md` |
| EDITAR | `.github/copilot-instructions.md` |
| EDITAR | `README.md` |
| EDITAR | `proyecto.config.template.md` |

### En `mod/restitutiva`:

| Operación | Archivo |
|-----------|---------|
| PULL | de main (hereda plantilla + prompt + docs) |
| MOVER | `GUION_*.md` → `guiones/*.guion.md` (×3) |
| EDITAR | `proyecto.config.md` |

---

## Decisiones

1. **Sin override de plantillas en mod.** Una sola plantilla en `.github/templates/`. Si un mod necesita algo diferente, edita el guion generado a mano.
2. **`/guion` sin agent.** Crear un guion es una acción del usuario previa al pipeline. No es competencia de @archivero (corpus), ni de @bartleby (análisis), ni de @cristalizador (diseño agéntico). Es utilidad de scaffolding.
3. **Orden de ejecución: main primero, mod después.** Main se actualiza con el feature, mod hace pull y migra. Las editoriales y guiones existentes en mod nunca se pierden (git mv preserva historia, pull no toca `corpus/` ni `guiones/`).
4. **Extensión `.guion.md`** — glob-matchable, no confunde con análisis ni editoriales.
5. **Carpeta `guiones/` en raíz** — no dentro de `corpus/` (no es dato analítico) ni de `mod/` (no es artefacto agéntico). Es documentación operativa de workflow, al nivel de `corpus/`.
6. **Convención de nombre:** `YYYY-MM-DD_slug.guion.md` — misma fecha-slug que la editorial correspondiente.
