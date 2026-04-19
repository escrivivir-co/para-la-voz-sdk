# TASK-03 — Gobernanza de `COPILOT/` y alerta

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CR-01
> **Entrega esperada:** contrato de frescura de `COPILOT/` materializado en `main`

## Lee primero

1. `README.md` § `COPILOT/ — Sincronización mensual`
2. `COPILOT/indice.md`
3. `COPILOT/hooks.instructions.md` — hooks y límites de preview
4. `COPILOT/custom-agents.instructions.md` — hooks scoped al agente
5. `COPILOT/language-models.instructions.md` — gating de modelos, opt-ins y premium requests
6. `.github/hooks/post-feed.json` — estilo actual de hooks del workspace
7. `.github/agents/cristalizador.agent.md` refactorizado por CR-01

## Objetivo

Crear una capa auditable para saber si `COPILOT/` está fresco y para que el Cristalizador pueda alertar al usuario cuando la maximización propuesta descansa sobre documentación potencialmente vencida o incompleta.

## Cambios requeridos

1. **Manifest de sync:** ampliar `COPILOT/indice.md` o crear un artefacto equivalente con origen, fecha de última actualización y familias documentales cubiertas.
2. **Política de warning:** definir cuándo una documentación se considera suficientemente desactualizada como para merecer aviso antes de usarla como base fuerte de diseño.
3. **Hook opcional, no obligatorio:** si el entorno soporta hooks, definir un warning automático scoped al Cristalizador o al workspace.
4. **Fallback sin hooks:** si no hay hooks o están deshabilitados, el agente o `/design` deben poder emitir el warning manualmente leyendo el manifest.
5. **Impacto explicado:** el warning debe decir qué falta o qué está viejo y por qué eso afecta a la propuesta.
6. **No bloquear por defecto:** salvo ausencia crítica de información, la alerta avisa y ofrece update; no convierte el Cristalizador en un agente inmóvil.

## Punto abierto admitido

La implementación final puede quedar en una de estas formas:

- hook scoped al agente
- hook de workspace
- chequeo manual del agente
- combinación de hook + chequeo manual

La task cierra si el comportamiento queda especificado y materializado con fallback robusto, no si fuerza una sola tecnología.

## Criterio de aceptación

- Existe una fuente canónica para saber cuándo se actualizó `COPILOT/`.
- El Cristalizador puede justificar por qué avisa que la documentación está vieja.
- La solución no depende en exclusiva de hooks preview.
- El usuario recibe una propuesta clara para actualizar `COPILOT/` cuando el warning aplica.