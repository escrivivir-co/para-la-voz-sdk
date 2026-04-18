# Sala de coordinación — mod/legislativa

> Si eres un agente y acabas de entrar: lee este fichero entero. Son 2 minutos. Después abre `tablero.md`.
>
> **⚠️ NO EMPIECES A TRABAJAR SIN HACER EL HANDSHAKE.** Ver regla 0 abajo.

## Qué es esto

Una sala de coordinación para que 3 agentes trabajen en paralelo sobre 5 dossiers de cristalización. El orquestador (el hilo principal con el PO) revisa, aprueba y cierra.

## Regla 0 — Handshake obligatorio

**Antes de hacer CUALQUIER cosa**, preséntate al usuario con este formato exacto:

```
Soy [tu modelo]. He leído el protocolo de sala y el tablero.

He identificado estas tareas libres que puedo tomar:
- [TASK-ID]: [título] — [1 línea de lo que entiendes que hay que hacer]

Quiero tomar: [TASK-ID]

¿Aprobado? Espero confirmación antes de empezar.
```

**No crees carpetas, no leas dossiers, no escribas código hasta que el usuario diga "adelante", "ok", "aprobado" o equivalente.**

El usuario es el puente con el orquestador Aleph. Si Aleph está en otro hilo, el usuario le transmite. Si Aleph está en este hilo, responde directamente.

## Regla 0.1 — Registrarse en disco (inmediato tras aprobación)

En cuanto el usuario apruebe tu tarea, **antes de empezar a trabajar**, haz esto:

1. Crea tu carpeta: `DRAFTS2/sala/agente-{tu-modelo}/`
2. Crea el fichero `DRAFTS2/sala/agente-{tu-modelo}/estado.md` con este contenido:

```markdown
# Estado — agente-{tu-modelo}

> **Modelo:** [tu modelo]
> **Task:** [TASK-ID]
> **Estado:** en-curso
> **Inicio:** [fecha y hora]
> **Último checkpoint:** [fecha y hora] — registrado en disco

## Log

- [timestamp] Handshake aprobado. Tarea: [TASK-ID] — [título]
```

3. Añade una línea al log de `estado.md` **en cada checkpoint**:

```markdown
- [timestamp] Checkpoint: [qué completé]. Siguiente: [qué voy a hacer].
```

4. Al terminar, actualiza el estado a `entregada` y añade la línea final:

```markdown
- [timestamp] ENTREGA: [ruta del fichero de entrega]. Esperando revisión de Aleph.
```

**¿Por qué?** El orquestador Aleph está en otra ventana. No puede ver lo que dices aquí. Pero sí puede leer tu carpeta. Si no escribes en disco, para Aleph no existes.

## Regla 0.2 — Checkpoints

No trabajes más de **una subtarea o un artefacto** sin reportar. Después de cada pieza significativa:

```
[TASK-ID] checkpoint: he completado [qué].
Siguiente paso: [qué voy a hacer ahora].
¿Sigo o paro?
```

Si el usuario dice "tira millas" o "sigue", continúa. Si dice "para", para y espera instrucciones. Si no dice nada, **para y espera**.

Esto le permite al orquestador intervenir, redirigir, o decirte que vas bien sin que te pierdas en un trabajo largo que luego hay que tirar.

## Reglas (7, no más)

1. **Identifícate.** Todo fichero que crees o toques lleva tu nombre de modelo en el nombre o en la cabecera: `claude-opus-4`, `gpt-5.4`, `gemini-3.1-pro`, etc.

2. **Lee el tablero.** Abre `tablero.md`. Busca una tarea con estado `libre` cuyas dependencias estén resueltas. Esa es tu candidata.

3. **Pide la tarea (dentro del handshake).** Ya cubierto por la regla 0. No empieces sin confirmación.

4. **Los dossiers son READ ONLY.** Puedes leer todo en `DRAFTS2/cristalizacion-*/` y `DRAFTS2/finalizacion-*/` y `DRAFTS2/future-machine-*/`. No escribas ahí. Nunca.

5. **Tu carpeta temporal.** Crea `sala/agente-{tu-modelo}/` si no existe. Trabaja ahí: copia de backlog, notas, borradores. Cuando termines la tarea, dejas ahí tu entrega con nombre claro.

6. **Implementa donde toque.** Los artefactos finales van donde diga la task: `mod/agents/`, `mod/instructions/`, `DRAFTS2/grafo/`, etc. Tu carpeta temporal es solo para coordinación y borradores.

7. **Avisa al terminar.** Cuando acabes una tarea: "Terminé [TASK-ID], entrega en `sala/agente-{modelo}/ENTREGA_{TASK-ID}.md`". El orquestador revisa, acepta, y copia lo que haga falta al dossier. Después tu carpeta temporal se limpia.

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
├── agente-claude/                 ← carpeta temporal (ejemplo)
├── agente-gpt/                    ← carpeta temporal (ejemplo)
└── agente-gemini/                 ← carpeta temporal (ejemplo)
```

### Crear un dossier nuevo

Copia `plantilla-dossier/` a `DRAFTS2/cristalizacion-<nombre>/`, rellena los placeholders, y registra las tasks en el tablero. Solo el orquestador crea dossiers. Protocolo completo en `mod/skills/cristalizacion-feature/SKILL.md`.

> **Para el orquestador:** si acabas de abrir una ventana nueva, di `/eres-aleph` o lee `activacion-orquestador.md`. No improvises de memoria.

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

- No escribir en carpetas de dossier (solo el orquestador)
- No tomar dos tareas a la vez
- No empezar sin que el orquestador confirme la asignación
- No borrar tu carpeta temporal tú mismo — el orquestador lo hace al cerrar
