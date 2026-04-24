# TASK-05 — Validación de la cadena completa con universo-1

> **Estado:** pendiente (reescrito 19-abr-2026 por Claude Opus 4.6)
> **Agente recomendado:** `Pipeline` + `Explore`
> **Dependencias:** dossiers hermanos (`cadena-agentica`, `grafo-json`, `pipeline-operativo`)
> **Entrega esperada:** `DRAFTS2/future-machine-universo-1/ENTREGA_FM-05_VALIDACION.md`

## Lee primero

- [Plan inicial local](../PLAN_FUTURE_MACHINE_UNIVERSO1.md) — incluye adenda 19-abr
- [Respuestas del usuario](../RESPUESTAS_USUARIO_FUTURE_MACHINE_UNIVERSO1.md) — incluye puntos 9-11
- [Plan madre del sprint](../../PLAN_UNIVERSO1_V2.md)
- [Grafo principal](../../LORE_F-02_UNIVERSO.md)
- [Rama universo-1](../../universo/universo-1.md)
- [Redirect canónico de corpus](../../../corpus/corpus.md)
- [Onboarding map](../../../mod/instructions/onboarding-map.instructions.md) — big picture de la cadena

## Objetivo

Comprobar que la **cadena de 5 agentes** (Puzzle → Archivero Lore → Grafista → Demiurgo → Dramaturgo Cortos) produce un resultado válido end-to-end usando `universo-1` como caso de prueba.

## Secuencia sugerida

1. **`Explore`** hace auditoría read-only:
   - ¿Todos los agentes del mod están creados y wired? (`mod/agents/`)
   - ¿Las instrucciones existen? (`lore-schema`, `lore-estado`, `lore-routing`, `onboarding-map`)
   - ¿Los prompts nuevos funcionan? (`/empieza-aqui`, `/status-lore`, `/ingest-lore`, `/refresh`, `/corto-universo`)
   - ¿Las rutas temporales de FM-01 siguen siendo necesarias o ya hay rutas canónicas?

2. **`Pipeline`** ejecuta `/refresh` y reporta:
   - ¿Se puede ingestar el pack completo de piezas?
   - ¿El corpus se genera correctamente?
   - ¿El grafo se genera (Markdown o JSON según estado de migración)?
   - ¿`universo-1` es alcanzable desde el grafo?

3. **`Dramaturgo Cortos`** genera un corto de prueba desde `universo-1`:
   - ¿El corto respeta los datos duros del corpus?
   - ¿El resultado es coherente con PLAN_UNIVERSO1_V2.md?

## Checks mínimos

### A. Cadena de agentes
- [ ] Los 5 agentes del mod existen y tienen handoffs correctos
- [ ] Pipeline orquesta la cadena sin errores manuales
- [ ] La cadena es ejecutable de punta a punta (aunque sea con intervención)

### B. Datos
- [ ] El lore vivo en DRAFTS2/ es alcanzable por los agentes
- [ ] CORPUS_PREVIEW.md refleja las 51 piezas
- [ ] El grafo tiene los 19 nodos y 4 ramas documentados

### C. Producción
- [ ] `universo-1` sigue siendo usable como fuente para Dramaturgo Cortos
- [ ] Un corto generado no contradice PLAN_UNIVERSO1_V2.md
- [ ] El flujo existente de `/corto-universo` no se ha degradado

### D. UX
- [ ] `/empieza-aqui` presenta el mapa completo
- [ ] `/status-lore` devuelve el dashboard con datos reales
- [ ] El Portal del mod ofrece handoffs operativos

## Criterio de aceptación

La validación deja evidencia suficiente para cerrar el feature o para abrir una segunda iteración acotada. Si los dossiers hermanos no están implementados aún, la validación documenta qué falta y establece el orden de ejecución recomendado.