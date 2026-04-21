# Nota de Onboarding — bot trabajador para sala en BotHubSDK

> Solo protocolo de sala. Sin contexto de producto.
> Esta nota resume lo que me resultó útil al preparar la entrada en sala desde BotHubSDK.

## 1. Qué significa "sala" en este repo

En este repo la sala efectiva no es `sala/`, sino `scrum/`.

Para el protocolo, piensa así:

- `{{SALA_DIR}}` = `scrum/`
- dossier activo = `scrum/dossiers/scriptorium-bot-hub-integration/`
- tu carpeta de trabajo = `scrum/agente-{alias}/`

Ahora mismo `scrum/` ya tiene `dossiers/`, `broadcast/` y `kickoff/`, pero no vi todavía `tablero.md` ni `README.md`. Si Aleph aún no los ha creado, no los inventes tú: registra presencia y espera.

## 2. Tu paso extra aquí: instalar el pack `agente`

BotHubSDK no trae todavía el pack de sala. En `.github/` solo vi prompts de producto; faltan las piezas de coordinación.

Instala, manteniendo rutas relativas exactas:

- `.github/instructions/sala-protocolo.instructions.md`
- `.github/prompts/sala-entrar.prompt.md`
- `.github/prompts/sala-reconectar.prompt.md`
- `.github/prompts/sala-seguir.prompt.md`
- `.github/prompts/sala-salir.prompt.md`
- `.github/templates/sala-agente.template.md`

Opcional pero recomendable:

- `.github/instructions/plan-attribution.instructions.md`
- `.github/skills/dossier-feature/SKILL.md`

No renombres nada. El protocolo depende de esas rutas.

## 3. La regla más importante

Disco primero, chat después.

Si Aleph no puede verlo en tu carpeta, para la sala no existe.

Eso significa:

- el contenido de trabajo va a fichero
- el chat solo sirve para notificaciones breves
- antes de escribir nada, comprueba que la ruta empieza por `scrum/agente-{alias}/`

## 4. Antes de cualquier task

Tu primer trabajo no es la task. Tu primer trabajo es dejar presencia en disco.

Secuencia mínima:

1. entra con alias, no con nombre de modelo
2. crea `scrum/agente-{alias}/`
3. crea `scrum/agente-{alias}/estado.md` si no existe
4. deja `Estado: handshake-pendiente`
5. anota en log que has entrado y que esperas tablero/aprobación

Si la carpeta ya existía, no la reinicies: lee, añade `RECONEXION`, refresca handoff.

## 5. Si README o tablero no están todavía

El prompt ideal asume que existen `{{SALA_DIR}}/README.md` y `{{SALA_DIR}}/tablero.md`.

En BotHubSDK puede que Aleph los esté creando ahora mismo. Si faltan:

- no inventes tareas
- no fabriques tablero
- deja el bloqueo en `estado.md`
- avisa en chat en 2-3 líneas
- espera a que Aleph termine la inicialización

Tu estado correcto en ese punto es: presencia registrada, handshake pendiente, esperando infraestructura mínima de sala.

## 6. Lo que NO puedes hacer

Estas líneas rojas son reales, no decorativas:

- no hagas `git commit`, `git branch`, `git merge`, `git push`
- no escribas en `.github/`, `scrum/dossiers/`, `scrum/tablero.md`, `broadcast/`, ni carpetas ajenas
- no edites `estado.md` de otro agente
- no cierres tareas por tu cuenta

Si tienes un candidato útil, lo dejas en tu carpeta y Aleph lo copia.

## 7. Cómo proponer trabajo correctamente

Cuando el tablero exista:

- lee tareas `libre`
- respeta dependencias
- propone task en tu `estado.md`
- si varias tasks son pequeñas y del mismo track, puedes proponer bloque
- espera aprobación atómica de Aleph antes de avanzar

Aprobación atómica significa que Aleph actualiza a la vez tu `estado.md` y el tablero. Si solo te lo dice por chat, no basta.

## 8. Cómo trabajar una vez aprobado

Antes de leer el dossier o producir artefactos:

- actualiza `Task:` en `estado.md`
- pon `Estado: en-curso`
- deja línea de log con la task aprobada
- refresca `Handoff Aleph`

Luego sí: lees brief, trabajas y vas dejando checkpoints.

Cada checkpoint:

- actualiza `estado.md`
- deja fichero si produjiste algo
- en chat, solo resumen corto

## 9. Cómo entregar

Toda task termina con entrega en disco. Sin excepciones.

Deja en tu carpeta:

- artefacto o informe
- `ENTREGA_{TASK-ID}.md`

La entrega debe decir:

- qué hiciste
- qué ficheros dejaste
- qué tiene que copiar, revisar o cerrar Aleph

## 10. Atajo útil si te pierdes

No reconstruyas desde memoria si la sesión se cortó.

Usa:

- `/sala-reconectar {alias}`

Eso es mejor que improvisar un resumen nuevo fuera de protocolo.

## 11. El mínimo mapa mental para entrar bien

- tu rol = worker, no orquestador
- Aleph lee disco, no tu chat
- tu unidad de verdad = `scrum/agente-{alias}/estado.md`
- el dossier es persistencia de diseño
- la carpeta del agente es ejecución
- la aprobación y el cierre los hace Aleph

## 12. El delta práctico de este repo

Lo que más me sirvió aquí fue asumir esto desde el principio:

- `scrum/` es la sala, aunque no se llame `sala/`
- el dossier ya existe aunque la sala aún no esté completa
- sin pack `agente`, los comandos `/sala-*` no están realmente aterrizados en BotHubSDK
- sin `tablero.md`, tu trabajo es solo handshake y espera, no exploración libre

Si respetas eso, entras limpio y no generas ruido para Aleph.
