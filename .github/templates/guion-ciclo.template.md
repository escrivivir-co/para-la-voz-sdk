# Guión: Ciclo completo para documento {{DOCUMENTO_FECHA}} — {{DOCUMENTO_TITULO}}

**Rama:** `{{MOD_RAMA}}`
**Documento:** `{{DOCUMENTO_ARCHIVO}}`
**Título:** *{{DOCUMENTO_TITULO}}*
**Número:** {{DOCUMENTO_NUMERO}}

> **Antes de empezar:** El corpus debe tener **{{CORPUS_PROCESADAS}} documento(s) procesado(s)**.
> Comprobar en `corpus/corpus.md`, línea `Documentos procesados:`.
> {{#GUION_ANTERIOR}}Guión anterior completado: `guiones/{{GUION_ANTERIOR}}`{{/GUION_ANTERIOR}}

---

## Qué vas a hacer

Vas a pasar este documento por el pipeline Bartleby. Son 3 pasos base con agentes + 1 capa opcional de cristalización + 1 commit manual. Cada paso es una instrucción que escribes en **Copilot Chat** (el panel lateral de VS Code). Los agentes hacen el trabajo; tú verificas y apruebas.

```
Tú escribes en Copilot Chat          El agente hace
─────────────────────────────────     ──────────────────────────
/feed {{DOCUMENTO_ARCHIVO}}       →   @bartleby analiza → .analisis.md
/diff-corpus                      →   @archivero compara → informe diff
  (tú apruebas)
/merge-corpus                     →   @archivero integra → corpus.md actualizado
{{#INCLUIR_DESIGN}}/design                            →   @cristalizador propone → target main/mod + gates
     (tú pactas e implementas solo si apruebas){{/INCLUIR_DESIGN}}
```

---

## Paso 1 · Análisis — `/feed`

**Escribe en Copilot Chat:**

```
/feed {{DOCUMENTO_ARCHIVO}}
```

**Qué sucede:** @bartleby lee el documento y el corpus acumulado ({{CORPUS_PROCESADAS}} documento(s) previo(s)) y produce un análisis con 5 secciones:

1. La corriente: herencia y linaje
2. La taxonomía que el texto maneja
3. Los mecanismos retóricos heredados
4. Lo emergente — qué aporta sobre la tradición
5. Vista desde el hueco

El resultado se guarda en `corpus/analisis/{{DOCUMENTO_FECHA}}_{{DOCUMENTO_SLUG}}.analisis.md`.

### ✓ Comprueba antes de seguir

- [ ] El archivo `corpus/analisis/{{DOCUMENTO_FECHA}}_{{DOCUMENTO_SLUG}}.analisis.md` existe
- [ ] Tiene las 5 secciones (búscalas por nombre)
- [ ] Al final tiene una tabla de metadatos con campos como `Nick corriente`, `Posición en corpus`, etc.
- [ ] Usa el vocabulario que ya está en `corpus/corpus.md` (no inventa sinónimos)
- [ ] No hay frases que juzguen el documento ("excelente argumento", "débil razonamiento", etc.)

**Si algo no cuadra:** no sigas. Dile a Copilot Chat qué está mal y pide que lo corrija. Solo cuando el análisis sea correcto, pasa al paso 2.

---

## Paso 2 · Comparación — `/diff-corpus`

**Escribe en Copilot Chat:**

```
/diff-corpus corpus/analisis/{{DOCUMENTO_FECHA}}_{{DOCUMENTO_SLUG}}.analisis.md
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
- El encabezado pasa a `Documentos procesados: {{CORPUS_PROCESADAS_DESPUES}}`
- Nunca se borra nada del corpus anterior

### ✓ Comprueba antes de seguir

- [ ] `corpus/corpus.md` dice `Documentos procesados: {{CORPUS_PROCESADAS_DESPUES}}`
- [ ] La fecha de última actualización es la de hoy
- [ ] Los nodos nuevos aparecen en sus secciones
- [ ] Los contadores han subido donde toca
- [ ] No se ha borrado nada del corpus previo

---

{{#INCLUIR_DESIGN}}
## Paso 4 · Cristalización y cierre de aprendizaje — `/design`

> Este paso solo se hace **una vez**, al final de un lote de inicialización o cuando el corpus
> ha crecido significativamente (≥3 documentos nuevos desde el último /design).

**Escribe en Copilot Chat:**

```
/design
```

**Qué sucede:** @cristalizador lee el corpus completo, los artefactos SDK (`.github/`), los artefactos mod (`mod/`) y la documentación de capacidades de VS Code Copilot (`COPILOT/`). La consulta documental no se limita a una lista fija: parte de `COPILOT/indice.md`, baja a las familias relevantes para la misión actual y reporta qué documentos consultó realmente.

El resultado no es solo una lista de archivos para `mod/`. El Cristalizador cierra el aprendizaje del ciclo y decide dónde debe cristalizar ese aprendizaje:

- en `mod/`, si hace falta una extensión u override local;
- en `main`, si el hueco pertenece al SDK;
- o como warning/dossier para `main`, si estás en una rama `mod/*` y el cambio correcto no debe implementarse desde ahí.

Genera 2-4 propuestas con:

- tipo de artefacto
- docs consultados
- superficie objetivo (`main`, `mod/` o warning/dossier para `main`)
- gates operativos (preview, hooks, plugins, MCP, coste/opt-in, instalaciones, etc.)
- fallback baseline si existe

### Tu decisión

Lee las propuestas. Si una variante reforzada depende de gates, pacta eso antes de implementarla. Responde, por ejemplo:

```
Implementa la 2
```

o:

```
Implementa la 2 con el fallback baseline
```

o:

```
Ninguna por ahora
```

### ✓ Si se implementa algo

- [ ] La propuesta declara qué docs de `COPILOT/` consultó
- [ ] La propuesta declara superficie objetivo (`main`, `mod/` o warning/dossier para `main`)
- [ ] Si la superficie es `mod/`, los artefactos nuevos quedan en `mod/`
- [ ] Si la superficie es `main`, el resultado queda como warning/dossier/backlog para `main`, no como edición de `.github/` desde esta rama
- [ ] Los gates operativos y el fallback baseline quedaron explícitos antes de implementar
- [ ] Puedes probar el artefacto o validar el resultado invocándolo en Copilot Chat, si aplica

---

{{/INCLUIR_DESIGN}}
## Paso {{PASO_COMMIT}} · Guardar cambios (terminal)

Abre la terminal de VS Code (`` Ctrl+` ``) y ejecuta:

```bash
git add corpus/ mod/
git status
```

Revisa que los cambios son solo en `corpus/` y `mod/`. **No debe haber cambios en `.github/`**. Si `/design` detectó una mejora que pertenece a `main`, no la metas desde esta rama: debe quedar como warning, dossier o trabajo pendiente para `main`, no como parche local en `.github/`.

Si todo está bien:

```bash
git commit -m "feat(corpus): análisis documental {{DOCUMENTO_FECHA}} {{DOCUMENTO_TITULO_SLUG}} — corpus {{CORPUS_PROCESADAS_DESPUES}} documentos"
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
corpus/corpus.md ({{CORPUS_PROCESADAS}} documento(s))
        │
   /feed → @bartleby → corpus/analisis/{{DOCUMENTO_FECHA}}_{{DOCUMENTO_SLUG}}.analisis.md
        │
   /diff-corpus → @archivero → NUEVO / CONFIRMA / DISCREPA / EVOLUCIONA
        │
   tú apruebas
        │
   /merge-corpus → @archivero → corpus/corpus.md ({{CORPUS_PROCESADAS_DESPUES}} documentos){{#INCLUIR_DESIGN}}
        │
   /design → @cristalizador → propuesta con docs consultados + target `main/mod` + gates
        │
   tú pactas e implementas solo si apruebas{{/INCLUIR_DESIGN}}
        │
   git add + commit{{#INCLUIR_PUSH}} + push{{/INCLUIR_PUSH}}
```

---

## Siguiente paso

{{#GUION_SIGUIENTE}}Cuando este guión esté completo, pasa a → `guiones/{{GUION_SIGUIENTE}}`{{/GUION_SIGUIENTE}}
{{^GUION_SIGUIENTE}}El corpus está inicializado. El flujo rutinario para futuros documentos: guardar en `corpus/documentos/`, ejecutar `/guion` para generar el roadmap, y seguir los pasos.{{/GUION_SIGUIENTE}}