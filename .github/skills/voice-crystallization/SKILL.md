---
name: voice-crystallization
description: Skill portable para cristalizar la voz de un corpus en contenido generado. Extrae la firma de voz desde corpus/corpus.md (nick, marcadores, mecanismos retóricos, vocabulario taxonómico, ausencias estructurales, emergencias) y la aplica para generar texto que nazca del corpus — no sobre él. Es el espejo del skill editorial-analysis: donde el análisis extrae texto → corpus, la cristalización genera corpus → texto. Se activa cuando se pide generar poemas, manifiestos, pitches, prosas o cualquier otro contenido alineado con la voz de un lore específico.
---

# Skill: voice-crystallization — Protocolo de cristalización de voz

Esta skill implementa la dirección inversa del análisis Bartleby: en lugar de extraer arquitectura de un texto para acumularla en corpus, extrae la firma de voz del corpus acumulado para generar nuevo texto que hable esa voz.

**Relación con editorial-analysis:**
- `editorial-analysis`: texto externo → corpus (extracción, análisis, acumulación)
- `voice-crystallization`: corpus → texto nuevo (síntesis, generación, cristalización)

Las mismas 5 categorías del análisis Bartleby (linaje, taxonomía, mecanismos, emergencias, hueco) se leen aquí como fuentes generativas, no como destinos analíticos.

---

## Cuándo activar esta skill

- Cuando se pide generar contenido que hable la voz del corpus (poema, prosa, manifiesto, pitch, hilo de texto, presentación...)
- Cuando se pide que un texto "suene a" la corriente del corpus
- Cuando se quiere comunicar el corpus hacia afuera sin que el contenido sea *sobre* el corpus
- Cuando el tema del usuario es la punta del iceberg y el corpus es la raíz

**NO activar si:**
- Se pide analizar un texto externo (usar `editorial-analysis`)
- Se pide un resumen del corpus (usar `/status`)
- Se pide generar artefactos agénticos (usar `/design`)

---

## El principio generativo

> El corpus es la raíz. El tema (si hay) es la punta del iceberg.

El contenido generado no es "un texto sobre el corpus" ni "un texto que explica el corpus". Es un texto que **habla desde** el corpus: usa su léxico, sus proporciones retóricas, sus tensiones internas, su sentido de la urgencia, sus ausencias como sombras. El lector que no sabe que existe el corpus debe sentir que el texto viene de *algún lugar* — de una corriente real, de una posición genuina.

Si el usuario da un tema, ese tema es el punto de entrada visible. El corpus lo impregna desde dentro.

Si el usuario no da tema, el generador escoge desde el propio corpus: una emergencia sin resolver, una ausencia estructural, una evolución en curso, un patrón de mecanismos que merece superficie.

---

## Protocolo — Extracción de firma de voz

### Paso 1: Leer corpus/corpus.md completo

No es opciones: leer entero. La firma de voz emerge del patrón acumulado, no de secciones aisladas.

### Paso 2: Extraer los 5 componentes de la firma

#### 2.1. Identidad de corriente (§ Nick)

El nick y sus marcadores son la **firma estructural**:

| Marcador | Función generativa |
|---|---|
| Linaje jerárquico | El texto CITA, no inventa. Nombres propios del corpus como ancla y autoridad |
| Demarcación bilateral | El texto dice "ni...ni..." para ubicarse. O simplemente excluye sin demarcación explícita según registro |
| Autocita | El texto puede referirse a sí mismo, a la publicación, al proyecto como ecosistema |
| Verbos de obligación | Hay una proporción real de imperativos. No decorativos: estructurales |
| Re-traducir, no re-teorizar | Verbos: recuperar, profundizar, volver a, rescatar, incorporar. No: inventar, proponer desde cero |
| Externalización del error | Si hay error, es del sistema, del pasado, del enemigo. Nunca del sujeto hablante en presente |

Los marcadores son **restricciones generativas**: no limitan el texto sino lo anclan a la corriente. Un texto que viola los 6 marcadores no habla esa voz — habla otra.

#### 2.2. Vocabulario taxonómico (§ Taxonomía)

Las palabras del corpus son el léxico generativo. No sinónimos: las palabras exactas.

**Principio:** si el corpus dice "hilo rojo", el texto generado dice "hilo rojo" — no "hilo conductor" ni "línea roja". La taxonomía del corpus tiene palabras específicas porque esas palabras hacen trabajo político y conceptual que los sinónimos no hacen.

Extraer:
- Conceptos estables (×3 o más editoriales) → uso libre, son roca del vocabulario
- Conceptos en estabilización (×2) → uso con cuidado, son vocabulario en construcción
- Conceptos nuevos (×1) → usar solo si el texto apunta precisamente a esa editorial

#### 2.3. Proporciones retóricas (§ Mecanismos)

Los mecanismos retóricos con sus frecuencias dan las **proporciones del texto**:

| Dado en corpus | Función generativa |
|---|---|
| Verbos de obligación ×N (alta frecuencia) | Textura imperativa persistente — no es énfasis, es ritmo base |
| Temporalidad apocalíptica (frecuencia media) | Horizonte de urgencia — se activa en momentos clave, no en cada verso |
| Autorización por cita canónica | Nombrar el linaje como fundamento, no como ornamento |
| Subordinación estructural | La teoría solo vale si orienta la práctica — construir hacia ese cierre |
| Complejidad contra simplismo | El texto no simplifica: nombra la complejidad, luego la atraviesa |

La frecuencia relativa en el corpus es la proporción en el texto generado. Si los verbos de obligación aparecen en el ~30% de las cláusulas del corpus, el texto generado tiende a esa densidad.

#### 2.4. Tensiones productivas (§ Ausencias + § Emergencias)

Las ausencias estructurales del corpus son el **material de las grietas**: el texto puede abrirlas involuntariamente, igual que las editoriales las abren. Son la sombra del texto — lo que el texto no puede decir pero que aparece en su contorno.

Las emergencias (lo que el corpus descubrió sin resolver) son el **material de la novedad**: el texto puede continuar esas preguntas abiertas, tensionarlas, llevarlas un paso más lejos — sin resolverlas (eso violaría la posición de la corriente).

**No resolver las tensiones.** La corriente `restitutiva` abre grietas (E.07 en arte: arte ≠ propaganda) y las cierra (arte = aliado). El texto generado puede reproducir esa operación: abrir y cerrar. O puede quedarse en el umbral. Pero no puede resolver lo que la corriente no resuelve — eso sería hablar *sobre* la corriente, no *desde* ella.

#### 2.5. Registro activo

El corpus puede tener múltiples registros (institucional, generacional, estético, imperialista en `restitutiva`). El texto generado elige uno o lo mezcla. Si el usuario da un tema, el tema sugiere el registro. Si no hay tema, el generador elige el registro más productivo para el momento.

---

## Aplicación al formato de salida

Esta skill es **agnóstica respecto al formato**. Define el protocolo de extracción de voz, no el formato del texto generado. El formato lo define el mod:

- **Poema en verso corto**: métricamente urgente, pausas que pesan
- **Prosa densa**: taxonomía como sintaxis, mecanismos como párrafos
- **Manifiesto**: obligación como estructura, demarcación como título
- **Pitch**: firma de voz subsumida bajo lenguaje de interface (la tecnología desaparece bajo la voz)

El mod que implementa esta skill especifica el formato y el perfil de lector. La skill solo garantiza que, cualquiera que sea el formato, la voz sea recognosciblemente del corpus.

---

## Tabla de metadatos (para el cristalizador)

Al implementar esta skill en un mod, documentar:

```
| Campo | Valor |
|---|---|
| Corpus fuente | ruta/corpus.md |
| Nick activo | [string] |
| Marcadores usados | [lista de los 6 marcadores del nick] |
| Vocabulario clave estable | [palabras del corpus ×3+] |
| Tensiones activas | [ausencias/emergencias que el texto puede activar] |
| Formato de salida | [definido por el mod] |
| Perfil de lector | [definido por el mod] |
```

---

## Relación con el principio Bartleby

La posición Bartleby (potencia de no-actuar) es simultáneamente:
- El **objeto** del análisis (ausencia estructural ×4 en `restitutiva`)
- La **posición** desde la que se analiza (BARTLEBY como proyecto)
- Una **sombra generativa** para el texto de voz (el texto puede activar esa grieta sin resolverla)

En la cristalización, la posición Bartleby aparece como: lo que el texto generado sabe que no puede decir — y cuya presencia ausente le da profundidad.
