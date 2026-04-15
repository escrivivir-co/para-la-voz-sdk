# Guión: Ciclo completo para editorial {{EDITORIAL_FECHA}} — {{EDITORIAL_TITULO}}

**Rama:** `{{MOD_RAMA}}`
**Editorial:** `{{EDITORIAL_ARCHIVO}}`
**Título:** *{{EDITORIAL_TITULO}}*
**Número:** {{EDITORIAL_NUMERO}}

> **Antes de empezar:** El corpus debe tener **{{CORPUS_PROCESADAS}} editorial(es) procesada(s)**.
> Compruébalo en `corpus/corpus.md`, línea `Editoriales procesadas:`.
> {{#GUION_ANTERIOR}}Guión anterior completado: `guiones/{{GUION_ANTERIOR}}`{{/GUION_ANTERIOR}}

---

## Qué vas a hacer

Vas a pasar esta editorial por el pipeline Bartleby. Son 3 pasos con agentes + 1 commit manual. Cada paso es una instrucción que escribes en **Copilot Chat** (el panel lateral de VS Code). Los agentes hacen el trabajo; tú verificas y apruebas.

```
Tú escribes en Copilot Chat          El agente hace
─────────────────────────────────     ──────────────────────────
/feed {{EDITORIAL_ARCHIVO}}       →   @bartleby analiza → .analisis.md
/diff-corpus                      →   @archivero compara → informe diff
  (tú apruebas)
/merge-corpus                     →   @archivero integra → corpus.md actualizado
  (tú haces commit en terminal)
```

---

## Paso 1 · Análisis — `/feed`

**Escribe en Copilot Chat:**

```
/feed {{EDITORIAL_ARCHIVO}}
```

**Qué sucede:** @bartleby lee la editorial y el corpus acumulado ({{CORPUS_PROCESADAS}} editorial(es) previa(s)) y produce un análisis con 5 secciones:

1. La corriente: herencia y linaje
2. La taxonomía que el texto maneja
3. Los mecanismos retóricos heredados
4. Lo emergente — qué aporta sobre la tradición
5. Vista desde el hueco

El resultado se guarda en `corpus/analisis/{{EDITORIAL_FECHA}}_{{EDITORIAL_SLUG}}.analisis.md`.

### ✓ Comprueba antes de seguir

- [ ] El archivo `corpus/analisis/{{EDITORIAL_FECHA}}_{{EDITORIAL_SLUG}}.analisis.md` existe
- [ ] Tiene las 5 secciones (búscalas por nombre)
- [ ] Al final tiene una tabla de metadatos con campos como `Nick corriente`, `Posición en corpus`, etc.
- [ ] Usa el vocabulario que ya está en `corpus/corpus.md` (no inventa sinónimos)
- [ ] No hay frases que juzguen la editorial ("excelente argumento", "débil razonamiento", etc.)

**Si algo no cuadra:** no sigas. Dile a Copilot Chat qué está mal y pide que lo corrija. Solo cuando el análisis sea correcto, pasa al paso 2.

---

## Paso 2 · Comparación — `/diff-corpus`

**Escribe en Copilot Chat:**

```
/diff-corpus corpus/analisis/{{EDITORIAL_FECHA}}_{{EDITORIAL_SLUG}}.analisis.md
```

**Qué sucede:** @archivero compara el análisis con todo lo que hay en `corpus/corpus.md` y clasifica cada hallazgo:

| Categoría | Significado |
|-----------|-------------|
| **NUEVO** | Algo que no existía en el corpus |
| **CONFIRMA** | Algo que ya estaba y se repite (el contador sube) |
| **DISCREPA** | Algo que contradice un patrón previo del corpus |
| **EVOLUCIONA** | Algo que desarrolla un patrón sin contradecirlo |

### ✓ Comprueba antes de seguir

- [ ] El diff cubre las secciones del corpus: linaje, exclusión, taxonomía, mecanismos, emergencias, ausencias, nick
- [ ] Cada elemento tiene su categoría (NUEVO / CONFIRMA / DISCREPA / EVOLUCIONA)
- [ ] Los contadores ×N son coherentes con el corpus previo

### Tu decisión

Lee el diff con calma. Si es correcto, responde:

```
Apruebo el merge
```

Si hay algo que quieras matizar o corregir, díselo al archivero antes de aprobar.

---

## Paso 3 · Integración — `/merge-corpus`

**Escribe en Copilot Chat:**

```
/merge-corpus
```

**Qué sucede:** @archivero toma el diff que aprobaste y actualiza `corpus/corpus.md`:

- Lo **NUEVO** se añade a su sección con `[añadido: fecha]`
- Lo que **CONFIRMA** sube su contador `[×N]`
- Lo que **DISCREPA** se registra en "Discrepancias abiertas"
- Lo que **EVOLUCIONA** se documenta como variante
- El encabezado pasa a `Editoriales procesadas: {{CORPUS_PROCESADAS_DESPUES}}`
- Nunca se borra nada del corpus anterior

### ✓ Comprueba antes de seguir

- [ ] `corpus/corpus.md` dice `Editoriales procesadas: {{CORPUS_PROCESADAS_DESPUES}}`
- [ ] La fecha de última actualización es la de hoy
- [ ] Los nodos nuevos aparecen en sus secciones
- [ ] Los contadores han subido donde toca
- [ ] No se ha borrado nada del corpus previo

---

{{#INCLUIR_DESIGN}}
## Paso 4 · Cristalización — `/design`

> Este paso solo se hace **una vez**, al final de un lote de inicialización o cuando el corpus
> ha crecido significativamente (≥3 editoriales nuevas desde el último /design).

**Escribe en Copilot Chat:**

```
/design
```

**Qué sucede:** @cristalizador lee el corpus completo, los artefactos SDK (`.github/`), los artefactos mod (`mod/`), y la documentación de capacidades de VS Code Copilot (`COPILOT/`). Genera 2-4 propuestas de artefactos nuevos, cada una con tipo, capacidad que activa, motivación y ruta en `mod/`.

### Tu decisión

Lee las propuestas. Responde "Implementa la N" o "Ninguna por ahora".

### ✓ Si se implementa algo

- [ ] Los archivos nuevos están en `mod/` (no en `.github/`)
- [ ] Puedes probar el artefacto invocándolo en Copilot Chat

---

{{/INCLUIR_DESIGN}}
## Paso {{PASO_COMMIT}} · Guardar cambios (terminal)

Abre la terminal de VS Code (`` Ctrl+` ``) y ejecuta:

```bash
git add corpus/ mod/
git status
```

Revisa que los cambios son solo en `corpus/` y `mod/`. **No debe haber cambios en `.github/`**.

Si todo está bien:

```bash
git commit -m "feat(corpus): análisis editorial {{EDITORIAL_FECHA}} {{EDITORIAL_TITULO_SLUG}} — corpus {{CORPUS_PROCESADAS_DESPUES}} editoriales"
```

{{#INCLUIR_PUSH}}
```bash
git push origin {{MOD_RAMA}}
```
{{/INCLUIR_PUSH}}
{{^INCLUIR_PUSH}}
> **No hagas push todavía** — continúa con el siguiente guión y harás un push único al final.
{{/INCLUIR_PUSH}}

---

## Resumen visual

```
corpus/corpus.md ({{CORPUS_PROCESADAS}} editorial(es))
        │
   /feed → @bartleby → corpus/analisis/{{EDITORIAL_FECHA}}_{{EDITORIAL_SLUG}}.analisis.md
        │
   /diff-corpus → @archivero → NUEVO / CONFIRMA / DISCREPA / EVOLUCIONA
        │
   tú apruebas
        │
   /merge-corpus → @archivero → corpus/corpus.md ({{CORPUS_PROCESADAS_DESPUES}} editoriales){{#INCLUIR_DESIGN}}
        │
   /design → @cristalizador → artefactos nuevos en mod/{{/INCLUIR_DESIGN}}
        │
   git add + commit{{#INCLUIR_PUSH}} + push{{/INCLUIR_PUSH}}
```

---

## Siguiente paso

{{#GUION_SIGUIENTE}}Cuando este guión esté completo, pasa a → `guiones/{{GUION_SIGUIENTE}}`{{/GUION_SIGUIENTE}}
{{^GUION_SIGUIENTE}}El corpus está inicializado. El flujo rutinario para futuras editoriales: guardar en `corpus/editoriales/`, ejecutar `/guion` para generar el roadmap, y seguir los pasos.{{/GUION_SIGUIENTE}}
