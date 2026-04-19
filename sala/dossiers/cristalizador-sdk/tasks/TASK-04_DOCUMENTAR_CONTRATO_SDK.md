# TASK-04 — Documentar el contrato SDK

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** CR-02, CR-03
> **Entrega esperada:** documentación SDK del Cristalizador actualizada

## Lee primero

1. `.github/copilot-instructions.md`
2. `README.md`
3. `.github/agents/cristalizador.agent.md` tras CR-01
4. `.github/prompts/design.prompt.md` tras CR-02
5. El artefacto de gobernanza que salga de CR-03

## Objetivo

Actualizar la documentación del SDK para que el uso del Cristalizador quede explicado con el nuevo contrato: default en `main`, override opcional en mods, consulta real de `COPILOT/`, warning de frescura y pacto de maximización.

## Cambios requeridos

1. **Cristalizador como agente por defecto:** documentar que el mod lo hereda de `main` si no lo especializa.
2. **Frontera `main/mod`:** explicar que `.github/` y `COPILOT/` se leen desde ramas `mod/*`, pero los artefactos del mod viven en `mod/`.
3. **`COPILOT/` como dependencia viva:** añadir el contrato de sync/frescura y cómo el warning se manifiesta.
4. **Ciclo documental:** reforzar que `/design` es la etapa donde el SDK aprende del uso y decide nuevas piezas.
5. **Condiciones de maximización:** dejar documentado que preview, opt-ins, premium requests, plugins o MCP se pactan con el usuario.

## Criterio de aceptación

- La documentación no presenta al Cristalizador solo como "el que escribe en `mod/`".
- Queda explícita la relación `main -> mod`.
- El lector entiende cuándo el agente puede abrir warning a `main` en vez de editar upstream.
- La política de `COPILOT/` deja de ser solo una frase de "sync mensual" y pasa a ser un contrato visible.