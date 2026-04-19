---
description: "Protocolo transversal de sala: disco > chat, formato de checkpoints, entrega obligatoria. Aplica a todos los prompts y carpetas de sala."
applyTo: "mod/prompts/sala-*.prompt.md,DRAFTS2/sala/**"
---

# Protocolo transversal de sala

> Estas reglas aplican a **todo agente y a Aleph** dentro de la sala de coordinación.
> Los prompts de sala (`/sala-entrar`, `/sala-seguir`, `/sala-reconectar`, `/sala-aleph`, `/sala-aprobar`) las heredan automáticamente.

---

## 1. Disco primero, chat después

**Si Aleph no puede verlo en tu carpeta, no existe.**

- El **chat** es para notificaciones breves: "he terminado", "checkpoint", "tengo un bloqueo". Máximo 3-5 líneas por mensaje operativo.
- El **contenido del trabajo** — informes, validaciones, análisis, borradores, candidatos — va siempre a un fichero en tu carpeta temporal (`DRAFTS2/sala/agente-{alias}/`).
- Aleph está en otra ventana. No puede leer tu chat. Solo puede leer disco.
- Lo mismo aplica a Aleph: toda decisión que afecte a un agente se escribe en disco (tablero + `estado.md`) **antes** de responder en chat.

**Test de chat:** antes de enviar un mensaje largo, pregúntate: "¿esto es contenido de trabajo o notificación?" Si es contenido → fichero en carpeta. Si es notificación → chat breve.

**Test de ruta (OBLIGATORIO antes de cada escritura):** antes de crear o editar un fichero, pregúntate: "¿la ruta empieza por `DRAFTS2/sala/agente-{mi-alias}/`?" Si no → **no escribas ahí**. Deja el artefacto en tu carpeta y documenta la ruta de destino en ENTREGA para que Aleph lo copie. Esto incluye `DRAFTS2/grafo/`, `DRAFTS2/universo/`, `mod/`, `corpus/`, dossiers, y cualquier otra ubicación fuera de tu carpeta. **Una entrega con escritura fuera de carpeta se devuelve automáticamente, incluso si el artefacto es correcto.**

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

**Aprobar una task = escribir en `estado.md` del agente + actualizar `tablero.md` en la misma acción. No existe aprobación a medias.**

Pasos mínimos al aprobar una propuesta:
1. Escribir línea `ALEPH: [TASK-ID] aprobada. Adelante.` en `estado.md` del agente.
2. Actualizar la fila del agente en `tablero.md`: `libre` → `en-curso:{alias}`.
3. Actualizar resumen (libres--, en-curso++).
4. Actualizar cabecera de `estado.md`: `Task: [TASK-ID]`, `Estado: en-curso`.

Si se aprueban varias tasks en la misma acción, usar `multi_replace_string_in_file` para aplicar todos los cambios en una sola llamada. Una aprobación que no sincroniza el tablero es **incompleta** y genera inconsistencias que bloquean a los agentes.

---

## 5. Limpieza post-cierre (Aleph)

Cuando Aleph cierra una tarea:
1. Copia artefactos al destino final.
2. Borra entregas y borradores de la carpeta temporal del agente.
3. Mantiene `estado.md` con log histórico (nunca se borra).
4. Actualiza cabecera de `estado.md`: `Task: —`, `Estado: disponible`.

El agente decidirá si toma otra tarea cuando entre con `/sala-entrar` o `/sala-seguir`. Aleph no le ofrece la siguiente.

### 5.1 Cierre atómico — regla obligatoria para Aleph

**Cerrar una task = actualizar `tablero.md` + `estado.md` del agente en la misma acción. No existe cierre a medias.**

Pasos mínimos al cerrar una entrega aprobada:
1. Fila del track en `tablero.md`: `entregada:{alias}` → `cerrada:{alias}` (o `cerrada`).
2. Añadir fila en la tabla de cerradas de `tablero.md`.
3. Actualizar resumen de `tablero.md` (cerradas++, en-curso--).
4. Actualizar cabecera de `estado.md`: `Task: —`, `Estado: disponible`.
5. Añadir línea de cierre en log de `estado.md`.

Si se cierran varias tasks en la misma acción, usar `multi_replace_string_in_file` para aplicar todos los cambios en una sola llamada. Un cierre que no sincroniza **las tres ubicaciones del tablero** (fila de track, tabla de cerradas, resumen) es **incompleto** y genera fantasmas que confunden a los agentes.
