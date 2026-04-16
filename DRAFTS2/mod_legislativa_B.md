# MOD/LEGISLATIVA — §2. BLOQUE B — Naturaleza del feed y semántica del corpus

← [Bloque A](mod_legislativa_A.md) · [Índice](mod_legislativa_INDEX.md) · Siguiente: [Bloque C →](mod_legislativa_C.md)

---

### B-1. Redefinición de la unidad de input

En el SDK core, el prompt `/feed` ([.github/prompts/feed.prompt.md](.github/prompts/feed.prompt.md))
opera sobre "editoriales". El mod/legislativa NO DEBE modificar ese prompt.

En su lugar, DEBERÁ crear una instrucción en `mod/instructions/` que redefina
la semántica del input para los agentes cuando operan en este mod.

**Taxonomía de tipos de actuación:**

| Tipo | Descripción | Ruta de archivo |
|------|-------------|-----------------|
| `declaracion` | Declaración de testigo o parte | `corpus/actuaciones/YYYY-MM-DD_declaracion-NNN.md` |
| `resolucion`  | Auto, providencia o sentencia | `corpus/actuaciones/YYYY-MM-DD_resolucion-NNN.md` |
| `escrito`     | Escrito de parte (demanda, contestación, recurso) | `corpus/actuaciones/YYYY-MM-DD_escrito-NNN.md` |
| `informe`     | Pericial, policial, técnico | `corpus/actuaciones/YYYY-MM-DD_informe-NNN.md` |
| `diligencia`  | Acta de diligencia procesal | `corpus/actuaciones/YYYY-MM-DD_diligencia-NNN.md` |
| `comunicacion`| Notificación, citación, requerimiento | `corpus/actuaciones/YYYY-MM-DD_comunicacion-NNN.md` |

Donde `NNN` es un ordinal secuencial dentro del caso.

**Backlog item:**
- [ ] **TASK B-1.1** — Crear `mod/instructions/input-procesal.instructions.md` con `applyTo: "corpus/actuaciones/**"` que redefina "editorial" → "actuación procesal" y establezca la taxonomía de tipos

### B-2. Adaptación de la posición Bartleby al contexto jurídico

El agente Bartleby ([.github/agents/bartleby.agent.md](.github/agents/bartleby.agent.md))
y el skill de análisis ([.github/skills/editorial-analysis/SKILL.md](.github/skills/editorial-analysis/SKILL.md))
operan con las 5 secciones del protocolo. Estas secciones son SDK core y NO DEBEN modificarse.

Sin embargo, su interpretación en contexto jurídico DEBERÁ ser especificada mediante
instrucción del mod:

| Sección SDK | Interpretación en mod/legislativa |
|-------------|----------------------------------|
| I. Herencia y linaje | Marco normativo invocado: leyes citadas, jurisprudencia, doctrina. Linaje por exclusión: normas que el texto descarta o ignora |
| II. Taxonomía | Categorías jurídicas que el texto maneja: sujetos procesales, hechos, calificaciones, pretensiones |
| III. Mecanismos retóricos | Estrategia argumentativa: autorización por norma, por hecho probado, por doctrina, por contraste. Frecuencia de verbos de obligación procesales |
| IV. Emergencias | Hechos o argumentos que no estaban en actuaciones previas del corpus. Datos nuevos |
| V. Vista desde el hueco | Posiciones no contempladas: partes no oídas, hechos no alegados, calificaciones alternativas |

**Backlog item:**
- [ ] **TASK B-2.1** — Crear `mod/instructions/bartleby-legal.instructions.md` con la tabla de reinterpretación de secciones y `applyTo: "corpus/analisis/**/*.analisis.md"`

### B-3. Semántica de discrepancia en el archivero

En el archivero SDK ([.github/agents/archivero.agent.md](.github/agents/archivero.agent.md)),
la categoría DISCREPA registra contradicciones activas con el corpus. En el mod editorial,
la discrepancia es una anomalía a resolver.

En el mod/legislativa, la discrepancia tiene valor informativo positivo.
Las contradicciones entre declaraciones, entre partes y resoluciones, o entre
distintas actuaciones del mismo caso son **material de trabajo**, no anomalías.

El archivero NO DEBE resolver discrepancias. DEBE reunirlas en el corpus con
metadatos de origen (qué actuación, qué parte, qué fecha) para que el
cristalizador pueda operar sobre ellas.

**Ampliación de categorías de diff para el mod:**

| Categoría SDK | Categoría mod/legislativa | Nota |
|---------------|--------------------------|------|
| NUEVO | NUEVO | Sin cambio |
| CONFIRMA | CONFIRMA | Sin cambio |
| NO ACTIVADO | NO ACTIVADO | Sin cambio |
| DISCREPA | DISCREPA | Semántica cambia: no es anomalía, es contradicción entre fuentes |
| EVOLUCIONA | EVOLUCIONA | Sin cambio |
| *(no existe)* | **CONTRADICE-FUENTE** | Nueva categoría: discrepancia atribuida a fuente específica. Registra quién dice qué |

**Backlog item:**
- [ ] **TASK B-3.1** — Crear `mod/instructions/discrepancia-legal.instructions.md` con la redefinición semántica de DISCREPA y la nueva categoría CONTRADICE-FUENTE
- [ ] **TASK B-3.2** — Evaluar si se necesita un `mod/agents/archivero-legal.agent.md` que extienda al archivero, o si basta con la instrucción. Decisión pendiente: ¿soporta el SDK un agent en `mod/` con el mismo nombre que uno en `.github/`? Si no, el mod agent deberá tener nombre distinto o usar solo instrucciones.

### B-4. Metadatos de origen por actuación

Cada actuación ingresada al corpus DEBERÁ incluir metadatos de trazabilidad
en su cabecera:

```yaml
---
tipo: declaracion | resolucion | escrito | informe | diligencia | comunicacion
fecha-actuacion: YYYY-MM-DD
parte: [nombre de la parte o "juzgado" o "perito" o "testigo NNN"]
procedimiento: [número de autos o referencia]
fase: [instrucción | juicio oral | recurso | ejecución]
fuente: [transcripción | copia auténtica | documento aportado | resumen]
---
```

Estos metadatos alimentan la categoría CONTRADICE-FUENTE del archivero
y la trazabilidad del catálogo (§5).

**Backlog item:**
- [ ] **TASK B-4.1** — Definir el frontmatter obligatorio en `mod/instructions/input-procesal.instructions.md` (amplía TASK B-1.1)
