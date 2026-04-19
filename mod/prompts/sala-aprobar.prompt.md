# /sala-aprobar — Aprobación atómica de task

Micro-prompt de aprobación. Garantiza que aprobar una propuesta de agente siempre sincroniza `estado.md` **y** `tablero.md` en una sola acción.

> **Protocolo transversal:** `mod/instructions/sala-protocolo.instructions.md` §4.1 aplica. Aprobación atómica obligatoria.

---

## Uso

```
/sala-aprobar {alias} {TASK-ID}
```

**Ejemplos:**
- `/sala-aprobar boris CA-07`
- `/sala-aprobar lai LP-01`
- `/sala-aprobar boris CA-07, lai LP-01, luna GJ-06`  ← múltiples en una llamada

---

## Pasos (Aleph los ejecuta)

### Para cada par {alias, TASK-ID}:

**1. Lee el dossier de la task** (si no lo tienes en contexto):
- Busca en `DRAFTS2/sala/agente-{alias}/estado.md` la propuesta del agente.
- Opcionalmente lee el dossier en la carpeta de cristalización correspondiente para formular instrucciones concretas.

**2. Escribe en `estado.md` del agente** (en una acción junto con el paso 3):
```
- [fecha] ALEPH: {TASK-ID} aprobada. Adelante. {instrucciones concretas: qué hacer, qué leer, dónde dejar el candidato}.
```
Y actualiza la cabecera:
```
Task: {TASK-ID}
Estado: en-curso
Último checkpoint: {fecha} — ALEPH: {TASK-ID} aprobada
```

**3. Actualiza `tablero.md`** (en la misma llamada multi_replace_string_in_file):
- Fila del track: `libre` → `en-curso:{alias}`
- Tabla resumen: libres--, en-curso++

**4. Confirma al PO** (una línea por aprobación):
```
{alias} ({modelo}): {TASK-ID} aprobada — tablero sincronizado ✓
```

---

## Regla de atomicidad

Usar **`multi_replace_string_in_file`** con todos los cambios en una sola llamada cuando se aprueban múltiples tasks. Si la llamada falla parcialmente, reportar qué quedó sin sincronizar antes de continuar.

**No existe**: "aprobé en estado.md, actualizaré tablero después."
**Sí existe**: "aprobé en estado.md y tablero en la misma operación."

---

## Por qué existe este prompt

El tablero es la única fuente de verdad compartida entre agentes. Si un agente lee su `estado.md` como "en-curso" pero el tablero dice "libre", interpreta inconsistencia y para — bloqueando el pipeline. Este prompt hace la sincronización imposible de olvidar.
