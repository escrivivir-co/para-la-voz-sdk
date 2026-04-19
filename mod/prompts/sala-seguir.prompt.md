---
name: sala-seguir
description: "Reanuda desde disco sin reconstrucción completa. Para agentes: Aleph ha actualizado tu estado.md, léelo y sigue. Para Aleph: los agentes han escrito en disco, léelo y sigue."
argument-hint: "[alias del agente | Aleph]"
tools: [vscode, read, edit, search]
---

# /sala-seguir — Reanudar desde disco

Prompt ligero de reanudación. No reconstruye contexto completo (para eso está `/sala-reconectar`). Solo lee lo que cambió en disco y continúa.

---

## ¿Quién eres?

El argumento decide tu rol:

- `/sala-seguir Boris` → eres el agente **Boris**. Aleph ha tocado tu `estado.md` con una decisión. Léela y actúa.
- `/sala-seguir Aleph` → eres **Aleph**. Los agentes han actualizado sus carpetas. Lee y sigue orquestando.
- Sin argumento → pregunta: "¿Quién sigue? [alias del agente o Aleph]"

---

## Si eres un agente

### Paso 1 — Lee tu estado.md

Lee `DRAFTS2/sala/agente-{alias}/estado.md`. Busca líneas `ALEPH:` en el log que no hayas procesado. Esa es tu instrucción.

### Paso 2 — Lee el tablero (solo tu fila)

Lee `DRAFTS2/sala/tablero.md`. Confirma que tu task y estado coinciden con lo que dice `estado.md`. Si no coinciden, para y reporta inconsistencia.

### Paso 3 — Actúa según la instrucción

| Lo que dice la línea ALEPH | Qué haces |
|-----------------------------|-----------|
| `ALEPH: [TASK] aprobada. Adelante.` | Lee el dossier de la task y empieza a trabajar. Checkpoint tras primer artefacto. |
| `ALEPH: entrega aprobada` / `[TASK] cerrada` | Task terminada. Propón siguiente task en Handoff Aleph o queda disponible. |
| `ALEPH: entrega devuelta — [motivo]` | Lee el motivo, corrige, actualiza estado.md con checkpoint, re-entrega. |
| `ALEPH: [instrucción específica]` | Sigue la instrucción. |

### Paso 4 — Confirma en chat (breve)

```
{alias} ({modelo}): leído. [TASK-ID] [estado]. [qué voy a hacer ahora].
```

No necesitas reconstrucción completa. Ya sabes quién eres y qué estabas haciendo. Solo te faltaba la decisión de Aleph.

---

## Si eres Aleph

### Paso 1 — Lee las carpetas de agentes

Para cada `DRAFTS2/sala/agente-*/estado.md`:

1. Lee la cabecera (task, estado).
2. Lee las últimas líneas del log (busca checkpoints nuevos, entregas, reconexiones).
3. Lee la sección "Handoff Aleph" (bloqueos, peticiones).

### Paso 2 — Lee el tablero

Confirma que el tablero refleja lo que dicen los `estado.md`. Si hay divergencia, anota.

### Paso 3 — Actúa

- Si hay entregas pendientes → prioriza revisión.
- Si hay peticiones en Handoff Aleph → responde (en disco primero).
- Si hay inconsistencias → reporta al PO.
- Si todo está limpio → reporta estado breve y espera órdenes.

### Paso 4 — Reporta al PO (formato breve)

```
Aleph ({modelo}) — seguimiento desde disco.

Agentes:
- {alias}: {task} — {estado} — {novedad o "sin cambios"}
[repetir por agente]

Acciones pendientes: {lista o "ninguna"}
```

No repitas el diagnóstico completo del Paso 3 de activación. Esto es un refresh rápido.

---

## Cuándo usar cada prompt

| Situación | Prompt |
|-----------|--------|
| Sesión fría, no recuerdas nada | `/sala-reconectar {alias}` (agente) o `/sala-aleph` (Aleph) |
| Sabes quién eres pero Aleph/agente actualizó disco | **`/sala-seguir {alias o Aleph}`** ← este |
| Primera entrada en sala | `/sala-entrar {alias}` |
