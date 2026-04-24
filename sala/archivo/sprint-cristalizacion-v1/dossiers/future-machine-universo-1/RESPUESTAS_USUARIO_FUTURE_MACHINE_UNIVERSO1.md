# Respuestas del usuario — Future-machine para universo-1

> **Fecha:** 18-abr-2026
> **Registradas por:** `GPT-5.4`
> **Propósito:** fijar en disco las respuestas a los 8 puntos del plan base para evitar pérdida de contexto.

## Punto 1 — DRY en el plan

- **Respuesta del usuario:** el punto 1 necesita más DRY porque la información ya vive en `.github/` o `mod/`.
- **Efecto operativo:** el backlog no duplicará protocolo SDK ni reglas del mod; cada task enlazará a sus fuentes y solo documentará delta local.

## Punto 2 — Cristalizador ejecutor

- **Respuesta del usuario:** esto es tarea del Cristalizador; hay que darle misión amplia para explotar bien la carpeta `COPILOT/` y proponer todo lo necesario para una intervención.
- **Efecto operativo:** se crea una task específica para `@Cristalizador`, con mandato explícito de maximizar uso agéntico en `mod/`.

## Punto 3 — Rutas oficiales faltantes

- **Respuesta del usuario:** el warning era correcto; hay que crear los ficheros y carpetas oficiales que faltan con notas de redirección temporal.
- **Efecto operativo:** se inicializan `corpus/`, `corpus/corpus.md`, `mod/skills/` y `mod/universos/` como workaround documentado hacia `DRAFTS2/`.

## Punto 4 — futures-engine local del mod

- **Respuesta del usuario:** si las operaciones ya están en `.github/skills/futures-engine/SKILL.md` y no están en `mod/`, el Cristalizador debe diseñar para que el mod las tenga y el agente las implemente.
- **Efecto operativo:** se abre una task dedicada a skill local del mod, sin copiar ciegamente el core.

## Punto 5 — Ignorar salvo fallo real

- **Respuesta del usuario:** esto le corresponde a `main`; si hubiera problema, lo correcto es investigarlo y dejar warning para el equipo main. Mientras tanto, somos equipo `mod/legislativa`.
- **Efecto operativo:** el backlog deja este punto como condicional y no bloqueante.

## Punto 6 — Propuesta formal

- **Respuesta del usuario:** ok.
- **Efecto operativo:** se mantiene una task de propuesta previa a la implementación fuerte.

## Punto 7 — Implementación en mod

- **Respuesta del usuario:** ok.
- **Efecto operativo:** toda la superficie nueva del feature se implementará en `mod/`.

## Punto 8 — Validación

- **Respuesta del usuario:** la validación debe hacerse con `universo-1` y [PLAN_UNIVERSO1_V2.md](../PLAN_UNIVERSO1_V2.md).
- **Efecto operativo:** el backlog cierra el feature solo si la machine sirve para ese caso concreto.

---

## [Claude Opus 4.6] Sesión 19-abr-2026 — Decisiones adicionales

### Punto 9 — Cadena de 5 agentes absorbe FM-02..04

- **Respuesta del usuario:** la cadena Puzzle → Archivero Lore → Grafista → Demiurgo → Dramaturgo Cortos está diseñada. Los dossiers `cristalizacion-cadena-agentica/`, `cristalizacion-pipeline-operativo/` y `cristalizacion-grafo-json/` cubren lo que este dossier proponía en FM-02, FM-03 y FM-04.
- **Efecto operativo:** FM-02, FM-03 y FM-04 se marcan como **Superseded**. No cancelados: el trabajo se ha hecho, pero en otros dossiers.

### Punto 10 — Simetría lore→corpus ≈ grafo-draft→grafo-json

- **Respuesta del usuario:** "salvar el lore de DRAFTS2 para meterlo con archivador sería como salvar el grafo draft y meterlo con grafo, ¿no?" — Sí.
- **Efecto operativo:** se registra el insight: ambas son la misma operación "promover borrador a formato estructurado". La primera la ejecuta Archivero Lore, la segunda Grafista. Ambas están diseñadas en sus dossiers respectivos.

### Punto 11 — Validación ahora es contra la cadena completa

- **Respuesta del usuario:** FM-05 no puede validar solo contra Dramaturgo Cortos; tiene que validar la cadena entera.
- **Efecto operativo:** FM-05 se reescribe. Valida: (a) que la cadena de 5 produce un corto desde piezas LORE_*, (b) que el grafo JSON se genera correctamente desde el corpus, (c) que universo-1 y PLAN_UNIVERSO1_V2.md siguen siendo compatibles con la cadena.