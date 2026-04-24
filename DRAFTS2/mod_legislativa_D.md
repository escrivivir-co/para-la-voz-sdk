# MOD/LEGISLATIVA — §4. BLOQUE D — Caso semilla y bootstrap del corpus

← [Bloque C](mod_legislativa_C.md) · [Índice](mod_legislativa_INDEX.md) · Siguiente: [Bloque E →](mod_legislativa_E.md)

---

### D-1. Naturaleza del caso semilla

El promotor dispone de un caso concreto que servirá como corpus fundacional.
Este caso establece el baseline del `corpus/corpus.md` — análogamente a como
la primera editorial procesada establece el baseline en el mod/restitutiva.

Las actuaciones del caso se ingresarán secuencialmente vía `/feed`, siguiendo
el orden procesal cronológico:

```
/feed corpus/actuaciones/YYYY-MM-DD_declaracion-001.md
/diff-corpus
  → aprobar
/merge-corpus
  → corpus.md baseline establecido

/feed corpus/actuaciones/YYYY-MM-DD_resolucion-001.md
/diff-corpus
  → detecta NUEVO, CONFIRMA, DISCREPA, CONTRADICE-FUENTE
  → aprobar
/merge-corpus
  → corpus.md crece

[repetir por cada actuación del caso]
```

### D-2. Orden de ingesta recomendado

DEBERÁ documentarse en el guion del caso el orden de ingesta, que
PODRÁ seguir una de estas estrategias:

| Estrategia | Descripción | Uso recomendado |
|-----------|-------------|-----------------|
| Cronológica | Orden de fecha de actuación | Casos con timeline lineal |
| Por parte | Todas las actuaciones de una parte, luego la siguiente | Casos con contradicción entre partes como eje central |
| Procesal | Orden de fases: instrucción → juicio → recurso | Casos cerrados con sentencia firme |

### D-3. Primer ciclo de cristalización

Una vez ingestadas suficientes actuaciones (mínimo: los hechos de ambas partes
+ al menos una resolución), el cristalizador PODRÁ ejecutar el primer ciclo:

```
/design → propuestas de artefactos basados en el corpus acumulado
/documento demanda → primer documento legal cristalizado
```

El Catálogo de documentos legales (`docs/catalogo.md`) se construye incrementalmente
conforme el cristalizador genera documentos.

**Backlog item:**
- [ ] **TASK D-3.1** — Preparar las actuaciones del caso semilla en `corpus/actuaciones/` con el frontmatter definido en B-4
- [ ] **TASK D-3.2** — Ejecutar el primer ciclo completo: feed → diff → merge → design → documento
- [ ] **TASK D-3.3** — Verificar que `corpus/corpus.md` refleja correctamente la acumulación procesal
