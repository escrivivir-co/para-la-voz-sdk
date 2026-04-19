# TASK-04 — Documentar cierre de ciclo e inicialización

> **Estado:** libre
> **Agente recomendado:** cualquiera
> **Dependencias:** FS-01, FS-02, FS-03, FS-05, FS-06
> **Entrega esperada:** docs SDK + lore init actualizados

## Lee primero

1. Todo el dossier future-machine-sdk (PLAN, BACKLOG, tasks FS-01 a FS-06)
2. `.github/copilot-instructions.md` — contrato actual del SDK
3. `README.md` — docs públicos actuales

## Objetivo

Documentar la future-machine como cierre compositivo del SDK. Registrar `@Pipeline` como sexto agente core. Documentar los 3 prompts de entrypoint como ampliación de los 7 comandos base. Actualizar la tabla de la arquitectura en el contrato SDK.

## Ficheros objetivo

- `.github/copilot-instructions.md` — añadir Pipeline a la tabla de agentes, los 3 prompts a la tabla de comandos, y la sección de future-machine
- `README.md` — reflejar lo mismo en documentación pública si aplica
- documentación o scaffold asociado a `lore-db-sdk` para que `lore init` deje preparado el manifiesto vacío

## Criterio de aceptación

- El SDK documenta cómo una lore-db puede levantarse con la carcasa de machine preparada
- `@Pipeline` está documentado como agente core del SDK
- Los 3 prompts de entrypoint están documentados como comandos base del SDK
- La tabla de agentes y comandos en `copilot-instructions.md` está actualizada