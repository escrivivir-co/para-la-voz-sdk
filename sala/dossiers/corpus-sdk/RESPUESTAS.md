# Respuestas del usuario — corpus-sdk

> **Fecha:** 19-abr-2026
> **Registradas por:** GPT-5.4

## Punto 1 — La capa corpus merece dossier propio

- **Contexto:** Tras separar `grafo`, `universos` y `cortos`, el usuario pregunta si también conviene abstraer con backward compatibility el viejo eje `archivero-corpus` y el ciclo `feed -> Bartleby -> corpus`.
- **Respuesta del usuario (19-abr-2026):** "absorver con back compatibility el archivero-corpus y el ciclo de feed-bartleby-corpus"
- **Efecto operativo:** Se crea la pareja `corpus-sdk` / `corpus-legislativa` para tratar `corpus` como capa propia, no absorbida dentro de `lore-db`.

## Punto 2 — El Archivero vuelve a definirse como agente de corpus

- **Contexto:** El usuario plantea si esto equivale a "devolver convertido al archivero como corpuseador".
- **Respuesta del usuario (19-abr-2026):** pregunta abierta sobre si el corte correcto es volver a elevar esa abstracción al SDK.
- **Efecto operativo:** La recomendación que cristaliza este dossier es: `@Archivero` sigue siendo el agente de corpus. No se le devuelve la gestión de piezas, pero sí se formaliza su rol de **curación incremental + corpuseado batch** dentro del mismo dominio.

## Punto 3 — El folder `corpus/` deja de ser solo workaround objetivo

- **Contexto:** El usuario pide considerar la migración del `corpus/` adjunto y no dejarlo como shim indefinido.
- **Respuesta del usuario (19-abr-2026):** pide evaluar si tiene sentido hacerlo canónico otra vez.
- **Efecto operativo:** `corpus-sdk` toma `corpus/` como superficie pública canónica del corpus, con compatibilidad para mods que resuelven sus piezas desde `{{LORE_DIR}}/piezas/`.