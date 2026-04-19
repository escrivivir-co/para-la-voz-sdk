# Respuestas del usuario — grafo-sdk

> **Fecha:** 19-abr-2026
> **Registradas por:** Claude Opus 4.6

## Punto 1 — Separación SDK / mod para grafo

- **Contexto:** El grafo de bifurcación y su gramática JSON viven hoy en mod/legislativa. futures-engine y Dramaturgo ya son SDK.
- **Respuesta del usuario (19-abr-2026):** "Tenemos que hacer un nuevo dossier para grafo. Igual, sacar la feature a main-sdk, y traer aquí, y entonces homogeneizar."
- **Efecto operativo:** Patrón idéntico a lore-db-sdk: extraer concepto genérico al SDK, luego el mod hereda y define tipos concretos.

## Punto 2 — ¿Grafista y Demiurgo al SDK?

- **Contexto:** Al revisar el Pipeline y la secuencia completa (`lore-db -> corpus -> grafo -> universos -> cortos`), aparece una capa explícita de universos que no debe quedar absorbida dentro de grafo.
- **Respuesta del usuario (19-abr-2026):** "adelante"
- **Efecto operativo:** En esta iteración **no** se suben `@Grafista` ni `@Demiurgo` al SDK como agentes completos. El SDK extrae la capa portable de **grafo** y la capa portable de **universo** mediante dos parejas de dossiers (`grafo-*` y `universos-*`). Grafista y Demiurgo siguen siendo especializaciones del mod por ahora.

## Punto 3 — La fase de cortos también merece pareja propia

- **Contexto:** El usuario corrige el corte y pide homogeneizar la cadena final: una fase para importar `DRAFTS2/universo/` y otra distinta para importar `LORE_F-02_CORTO-universo-X-<modelo>.md`.
- **Respuesta del usuario (19-abr-2026):** "no, no, que si salga ya separado"
- **Efecto operativo:** Nace una tercera pareja `cortos-sdk` / `cortos-legislativa`. La secuencia cristalizada queda: `grafo -> universos -> cortos`.
