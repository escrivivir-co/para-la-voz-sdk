# Guión: Ciclo completo para editorial 2024-11-20_materialismo

**Rama:** `mod/restitutiva`
**Editorial:** `corpus/editoriales/2024-11-20_materialismo.md`
**Fecha:** 2026-04-15

---

## Prerequisitos

- [x] Estar en rama `mod/restitutiva`
- [x] Editorial guardada en `corpus/editoriales/2024-11-20_materialismo.md`
- [ ] VS Code abierto en la raíz del repo `para-la-voz-sdk`

---

## Paso 1: `/feed` → @bartleby analiza la editorial

**Agente:** `@bartleby`
**Comando:** Escribir en Copilot Chat:

```
/feed corpus/editoriales/2024-11-20_materialismo.md
```

**Qué hace el agente:**
1. Lee `corpus/corpus.md` (mapa acumulativo — ya tiene 1 editorial procesada)
2. Lee `corpus/analisis/2024-05-01_primero-de-mayo.analisis.md` (análisis previo)
3. Lee la editorial `corpus/editoriales/2024-11-20_materialismo.md`
4. Produce análisis con 5 secciones:
   - I. La corriente: herencia y linaje
   - II. La taxonomía que el texto maneja
   - III. Los mecanismos retóricos heredados
   - IV. Lo emergente — qué aporta sobre la tradición
   - V. Vista desde el hueco
5. Guarda en `corpus/analisis/2024-11-20_materialismo.analisis.md`

**Verificación antes de continuar:**
- [ ] Existe `corpus/analisis/2024-11-20_materialismo.analisis.md`
- [ ] Tiene las 5 secciones completas
- [ ] Tiene tabla de metadatos al final
- [ ] Usa vocabulario de `corpus/corpus.md` (no inventa sinónimos)
- [ ] No hay juicios de valor (ver frases prohibidas en bartleby-voice)

**Si algo falla:** No continuar. Revisar que @bartleby tiene acceso al corpus y que la editorial está leíble.

---

## Paso 2: `/diff-corpus` → @archivero compara con corpus

**Agente:** `@archivero`
**Comando:**

```
/diff-corpus corpus/analisis/2024-11-20_materialismo.analisis.md
```

**Qué hace el agente:**
1. Lee el análisis recién creado
2. Lee `corpus/corpus.md` completo
3. Produce informe con 4 categorías:
   - **NUEVO**: elementos en el análisis ausentes en corpus.md
   - **CONFIRMA**: elementos que reiteran patrones (con contador ×N)
   - **DISCREPA**: elementos que contradicen el patrón
   - **EVOLUCIONA**: variaciones que desarrollan sin contradecir
4. Pregunta: "¿Apruebas el merge?"

**Verificación antes de continuar:**
- [ ] El diff cubre las 7 secciones de corpus.md (linaje, exclusión, taxonomía, mecanismos, emergencias, ausencias, nick)
- [ ] Cada elemento está clasificado en NUEVO/CONFIRMA/DISCREPA/EVOLUCIONA
- [ ] Los contadores ×N son coherentes con el corpus previo

**Decisión del usuario:** Revisar el diff. Si es correcto, responder "Sí, apruebo el merge" o similar.

---

## Paso 3: `/merge-corpus` → @archivero integra en corpus.md

**Agente:** `@archivero`
**Comando:**

```
/merge-corpus
```

(El archivero toma el diff aprobado del contexto de la conversación.)

**Qué hace el agente:**
1. Lee el diff aprobado
2. Edita `corpus/corpus.md`:
   - NUEVO → añade con `[añadido: 2026-04-15]`
   - CONFIRMA → actualiza contadores `[×N]`
   - DISCREPA → registra en sección "Discrepancias abiertas"
   - EVOLUCIONA → documenta como variante del patrón
3. Actualiza encabezado: `Editoriales procesadas: 2`, `Última actualización: 2026-04-15`
4. **Nunca borra** — principio de palimpsesto

**Verificación antes de continuar:**
- [ ] `corpus/corpus.md` tiene `Editoriales procesadas: 2`
- [ ] La fecha está actualizada
- [ ] Los nodos nuevos de linaje aparecen en sus secciones
- [ ] Los contadores han subido donde aplica
- [ ] No se ha borrado nada del corpus previo

---

## Paso 4: `/design` → @cristalizador propone artefactos

**Agente:** `@cristalizador`
**Comando:**

```
/design
```

**Qué hace el agente:**
1. Lee `corpus/corpus.md` actualizado
2. Lee `.github/` (artefactos SDK) y `mod/` (artefactos mod existentes)
3. Lee `COPILOT/` (docs de capacidades VS Code Copilot)
4. Genera 2-4 propuestas, cada una con:
   - Tipo de artefacto
   - Capacidad Copilot nueva que activa
   - Motivación desde el corpus
   - Ruta en `mod/` (NUNCA en `.github/`)
   - Boceto de implementación
5. Pregunta: "¿Implemento alguna?"

**Decisión del usuario:** Revisar propuestas. Aprobar las que tengan sentido.

**Verificación si se implementa algo:**
- [ ] Los archivos nuevos están en `mod/` (no en `.github/`)
- [ ] El artefacto funciona (probarlo invocándolo)

---

## Paso 5: Commit y push

**Comando terminal (no agente):**

```bash
git add corpus/ mod/
git status
# Verificar que solo hay cambios en corpus/ y mod/
# NO debe haber cambios en .github/ (eso es SDK)

git commit -m "feat(corpus): análisis editorial 2024-11-20 materialismo militante

- Análisis Bartleby completo (5 secciones)
- Diff y merge ejecutados — corpus.md actualizado (2 editoriales)
- [si hubo cristalización: listar artefactos creados en mod/]"

git push origin mod/restitutiva
```

**Verificación final:**
- [ ] `git diff --name-only HEAD~1` muestra solo cambios en `corpus/` y `mod/`
- [ ] `git log --oneline -3` tiene los commits documentados

---

## Resumen del ciclo

```
Editorial 2024-11-20_materialismo.md
        │
   /feed → @bartleby → corpus/analisis/2024-11-20_materialismo.analisis.md
        │
   /diff-corpus → @archivero → informe NUEVO/CONFIRMA/DISCREPA/EVOLUCIONA
        │
   usuario aprueba
        │
   /merge-corpus → @archivero → corpus/corpus.md actualizado (2 editoriales)
        │
   /design → @cristalizador → propuestas de artefactos en mod/
        │
   git add corpus/ mod/ && git commit && git push
```

Cada paso es secuencial. No saltar ninguno. Si un agente falla, repetir ese paso antes de continuar.
