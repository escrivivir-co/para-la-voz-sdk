---
name: dossier
description: "Crea, continúa o lista dossiers de cristalización. Los dossiers son el diseño de features; la sala es su ejecución."
argument-hint: "[crear {nombre} | continuar {nombre} | listar]"
tools: [vscode, read, edit, search]
---

# /dossier — Gestión de dossiers de cristalización

Los dossiers son carpetas autocontenidas de diseño de features. Viven en `sala/dossiers/{nombre}/`. El protocolo completo está en `mod/skills/cristalizacion-feature/SKILL.md` — léelo antes de actuar.

> **Quién crea dossiers:** el PO y/o el scrum master, asistidos por este prompt.
> **Quién los ejecuta:** los agentes de la sala, coordinados por Aleph.

---

## Operación: crear

**Argumento:** `/dossier crear {nombre-kebab}`

### Paso 1 — Scaffolding

Copia la estructura de `sala/plantilla-dossier/` a `sala/dossiers/{nombre}/`:

```
sala/dossiers/{nombre}/
├── PLAN_{NOMBRE_UPPER}.md
├── BACKLOG_{NOMBRE_UPPER}.md
├── RESPUESTAS_USUARIO_{NOMBRE_UPPER}.md
├── activacion.prompt.md
└── tasks/
    └── TASK-00_CONTEXTO_Y_PERSISTENCIA.md
```

Renombra los ficheros con el `{NOMBRE_UPPER}` (versión UPPER_SNAKE del nombre). Sustituye los placeholders de la plantilla con los datos que el usuario proporcione.

### Paso 2 — Conversación de diseño

Pregunta al usuario lo mínimo para rellenar el PLAN:

1. **¿Qué problema resuelve este feature?** → Sección Contexto
2. **¿Qué anclas existen?** (ficheros, decisiones previas) → Sección Anclas
3. **¿Cuáles son las tasks?** (lista breve: título + entrega esperada) → Seeds para `tasks/`

No hagas más preguntas de las necesarias. Si el usuario ya tiene un brief claro, ve directo.

### Paso 3 — Generar contenido

Con las respuestas:

1. Rellena `PLAN_{NOMBRE_UPPER}.md` con contexto, anclas, restricciones y propuesta.
2. Rellena `BACKLOG_{NOMBRE_UPPER}.md` con la tabla de tracking (tasks XX-00 a XX-NN).
3. Rellena `RESPUESTAS_USUARIO_{NOMBRE_UPPER}.md` con las decisiones del usuario.
4. Crea cada `TASK-NN_{TITULO}.md` en `tasks/` con: estado, dependencias, entrega esperada, "Lee primero", objetivo.
5. Rellena `activacion.prompt.md` con el resumen ejecutivo.

### Paso 4 — Registrar track en tablero

Lee `sala/tablero.md`. Añade una nueva sección `## Track {XX}` con las tasks del dossier, todas en estado `libre` (excepto XX-00 que es `cerrada`). Actualiza la tabla Resumen.

### Paso 5 — Confirmar

```
Dossier creado: sala/dossiers/{nombre}/
- PLAN: {N} secciones
- Tasks: {M} (XX-00 cerrada, XX-01..XX-{M} libres)
- Track registrado en tablero.

Siguiente: /sala-aleph para que Aleph cargue el nuevo track, o /sala-entrar {alias} para que un agente proponga tarea.
```

---

## Operación: continuar

**Argumento:** `/dossier continuar {nombre}`

1. Lee `sala/dossiers/{nombre}/activacion.prompt.md`.
2. Lee `sala/dossiers/{nombre}/BACKLOG_{NOMBRE_UPPER}.md` — identifica tasks pendientes.
3. Presenta al usuario: estado actual, tasks cerradas, tasks pendientes, siguiente paso.
4. Si el usuario quiere modificar el plan o añadir tasks, edita los ficheros correspondientes.

No ejecutes tasks — eso es trabajo de la sala. Aquí solo se revisa y ajusta el diseño.

---

## Operación: listar

**Argumento:** `/dossier listar`

Lista todas las carpetas `sala/dossiers/*/`. Para cada una, lee `activacion.prompt.md` (primera línea) y el BACKLOG (conteo de tasks cerradas/pendientes).

Formato:

```
Dossiers activos:
- cristalizacion-cadena-agentica: 3/7 cerradas — Cadena de 5 agentes especializados
- cristalizacion-grafo-json: 1/7 cerradas — Migración del grafo a JSON
- cristalizacion-pipeline-operativo: 5/5 cerradas ✅ — Pipeline operativo
- finalizacion-lore-plan: 0/8 cerradas — Cerrar LORE_PLAN.md
- future-machine-universo-1: 1/2 cerradas — Future machine para universo 1
```
