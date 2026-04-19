# PLAN INICIAL — Cristalización del grafo JSON

> **Fecha:** 19-abr-2026
> **Modelo:** `Claude Opus 4.6`
> **Estado:** abierto
> **Anclas:** `DRAFTS2/LORE_F-02_UNIVERSO.md`, `DRAFTS2/LORE_F-02_ARTEFACTO.md`, `DRAFTS2/CORPUS_PREVIEW.md`
> **Protocolo:** según `mod/skills/cristalizacion-feature/SKILL.md`

---

## [Claude Opus 4.6] Inicialización del plan base

Este dossier cubre la migración del grafo de bifurcación del lore legislativa de formato Markdown narrativo a una **gramática JSON estructurada** consumible por agentes.

---

## 1. Contexto DRY

| Qué | Dónde | Estado |
|-----|-------|--------|
| Grafo actual (Markdown) | [LORE_F-02_UNIVERSO.md](../LORE_F-02_UNIVERSO.md) | 19 nodos, 4 ramas, pivote X con 4 direcciones |
| Artefacto de construcción | [LORE_F-02_ARTEFACTO.md](../LORE_F-02_ARTEFACTO.md) | 6 reglas vinculantes, ficha técnica |
| Corpus fuente | [CORPUS_PREVIEW.md](../CORPUS_PREVIEW.md) | Taxonomía y linajes para validar nodos |
| Ramas expandidas | [DRAFTS2/universo/](../universo/) | 3 universos (R4, R1, R2) |
| Grafista (consumidor) | [mod/agents/grafista.agent.md](../../mod/agents/grafista.agent.md) | Genera grafo, hoy lee Markdown |
| Demiurgo (consumidor) | — | Leerá grafo para diseñar universos (ver dossier `cristalizacion-cadena-agentica/`) |

## 2. Agentes involucrados

- **`@Cristalizador`** — diseña la gramática y crea los ficheros JSON iniciales.
- **`@Grafista`** — consumidor principal: leerá y escribirá el grafo en JSON.
- **`@Demiurgo`** — consumidor: leerá el grafo para instanciar universos.

## 3. Restricciones

- No tocar `.github/`.
- La gramática es del mod (genérica legislativa), no del caso.
- Los datos del caso (los 19 nodos actuales) son la primera instancia de la gramática.
- **Regla fundamental:** el grafo JSON solo acepta términos que estén identificados en el corpus (`CORPUS_PREVIEW.md`). Si un nodo referencia una pieza o concepto que no existe en el corpus, es error.
- El Markdown actual (`LORE_F-02_UNIVERSO.md`) se preserva como legacy y referencia. No se elimina.

---

## 4. Diseño de la gramática

### 4.1. Estructura de ficheros

```
DRAFTS2/grafo/
├── index.json        # Metadatos del grafo: caso, fecha, versión, referencia a corpus
├── nodos.json        # Array de nodos con ID, contenido, piezas ancla, estrato temporal
├── arcos.json        # Array de arcos: origen→destino, peso, justificación
├── huecos.json       # Array de huecos no resueltos (los H* del artefacto)
└── gramatica.md      # Spec legible de la gramática: reglas de validación, tipos, restricciones
```

### 4.2. Schema de `index.json`

```json
{
  "version": "1.0",
  "caso": "Zoowoman / caso Feo",
  "corpus_ref": "DRAFTS2/CORPUS_PREVIEW.md",
  "artefacto_ref": "DRAFTS2/LORE_F-02_ARTEFACTO.md",
  "hilo_ref": "DRAFTS2/LORE_F.md",
  "fecha_generacion": "2026-04-19",
  "fecha_corte_corpus": "2026-04-18",
  "estadisticas": {
    "nodos": 19,
    "arcos": 10,
    "ramas": 4,
    "huecos": 0,
    "universos_instanciados": 3
  }
}
```

### 4.3. Schema de `nodos.json`

```json
[
  {
    "id": "0.1",
    "estrato": "T0",
    "contenido": "Veredicto pendiente: fecha candidata 21-abr, desplazable",
    "piezas_ancla": ["T-12", "T-14", "R-09"],
    "tipo": "estado",
    "plausibilidad": null,
    "metadatos": {}
  },
  {
    "id": "X-A",
    "estrato": "X",
    "contenido": "Salida favorable: no se encuentra ánimo de lucro suficiente",
    "piezas_ancla": ["T-12", "T-13", "N-04"],
    "tipo": "bifurcacion",
    "plausibilidad": "media",
    "metadatos": {
      "direccion": "favorable"
    }
  }
]
```

**Tipos de nodo:** `estado`, `bifurcacion`, `rama`, `hueco`.
**Estratos temporales:** `T0` (presente), `T0-X` (arco hacia pivote), `X` (pivote), `X-Tinf` (post-pivote).

### 4.4. Schema de `arcos.json`

```json
[
  {
    "origen": "0.1",
    "destino": "X",
    "peso": null,
    "justificacion": "Directo: el veredicto resuelve la espera",
    "piezas_ancla": ["T-12", "T-14"]
  }
]
```

**Regla de validación:** toda pieza_ancla en un arco o nodo debe existir como pieza tipada en el corpus. Si no existe, es error de gramática.

### 4.5. Schema de `huecos.json`

```json
[
  {
    "id": "H-01",
    "descripcion": "¿Cuál será la reacción del juez ante la segunda ola mediática?",
    "nodos_afectados": ["0.6", "X"],
    "estado": "abierto",
    "resolucion": null
  }
]
```

### 4.6. Reglas de la gramática

1. **Vocabulario cerrado:** Solo se aceptan piezas ancla que existan en el corpus. Se valida contra `CORPUS_PREVIEW.md`.
2. **IDs únicos:** Cada nodo tiene un ID único dentro de su estrato. El formato es `<estrato>.<número>` o un ID nominal para pivote (`X`, `X-A`, etc.).
3. **Arcos tipados:** Todo arco tiene origen y destino que referencian IDs existentes en `nodos.json`.
4. **Huecos declarados:** Los huecos que el artefacto identifica como no resueltos se registran explícitamente, no se dejan como texto suelto.
5. **Metadatos extensibles:** Cada nodo puede tener `metadatos` como objeto abierto para atributos específicos del caso.
6. **Versionado:** `index.json` tiene versión de gramática. Si la gramática cambia, se incrementa.

---

## 5. Plan de migración

| Paso | Acción | Input | Output |
|------|--------|-------|--------|
| 1 | Escribir `gramatica.md` | Secciones §4.2–§4.6 de este plan | `DRAFTS2/grafo/gramatica.md` |
| 2 | Migrar nodos T0 | `LORE_F-02_UNIVERSO.md` §T=0 | Entradas 0.1–0.8 en `nodos.json` |
| 3 | Migrar arcos T0→X | `LORE_F-02_UNIVERSO.md` §Arcos | `arcos.json` |
| 4 | Migrar pivote X | `LORE_F-02_UNIVERSO.md` §Pivote | Entradas X-A..X-D en `nodos.json` |
| 5 | Migrar ramas R1..R4 | `LORE_F-02_UNIVERSO.md` §Ramas + detalle | Entradas R*.N en `nodos.json` + arcos |
| 6 | Extraer huecos | Artefacto + UNIVERSO (los `[?]` y `H*`) | `huecos.json` |
| 7 | Generar `index.json` | Estadísticas de pasos 2–6 | `index.json` |
| 8 | Validar vocabulario | `nodos.json` + `arcos.json` vs `CORPUS_PREVIEW.md` | Informe de validación |

---

## 6. Resumen de entregas

| # | Artefacto | Ruta | Tipo | Dependencias |
|---|-----------|------|------|-------------|
| GJ-01 | Gramática legible | `DRAFTS2/grafo/gramatica.md` | spec | Ninguna |
| GJ-02 | Nodos JSON | `DRAFTS2/grafo/nodos.json` | datos | GJ-01 |
| GJ-03 | Arcos JSON | `DRAFTS2/grafo/arcos.json` | datos | GJ-01 |
| GJ-04 | Huecos JSON | `DRAFTS2/grafo/huecos.json` | datos | GJ-01 |
| GJ-05 | Índice JSON | `DRAFTS2/grafo/index.json` | metadatos | GJ-02..GJ-04 |
| GJ-06 | Validación de vocabulario | informe en dossier | validación | GJ-02..GJ-05 |
| GJ-07 | Update Grafista para JSON | edición `grafista.agent.md` | refactor | GJ-05 + dossier cadena-agéntica |

---

## Salida operativa

- Tracking: [BACKLOG_GRAFO_JSON.md](./BACKLOG_GRAFO_JSON.md)
- Respuestas: [RESPUESTAS_USUARIO_GRAFO_JSON.md](./RESPUESTAS_USUARIO_GRAFO_JSON.md)
- Tasks: carpeta [tasks](./tasks)
