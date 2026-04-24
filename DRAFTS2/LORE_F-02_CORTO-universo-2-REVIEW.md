# Benchmark comparativo — universo-2 × 3 modelos

> **Fecha:** 2026-04-20
> **Modelo revisor:** Claude Opus 4.6
> **Universo fuente:** [universo/universo-2.md](universo/universo-2.md)
> **Cortos evaluados:**
> - [LORE_F-02_CORTO-universo-2-claude-opus-4-6.md](LORE_F-02_CORTO-universo-2-claude-opus-4-6.md)
> - [LORE_F-02_CORTO-universo-2-gemini-3.1-pro.md](LORE_F-02_CORTO-universo-2-gemini-3.1-pro.md)
> - [LORE_F-02_CORTO-universo-2-gpt-5-4.md](LORE_F-02_CORTO-universo-2-gpt-5-4.md)
> **Pipeline validado contra:** engine-plan.prompt.md + futures-engine SKILL.md

---

## 0. Parámetros del spec ([universo-2.md](universo/universo-2.md))

| Parámetro | Valor especificado |
|---|---|
| Registro | Omnisciente fría |
| Foco | Colectivo (sustrato), no individuo |
| Palabras | ~900–1100 |
| Estructura | 5 movimientos (I→V) |
| Consignas activables | 3 ("el cine es nuestro", "cada vez que tumben algo…", "que internet haga lo suyo") — max 1 vez cada una |
| Metáforas prohibidas | "cervatillo se vuelve manada" |
| Punto ciego | Burocratización del ecosistema |
| Cierre | Tensión abierta, no utopía |

---

## 1. Cobertura de estaciones (R4.1–R4.7)

| Estación | Opus 4.6 | Gemini 3.1 Pro | GPT-5.4 |
|---|---|---|---|
| **R4.1** 11.007 vs 40 | ✅ Párrafo 3, desarrollado | ✅ Párrafo 2, compacto | ✅ Párrafo 4, desarrollado |
| **R4.2** Suspensión cautelar | ✅ Párrafo 5 | ✅ Párrafo 1 (abre con ella) | ✅ Párrafo 5-6 |
| **R4.3** Ecosistema / segunda ola | ✅ Párrafos 7-9 (amplio) | ✅ Párrafo 3-4 (comprimido) | ✅ Párrafos 7-9 (amplio) |
| **R4.4** Equipo legal / tándem | ✅ Párrafo 10, tándem nombrado | ⚠️ Implícito ("la defensa legal…plantilla") | ✅ Párrafo 6, roles nombrados |
| **R4.5** Desgaste / león afloja | ✅ Párrafo 11 | ✅ Párrafo 2 ("la escala devora al castigador") | ✅ Párrafo 10 |
| **R4.6** Federación territorial | ✅ Párrafo 12 | ✅ Implícito ("células asignándose tareas") | ✅ Párrafo 11 |
| **R4.7** "No era esto" / tensión | ✅ Párrafo 13 | ⚠️ Insinuado ("seguirá intacto, pero ya estará habitado") | ✅ Párrafo 12 |

**Resultado:** Opus cubre 7/7 explícitamente. GPT-5.4 cubre 7/7 explícitamente. Gemini cubre 4/7 explícitamente y 3/7 por compresión o elisión. Gemini sacrifica R4.4 y R4.7 como estaciones autónomas.

---

## 2. Datos duros del corpus utilizados

| Dato | Opus 4.6 | Gemini 3.1 Pro | GPT-5.4 |
|---|---|---|---|
| 11.007 vs 40 | ✅ | ✅ | ✅ |
| Mercury 70-80% | ✅ | ❌ | ✅ |
| Patrón denuncias EGEDA | ✅ | ❌ | ✅ |
| Oferta ene-2025 (100k€) | ✅ | ❌ | ✅ |
| ~4.000 análisis | ✅ | ❌ | ✅ |
| ~500 GB / hydra archiving | ✅ | ❌ | ✅ |
| RD 2016 obras huérfanas | ✅ | ✅ | ✅ |
| Zoowoman enlazaba, no alojaba | ✅ | ❌ | ✅ |
| Hachette vs Internet Archive | ❌ | ❌ | ❌ |
| Cine iraní/Bután/Uganda | ✅ | ✅ (iraní, Bután, Europa del Este) | ✅ |
| 870k€ + 2.5 años | ✅ | ✅ (87k€→error; prisión mencionada) | ✅ |

**Resultado:** Opus usa 10/11 datos. GPT-5.4 usa 10/11. Gemini usa 5/11. Gemini compensa con densidad conceptual pero pierde granularidad factual, lo cual debilita el eje `dato` del spec. Ninguno de los tres usa el precedente Hachette, que el universo-2 especifica en R4.5.

**Error Gemini:** El texto dice "ochenta y siete mil euros de fianza" — la cifra real del spec es 870.000€. Esto es un fallo de dato duro, no de estilo.

---

## 3. Consignas y léxico prohibido

| Consigna | Opus 4.6 | Gemini 3.1 Pro | GPT-5.4 |
|---|---|---|---|
| "el cine es nuestro" | ✅ ×1 | ✅ ×1 (implícito: "el cine vuelve a pasarse de mano en mano") | ✅ ×1 |
| "cada vez que tumben algo…" | ✅ ×1 (cierre) | ✅ ×1 (adaptado: "escarmiento ejemplar les salió demasiado caro") | ✅ ×1 (cierre) |
| "que internet haga lo suyo" | ✅ ×1 | ❌ | ✅ ×1 |
| "cervatillo→manada" (prohibido) | ✅ ausente | ✅ ausente | ✅ ausente |

**Resultado:** Los tres respetan la prohibición. Opus y GPT activan las 3 consignas exactas. Gemini no activa "que internet haga lo suyo" y parafrasea las otras dos, lo cual es legítimo pero pierde la fuerza del verbatim del corpus.

---

## 4. Adherencia al registro literario (Omnisciente fría)

| Criterio | Opus 4.6 | Gemini 3.1 Pro | GPT-5.4 |
|---|---|---|---|
| Distancia narrativa | ✅ Consistente, sin inmersión en subjetividad | ✅ Muy conseguida, casi ensayística | ⚠️ Desliza a calidez en los párrafos de ecosistema |
| Foco colectivo | ✅ Feo es pieza, no protagonista | ✅ Estricto: casi no nombra individuos | ⚠️ Nombra a todos (Feo, Bravo, Cristóbal, Rubén, Facu) con cercanía |
| Sin chimichimi | ✅ | ✅ | ⚠️ "Hablan como si el archivo siguiera abierto. En cierto sentido, lo está." — coquetea con el chimichimi |
| Asimetría como textura | ✅ ("una persona vs un entramado") | ✅ ("la escala devora al castigador") | ✅ ("12.000€ vs 870.000€" implícito) |

**Resultado:** Gemini es el más limpio en registro frío — casi quirúrgico. Opus mantiene la distancia con oficio. GPT-5.4 desliza hacia un narrador más empático, lo cual viola parcialmente el spec "fría" / "colectivo". El primer párrafo de GPT ("la gente entra con abrigos ligeros y sale tarde") es narración cálida, no fría.

---

## 5. Ejes de drama del futures-engine

| Eje | Opus 4.6 | Gemini 3.1 Pro | GPT-5.4 |
|---|---|---|---|
| **Relato vs relato** | ✅ Mov II explícito: "obliga a mirar la mano que reclama" | ✅ Implícito por inversión aritmética | ✅ Mov IV: "obligaba a mirar la mano que reclamaba" |
| **Portería móvil** | ✅ Suspensión cautelar como portería | ⚠️ Mencionada pero no desarrollada como eje | ✅ Suspensión + oferta como portería |
| **Paradoja recursiva** | ✅ "la reclamación masiva… proporcionada al aparato" + grieta final | ✅ "la escala del castigo devora al castigador" — paradoja explícita | ✅ "La aritmética deja de obedecer…" + grieta final |

**Resultado:** Los tres activan los 3 ejes. Gemini lo hace con la sentencia más potente ("la escala del castigo devora al castigador") pero sin el desarrollo que el spec exigía.

---

## 6. Punto ciego y cierre en tensión abierta

| Criterio | Opus 4.6 | Gemini 3.1 Pro | GPT-5.4 |
|---|---|---|---|
| Tensión post-monopolio | ✅ Párrafo 13: quién decide catálogo, filtros, agotamiento | ⚠️ "el vacío…seguirá intacto" — no desarrolla las tensiones internas | ✅ Párrafo 12: tensiones nombradas explícitamente |
| "No era esto" | ✅ Textual | ❌ Ausente | ✅ Textual |
| Cierre sin utopía | ✅ "cada vez que tumben algo…" como certeza modesta | ✅ "escarmiento ejemplar les salió demasiado caro" — cierre seco | ✅ "cada vez que tumben algo…" como certeza modesta |
| Punto ciego nombrado | ⚠️ Implícito (cuánto tarda una institución en parecerse al filtro) | ❌ No se nombra | ⚠️ Implícito (misma formulación que Opus) |

**Resultado:** Ninguno de los tres nombra explícitamente la burocratización como punto ciego, que es lo que universo-2 pide. Los tres eluden la sombra nueva. Opus y GPT llegan cerca con "cuánto tarda una institución en parecerse al filtro que vino a corregir" — pero eso es tensión de R4.7, no el punto ciego de la rama. Gemini lo omite completamente.

---

## 7. Solapamiento entre generaciones

| Dimensión | Nivel de solapamiento |
|---|---|
| Estructura narrativa | **Alto.** Opus y GPT siguen la misma secuencia de 5 movimientos. GPT añade un prólogo en el futuro (martes de 2027). Gemini comprime a 4 párrafos con secuencia distinta. |
| Frases casi idénticas | **Crítico entre Opus y GPT.** "La reclamación masiva dejaba/deja de parecer proporcionada al daño y empieza/empezaba a parecer proporcionada al aparato" — formulación convergente al 90%. El cierre (disco duro en mochila + proyector + pared vacía) es idéntico en ambos. |
| Diferenciación estructural | **Solo Gemini.** Invierte la cronología (abre con la cautelar), comprime 7 estaciones en 4 bloques, y cierra con una sentencia-resumen en lugar de una escena. Es el único texto que no replica la plantilla. |
| Contenido exclusivo | Opus: "los créditos de la película iraní estaban en un idioma que nadie hablaba con fluidez". GPT: prólogo in-media-res de 2027. Gemini: "hidra descabezada→células asignándose tareas". |

**Diagnóstico de solapamiento:** GPT-5.4 parece haber convergido con Opus al punto de compartir cierre escénico casi textual. Esto puede indicar que ambos siguieron la "estructura sugerida" del spec de forma demasiado literal, o que GPT recibió el corto de Opus como contexto (verificar si hubo leak de attachment).

---

## 8. Validación contra el pipeline (engine-plan)

| Checkpoint del pipeline | Estado |
|---|---|
| **Upstream Loreador → INDEX** | ✅ Los 3 cortos referencian 51/51 piezas vía grafo rev-045 |
| **Upstream Bartleby → Corpus** | ✅ Los 3 referencian CORPUS_PREVIEW-rev-045 |
| **Upstream Grafista → Grafo** | ✅ Los 3 dicen 27 nodos, 35 arcos |
| **Upstream Demiurgo → Universo** | ✅ Los 3 referencian universo-2.md |
| **Dramaturgo → Obra** | ⚠️ Los 3 son obras generables, pero la convergencia Opus↔GPT sugiere que la spec es demasiado directiva — el Dramaturgo downstream pierde grados de libertad |
| **Metadata requerida** | ✅ Los 3 tienen la cabecera completa con todos los campos |
| **Pipeline refresh viable** | ✅ Si cambia el grafo o el corpus, los 3 podrían regenerarse — la trazabilidad es completa |

---

## 9. Tabla resumen por modelo

| Criterio (peso) | Opus 4.6 | Gemini 3.1 Pro | GPT-5.4 |
|---|---|---|---|
| Cobertura de estaciones | ★★★★★ | ★★★☆☆ | ★★★★★ |
| Datos duros del corpus | ★★★★★ | ★★★☆☆ | ★★★★★ |
| Registro literario | ★★★★★ | ★★★★★ | ★★★★☆ |
| Ejes de drama | ★★★★★ | ★★★★☆ | ★★★★★ |
| Punto ciego / cierre | ★★★★☆ | ★★★☆☆ | ★★★★☆ |
| Diferenciación (anti-overlap) | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| Wordcount (~900-1100) | ~1080 ✅ | ~350 ❌ | ~1250 ⚠️ |
| Error factual | 0 | 1 (87k€ ≠ 870k€) | 0 |

---

## 10. Diagnóstico para el pipeline

1. **Gemini 3.1 Pro es demasiado corto.** ~350 palabras vs ~900-1100 spec. Funciona como abstract denso, no como corto grabable. El pipeline necesitaría un paso de expansión o un re-prompt con constraint de longitud.

2. **GPT-5.4 converge excesivamente con Opus.** El cierre escénico (disco duro, mochila, proyector, pared vacía) es prácticamente idéntico. Para un benchmark multi-modelo, esto resta valor comparativo. O la spec es demasiado directiva (la tabla de movimientos del universo-2 dicta la estructura) o hubo filtración de contexto.

3. **Ninguno nombra el punto ciego que el universo-2 define.** La burocratización como sombra propia del ecosistema queda en el universo pero no baja al corto. Esto es un gap del pipeline: el Dramaturgo downstream no está obligado por contrato a materializar el punto ciego como texto, y los tres lo eliden.

4. **Nadie usa Hachette vs Internet Archive.** Dato específico de R4.5 que los 3 omiten. Sugiere que los modelos lo consideran secundario o que la spec no lo marca como obligatorio.

5. **GPT-5.4 tiene un problema de encoding.** El título dice "Los Martes Del Ano Ganado" (sin tilde en "Año") y todo el texto carece de acentos. Esto es un artefacto del modelo, no del pipeline, pero para un corto grabable es un problema de producción.

**Recomendación para el futures-engine:** Añadir al contrato del Dramaturgo un checklist mínimo de materialización (punto ciego, datos obligatorios, constraint de wordcount) que el pipeline pueda verificar automáticamente sin requerir revisión humana.
