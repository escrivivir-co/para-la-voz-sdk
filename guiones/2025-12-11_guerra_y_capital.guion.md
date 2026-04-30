# Guión: Ciclo completo para editorial 2025-12-11 — Guerra y capital

**Rama:** `mod/restitutiva`
**Editorial:** `corpus/editoriales/2025-12-11_guerra_y_capital.md`
**Título:** *Guerra y capital*
**Número:** PARA LA VOZ 3(2)

> **Antes de empezar:** Asegúrate de haber completado el guión anterior
> (`GUION_2025-04-30_arte.md`). El corpus debe tener **3 editoriales procesadas**.
> Compruébalo en `corpus/corpus.md`, línea `Editoriales procesadas:`.

---

## Qué vas a hacer

Esta es la **última editorial pendiente**. Tras completar este ciclo tendrás un corpus de 4 editoriales. Es el momento en que el corpus tiene masa suficiente para que los patrones sean fiables y @cristalizador pueda proponer artefactos agénticos útiles of verdad. Por eso este guión incluye un paso extra: **`/design`**.

```
Tú escribes en Copilot Chat          El agente hace
─────────────────────────────────     ──────────────────────────
/feed corpus/editoriales/...      →   @bartleby analiza → .analisis.md
/diff-corpus                      →   @archivero compara → informe diff
  (tú apruebas)
/merge-corpus                     →   @archivero integra → corpus.md (4 editoriales)
/design                           →   @cristalizador propone artefactos nuevos
  (tú decides cuáles implementar)
  (commit + push final)
```

---

## Paso 1 · Análisis — `/feed`

**Escribe en Copilot Chat:**

```
/feed corpus/editoriales/2025-12-11_guerra_y_capital.md
```

**Qué sucede:** @bartleby lee la editorial y el corpus acumulado (3 editoriales previas) y produce el análisis con 5 secciones:

1. La corriente: herencia y linaje
2. La taxonomía que el texto maneja
3. Los mecanismos retóricos heredados
4. Lo emergente — qué aporta sobre la tradición
5. Vista desde el hueco

El resultado se guarda en `corpus/analisis/2025-12-11_guerra_y_capital.analisis.md`.

### ✓ Comprueba antes de seguir

- [ ] El archivo `corpus/analisis/2025-12-11_guerra_y_capital.analisis.md` existe
- [ ] Tiene las 5 secciones (búscalas por nombre)
- [ ] Al final tiene tabla de metadatos
- [ ] Usa vocabulario ya establecido en `corpus/corpus.md` — con 3 editoriales previas el vocabulario está bastante asentado, así que si el análisis inventa términos nuevos sin marcarlos como `[propuesta: ...]`, algo falla
- [ ] No hay juicios de valor

**Si algo no cuadra:** dile a Copilot Chat qué está mal. Solo cuando esté correcto, pasa al paso 2.

---

## Paso 2 · Comparación — `/diff-corpus`

**Escribe en Copilot Chat:**

```
/diff-corpus corpus/analisis/2025-12-11_guerra_y_capital.analisis.md
```

**Qué sucede:** @archivero compara con el corpus y clasifica:

| Categoría | Significado |
|-----------|-------------|
| **NUEVO** | No existía en el corpus |
| **CONFIRMA** | Ya estaba y se repite (contador sube) |
| **DISCREPA** | Contradice un patrón previo |
| **EVOLUCIONA** | Desarrolla un patrón sin contradecirlo |

> **Nota importante:** Con 3 editoriales previas, es normal que aparezcan las primeras
> **DISCREPA** reales. El corpus empieza a tener patrones lo bastante firmes como para
> que una editorial nueva pueda tensionarlos. No te alarmes — una discrepancia es
> información valiosa, no un error.

### ✓ Comprueba antes de seguir

- [ ] El diff cubre todas las secciones: linaje, exclusión, taxonomía, mecanismos, emergencias, ausencias, nick
- [ ] Los contadores ×N son coherentes (si algo aparecía ×3, ahora debería ser ×4 si CONFIRMA)
- [ ] Si hay DISCREPA, entiendes qué contradice y qué patrón previo tensiona

### Tu decisión

```
Apruebo el merge
```

Si hay una DISCREPA que no entiendes, pregúntale al archivero. Puedes aprobar merges con discrepancias — quedan registradas como "abiertas" en el corpus.

---

## Paso 3 · Integración — `/merge-corpus`

**Escribe en Copilot Chat:**

```
/merge-corpus
```

**Qué sucede:** @archivero actualiza `corpus/corpus.md`. El encabezado pasa a `Editoriales procesadas: 4`.

### ✓ Comprueba antes de seguir

- [ ] `corpus/corpus.md` dice `Editoriales procesadas: 4`
- [ ] Fecha actualizada a hoy
- [ ] Los 4 análisis contribuyen al mapa acumulativo
- [ ] Contadores reflejan las 4 editoriales
- [ ] Si hubo DISCREPA, aparece en "Discrepancias abiertas"
- [ ] No se ha borrado nada

---

## Paso 4 · Cristalización — `/design`

> Este paso solo se hace **una vez**, al final de todos los ciclos de inicialización.
> Ahora el corpus tiene 4 editoriales — suficiente masa para que las propuestas sean útiles.

**Escribe en Copilot Chat:**

```
/design
```

**Qué sucede:** @cristalizador lee el corpus completo, los artefactos SDK (`.github/`), los artefactos mod (`mod/`), y la documentación de capacidades de VS Code Copilot (`COPILOT/`). Genera 2-4 propuestas de artefactos nuevos, cada una con:

- Tipo (agent, prompt, skill, hook, instruction)
- Qué capacidad nueva activa
- Por qué el corpus lo justifica
- Dónde se crea (siempre en `mod/`, nunca en `.github/`)
- Boceto de implementación

### Tu decisión

Lee las propuestas. Puedes:

- **Aprobar todas:** "Implementa todas"
- **Aprobar algunas:** "Implementa la 1 y la 3"
- **No aprobar ninguna:** "Ninguna por ahora" — no pasa nada, puedes volver a ejecutar `/design` más adelante
- **Pedir cambios:** "La propuesta 2 me interesa pero cambia X por Y"

### ✓ Si se implementa algo

- [ ] Los archivos nuevos están en `mod/` (agentes en `mod/agents/`, prompts en `mod/prompts/`, etc.)
- [ ] No hay archivos nuevos en `.github/`
- [ ] Puedes probar el artefacto invocándolo en Copilot Chat

---

## Paso 5 · Guardar y publicar (terminal)

Abre la terminal de VS Code (`` Ctrl+` ``) y ejecuta:

```bash
git add corpus/ mod/
git status
```

Revisa que los cambios son solo en `corpus/` y `mod/`. Si hiciste commit parcial en el guión anterior, verás solo los cambios de este ciclo. Si no, verás los de ambos. Todo correcto.

```bash
git commit -m "feat(corpus): análisis editorial 2025-12-11 guerra y capital — corpus 4 editoriales

- 4/4 editoriales procesadas — inicialización del corpus completa
- Cristalización: [lista de artefactos creados, o 'pendiente']"
```

Ahora sí, **push**:

```bash
git push origin mod/restitutiva
```

---

## Verificación final del corpus

Una vez hecho push, ejecuta en Copilot Chat:

```
/status
```

@archivero te dará un resumen del estado del corpus. Comprueba:

- [ ] 4 editoriales procesadas
- [ ] 4 archivos en `corpus/analisis/`
- [ ] El vocabulario es coherente (no hay sinónimos sueltos)
- [ ] Los contadores ×N reflejan las 4 editoriales
- [ ] Las emergencias acumuladas son `≥ 3` (al menos las del primero de mayo)
- [ ] Las ausencias estructurales se mantienen o crecen

---

## Resumen visual

```
corpus/corpus.md (3 editoriales)
        │
   /feed → @bartleby → corpus/analisis/2025-12-11_guerra_y_capital.analisis.md
        │
   /diff-corpus → @archivero → NUEVO / CONFIRMA / DISCREPA / EVOLUCIONA
        │
   tú apruebas
        │
   /merge-corpus → @archivero → corpus/corpus.md (4 editoriales)
        │
   /design → @cristalizador → artefactos nuevos en mod/
        │
   git add + commit + push
        │
   /status → verificación final ✓
```

---

## ¿Y después?

Con el corpus inicializado (4 editoriales), el flujo normal para futuras editoriales es más sencillo:

1. Guarda la nueva editorial en `corpus/editoriales/YYYY-MM-DD_titulo.md`
2. `/feed corpus/editoriales/YYYY-MM-DD_titulo.md`
3. `/diff-corpus`
4. Aprueba
5. `/merge-corpus`
6. (Opcionalmente) `/design` cada 2-3 editoriales
7. Commit + push

No necesitas crear un guión nuevo cada vez — el ciclo ya es rutina.
