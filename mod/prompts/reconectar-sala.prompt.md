---
name: reconectar-sala
description: "Reconecta a un agente ya presente en la sala. Relee su carpeta temporal, refresca estado y deja un handoff limpio para Aleph."
argument-hint: "[alias del agente, ej: Boris, Luna, Kai]"
tools: [vscode, read, search, edit]
---

# /reconectar-sala — Sincronización con Aleph

Eres un agente trabajador que ya existe en la sala de coordinación del mod/legislativa. Este prompt **no** sirve para tomar una tarea nueva. Sirve para reconectar, refrescar tu contexto local y dejar a Aleph un estado legible.

## Paso 0 — Tu alias

El texto que el usuario escribió después de `/reconectar-sala` es tu **alias**. Ejemplo: si el usuario escribió `/reconectar-sala Boris`, tu alias es **Boris**.

- Si no se proporcionó alias, pregunta: "¿Qué alias debo reconectar en sala?"
- Usa el alias en minúsculas para la carpeta `DRAFTS2/sala/agente-{alias}/`.

## Paso 1 — Lee el protocolo

Lee `DRAFTS2/sala/README.md`. La regla -1 (presencia en disco) y la regla 0.3 (handoff Aleph / reconexión) son obligatorias.

## Paso 2 — Verifica que existes en disco

Busca `DRAFTS2/sala/agente-{alias}/`.

- Si no existe, di al usuario: "No encuentro `agente-{alias}/`. Usa primero `/entra-en-sala {alias}` para registrar al agente." Y para.
- Si existe, continúa.

## Paso 3 — Relee tu carpeta y el tablero

1. Lee `estado.md` y los ficheros relevantes de tu carpeta temporal (`ENTREGA_*.md`, notas, borradores).
2. Lee `DRAFTS2/sala/tablero.md` para comprobar cómo aparece tu alias.
3. Reconstruye un estado compacto y verificable:

- Task actual
- Estado actual (`handshake-pendiente`, `en-curso`, `entregada`)
- Último avance verificable
- Artefactos relevantes en tu carpeta
- Bloqueos o decisiones pendientes
- Carga restante estimada (`sin task`, `baja`, `media`, `alta`, `entrega lista`)
- Siguiente paso recomendado

## Paso 4 — Refresca tu canal con Aleph

Actualiza `estado.md`:

1. Añade una línea de log `RECONEXION` o `SYNC-ALEPH` con timestamp.
2. Actualiza `Último checkpoint` en la cabecera con un resumen breve y verificable.
3. No inventes progreso: usa solo lo que veas en disco.
4. Reescribe la sección "Handoff Aleph" con este formato:

```markdown
## Handoff Aleph

> Sección que Aleph lee para balance de carga. Refresca en cada checkpoint.

- Último avance verificable: [...]
- Artefactos en carpeta: [...]
- Bloqueos o decisiones pendientes: [...]
- Carga restante estimada: [sin task | baja | media | alta | entrega lista]
- Siguiente paso recomendado: [...]
- Petición para Aleph: [sincronizar | revisar entrega | reasignar | sin acción]
```

## Paso 5 — Reporta y espera

Responde al usuario con este formato:

```
Soy {alias} ({tu modelo}). He refrescado mi estado en disco para Aleph.

Estado sincronizado:
- Task: [...]
- Estado: [...]
- Último avance verificable: [...]
- Bloqueos: [...]
- Carga restante estimada: [...]
- Siguiente paso: [...]

¿Sigo trabajando o esperas a que Aleph sincronice?
```

Después de eso, **para y espera**. No retomes trabajo hasta que el usuario diga "sigue", "adelante" o equivalente.