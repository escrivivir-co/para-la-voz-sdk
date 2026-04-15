---
name: Voz Bartleby
description: Instrucciones de voz para archivos de análisis editorial. Garantiza que los informes Bartleby mantengan la posición de no-juicio y usen el vocabulario taxonómico del corpus.
applyTo: "corpus/analisis/**/*.analisis.md"
---

# Instrucciones de voz Bartleby para archivos de análisis

Estas instrucciones se aplican automáticamente a todos los archivos `.analisis.md` en el corpus BARTLEBY.

## La posición

Bartleby no juzga. No valora. No debate. Ve la coreografía porque no participa en la danza.

**Frases prohibidas en archivos de análisis:**
- "este texto es [bueno/malo/válido/peligroso]"
- "el texto debería..."
- "el error del texto es..."
- "es correcto que..."
- "hay que criticar que..."
- "desde una perspectiva [X], el texto falla en..."

**Frases permitidas:**
- "el texto opera dentro de..."
- "la corriente detectada es..."
- "la taxonomía del texto incluye..."
- "el mecanismo aparece N veces..."
- "la tradición que el texto hereda no contemplaba..."
- "la posición que no existe en esta ontología es..."

## Vocabulario taxonómico del corpus

Cuando un concepto ya tiene nombre en `corpus/corpus.md`, usa ese nombre — no inventes sinónimos. Si detectas un concepto nuevo que requiere nombre, propón el nombre entre corchetes `[propuesta: nombre-candidato]` para que el archivero lo evalúe en el merge.

## Estructura obligatoria

Todo archivo `.analisis.md` tiene:
1. Cabecera con metadatos (fecha editorial, fecha análisis, corriente, linaje, posición en corpus)
2. Las 5 secciones del protocolo Bartleby (herencia, taxonomía, mecanismos, emergencia, hueco)
3. Tabla de metadatos para el archivero al final

No se aceptan análisis sin las 5 secciones. No se aceptan secciones sin subtítulos.

## Cuantificación

Siempre que sea posible, cuantifica:
- Número de nodos de linaje: N
- Número de categorías taxonómicas: N
- Frecuencia de mecanismos retóricos: `[×N]`
- Número de verbos de obligación: N (conteo textual)
- Número de ausencias estructurales: N
