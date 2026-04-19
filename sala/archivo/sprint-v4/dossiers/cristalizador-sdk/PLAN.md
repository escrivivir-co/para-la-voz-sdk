# Plan — cristalizador-sdk

> **Fecha:** 19-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/cristalizador-sdk/`

## 1. Contexto

El Cristalizador ya existe como agente core del SDK en `.github/agents/cristalizador.agent.md`, con su entrypoint `/design` en `.github/prompts/design.prompt.md` y su posición explícita al final del ciclo documental en `.github/templates/guion-ciclo.template.md`.

Su contrato actual ya contiene la intuición correcta:

- lee el corpus, `.github/`, `mod/` y `COPILOT/`
- propone antes de implementar
- escribe en `mod/`, no en `.github/`
- intenta activar capacidades nuevas de Copilot en cada iteración

Pero ese contrato todavía está formulado en una versión anterior del ecosistema y deja huecos que ahora son estructurales:

- no distingue con claridad entre **Cristalizador como agente SDK en `main`** y **Cristalizador operando dentro de una rama `mod/*`**
- no formaliza que los mods heredan el Cristalizador de `main` salvo override local en `mod/agents/`
- trata `COPILOT/` como una lista fija de documentos, no como un observatorio vivo de capacidades que puede quedarse obsoleto
- no pacta explícitamente con el usuario cuando maximizar el diseño implica features preview, opt-ins de organización, multiplicadores premium, instalaciones extra o gating operativo
- no tiene una señal auditable de frescura para `COPILOT/`: hoy solo existe la convención de "sync mensual"

Además, el archivo de `mod/legislativa` ya dejó una pista útil: en `future-machine-universo-1` se pidió expresamente que el Cristalizador leyera `COPILOT/`, detectara capacidades aprovechables, maximizara el uso agéntico en `mod/` y abriera warning a `main` solo con evidencia real. Ese comportamiento ya fue pensado en disco; falta promoverlo a contrato portable del SDK.

## 2. Anclas

| Artefacto | Ubicación | Papel |
|-----------|-----------|-------|
| Agente core actual | `.github/agents/cristalizador.agent.md` | Contrato vivo del Cristalizador en `main` |
| Prompt de entrada | `.github/prompts/design.prompt.md` | Superficie `/design` |
| Ciclo documental | `.github/templates/guion-ciclo.template.md` | Sitúa la cristalización en el pipeline |
| Identidad del SDK | `.github/copilot-instructions.md` | Define `mod/` como espacio de extensión y el flujo `main -> mod/*` |
| Política actual de `COPILOT/` | `README.md` | Declara el "sync mensual" y el uso por parte del Cristalizador |
| Dossier histórico | `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/PLAN_FUTURE_MACHINE_UNIVERSO1.md` | Formula al Cristalizador como agente ejecutor de intervención |
| Task histórica de misión | `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/tasks/TASK-02_CRISTALIZADOR_MISION_INTERVENCION.md` | Pide leer `COPILOT/` y proponer wiring útil |
| Task histórica de warning | `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/tasks/TASK-06_WARNING_MAIN_SI_APLICA.md` | Condiciona el warning a evidencia real |
| Nota de refactor del mod | `DRAFTS2/mod_legislativa_R.md` | Ya registró `cristalizador.agent.md` como pieza a refactorizar hacia `main` |

## 3. Restricciones

- El Cristalizador es un **agente de `main`**. Los mods lo usan por defecto si no crean override en `mod/agents/cristalizador.agent.md`.
- En una rama `mod/*`, `.github/` y `COPILOT/` son superficies de referencia. El territorio de escritura del Cristalizador es `mod/` y, si trabaja bajo `sala`, su carpeta temporal/dossier según protocolo.
- Si el Cristalizador detecta un déficit del SDK mientras opera en un mod, no debe parchear `.github/` desde esa rama. Debe abrir warning, dossier o backlog para `main`.
- La maximización de capacidades no puede ser muda: si una propuesta depende de preview, políticas de organización, multiplicadores premium, instalaciones adicionales, plugins o MCP, el Cristalizador debe exponer el coste/condición y pactarlo con el usuario.
- La alerta de obsolescencia de `COPILOT/` no puede depender solo de hooks, porque los hooks están en preview y pueden estar deshabilitados por política. Debe existir un fallback que funcione sin ellos.

## 4. Propuesta

### 4.1. Contrato de doble capa: SDK por defecto + ejecución en mod

El dossier propone cristalizar dos capas complementarias:

1. **Cristalizador-SDK**: vive en `main`, define el comportamiento por defecto y la lectura canónica del ecosistema.
2. **Cristalizador-en-mod**: ejecuta ese contrato dentro de una rama `mod/*`, hereda de `.github/` y solo materializa artefactos en `mod/` salvo override local justificado.

El override de un mod no sustituye el contrato base: lo extiende o especializa.

### 4.2. Territorio de escritura branch-aware

El Cristalizador debe clasificar cada misión en una de estas superficies:

- **Refactor SDK**: afecta a `.github/`, `COPILOT/`, README del SDK o artefactos core. Solo procede en `main` o como dossier/warning preparado para `main`.
- **Extensión de mod**: afecta a `mod/agents/`, `mod/prompts/`, `mod/skills/`, `mod/hooks/`, `mod/instructions/`.
- **Trabajo de sala**: afecta a dossiers o carpetas temporales de ejecución, pero no rompe la frontera `main/mod`.

La salida del Cristalizador debe declarar siempre qué superficie está tocando y por qué.

### 4.3. `COPILOT/` como observatorio de capacidades

En vez de depender de un catálogo estático, el Cristalizador debe operar así:

1. leer `COPILOT/indice.md`
2. identificar qué familias documentales aplican a la petición real
3. bajar a esos documentos antes de proponer la solución maximizada
4. reportar qué documentos consultó y qué capacidad nueva o infrautilizada detectó

Las familias mínimas que deben poder entrar en juego son:

- custom agents
- skills
- prompt files
- hooks
- agent architecture y subagents
- MCP servers
- language models
- tools
- plugins
- contexto/indexación cuando la propuesta dependa de ello

El Cristalizador necesita, además, un registro práctico de capacidad con estados como:

- `ya-usada`
- `disponible`
- `preview`
- `requiere-admin`
- `coste-premium`
- `no-verificada-por-docs`

### 4.4. Pacto de maximización con el usuario

"Maximizar el uso" no significa asumir cualquier feature avanzada sin aviso. Antes de proponer o implementar una variante reforzada, el Cristalizador debe exponer:

- qué gana el usuario
- qué condición técnica o política introduce
- si existe versión baseline sin esa dependencia

Esto aplica, como mínimo, a:

- hooks preview
- subagents anidados o configuraciones especiales
- modelos con gating por tool-calling, premium requests o preview organizacional
- plugins, MCP servers o instalaciones externas
- cualquier cambio que modifique el contrato operativo del workspace

### 4.5. Frescura de `COPILOT/` y sistema de alerta

Hoy `COPILOT/indice.md` solo registra la URL de origen. Falta una capa de gobernanza mínima.

Este dossier propone fijar un contrato de frescura con tres piezas:

1. **Manifest o metadato de sync**: origen, fecha de última actualización, familias presentes y huecos conocidos.
2. **Regla de warning**: si el sync está ausente o vencido respecto al ciclo mensual, el Cristalizador avisa antes de apoyar una maximización fuerte en esos docs.
3. **Doble vía de implementación**:
   - preferente: hook scoped al agente o hook de workspace, si el entorno lo soporta
   - fallback obligatorio: chequeo manual en el propio agente o en `/design`

El trigger exacto del warning (mensual estricto o con pequeña gracia) queda abierto para CR-03, pero el comportamiento esperado ya queda fijado: **avisar, explicar impacto y ofrecer update**.

### 4.6. Recolocar al Cristalizador en el ciclo entero

El Cristalizador no es un añadido ornamental al final del pipeline. Es el punto donde el SDK aprende de su uso real y decide si hace falta crear:

- agentes nuevos
- prompts nuevos
- skills nuevas
- hooks
- MCP servers
- documentación o wiring adicional

Los dossiers de cristalización archivados en `mod/legislativa` son prueba de ese papel upstream. El refactor debe dejarlo claro en el agente, en `/design` y en la documentación del ciclo.

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)