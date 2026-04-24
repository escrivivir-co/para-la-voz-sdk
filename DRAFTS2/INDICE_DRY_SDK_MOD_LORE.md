# Índice DRY — SDK, mod y lore del caso

> Ficha de referencia técnica.
> Propósito: dar acceso al materialde proyecto

---

## 1. Fórmula corta

El repositorio tiene hoy tres capas distintas que no deben confundirse:

1. El SDK agéntico de análisis documental, que vive en la rama `main` y define el protocolo general.
2. El mod jurídico proyectado, que en la rama `mod/legislativa` ya está especificado pero aún no completado como infraestructura reusable por casos.
3. El lore concreto del caso, que en esa misma rama se priorizó primero como bootstrap documental y ya produjo un primer artefacto narrativo compuesto: `LORE_F.md`.

La secuencia real de trabajo no fue: SDK → mod terminado → caso.
La secuencia real fue: SDK → especificación del mod → bootstrap del lore del caso → primer hilo narrativo → pendiente de cierre diario + pendiente de convertir el mod en infraestructura reusable con archivo/reset.

---

## 2. Índice funcional

| Capa | Artefacto | Función | Rama GitHub | Enlace |
|------|-----------|---------|-------------|--------|
| SDK | `README.md` | Define el SDK agéntico documental, la separación `main` / `mod/*` y el flujo unidireccional del pull | `main` | [SDK base](https://github.com/escrivivir-co/para-la-voz-sdk/blob/main/README.md) |
| Mod proyectado | `DRAFTS2/mod_legislativa_INDEX.md` | Especifica el mod jurídico-procesal como arquitectura objetivo y backlog por fases | `mod/legislativa` | [Especificación del mod](https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/DRAFTS2/mod_legislativa_INDEX.md) |
| Bootstrap del caso | `DRAFTS2/LORE_PLAN.md` | Ordena la extracción de piezas, la política de soportes y la refactorización del lore del caso | `mod/legislativa` | [Plan del lore](https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/DRAFTS2/LORE_PLAN.md) |
| Cantera cruda | `DRAFTS2/LORE_DRAFT.md` | Conserva el material bruto e intuiciones recuperables para no perder señales del draft inicial | `mod/legislativa` | [Draft crudo](https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/DRAFTS2/LORE_DRAFT.md) |
| Salida compuesta | `DRAFTS2/LORE_F.md` | Primer artefacto narrativo compuesto del caso; concentra las marcas limpias disponibles hasta la fecha de corte | `mod/legislativa` | [Hilo narrativo actual](https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/DRAFTS2/LORE_F.md) |
| Ciclo por casos | `DRAFTS2/mod_legislativa_F.md` | Define el mecanismo pendiente de archivo y reinicio (`/archive`, `/reset`) para reutilizar el mod caso a caso | `mod/legislativa` | [Ciclo de vida y reset](https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/DRAFTS2/mod_legislativa_F.md) |

---

## 3. Lectura correcta de la situación

### 3.1. Qué está ya resuelto

- El SDK documental existe y está definido en `main`.
- El mod `mod/legislativa` ya tiene especificación técnica suficiente para orientar su construcción.
- El trabajo concreto del caso ya dejó de ser solo borrador disperso: existe un plan explícito de producción del lore.
- Ese plan ya produjo un primer resultado compuesto, `LORE_F.md`, que funciona como salida narrativa inicial del caso.

### 3.2. Qué NO está resuelto todavía

- `LORE_F.md` no está cerrado como relato completo del caso: debe seguir absorbiendo novedades según pasen los días y aparezcan nuevas piezas.
- El mod jurídico no está aún terminado como infraestructura reusable: faltan artefactos de `mod/`, prompts, skills, layouts y decisiones operativas.
- El mecanismo de reinicio por caso no está implementado todavía: está especificado, pero no convertido aún en prompts/flujo ejecutable.
- La integración completa del lore del draft en el mod no está cerrada: hoy el lore funciona como bootstrap del caso, no como instancia ya absorbida por un mod operativo acabado.

---

## 4. Relación DRY entre documentos

Cada documento responde a una pregunta distinta:

| Pregunta | Documento de referencia |
|----------|-------------------------|
| ¿Qué es el SDK y cómo se separa de los mods? | [SDK base](https://github.com/escrivivir-co/para-la-voz-sdk/blob/main/README.md) |
| ¿Qué mod jurídico se quería crear? | [Especificación del mod](https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/DRAFTS2/mod_legislativa_INDEX.md) |
| ¿Cómo se decidió trabajar primero el caso concreto? | [Plan del lore](https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/DRAFTS2/LORE_PLAN.md) |
| ¿Qué artefacto produjo ya ese trabajo? | [Hilo narrativo actual](https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/DRAFTS2/LORE_F.md) |
| ¿De dónde se recupera material no absorbido todavía? | [Draft crudo](https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/DRAFTS2/LORE_DRAFT.md) |
| ¿Cómo debería cerrarse un caso y reiniciar el mod para otro? | [Ciclo de vida y reset](https://github.com/escrivivir-co/para-la-voz-sdk/blob/mod/legislativa/DRAFTS2/mod_legislativa_F.md) |

La regla DRY aquí es simple:

- `README.md` no debe volver a explicar el caso concreto.
- `mod_legislativa_INDEX.md` no debe rehacer el lore del caso.
- `LORE_PLAN.md` no debe redefinir todo el SDK ni toda la arquitectura del mod.
- `LORE_F.md` no debe funcionar como especificación del mod.
- `LORE_DRAFT.md` no debe citarse como salida final, sino como cantera.

---

## 5. Secuencia operativa recomendada

### 5.1. Estado actual

1. Presentar el SDK documental.
2. Señalar que se proyectó un mod jurídico nuevo.
3. Precisar que, antes de terminar ese mod, se priorizó construir el lore del caso como uso semilla.
4. Referir que ese trabajo ya produjo `LORE_F.md`.
5. Aclarar que faltan dos cierres: completar el relato según avance el caso y terminar el mod reusable con archivo/reset.

### 5.2. Estado objetivo

1. Completar el mod `mod/legislativa` según su backlog.
2. Implementar el ciclo `/archive` y `/reset` para trabajo por casos.
3. Integrar el lore ya producido como caso semilla del mod, en vez de mantenerlo solo como capa draft paralela.
4. Reutilizar ese mod ya resuelto para nuevos casos con reinicio controlado.

---

## 6. Cita breve reutilizable

> El repositorio distingue tres niveles: el SDK documental general en `main`, la especificación del mod jurídico en `mod/legislativa`, y el lore concreto del caso desarrollado en esa misma rama como bootstrap previo a la finalización del mod. Ese bootstrap ya produjo `LORE_F.md` como primer artefacto compuesto, mientras que siguen pendientes tanto el cierre diario del caso como la implementación completa del mod reusable con mecanismo de archivo y reinicio.

---

## 7. Nota de uso

Esta ficha sirve como índice de referencia. Si un texto necesita justificar la arquitectura del proyecto, debe enlazar al SDK y al mod. Si necesita justificar el estado del caso, debe enlazar al plan del lore y a `LORE_F.md`. Si necesita explicar el paso pendiente hacia un mod reusable por casos, debe enlazar al bloque de ciclo de vida y reset.

---

## 8. Dramaturgo: diseño de universos y generación de relatos

### 8.1. Feature del SDK

El SDK incluye un agente **@dramaturgo** ([`.github/agents/dramaturgo.agent.md`](https://github.com/escrivivir-co/para-la-voz-sdk/blob/main/.github/agents/dramaturgo.agent.md)) que construye **universos propios**: grafos de futuros posibles sostenidos por el corpus. Opera sobre el skill [`futures-engine`](https://github.com/escrivivir-co/para-la-voz-sdk/blob/main/.github/skills/futures-engine/SKILL.md) (protocolo de bifurcación dramatúrgica) y el comando [`/universo`](https://github.com/escrivivir-co/para-la-voz-sdk/blob/main/.github/prompts/universo.prompt.md).

El dramaturgo no inventa personajes ni hechos. Los encuentra en el corpus. Construye grafos dirigidos ponderados donde cada nodo cita piezas ancla y cada arco tiene plausibilidad estructural. Las operaciones disponibles sobre el grafo son: expandir, bifurcar, podar, reponderar, anclar, generar obra, persistir.

### 8.2. Extensión para el mod legislativa

Para este lore se creó una extensión del dramaturgo en [`mod/agents/dramaturgo.agent.md`](mod/agents/dramaturgo.agent.md) que añade la operación **generar corto desde universo**. La extensión:

- Lee el grafo principal ([`LORE_F-02_UNIVERSO.md`](LORE_F-02_UNIVERSO.md)), el detalle de la rama, el artefacto original ([`LORE_F-02_ARTEFACTO.md`](LORE_F-02_ARTEFACTO.md)) y el corto original ([`LORE_F-02_CORTO.md`](LORE_F-02_CORTO.md)) como inputs
- Carga las instrucciones específicas del mod ([`mod/instructions/legislativa-universo.instructions.md`](../mod/instructions/legislativa-universo.instructions.md)) con los datos post-artefacto (48 piezas, huecos, consignas)
- Genera la pieza literaria y la guarda con sufijo de modelo para permitir múltiples versiones
- Se invoca con el prompt [`/corto-universo`](../mod/prompts/corto-universo.prompt.md)

### 8.3. Universo-1: el contraataque (rama R4)

El grafo principal tiene 4 ramas (R1-R4). La rama R4 se expandió en detalle: 6 nodos diseñados en [`universo/universo-1.md`](universo/universo-1.md) que trazan un contraataque donde la posición de Cerezo se erosiona (demanda invertida → suspensión cautelar → doble corriente institucional/ciudadana → retirada negociada → filmotecas federadas).

Se generaron 3 relatos con 3 modelos distintos usando el mismo grafo, las mismas instrucciones y el mismo protocolo:

| Relato | Modelo | Enlace |
|--------|--------|--------|
| *Once Mil Siete* | Claude Opus 4.6 | [LORE_F-02_CORTO-universo-1-claude-opus-4.md](LORE_F-02_CORTO-universo-1-claude-opus-4.md) |
| *El Peso del Reloj* | Gemini 3.1 Pro | [LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md](LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md) |
| *El Lunes Que Tardó Un Año* | GPT-5.4 | [LORE_F-02_CORTO-universo-1-gpt-5-4.md](LORE_F-02_CORTO-universo-1-gpt-5-4.md) |

Los tres recorren R4.1→R4.6 en el mismo orden, activan las mismas consignas del corpus y cierran con la misma paradoja recursiva (el caso se cerró sin sentencia, ergo sin jurisprudencia). Son el mismo relato con distinto estilo. La variación es de prosa, no de decisión narrativa: el grafo determina el relato tan completamente que no deja espacio para que el modelo tome decisiones propias.
