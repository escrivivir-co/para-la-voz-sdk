# TASK-06 — Validación de vocabulario

> **Estado:** pendiente
> **Agente recomendado:** `Grafista`
> **Dependencias:** GJ-05
> **Entrega esperada:** `DRAFTS2/cristalizacion-grafo-json/ENTREGA_GJ-06_VALIDACION.md`

## Lee primero

- [gramatica.md](../../grafo/gramatica.md) — regla de vocabulario cerrado
- [CORPUS_PREVIEW.md](../../CORPUS_PREVIEW.md) — fuente de vocabulario válido
- Los 4 ficheros JSON en `DRAFTS2/grafo/`

## Objetivo

Verificar que todas las piezas ancla referenciadas en `nodos.json` y `arcos.json` existen como piezas en el corpus. Identificar violaciones.

## Secuencia de validación

1. Extraer todas las piezas ancla únicas de `nodos.json` y `arcos.json`.
2. Extraer todas las piezas tipadas de `CORPUS_PREVIEW.md` (marcas `[P-NN]`, `[S-NN]`, etc.).
3. Calcular: piezas en grafo pero no en corpus (error), piezas en corpus pero no en grafo (info: cobertura).
4. Documentar resultado.

## Criterio de aceptación

Cero piezas en grafo que no existan en corpus. El porcentaje de cobertura del corpus por el grafo se documenta como dato.
