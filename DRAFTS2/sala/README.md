# Sala de coordinación — mod/legislativa

> Si eres un agente y acabas de entrar: lee este fichero entero. Son 2 minutos. Después abre `tablero.md`.
>
> **⚠️ NO EMPIECES A TRABAJAR SIN HACER EL HANDSHAKE.** Ver regla 0 abajo.

## Qué es esto

Una sala de coordinación para que 3 agentes trabajen en paralelo sobre 5 dossiers de cristalización. El orquestador (Aleph, en otro hilo) revisa, aprueba y cierra. **Aleph no asigna tareas: los agentes proponen, Aleph valida.**

## Regla -1 — Presencia en disco al entrar

Cada vez que un agente ejecuta `/sala-entrar` o `/sala-reconectar`, debe dejar rastro en disco **antes de pedir tarea o retomar trabajo**.

1. Asegura su carpeta: `DRAFTS2/sala/agente-{alias}/` (alias en minúsculas).
2. Crea o actualiza `estado.md` (incluye sección Handoff para Aleph).
3. Añade una línea `ENTRADA` o `RECONEXION` en el log.

Template de `estado.md`:

```markdown
# Estado — agente-{alias}

> **Alias:** {alias}
> **Modelo:** [tu modelo]
> **Task:** [TASK-ID o —]
> **Estado:** [handshake-pendiente | en-curso | entregada]
> **Inicio:** [fecha y hora]
> **Último checkpoint:** [fecha y hora]

## Log

- [timestamp] ENTRADA: alias registrado en sala. Sin tarea todavía.

## Handoff Aleph

> Sección que Aleph lee para balance de carga. Refresca en cada checkpoint.

- Último avance verificable: [...]
- Artefactos en carpeta: [...]
- Bloqueos o decisiones pendientes: [...]
- Carga restante estimada: [sin task | baja | media | alta | entrega lista]
- Siguiente paso recomendado: [...]
```

Un solo fichero, una sola fuente de verdad. Aleph lee la cabecera para el estado y la sección "Handoff Aleph" para balance de carga.

Esta escritura en disco es la **única excepción** al "no escribas nada antes de la aprobación". No autoriza trabajo: solo sincroniza presencia para que Aleph pueda verte y balancear carga.

## Regla 0 — Handshake obligatorio

**Antes de hacer CUALQUIER cosa**, preséntate y deja tu propuesta en disco:

1. Registra tu presencia (regla -1).
2. Lee el tablero, identifica tareas libres.
3. Actualiza la sección "Handoff Aleph" de tu `estado.md` con tu propuesta: `Propongo tomar [TASK-ID]`.
4. Di al usuario:

```
Soy {alias} ({tu modelo}). He leído el protocolo de sala y el tablero.

He dejado mi presencia y mi propuesta en disco para Aleph.

He identificado estas tareas libres que puedo tomar:
- [TASK-ID]: [título] — [1 línea de lo que entiendes que hay que hacer]

Propongo tomar: [TASK-ID]

Esperando a que Aleph apruebe (en tablero o en mi carpeta).
```

**Tu alias** es el nombre que el PO te asignó al invocarte (ej: `/sala-entrar Boris` → alias = Boris). Tu **modelo** es tu nombre técnico (`gpt-5.4`, `claude-opus-4`, etc.). Usas el alias para todo lo visible en la sala (carpeta, tablero, entregas). El modelo va en `estado.md` para trazabilidad.

**No leas dossiers ni escribas código hasta que te digan que Aleph aprobó.** La única escritura permitida antes de la aprobación es la de la regla -1 (presencia en disco + propuesta en Handoff Aleph).

### Cómo funciona la comunicación

- **Agente → Aleph** (lectura): a través de **disco**. Tú escribes en `estado.md`, Aleph lo lee.
- **Aleph → Agente** (decisiones): a través de **disco**. Aleph escribe en tu `estado.md` (líneas `ALEPH: ...` en el log) y en el tablero. **Si no está en disco, no ha pasado.** Aleph nunca comunica una decisión solo por chat.
- **Con el usuario** (PO): en el chat. Te habla sobre contenido de tareas, contexto, decisiones. También actúa como timbre: "Aleph aprobó, mira tu carpeta". Pero la fuente de verdad de qué hacer está en disco.

**Regla de verificación para el agente:** al reconectar, lee tu `estado.md`. Si ves una línea `ALEPH: ...` en el log que no habías leído, esa es la instrucción. No dependas de que el usuario te la repita.

## Regla 0.1 — Activar la task tras aprobación

En cuanto Aleph apruebe tu tarea (te lo dirá el usuario o lo verás en el tablero), **antes de empezar a trabajar**, haz esto:

1. Si no existía, crea tu carpeta: `DRAFTS2/sala/agente-{alias}/` (alias en minúsculas)
2. Actualiza `DRAFTS2/sala/agente-{alias}/estado.md` para que refleje la task aprobada:

```markdown
# Estado — agente-{alias}

> **Alias:** {alias}
> **Modelo:** [tu modelo]
> **Task:** [TASK-ID]
> **Estado:** en-curso
> **Inicio:** [fecha y hora]
> **Último checkpoint:** [fecha y hora] — registrado en disco

## Log

- [timestamp] Handshake aprobado. Tarea: [TASK-ID] — [título]
```

3. Añade una línea al log de `estado.md` **en cada checkpoint** y refresca la sección "Handoff Aleph" del mismo fichero:

```markdown
- [timestamp] Checkpoint: [qué completé]. Siguiente: [qué voy a hacer].
```

4. Al terminar, actualiza el estado a `entregada`, refresca la sección "Handoff Aleph" y añade la línea final:

```markdown
- [timestamp] ENTREGA: [ruta del fichero de entrega]. Esperando revisión de Aleph.
```

**¿Por qué?** El orquestador Aleph está en otra ventana. No puede ver lo que dices aquí. Pero sí puede leer tu carpeta. Si no escribes en disco, para Aleph no existes; si no refrescas la sección "Handoff Aleph", para Aleph existes pero estás borroso.

## Regla 0.2 — Checkpoints

> Formato detallado en `mod/instructions/sala-protocolo.instructions.md` (se carga automáticamente en todos los prompts de sala).

No trabajes más de **una subtarea o un artefacto** sin reportar. Disco primero (estado.md + fichero si aplica), chat después (3-5 líneas de notificación).

Si el usuario dice "tira millas" o "sigue", continúa. Si dice "para", para y espera instrucciones. Si no dice nada, **para y espera**.

## Regla 0.3 — Handoff Aleph / reconexión

Si vuelves tras una pausa, te has perdido, acumulas demasiado trabajo o Aleph necesita balancear carga, ejecuta `/sala-reconectar {alias}`.

Ese prompt hace tres cosas y **luego para**:

1. Relee tu carpeta temporal y el tablero.
2. Refresca `estado.md` con una línea `RECONEXION` o `SYNC-ALEPH`.
3. Reescribe la sección "Handoff Aleph" de `estado.md` con estado verificable, bloqueos y carga restante.

No uses `/sala-reconectar` para avanzar trabajo. Úsalo para volver a estar sincronizado con Aleph.

## Reglas (7, no más)

1. **Identifícate.** Tu alias es tu nombre en la sala. Tu modelo (`claude-opus-4`, `gpt-5.4`, `gemini-3.1-pro`, etc.) va en la cabecera de `estado.md` y en los ficheros de entrega para trazabilidad.

2. **Lee el tablero.** Abre `tablero.md`. Busca una tarea con estado `libre` cuyas dependencias estén resueltas. Esa es tu candidata.

3. **Propone la tarea (dentro del handshake).** Tú eliges qué tarea tomar según el tablero, las dependencias y tus capacidades. Dejas tu propuesta en `estado.md` (sección Handoff Aleph). Aleph aprueba, redirige con motivo, o rechaza. **Aleph nunca te asigna de oficio.** Ya cubierto por la regla 0. No empieces sin confirmación.

4. **Los dossiers son READ ONLY.** Puedes leer todo en `DRAFTS2/cristalizacion-*/` y `DRAFTS2/finalizacion-*/` y `DRAFTS2/future-machine-*/`. No escribas ahí. Nunca. Solo Aleph escribe en dossiers.

5. **Tu carpeta temporal — todo el trabajo va a disco.** Crea `sala/agente-{alias}/` si no existe. Todo artefacto, informe o análisis que produzcas va como fichero en tu carpeta temporal. Nunca edites directamente en `mod/`, `corpus/`, `.github/`. Tú produces candidatos; Aleph copia al destino final. **Si Aleph no puede verlo en tu carpeta, no existe.** (Detalle en `sala-protocolo.instructions.md`)

6. **Solo Aleph toca ficheros permanentes, git y dossiers.** Tú no haces commits, no haces push, no tocas ramas. Tú no editas ficheros en `mod/`, `corpus/`, `.github/`, ni en los dossiers (`DRAFTS2/cristalizacion-*/`, `DRAFTS2/finalizacion-*/`, `DRAFTS2/future-machine-*/`). Toda responsabilidad de cambios permanentes es de Aleph. Tú preparas candidatos en tu carpeta temporal; Aleph ejecuta.

7. **Avisa al terminar — entrega obligatoria, sin excepciones.** Toda tarea produce un `ENTREGA_{TASK-ID}.md` en tu carpeta con: resumen, rutas de ficheros, pasos para Aleph. Si es código → candidato en carpeta. Si es validación → informe en carpeta. No hay tareas que "solo se documentan en el chat". (Detalle y tabla de tipos en `sala-protocolo.instructions.md`)

### Ciclo de vida de la carpeta post-cierre

Cuando Aleph cierra una tarea:
1. Copia los artefactos al destino final.
2. Borra entregas y borradores de tu carpeta temporal.
3. Mantiene `estado.md` con el log histórico (nunca se borra).
4. Actualiza `estado.md`: `Task: —`, `Estado: disponible`.

**Tu carpeta sigue existiendo** con `estado.md` limpio. La próxima vez que entres con `/sala-entrar` o `/sala-seguir`, lees el tablero, propones otra tarea, y el ciclo se repite. Aleph no te ofrece la siguiente tarea: tú la eliges.

## Estructura de la sala

```
DRAFTS2/sala/
├── README.md                      ← estás aquí
├── tablero.md                     ← qué hay, quién tiene qué
├── activacion-orquestador.md      ← protocolo para levantar al orquestador en sesión fría
├── plantilla-dossier/             ← plantilla vacía para crear dossiers nuevos
│   ├── PLAN.md
│   ├── BACKLOG.md
│   ├── RESPUESTAS.md
│   ├── activacion.prompt.md
│   └── tasks/TASK-00_CONTEXTO_Y_PERSISTENCIA.md
├── agente-boris/                  ← carpeta temporal
│   └── estado.md                  ← log + sección Handoff Aleph
├── agente-luna/                   ← carpeta temporal
└── agente-kai/                    ← carpeta temporal
```

### Crear un dossier nuevo

Copia `plantilla-dossier/` a `DRAFTS2/cristalizacion-<nombre>/`, rellena los placeholders, y registra las tasks en el tablero. Solo el orquestador crea dossiers. Protocolo completo en `mod/skills/cristalizacion-feature/SKILL.md`.

> **Para el orquestador:** si acabas de abrir una ventana nueva, di `/sala-aleph` o lee `activacion-orquestador.md`. No improvises de memoria.

## Cómo leer una tarea

Cada tarea tiene un ID tipo `PO-01`, `CA-03`, `GJ-05`. El brief completo está en el dossier:

| Prefijo | Dossier | Ruta |
|---------|---------|------|
| PO-* | pipeline-operativo | `DRAFTS2/cristalizacion-pipeline-operativo/tasks/` |
| CA-* | cadena-agentica | `DRAFTS2/cristalizacion-cadena-agentica/tasks/` |
| GJ-* | grafo-json | `DRAFTS2/cristalizacion-grafo-json/tasks/` |
| LP-* | finalizacion-lore-plan | `DRAFTS2/finalizacion-lore-plan/tasks/` |
| FM-* | future-machine-universo-1 | `DRAFTS2/future-machine-universo-1/tasks/` |

Lee el brief. Lee el PLAN del dossier si necesitas contexto. Lee `RESPUESTAS_USUARIO_*.md` para ver decisiones del PO ya tomadas.

## Contexto mínimo del proyecto

- El mod legislativa tiene 51 piezas de lore en `DRAFTS2/LORE_*.md`
- Hay una cadena de 5 agentes: Puzzle → Archivero Lore → Grafista → Demiurgo → Dramaturgo Cortos
- El big picture está en `mod/instructions/onboarding-map.instructions.md`
- El SDK base está en `.github/` — **no se toca**
- Todo lo nuevo va en `mod/` o `DRAFTS2/`

## Qué NO hacer

- No escribir en carpetas de dossier (solo Aleph)
- No hacer `git commit`, `git push`, ni tocar ramas (solo Aleph)
- No tomar dos tareas a la vez
- No empezar sin que el orquestador confirme la asignación
- No seguir tras una pausa larga sin refrescar antes la sección "Handoff Aleph" de `estado.md`
- No borrar tu carpeta temporal tú mismo — el orquestador lo hace al cerrar
