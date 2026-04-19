---
description: "Protocolo transversal de sala: disco > chat, formato de checkpoints y entrega obligatoria. Aplica a todos los prompts y carpetas de sala."
applyTo: ".github/prompts/sala-*.prompt.md,**/sala/**"
---

# Protocolo transversal de sala

> Estas reglas aplican a **todo agente y a Aleph** dentro de la sala de coordinación.
> Los prompts de sala (`/sala-entrar`, `/sala-seguir`, `/sala-reconectar`, `/sala-aleph`, `/sala-aprobar`, `/sala-revisar`, `/sala-salir`, `/sala-archivar`) las heredan automáticamente.

## Variable de ruta

- `{{SALA_DIR}}` — carpeta raíz de la sala de coordinación del workspace o mod activo.

---

## 1. Disco primero, chat después

**Si Aleph no puede verlo en tu carpeta, no existe.**

- El **chat** es para notificaciones breves: "he terminado", "checkpoint", "tengo un bloqueo". Máximo 3-5 líneas por mensaje operativo.
- El **contenido del trabajo** — informes, validaciones, análisis, borradores, candidatos — va siempre a un fichero en tu carpeta temporal (`{{SALA_DIR}}/agente-{alias}/`).
- Aleph está en otra ventana. No puede leer tu chat. Solo puede leer disco.
- Lo mismo aplica a Aleph: toda decisión que afecte a un agente se escribe en disco (tablero + `estado.md`) **antes** de responder en chat.

**Test de chat:** antes de enviar un mensaje largo, pregúntate: "¿esto es contenido de trabajo o notificación?" Si es contenido → fichero en carpeta. Si es notificación → chat breve.

**Test de ruta (OBLIGATORIO antes de cada escritura):** antes de crear o editar un fichero, pregúntate: "¿la ruta empieza por `{{SALA_DIR}}/agente-{mi-alias}/`?" Si no → **no escribas ahí**. Deja el artefacto en tu carpeta y documenta la ruta de destino en ENTREGA para que Aleph lo copie. Esto incluye `mod/`, `corpus/`, `.github/`, carpetas de dossier, salidas finales del proyecto y cualquier otra ubicación fuera de `{{SALA_DIR}}`. **Una entrega con escritura fuera de carpeta se devuelve automáticamente, incluso si el artefacto es correcto.**

---

## 2. Formato de checkpoint (agentes)

Después de cada subtarea o artefacto:

**En disco:**
- Actualiza `estado.md` (log + sección Handoff Aleph).
- Si has producido un borrador, informe o análisis parcial, déjalo como fichero en tu carpeta.

**En chat** (máximo 3-5 líneas):
```
[TASK-ID] checkpoint: he completado [qué].
Fichero: sala/agente-{alias}/[nombre si aplica]
Siguiente paso: [qué voy a hacer ahora].
¿Sigo o paro?
```

---

## 3. Entrega — sin excepciones por tipo de tarea

Toda tarea produce una **ENTREGA en disco**, sin importar su tipo:

| Tipo de tarea | Qué dejas en tu carpeta |
|---------------|------------------------|
| Código / agente / instructions | El fichero candidato + `ENTREGA_{TASK-ID}.md` |
| Validación / auditoría | El informe como fichero + `ENTREGA_{TASK-ID}.md` |
| Análisis / investigación | El documento como fichero + `ENTREGA_{TASK-ID}.md` |

El `ENTREGA_{TASK-ID}.md` contiene:
- Resumen del resultado (3-5 líneas)
- Rutas de ficheros producidos en la carpeta
- Pasos que Aleph debe ejecutar (copiar, cerrar, o solo revisar)

**No hay tareas que "solo se documentan en el chat".** Si produjiste trabajo, ese trabajo es un fichero.

---

## 4. Quién propone, quién aprueba

- **Agentes proponen** qué tarea tomar (leen tablero, evalúan deps y capacidades, dejan propuesta en `estado.md`).
- **Aleph aprueba o redirige** (nunca asigna de oficio, nunca ofrece "¿reasigno?").
- Si Aleph tiene una sugerencia estratégica, la deja en la sección "Tracks recomendados" del tablero. El agente la lee como input, no como orden.

### 4.1 Aprobación atómica — regla obligatoria para Aleph

**Aprobar una task = escribir en `estado.md` del agente + actualizar `{{SALA_DIR}}/tablero.md` en la misma acción. No existe aprobación a medias.**

Pasos mínimos al aprobar una propuesta:
1. Escribir línea `ALEPH: [TASK-ID] aprobada. Adelante.` en `estado.md` del agente.
2. Actualizar la fila del agente en `{{SALA_DIR}}/tablero.md`: `libre` → `en-curso:{alias}`.
3. Actualizar resumen (libres--, en-curso++).
4. Actualizar cabecera de `estado.md`: `Task: [TASK-ID]`, `Estado: en-curso`.

Si se aprueban varias tasks en la misma acción, aplica todos los cambios en **una sola operación de edición**. Una aprobación que no sincroniza el tablero es **incompleta** y genera inconsistencias que bloquean a los agentes.

### 4.2 Propuesta en bloque

Un agente puede proponer **varias tasks a la vez** cuando:

1. Las tasks son pequeñas (cambio de una línea, validación sin edición, marca de estado).
2. Son del mismo track o tienen dependencias secuenciales resueltas.
3. El agente estima que puede entregarlas todas en una sola sesión.

**Formato de propuesta en bloque** (en `estado.md`, sección Handoff Aleph):

```
- Siguiente paso recomendado: Propongo bloque [{TASK-A}, {TASK-B}, {TASK-C}].
  Motivo: son tareas de una línea / validación rápida / dependencia secuencial resuelta.
  Entrega: un solo ENTREGA con los 3 resultados.
```

**Aleph puede:**
- Aprobar el bloque entero → una sola aprobación atómica con todas las tasks.
- Aprobar parcial → solo las que considere agrupables.
- Redirigir → reasignar alguna task del bloque a otro agente.

**Entrega de bloque:** un solo `ENTREGA_{TASK-A}+{TASK-B}+{TASK-C}.md` con sección por task. Aleph cierra todas en una sola acción atómica (§5.1 aplica a cada task del bloque).

**Anti-patrón:** no agrupar tasks complejas (refactor, creación de agente, validación end-to-end) solo para ir rápido. El bloque es para tasks que individualmente generarían más overhead operativo que trabajo real.

---

## 5. Limpieza post-cierre (Aleph)

Cuando Aleph cierra una tarea:
1. Copia artefactos al destino final.
2. Borra entregas y borradores de la carpeta temporal del agente.
3. Mantiene `estado.md` con log histórico (nunca se borra).
4. Actualiza cabecera de `estado.md`: `Task: —`, `Estado: disponible`.

El agente decidirá si toma otra tarea cuando entre con `/sala-entrar` o `/sala-seguir`. Aleph no le ofrece la siguiente.

### 5.1 Cierre atómico — regla obligatoria para Aleph

**Cerrar una task = actualizar `{{SALA_DIR}}/tablero.md` + `estado.md` del agente en la misma acción. No existe cierre a medias.**

Pasos mínimos al cerrar una entrega aprobada:
1. Fila del track en `{{SALA_DIR}}/tablero.md`: `entregada:{alias}` → `cerrada:{alias}` (o `cerrada`).
2. Añadir fila en la tabla de cerradas de `{{SALA_DIR}}/tablero.md`.
3. Actualizar resumen de `{{SALA_DIR}}/tablero.md` (cerradas++, en-curso--).
4. Actualizar cabecera de `estado.md`: `Task: —`, `Estado: disponible`.
5. Añadir línea de cierre en log de `estado.md`.

Si se cierran varias tasks en la misma acción, aplica todos los cambios en **una sola operación de edición**. Un cierre que no sincroniza **las tres ubicaciones del tablero** (fila de track, tabla de cerradas, resumen) es **incompleto** y genera fantasmas que confunden a los agentes.

---

## 6. Cierre de sprint y archivado (Aleph)

Cuando **todas las tasks del tablero están cerradas** (o `no-aplica`), el sprint ha terminado. Antes de inicializar una nueva sala:

### 6.1 Precondición

- El resumen del tablero muestra 0 libres, 0 en-curso.
- Todos los agentes tienen `Estado: disponible` en su `estado.md`.
- Los artefactos de cada task ya están copiados a su destino final (§5 cumplido).

### 6.2 Archivado

Aleph ejecuta `/sala-archivar` para:

1. **Verificar** que el sprint está realmente cerrado (precondición §6.1).
2. **Mover** la carpeta de sala completa (`{{SALA_DIR}}/`) a archivo: `{{SALA_DIR}}/archivo/sprint-{nombre}/`.
3. **Conservar** tablero + estados como registro histórico (read-only).
4. **Registrar** el backlog post-sprint que no se ejecutó en este ciclo.

### 6.3 Inicialización del siguiente sprint

Tras archivar, Aleph puede crear una nueva sala:

1. Crear `{{SALA_DIR}}/tablero.md` nuevo con los tracks del siguiente lote.
2. Crear carpetas `agente-{alias}/estado.md` vacías para cada agente que participará.
3. Los dossiers del nuevo lote viven en sus propias carpetas de cristalización.

### 6.4 Relación con dossiers

- Un dossier **cerrado** (todas sus tasks cerradas) es candidato a archivarse junto con la sala.
- Un dossier **parcial** (tasks pendientes transferidas al nuevo sprint) se mantiene activo.
- Los dossiers no se borran: se mueven al archivo o se reutilizan.

**Regla:** la sala es efímera (un sprint). Los dossiers son persistentes (sobreviven a la sala que los ejecutó).