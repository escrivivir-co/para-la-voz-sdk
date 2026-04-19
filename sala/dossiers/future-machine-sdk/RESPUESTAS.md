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