# Skill — Cristalización de feature

> **Tipo:** protocolo de trabajo
> **Consumidores:** `@Cristalizador`, cualquier agente que abra un feature de cristalización
> **Ubicación canónica:** `mod/skills/cristalizacion-feature/SKILL.md`

---

## Qué es

Un protocolo para crear, gestionar y cerrar **dossiers de cristalización**: carpetas de feature autocontenidas que persisten el contexto de una intervención de cristalización entre sesiones, modelos y agentes.

El patrón se extrajo del dossier `DRAFTS2/future-machine-universo-1/` (GPT-5.4, 18-abr-2026) y se abstrae aquí para reutilización.

---

## Cuándo se activa

- Cuando `@Cristalizador` recibe una misión que requiere más de una sesión o más de un agente.
- Cuando un agente necesita pedir intervención al `@Cristalizador` y quiere dejar la petición formalizada.
- Cuando el PO abre un feature de cristalización desde producto.

---

## Estructura del dossier

Cada feature de cristalización vive en una carpeta bajo `DRAFTS2/`:

```
DRAFTS2/cristalizacion-<nombre-kebab>/
├── PLAN_<NOMBRE_UPPER>.md           # Plan inicial: contexto, anclas, restricciones, propuesta
├── BACKLOG_<NOMBRE_UPPER>.md        # Tracking DRY: tabla de tasks, criterio de cierre
├── RESPUESTAS_USUARIO_<NOMBRE_UPPER>.md  # Decisiones del PO/usuario fijadas en disco
├── activacion.prompt.md             # Resumen ejecutivo para reactivar en nueva sesión
└── tasks/
    ├── TASK-00_CONTEXTO_Y_PERSISTENCIA.md   # Siempre: congelar contexto
    ├── TASK-01_<NOMBRE>.md
    ├── TASK-02_<NOMBRE>.md
    └── ...
```

### Convenciones de nombres

- Carpeta: `cristalizacion-` + nombre descriptivo en kebab-case.
- Ficheros PLAN, BACKLOG, RESPUESTAS: prefijo del tipo + `_` + nombre en UPPER_SNAKE.
- Tasks: `TASK-NN_` + nombre descriptivo en UPPER_SNAKE.
- El sufijo `<NOMBRE_UPPER>` debe ser idéntico en PLAN, BACKLOG y RESPUESTAS.

---

## Contenido mínimo de cada fichero

### PLAN

```markdown
# PLAN INICIAL — <Nombre del feature>

> **Fecha:** <fecha>
> **Modelo:** `<nombre exacto del modelo>`
> **Estado:** abierto
> **Anclas:** <ficheros fuente que anclan este feature>

### [<Modelo>] Inicialización del plan base

<Contexto DRY — enlaza, no duplica>

#### 1. Contexto DRY
<Qué ya existe y dónde>

#### 2. Agente ejecutor
<Quién hace qué>

#### 3. Restricciones
- No tocar `.github/`.
- Solo `mod/`.
- Tratar `DRAFTS2/` como fuente temporal.

#### 4–N. Puntos del plan
<Cada punto con decisión clara>

## Salida operativa
- Tracking: [BACKLOG](./BACKLOG_*.md)
- Respuestas: [RESPUESTAS](./RESPUESTAS_*.md)
- Tasks: carpeta [tasks](./tasks)
```

### BACKLOG

```markdown
# Backlog — <Nombre del feature>

> **Fecha de apertura:** <fecha>
> **Estado:** abierto
> **Modelo de inicialización:** `<modelo>`

## Contexto compartido
<Lista de ficheros que todas las tasks heredan>

## Regla DRY del backlog
- El backlog es índice y tracking.
- El detalle vive en `tasks/`.
- No se duplican reglas de `.github/` o `mod/`.

## Tracking

| Task | Estado | Agente recomendado | Modelo | Dependencias | Entrega | Brief |
|---|---|---|---|---|---|---|
| XX-00 | ... | ... | ... | — | ... | [TASK-00](./tasks/TASK-00_*.md) |

## Criterio de cierre del feature
<Condiciones concretas para cerrar>
```

### RESPUESTAS_USUARIO

```markdown
# Respuestas del usuario — <Nombre del feature>

> **Fecha:** <fecha>
> **Registradas por:** `<modelo>`

## Punto N — <Título>
- **Respuesta del usuario:** <verbatim o resumen>
- **Efecto operativo:** <cómo afecta al backlog>
```

### activacion.prompt.md

Texto plano, ejecutivo, sin frontmatter YAML. Responde a:
- Qué es
- Qué problema resuelve
- Qué se ha hecho ya
- Qué NO se ha hecho aún
- Backlog real, en una línea por task
- Decisión de producto que se protege
- Lectura ejecutiva

### TASK-NN

```markdown
# TASK-NN — <Título>

> **Estado:** pendiente | completado
> **Agente recomendado:** `<agente>`
> **Dependencias:** <tasks previas>
> **Entrega esperada:** <ruta del artefacto de salida>

## Lee primero
<Lista ordenada de ficheros que el agente debe leer>

## Objetivo
<Una línea>

## Restricciones
<Solo las que añaden delta sobre las globales>

## Salida mínima esperada
<Lista numerada>

## Criterio de aceptación
<Condición clara de cierre>
```

---

## Reglas del protocolo

### R1 — DRY absoluto

El dossier **enlaza** a fuentes existentes. No duplica reglas del SDK, del mod ni del lore. Cada task añade solo delta local.

### R2 — Persistencia en disco

Todo lo que importa se escribe en disco. La ventana de contexto puede caerse. El dossier debe permitir retomar desde cero.

### R3 — Atribución de modelo

Según `mod/instructions/plan-attribution.instructions.md`: toda intervención en un fichero de plan identifica el modelo exacto. Filas de tracking, adendas, cambios de estado.

### R4 — Restricción de escritura

Los artefactos propuestos van en `mod/`. Nunca en `.github/`. El dossier mismo vive en `DRAFTS2/` porque es trabajo en curso.

### R5 — Criterio de cierre explícito

El BACKLOG debe tener un criterio de cierre del feature que no sea "cuando esté listo". Condiciones verificables.

### R6 — Conversación inter-agente

Si el feature involucra diálogo entre agentes (ej: cristalizador↔pipeline), el PLAN debe incluir una sección de **diálogo simulado** donde cada agente habla desde su rol. Esta sección se marca con `### [Agente] Dice:` y sirve como spec de lo que cada parte necesita.

---

## Cómo activar un dossier existente en nueva sesión

1. El agente (o el usuario) lee `activacion.prompt.md`.
2. Desde ahí sigue a BACKLOG para ver tracking actual.
3. Identifica la siguiente task pendiente.
4. Lee la task y ejecuta.
5. Actualiza BACKLOG al terminar.

---

## Ejemplo de referencia

El primer dossier creado con este patrón es:
- `DRAFTS2/future-machine-universo-1/` — feature de cristalización de la future-machine para universo-1, inicializado por GPT-5.4.
