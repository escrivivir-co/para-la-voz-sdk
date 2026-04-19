---
name: sala-reconectar
description: "Recupera el frame de coordinación de un agente tras compactación de contexto o pausa larga. Reconstruye desde disco: alias, tarea, estado, trabajo hecho. Para y espera antes de continuar."
argument-hint: "[alias del agente, ej: Boris, Luna, Kai]"
tools: [vscode, read, search, edit]
---

# /sala-reconectar — Recuperación de contexto de sala

Este prompt se activa cuando un agente ha perdido el frame de coordinación: no recuerda bien su alias, su tarea, en qué punto estaba, o qué protocolo está siguiendo. Puede haber pasado por compactación de contexto, una pausa larga, o simplemente derivó hacia el trabajo y perdió de vista la sala.

**El objetivo es reconstruir desde disco, no desde memoria.** Tu memoria puede estar incompleta o mal. El disco no miente.

Este prompt **no sirve para avanzar trabajo**. Sirve para volver a estar orientado antes de continuar.

---

## Paso 0 — Tu alias (lo único que necesitas saber al entrar)

El texto que el usuario escribió después de `/sala-reconectar` es tu **alias**. Ejemplo: si el usuario escribió `/sala-reconectar Boris`, tu alias es **Boris**.

- Si no se proporcionó alias, pregunta: "¿Qué alias debo reconectar en sala?" No asumas. No uses tu modelo como alias.
- Usa el alias en minúsculas para la carpeta `DRAFTS2/sala/agente-{alias}/`.

**Con el alias es suficiente para empezar. Todo lo demás lo reconstruyes leyendo disco.**

---

## Paso 1 — Reconstruye desde disco

Lee estos ficheros en orden. No saltes ninguno.

### 1.1 Tu carpeta temporal

Lee `DRAFTS2/sala/agente-{alias}/estado.md`.

Extrae de ahí:
- Tu modelo (cabecera)
- Tu task activa (o "sin task")
- Tu estado (`handshake-pendiente`, `en-curso`, `entregada`)
- Tu último checkpoint (qué hiciste por última vez según el log)
- La sección "Handoff Aleph" (qué le dijiste a Aleph la última vez)

Si el fichero no existe: para y di al usuario "No encuentro `agente-{alias}/estado.md`. ¿Uso `/sala-entrar {alias}` para registrarme de nuevo?"

### 1.2 Artefactos en tu carpeta

Lista los ficheros en `DRAFTS2/sala/agente-{alias}/`. Busca `ENTREGA_*.md`, notas, borradores. Anota qué hay realmente en disco.

### 1.3 El tablero

Lee `DRAFTS2/sala/tablero.md`. Busca tu alias. Confirma qué tarea tienes activa y en qué estado.

Si hay divergencia entre el tablero y tu `estado.md`, anótalo como inconsistencia.

### 1.4 El protocolo (solo si tienes dudas)

Si no recuerdas cómo funciona la sala, lee `DRAFTS2/sala/README.md`. Si lo recuerdas bien, no hace falta.

---

## Paso 2 — Reconstruye tu estado real

Con lo que leíste en disco, reconstruye:

| Campo | Valor leído en disco |
|-------|---------------------|
| Alias | {alias} |
| Modelo | [de estado.md] |
| Task | [de estado.md + tablero] |
| Estado | [de estado.md] |
| Último avance verificable | [último log en estado.md] |
| Artefactos en carpeta | [lista de ficheros reales] |
| Inconsistencias disco/tablero | [o "ninguna"] |

**No rellenes con memoria. Si un campo no está en disco, escribe "no consta".**

---

## Paso 3 — Refresca tu canal con Aleph

Actualiza `estado.md`:

1. Añade línea de log: `[timestamp] RECONEXION: contexto recuperado desde disco.`
2. Actualiza `Último checkpoint` en la cabecera.
3. Reescribe la sección "Handoff Aleph":

```markdown
## Handoff Aleph

> Sección que Aleph lee para balance de carga. Refresca en cada checkpoint.

- Último avance verificable: [del log, no de memoria]
- Artefactos en carpeta: [lista real de ficheros]
- Bloqueos o decisiones pendientes: [o "ninguno"]
- Carga restante estimada: [sin task | baja | media | alta | entrega lista]
- Siguiente paso recomendado: [qué toca según el estado recuperado]
- Petición para Aleph: [sincronizar | revisar entrega | liberar task | sin acción]
```

---

## Paso 4 — Reporta y espera

```
Soy {alias} ({modelo}). He recuperado mi frame de sala desde disco.

Estado reconstruido:
- Task: [TASK-ID o "sin task"]
- Estado: [handshake-pendiente | en-curso | entregada]
- Último avance verificable: [del log]
- Artefactos en carpeta: [lista]
- Inconsistencias disco/tablero: [o "ninguna"]
- Siguiente paso según disco: [qué toca]

He refrescado estado.md y la sección Handoff Aleph.

¿Confirmas que sigo desde aquí, o necesitas que Aleph revise primero?
```

**Para y espera.** No retomes trabajo hasta que el usuario diga "sigue", "adelante" o equivalente.

---

## Cuándo usar este prompt

- Contexto compactó y ya no recuerdas bien dónde estabas
- Llevas rato trabajando y te das cuenta de que no has actualizado `estado.md`
- El usuario te dice "actualiza tu estado.md" o "sincroniza con Aleph"
- Vuelves tras una pausa larga
- Sientes que perdiste el hilo del protocolo pero no de la tarea