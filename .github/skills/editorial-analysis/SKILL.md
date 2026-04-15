---
name: editorial-analysis
description: Skill portable para análisis Bartleby de textos editoriales. Extrae herencia de tradición (linaje, corriente), taxonomía funcional, mecanismos retóricos heredados, emergencias sobre la tradición, y la vista desde el hueco (posiciones ausentes). No juzga, no valora, no debate. Se activa cuando se pide analizar, radiografiar o cartografiar una editorial, manifiesto, artículo de posicionamiento político-intelectual o texto de revista.
---

# Skill: editorial-analysis — Protocolo de análisis Bartleby

Esta skill implementa el análisis Bartleby de textos editoriales: radiografía de la arquitectura sin juicio de valor. Se puede usar en cualquier agente compatible con agent skills.

## Cuándo activar esta skill

- Cuando el usuario pide "analizar" una editorial o texto de posicionamiento
- Cuando el usuario pide "radiografiar la corriente" o "mapa de herencia"
- Cuando el usuario pide "qué hereda y qué aporta este texto"
- Cuando el usuario quiere "arquitectura sin juicio" de un texto

## La posición Bartleby

El análisis opera desde la potencia de no-actuar:
- **No juzga** si el texto es correcto o incorrecto, útil o peligroso
- **No debate** con el texto ni desde el texto
- **No aplica categorías externas** a la tradición del texto
- **Ve la coreografía** porque no participa en la danza
- **Cuantifica** cuando puede: contadores de apariciones, nodos de linaje, frecuencias de mecanismos

La posición Bartleby no es neutralidad. Es una posición específica: la del habitante del hueco, el punto equidistante que revela las condiciones de posibilidad del sistema desde su exterior.

## Protocolo — 5 secciones

### I. La corriente: herencia y linaje

**Linaje primario** — tabla con columnas:
| Eslabón | Texto/obra citada | Función en el texto |
|---------|-------------------|---------------------|
| [autor] | [obra] | [qué autoriza: fundamento científico / arquitecto estratégico / sistematizador / epistemólogo / ...] |

**Linaje por exclusión** — lista de quién/qué descarta el texto explícitamente. Las exclusiones definen la corriente tanto como las inclusiones.

**Corriente resultante** — un párrafo que nombra la tradición. Si no tiene nombre canónico, propone un nick descriptivo provisional entre corchetes: por ejemplo `[restitutiva]`, `[heterodoxa revisionista]`, `[autonomista postmarxista]`.

---

### II. La taxonomía que el texto maneja

Extrae el sistema clasificatorio completo:

**Árbol funcional** (ASCII cuando es posible):
```
CATEGORÍA-RAÍZ
├── subcategoría A ── verbo: [qué hace]
├── subcategoría B ── verbo: [qué hace]
│   └── sub-subcategoría C ── verbo: [qué hace]
```

**Tabla de categorías**:
| Categoría | Definición en el texto | Verbo asociado | Nodo obligatorio? |
|-----------|------------------------|----------------|-------------------|

**Vista desde el hueco**: ¿qué posición no existe en esta taxonomía? ¿Qué clase o modo de ser el texto no puede contemplar?

---

### III. Los mecanismos retóricos heredados

Identifica y nombra los procedimientos discursivos con su frecuencia (`[×N]`):

| Mecanismo | Descripción | Ejemplos en el texto | Frecuencia |
|-----------|-------------|----------------------|------------|
| Autorización por cita canónica | El argumento descuelga de autoridad, no construye desde cero | [citas] | ×N |
| Demarcación bilateral | *ni...ni...* — se ubica entre dos errores simétricos | [ejemplos] | ×N |
| Autocita como ecosistema | Referencias al propio corpus de la publicación como validación | [referencias] | ×N |
| Humildad performativa | Declaración de límites como gesto de lucidez | [ejemplos] | ×N |
| [otros detectados] | ... | ... | ×N |

---

### IV. Lo emergente — qué aporta sobre la tradición

Sólo aquí Bartleby mira hacia adelante (sin juzgar si es "bueno"):

1. **Diagnósticos que la tradición no tenía** — problemas que el texto nombra aunque la herencia no los resolvía
2. **Operaciones que desplazan la herencia** — aunque sea mínimamente, qué hace el texto que la tradición no contemplaba
3. **Ausencias estructurales** — qué no puede ver el texto por ser constitutivamente lo que es (sin que el texto lo sepa)

---

### V. Vista desde el hueco

La perspectiva Bartleby pura — qué revela la posición de no-participación:

- ¿Qué posibilidad el texto no puede contemplar?
- Si el sistema de obligaciones del texto (verbos: "debe", "necesario", "hay que", "tiene que") fuera exhaustivo, ¿qué queda fuera?
- ¿Cuál sería la posición de quien pudiera ver el sistema entero desde fuera?

---

## Tablas de metadatos (para el archivero)

Al final de cada análisis, incluir siempre:

```
| Campo | Valor |
|---|---|
| Fecha editorial | YYYY-MM-DD |
| Linaje primario (nodos) | N |
| Linaje por exclusión (nodos) | N |
| Categorías taxonómicas | N |
| Mecanismos retóricos | N |
| Frecuencia total verbos obligación | N |
| Emergencias identificadas | N |
| Ausencias estructurales | N |
| Nick corriente | [string] |
| Posición en corpus | primera | confirma | amplía | discrepa | nueva subcorriente |
```

---

## Vocabulario y ejemplo canónico

El vocabulario taxonómico vive en `corpus/corpus.md` del mod activo. Si el corpus está vacío, el primer análisis establece el baseline.

Los ejemplos canónicos y la taxonomía base específica del lore viven en `mod/skills/editorial-analysis/` — no en este SDK. El mod los gestiona.
