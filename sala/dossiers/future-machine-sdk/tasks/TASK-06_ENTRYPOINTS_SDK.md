# TASK-06 — 3 prompts de entrypoint base

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** FS-01, FS-05
> **Entrega esperada:** 3 prompts en `.github/prompts/`

## Lee primero

1. `.github/instructions/future-machine-schema.instructions.md` — el schema de slots (FS-01)
2. `.github/agents/pipeline.agent.md` — el Pipeline SDK (FS-05)
3. `mod/prompts/user-empieza-aqui.prompt.md` en `mod/legislativa` — override rico de referencia
4. `mod/prompts/lore-status.prompt.md` en `mod/legislativa` — override rico de referencia
5. `mod/prompts/pipeline-refresh.prompt.md` en `mod/legislativa` — override rico de referencia

## Objetivo

Crear 3 prompts SDK base que cubran los entrypoints genéricos de la machine. Son **baseline overrideable**: cada mod puede sustituirlos con versiones ricas.

## Los 3 prompts

### `/machine-start` — `.github/prompts/machine-start.prompt.md`

1. Lee `FUTURE_MACHINE.md` si existe
2. Muestra la big picture del ciclo (slots llenos, slots vacíos)
3. Ofrece el siguiente paso lógico al usuario
4. Si no hay machine: dice que no hay ciclo configurado y sugiere `/design`

### `/machine-status` — `.github/prompts/machine-status.prompt.md`

1. Lee `FUTURE_MACHINE.md`
2. Muestra el estado de cada slot: agente propietario, ruta, estado (operativo/pendiente/legacy)
3. Marca desincronizaciones visibles entre niveles
4. Si no hay machine: muestra el estado base del corpus vía `/status`

### `/machine-refresh` — `.github/prompts/machine-refresh.prompt.md`

1. Delega directamente a `@Pipeline` con el manifest precargado
2. Es el equivalente SDK de `/pipeline-refresh` del mod
3. Si no hay `@Pipeline` configurado: informa y sugiere refresh manual

## Salida mínima esperada

1. Tres ficheros `.prompt.md` en `.github/prompts/`
2. ENTREGA con nota de cómo mod/legislativa puede override cada uno

## Criterio de aceptación

- Los 3 prompts existen y funcionan con machine vacía (degradan graceful)
- Los 3 prompts funcionan con machine poblada (muestran datos reales)
- `mod/legislativa` puede sustituir cualquiera de ellos sin conflicto
