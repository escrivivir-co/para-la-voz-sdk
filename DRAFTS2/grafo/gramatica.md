# Gramática JSON del Grafo de Universos

> **Versión:** 1.0
> **Target:** Humanos y agentes consumidores (`@Grafista`, `@Demiurgo`)
> **Referencia:** Esta especificación rige los ficheros JSON bajo `DRAFTS2/grafo/` para el mod legislativa.

Esta gramática define cómo se estructura el grafo de futuros ramificados (universos) en formato JSON, permitiendo trazabilidad estricta contra el corpus documental.

---

## 1. Estructura del Grafo

El grafo se compone de cuatro ficheros fuertemente tipados:

*   `index.json` — Metadatos, versión y estadísticas del grafo.
*   `nodos.json` — Vértices del grafo (presente, puntos de bifurcación, futuros).
*   `arcos.json` — Conectores dirigidos entre nodos.
*   `huecos.json` — Preguntas o vacíos estructurales explícitos.

---

## 2. Definición de Nodos (`nodos.json`)

Los nodos representan unidades discretas de estado, eventos o contextos dentro de una línea temporal.

### Campos obligatorios por nodo
*   `id` (String): Identificador único del nodo.
*   `tipo` (String): Clasificación funcional del nodo.
*   `estrato` (String): Coordenada temporal a la que pertenece.
*   `contenido` (String): Descripción textual en lenguaje natural descriptivo.
*   `piezas_ancla` (Array de Strings): Referencias exactas a IDs del corpus que sostienen este nodo. (Puede estar vacío `[]` si es puramente especulativo en futuros lejanos, sujeto a reglas de validación).
*   `plausibilidad` (String | null): `alta`, `media`, `baja` (generalmente para ramas y pivotes) o `null`.
*   `metadatos` (Object): Objeto abierto y extensible para atributos específicos (ej. `direccion` en un pivote).

### Tipos de nodo autorizados
1.  **`estado`**: Hecho probado, situación actual inmutable o contexto factual documentado.
2.  **`bifurcacion`**: Nodo pivote (evento futuro) donde la línea se parte en varias salidas excluyentes (ej. veredicto, resolución judicial).
3.  **`rama`**: Posibilidad futura materializada tras una bifurcación (estado especulativo o derivado).
4.  **`hueco`**: Vacío de información o tensión no resuelta en la historia que afecta otros nodos.

*(Nota: Los huecos principales también se catalogan al detalle en `huecos.json`, pero pueden existir representados como vértices en el grafo si son precondición temporal de otro nodo).*

### Estratos temporales
Orden cronológico estricto:
1.  **`T0`**: Presente. Cobertura del estado factual actual y la base documentada.
2.  **`T0-X`**: Tiempo de descuento (arco hacia el pivote). Tiempo real de espera documentado.
3.  **`X`**: El Pivote. Escenario central de bifurcación, momento de resolución del evento disruptivo.
4.  **`X-Tinf`**: Tiempo de post-resolución (futuro, salidas del pivote). Donde habitan los universos ramificados.

### Formato de IDs
*   **Nodos regulares (T0, X-Tinf):** Formato `<estrato>.<número>` o `<rama>.<número>` (ej. `0.1`, `0.2`, `R4.1`, `R1.2`).
*   **Pivot Central (X):** ID nominal exacto `X`.
*   **Entradas del Pivot:** IDs nominales direccionales paralelos, típicamente `X-A`, `X-B`, `X-C`, `X-D`.

---

## 3. Definición de Arcos (`arcos.json`)

Conexiones lógicas y temporales que arman la red. Son arcos dirigidos (origen → destino).

### Campos
*   `origen` (String): ID de un nodo existente.
*   `destino` (String): ID de un nodo existente.
*   *Restricción de integridad*: Ambos extremos (`origen` y `destino`) **deben existir obligatoriamente** dentro de `nodos.json`.
*   `peso` (Number | null): Fuerza de correlación o probabilidad matemática (opcional).
*   `justificacion` (String): Razón lógico-narrativa de la conexión. Eje central del enlace (ej. "Directo: el veredicto resuelve la espera").
*   `piezas_ancla` (Array de Strings): Documentos del corpus que prueban la relación entre los dos nodos (ej. `["T-12"]`). Opcional o vacío para conexiones lógicamente derivadas en `X-Tinf`.

---

## 4. Huecos explícitos (`huecos.json`)

La incertidumbre se debe modelar como data, no como texto literario. Los antiguos comodines literarios `[?]` en el Markdown original deben estar totalmente encapsulados en este fichero.

### Campos
*   `id` (String): Típicamente formato secuencial `H-01`, `H-02`.
*   `descripcion` (String): Formulación de la duda, agujero en el relato procesal o tensión abierta.
*   `nodos_afectados` (Array de Strings): Lista de IDs de nodos dependientes o afectados por esta incógnita.
*   `estado` (String): Ej. `abierto`, `parcialmente resuelto`, `resuelto`.
*   `resolucion` (String | null): Si fue resuelto o cerrado, justificación textual del motivo.

---

## 5. Regla Suprema: Vocabulario Cerrado

**Toda pieza designada como `pieza_ancla` en un nodo o en un arco DEBE existir incondicionalmente en el corpus oficial** (actualmente actuando `CORPUS_PREVIEW.md` como fuente de verdad).

*   La validación de la gramática requiere parsear `nodos.json` y `arcos.json`, recolectar todos los stubs (ej. `T-12`, `N-04`, `S-10`) y comprobar que la definición existe tipificada en el corpus.
*   Si un nodo contiene `N-99` y la ref no está en el mapa acumulativo: es un **error crítico de gramática**. El lore no permite alucinación de referencias (Regla - 0 invenciones).

---

## 6. Versionado y Metadatos (`index.json`)

El control de gramática se apoya en `index.json`.

*   Posee la ruta estricta para resolver las validaciones: `corpus_ref` y `artefacto_ref`.
*   Presente el valor semver en el campo `version` (ej. `"1.0"`).
*   **Regla de aumento:** Si las claves dentro de `nodos`, la tipología obligatoria, los estratos admitidos o las directivas de enlace de `arcos` cambian estructuralmente en un futuro, el versionado del `index.json` obligatoriamente cambiará (ej. `1.1` o `2.0`). Los consumidores (`@Grafista`, `@Demiurgo`) leen la versión para saber qué parser aplicar.
