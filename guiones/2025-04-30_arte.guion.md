# Guión: Ciclo completo para editorial 2025-04-30 — Marxismo y arte

**Rama:** `mod/restitutiva`
**Editorial:** `corpus/editoriales/2025-04-30_arte.md`
**Título:** *Entre lo bello y lo justo; Marxismo y arte en Lukács y Lifschitz*
**Número:** PARA LA VOZ 3(1)

> **Antes de empezar:** Asegúrate de haber completado el guión de la editorial anterior
> (`GUION_2024-11-20_materialismo.md`). El corpus debe tener **2 editoriales procesadas**
> antes de iniciar este ciclo. Compruébalo en `corpus/corpus.md`, línea `Editoriales procesadas:`.

---

## Qué vas a hacer

Vas a pasar la editorial de arte por el pipeline Bartleby. Son 3 pasos con agentes + 1 commit manual. Cada paso es una instrucción que escribes en **Copilot Chat** (el panel lateral de VS Code). Los agentes hacen el trabajo; tú verificas y apruebas.

```
Tú escribes en Copilot Chat          El agente hace
─────────────────────────────────     ──────────────────────────
/feed corpus/editoriales/...      →   @bartleby analiza → .analisis.md
/diff-corpus                      →   @archivero compara → informe diff
  (tú apruebas)
/merge-corpus                     →   @archivero integra → corpus.md actualizado
  (tú haces commit en terminal)
```

---

## Paso 1 · Análisis — `/feed`

**Escribe en Copilot Chat:**

```
/feed corpus/editoriales/2025-04-30_arte.md
```

**Qué sucede:** @bartleby lee la editorial y el corpus acumulado (2 editoriales previas) y produce un análisis con 5 secciones:

1. La corriente: herencia y linaje
2. La taxonomía que el texto maneja
3. Los mecanismos retóricos heredados
4. Lo emergente — qué aporta sobre la tradición
5. Vista desde el hueco

El resultado se guarda en `corpus/analisis/2025-04-30_arte.analisis.md`.

### ✓ Comprueba antes de seguir

- [ ] El archivo `corpus/analisis/2025-04-30_arte.analisis.md` existe
- [ ] Tiene las 5 secciones (búscalas por nombre)
- [ ] Al final tiene una tabla de metadatos con campos como `Nick corriente`, `Posición en corpus`, etc.
- [ ] Usa el vocabulario que ya está en `corpus/corpus.md` (por ejemplo, si el corpus dice "restitutiva", el análisis no debería inventar "restauradora" como sinónimo)
- [ ] No hay frases que juzguen la editorial ("excelente argumento", "débil razonamiento", etc.)

**Si algo no cuadra:** no sigas. Dile a Copilot Chat qué está mal y pide que lo corrija. Solo cuando el análisis sea correcto, pasa al paso 2.

---

## Paso 2 · Comparación — `/diff-corpus`

**Escribe en Copilot Chat:**

```
/diff-corpus corpus/analisis/2025-04-30_arte.analisis.md
```

**Qué sucede:** @archivero compara el análisis recién creado con todo lo que hay en `corpus/corpus.md` y clasifica cada hallazgo en una de estas categorías:

| Categoría | Significado |
|-----------|-------------|
| **NUEVO** | Algo que no existía en el corpus (nuevo nodo de linaje, nueva categoría, etc.) |
| **CONFIRMA** | Algo que ya estaba y se repite (el contador sube: ×2 → ×3) |
| **DISCREPA** | Algo que contradice un patrón previo del corpus |
| **EVOLUCIONA** | Algo que desarrolla un patrón sin contradecirlo |

### ✓ Comprueba antes de seguir

- [ ] El diff cubre las secciones del corpus: linaje, exclusión, taxonomía, mecanismos, emergencias, ausencias, nick
- [ ] Cada elemento tiene su categoría (NUEVO / CONFIRMA / DISCREPA / EVOLUCIONA)
- [ ] Los contadores ×N son coherentes (si Lenin aparecía ×1 y se repite, debería ser ×2)

### Tu decisión

Lee el diff con calma. Si es correcto, responde:

```
Apruebo el merge
```

Si hay algo que quieras matizar o corregir, díselo al archivero antes de aprobar. Si ves un DISCREPA que no entiendes, pregunta.

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
- El encabezado pasa a `Editoriales procesadas: 3`
- Nunca se borra nada del corpus anterior

### ✓ Comprueba antes de seguir

- [ ] `corpus/corpus.md` dice `Editoriales procesadas: 3`
- [ ] La fecha de última actualización es la de hoy
- [ ] Los nodos nuevos (Lifschitz, Lukács-estético, etc.) aparecen donde corresponde
- [ ] Los contadores han subido donde toca
- [ ] No se ha borrado nada del corpus previo

---

## Paso 4 · Guardar cambios (terminal)

Abre la terminal de VS Code (`` Ctrl+` ``) y ejecuta:

```bash
git add corpus/ mod/
git status
```

Revisa que los archivos modificados son solo de `corpus/` y `mod/`. **No debe haber cambios en `.github/`** (eso es SDK, no se toca desde aquí).

Si todo está bien:

```bash
git commit -m "feat(corpus): análisis editorial 2025-04-30 arte — corpus 3 editoriales"
```

> **No hagas push todavía** si vas a continuar con el siguiente guión (`GUION_2025-12-11_guerra_y_capital.md`). Puedes hacer un solo push al final de todos los ciclos.

---

## Resumen visual

```
corpus/corpus.md (2 editoriales)
        │
   /feed → @bartleby → corpus/analisis/2025-04-30_arte.analisis.md
        │
   /diff-corpus → @archivero → NUEVO / CONFIRMA / DISCREPA / EVOLUCIONA
        │
   tú apruebas
        │
   /merge-corpus → @archivero → corpus/corpus.md (3 editoriales)
        │
   git add + commit
```

---

## Siguiente paso

Cuando este guión esté completo, pasa a → `GUION_2025-12-11_guerra_y_capital.md`
