# Respuestas del PO — cristalizador-sdk

## Punto 1 — Estatus del Cristalizador

- **Respuesta del usuario:** es un agente de `main`; los mods lo usan si no lo customizan.
- **Efecto operativo:** el dossier trata `.github/agents/cristalizador.agent.md` como contrato por defecto y cualquier override en `mod/agents/` como especialización, no como origen.

## Punto 2 — Frontera de escritura en ramas mod

- **Respuesta del usuario:** en ramas `mod/*`, `.github/` es readonly; el Cristalizador vigila esto y su carpeta de trabajo es `mod/`, extendiendo desde `.github/`.
- **Efecto operativo:** el dossier fija un comportamiento branch-aware y prohíbe que el agente parchee `.github/` desde un mod salvo que esté trabajando expresamente en `main`.

## Punto 3 — Uso de `COPILOT/`

- **Respuesta del usuario:** el Cristalizador escucha lo que se le pide, busca siempre en la documentación oficial de `COPILOT/` y pacta con el usuario si puede maximizar el uso.
- **Efecto operativo:** el refactor debe sustituir la lista estática de docs por un protocolo de consulta real y una salida que explicite qué documentación se ha usado.

## Punto 4 — Alerta de obsolescencia

- **Respuesta del usuario:** necesita un sistema de alerta que pida actualizar `COPILOT/` bajando la información cuando toque.
- **Efecto operativo:** el dossier abre una línea específica de gobernanza y warning de frescura; se admite dejar abierta la implementación exacta si el entorno obliga a fallback sin hooks.

## Punto 5 — Alcance del dossier

- **Respuesta del usuario:** necesita el dossier en `main` para modernizar y refactorizar el Cristalizador al nuevo ecosistema.
- **Efecto operativo:** el dossier queda planteado como backlog SDK. No depende de un lore concreto y toma el archivo de `mod/legislativa` como evidencia histórica, no como contrato local.