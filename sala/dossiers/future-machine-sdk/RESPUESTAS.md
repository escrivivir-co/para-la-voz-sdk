# Respuestas del usuario — future-machine-sdk

> **Fecha:** 19-abr-2026
> **Registradas por:** GPT-5.4

## Punto 1 — Hay que exportar la future-machine a main

- **Contexto:** El usuario pide retomar el último dossier, `future-machine`, y rediseñarlo para exportarlo de la rama `mod` a `main`.
- **Respuesta del usuario (19-abr-2026):** quiere el mismo patrón de doble dossier que el resto de capas.
- **Efecto operativo:** Se crea `future-machine-sdk` como contraparte main del cierre de ciclo.

## Punto 2 — La future-machine no duplica capas, las compone en slots

- **Contexto:** El usuario aclara que quiere una estructura con slots donde van los otros dossiers.
- **Respuesta del usuario (19-abr-2026):** “estructura con slots donde van los otros dosieres”.
- **Efecto operativo:** El SDK no crea otra capa de datos. Crea una carcasa compositiva con slots para `lore-db`, `corpus`, `grafo`, `universos`, `cortos`, `Portal` y `Pipeline`.

## Punto 3 — Tiene que cerrar el ciclo y conectar con Portal

- **Contexto:** El usuario pregunta si esto es el cierre de todo el ciclo y exige conexión con `Portal`, `empezar aquí` y superficies similares.
- **Respuesta del usuario (19-abr-2026):** lo plantea explícitamente como cierre del ciclo completo.
- **Efecto operativo:** `future-machine-sdk` se diseña como contrato de navegación y orquestación del ciclo completo, con entrypoints declarables para Portal, status y refresh.

## Punto 4 — Refactor agente-oriented: Pipeline sube a main, tabla del pipeline como frontal

- **Contexto:** El usuario pide dejar de tratar el dossier como boilerplate y hacerlo agent-oriented. Confirma que `@Pipeline` (validado en mod/legislativa) debe subir a main como agente SDK genérico. Pide que la tabla del pipeline completo (agente, ficheros, I/O) sea el frontal del dossier.
- **Respuesta del usuario (19-abr-2026):** "Cuadra perfectamente tanto que se la vamos a poner verbatim literal en el frontal del dosier".
- **Efecto operativo:**
  - Se añaden FS-05 (`@Pipeline` SDK) y FS-06 (3 prompts de entrypoint) al backlog.
  - FS-04 (documentación de cierre) pasa a depender de FS-05 y FS-06.
  - La sección 0 del PLAN pasa a ser la tabla del pipeline completo (main + mod/legislativa + datos pendientes de migración).
  - Se incluyen notas pendientes para dossiers hermanos: dualidad piezas/LORE_F, protocolo de acumulación del merge, doble fuente del grafo, universo como variables+inicializaciones, cortos como output final.

## Punto 5 — Ideas de rediseño para dossiers hermanos

- **Contexto:** El usuario aporta ideas específicas durante la sesión de asesoría que afectan a los dossiers individuales, no solo a future-machine.
- **Respuesta del usuario (19-abr-2026):** dicta las ideas en bruto para que se registren como notas.
- **Efecto operativo:** Se registran en sección 7 del PLAN como notas pendientes para cada dossier hermano. No se modifican los dossiers hermanos directamente.