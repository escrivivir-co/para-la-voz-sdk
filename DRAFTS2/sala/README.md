# Sala de coordinación — mod/legislativa

> Si eres un agente y acabas de entrar: lee este fichero entero. Son 2 minutos. Después abre `tablero.md`.

## Qué es esto

Una sala de coordinación para que 3 agentes trabajen en paralelo sobre 5 dossiers de cristalización. El orquestador (el hilo principal con el PO) revisa, aprueba y cierra.

## Reglas (7, no más)

1. **Identifícate.** Todo fichero que crees o toques lleva tu nombre de modelo en el nombre o en la cabecera: `claude-opus-4`, `gpt-5.4`, `gemini-3.1-pro`, etc.

2. **Lee el tablero.** Abre `tablero.md`. Busca una tarea con estado `libre` cuyas dependencias estén resueltas. Esa es tu candidata.

3. **Pide la tarea.** Dile al orquestador: "Quiero [TASK-ID]". Él la marca como tuya en el tablero. No empieces sin confirmación.

4. **Los dossiers son READ ONLY.** Puedes leer todo en `DRAFTS2/cristalizacion-*/` y `DRAFTS2/finalizacion-*/` y `DRAFTS2/future-machine-*/`. No escribas ahí. Nunca.

5. **Tu carpeta temporal.** Crea `sala/agente-{tu-modelo}/` si no existe. Trabaja ahí: copia de backlog, notas, borradores. Cuando termines la tarea, dejas ahí tu entrega con nombre claro.

6. **Implementa donde toque.** Los artefactos finales van donde diga la task: `mod/agents/`, `mod/instructions/`, `DRAFTS2/grafo/`, etc. Tu carpeta temporal es solo para coordinación y borradores.

7. **Avisa al terminar.** Cuando acabes una tarea: "Terminé [TASK-ID], entrega en `sala/agente-{modelo}/ENTREGA_{TASK-ID}.md`". El orquestador revisa, acepta, y copia lo que haga falta al dossier. Después tu carpeta temporal se limpia.

## Estructura de la sala

```
DRAFTS2/sala/
├── README.md          ← estás aquí
├── tablero.md         ← qué hay, quién tiene qué
├── agente-claude/     ← carpeta temporal (ejemplo)
├── agente-gpt/        ← carpeta temporal (ejemplo)
└── agente-gemini/     ← carpeta temporal (ejemplo)
```

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
