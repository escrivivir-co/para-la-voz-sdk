# TASK ES-02 — Promover prompts sala a SDK

- **Estado:** libre
- **Agente sugerido:** cualquiera

## Descripción

Copiar los 7 prompts `sala-*.prompt.md` de `mod/prompts/` a `.github/prompts/`. Generalizar eliminando referencias específicas al lore legislativa (nombres de agentes del mod, rutas DRAFTS2, etc.).

## Ficheros

- sala-entrar.prompt.md
- sala-seguir.prompt.md
- sala-aprobar.prompt.md
- sala-reconectar.prompt.md
- sala-salir.prompt.md
- sala-archivar.prompt.md
- sala-aleph.prompt.md → **decidir**: ¿es genérico o queda en mod?

## Criterios de aceptación

1. Cada prompt existe en `.github/prompts/`
2. No contienen referencias hardcoded al lore legislativa
3. Usan variables/placeholders genéricos donde el mod debe inyectar datos específicos
4. Mantienen la estructura y semántica original
