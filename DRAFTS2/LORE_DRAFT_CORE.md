# FEAT-03 — Refactor de `LORE_F.md`

> **Tipo:** issue editorial / Carril D del [LORE_PLAN.md](LORE_PLAN.md)
> **Prioridad:** alta — el hilo narrativo es la salida principal del lore
> **Bloqueado por:** nada (todo el input necesario ya existe en el corpus)
> **Afecta a:** `LORE_F.md` (no cambia el total de piezas, solo reescribe el concentrado)

---

## Problema

`LORE_F.md` fue escrita como mock de datos antes de que existieran los soportes documentales `[S-01]`, `[S-02]`, `[S-03]`, `[N-02]`, `[N-03]`. Ahora que el corpus ha crecido con transcripciones completas, verbatim de prensa y fichas consolidadas, el hilo narrativo:

1. **No absorbe la nueva evidencia**: `[S-01]` y `[S-02]` aparecen en una sola línea cada uno ("Feo publica un video"). Los testimonios directos con su material sobre lucro, ecosistema, defensa del proyecto y consignas no están integrados.

2. **Presupone culpabilidad en algunos pasajes**:
   - §2 `[T-08]`: *"'Apropiarse' [...] es el mismo acto jurídico con licencia (legal) o sin ella (delito)"* — describe el marco legal como si la tipificación del delito estuviera ya establecida para este caso.
   - El texto no distingue con suficiente claridad entre lo que la acusación sostiene y lo que está probado.

3. **No integra los contrapesos documentales** que ahora existen:
   - `[S-02]`: Feo discute los ~12.000€ vs 870.000€, el concepto de "ecosistema", la edición en papel del Diario de Burgos.
   - `[S-03]`: Cristóbal cuestiona la base empírica del lucro cesante, formula FlixOlé como "Zoowoman de pago".
   - `[N-02]` vs `[N-03]`: los dos encuadres de prensa (criminalizante vs preservación cultural) ya están disponibles pero no producen tensión narrativa en F.

4. **Las fichas nuevas (`[P-01]`, `[P-09]`, `[T-09]`, `[T-13]`) consolidan material disperso** que F debería poder referenciar o absorber en vez de repetir.

---

## Pasajes a revisar

| Sección | Línea aprox. | Problema | Acción |
|---------|-------------|----------|--------|
| §2 `[T-08]` | L126 | "sin ella (delito)" — tipifica antes de que haya sentencia | Reformular: el marco legal tipifica el acto, pero en este caso la defensa y la acusación discuten si se dan los elementos del tipo |
| §2 `[T-09]` | L128 | Bien equilibrado, pero puede absorber material de `[T-09]` ficha | Expandir con la tabla de categorías |
| §3 `[S-01]`+`[S-02]` | L153 | Una línea para cada testimonio — ahora hay transcripciones completas | Expandir: integrar las posiciones de Feo sobre el proyecto, el lucro, el ecosistema |
| §3 `[N-03]` | L136-139 | Bien manejado (nota que el titular "adelanta culpabilidad") — mantener | Solo vincular con `[S-02]` donde Feo responde a la edición en papel |
| §4 `[S-03]` | L160-165 | Razonablemente denso pero no integra la lectura de oportunismo económico ni la pregunta sobre estudio de mercado | Absorber material de la ficha `[S-03]` |
| §4 general | L156-180 | Mock prospectivo: `[S-05]`…`[S-08]` son placeholders | Decisión: mantener como mock o eliminar hasta que haya material real (Carril B) |

---

## Regla de prudencia para la reescritura

Directamente de [LORE_PLAN.md](LORE_PLAN.md) §3.3:

> El lore no debe convertir imputación en culpabilidad probada.
> Cuando el corpus solo permite decir que algo se imputa, presume o acusa, así debe quedar escrito.

---

## Input disponible

| Fuente | Tipo | Fichero |
|--------|------|---------|
| Feo — detención | Transcripción completa | [LORE_S-01.md](LORE_S-01.md) |
| Feo — post-juicio | Transcripción completa | [LORE_S-02.md](LORE_S-02.md) |
| Cristóbal — análisis | Transcripción GPU completa | [LORE_S-03.md](LORE_S-03.md) |
| Diario Socialista | Verbatim web | [LORE_N-02.md](LORE_N-02.md) |
| Diario de Burgos | Verbatim anuncio | [LORE_N-03.md](LORE_N-03.md) |
| Feo — ficha personaje | Derivada corpus | [LORE_P-01.md](LORE_P-01.md) |
| Cerezo — ficha personaje | Derivada corpus | [LORE_P-09.md](LORE_P-09.md) |
| Lucro — ficha fase | Consolidación | [LORE_T-09.md](LORE_T-09.md) |
| Penas — ficha fase | Consolidación | [LORE_T-13.md](LORE_T-13.md) |
| Cantera cruda | Draft original | [LORE_DRAFT.md](LORE_DRAFT.md) |

---

## Definition of Done (de [LORE_PLAN.md](LORE_PLAN.md) §6.4)

- [ ] Usa el corpus actualizado
- [ ] No sentencia antes del veredicto
- [ ] Absorbe los contrapesos documentales entre piezas
- [ ] Conserva la función de relato mínimo robusto que usa todas las marcas