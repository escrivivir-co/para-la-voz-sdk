# Respuestas del usuario — universos-sdk

> **Fecha:** 19-abr-2026
> **Registradas por:** GPT-5.4

## Punto 1 — Falta una pareja de dossiers para Demiurgo y universos

- **Contexto:** El usuario detecta que, cerrada la migración de lore-db y grafo, falta una capa explícita para Demiurgo y los universos persistidos.
- **Respuesta del usuario (19-abr-2026):** "adelante"
- **Efecto operativo:** Se crea la pareja `universos-sdk` / `universos-legislativa`, separada de `grafo-*`.

## Punto 2 — La migración de los universos existentes no va en el SDK

- **Contexto:** El usuario pregunta si `universos-sdk` debe incluir la migración de los 3 universos actuales.
- **Respuesta del usuario (19-abr-2026):** "adelante" sobre la propuesta de corte SDK/mod.
- **Efecto operativo:** `universos-sdk` cristaliza el contrato portable. La migración de `universo-1`, `universo-1-r1` y `universo-1-r2` queda en `universos-legislativa`.

## Punto 3 — Los cortos salen del dossier de universos

- **Contexto:** El usuario pide separar de forma homogénea la fase de universos de la fase de cortos.
- **Respuesta del usuario (19-abr-2026):** "que si salga ya separado"
- **Efecto operativo:** `universos-sdk` deja de absorber convenciones de Dramaturgo/obras. Esa capa pasa a `cortos-sdk`.