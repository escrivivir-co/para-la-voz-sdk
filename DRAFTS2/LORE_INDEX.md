# LORE — Inventario de piezas mock para validación del plan

> **Estado:** lluvia de ideas en bruto — pendiente de formalización pieza a pieza
> **Uso:** cada pieza lleva marca `[P-XX]` (personaje), `[S-XX]` (pieza social),
> `[T-XX]` (fase temporal), `[R-XX]` (recurso contextual), `[N-XX]` (noticia/caso).
> Las marcas son estables: se pueden referenciar desde los bloques del plan
> y desde la entrada documental.
>
> **Draft original:** [LORE_DRAFT.md](LORE_DRAFT.md) (lluvia de ideas verbatim, no tocar)
> **Fichero monolítico:** [LORE.md](LORE.md) (versión limpia y marcada, todo junto)

---

## Índice de bloques

| Bloque | Título | Piezas | Fichero |
|--------|--------|--------|---------|
| A | Personajes | `[P-01]`…`[P-09]` (9) | [LORE_A.md](LORE_A.md) |
| B | Piezas de redes sociales | `[S-01]`…`[S-08]` (8) | [LORE_B.md](LORE_B.md) |
| C | Noticias / Casos oficiales | `[N-01]`…`[N-02]` (2) | [LORE_C.md](LORE_C.md) |
| D | Meta-fases cronológicas | `[T-01]`…`[T-14]` (14) | [LORE_D.md](LORE_D.md) |
| E | Recursos contextuales | `[R-01]`…`[R-08]` (8) | [LORE_E.md](LORE_E.md) |
| **F** | **Hilo narrativo — 1ª mitad (T-∞ → presente)** | todas (41) | [LORE_F.md](LORE_F.md) |

**Total:** 41 piezas

---

## Mapa de referencias cruzadas

```
Personajes [P-*] ──producen──→ Piezas sociales [S-*]
                                    │
Noticias [N-*] ←──protagoniza──── [P-09]
                                    │
Fases [T-*] ──contexto temporal──→ todo el inventario
                                    │
Recursos [R-*] ──enmarcan──→ Fases [T-*] + Piezas [S-*]
```

---

## Convenciones

- **Marcas estables:** una vez asignada, la marca no se reasigna a otra pieza.
- **(+)** después de una pieza indica emergencia (no estaba en el draft original, surgió del proceso).
- Las correcciones ortográficas se hacen en los bloques; el [draft original](LORE_DRAFT.md) conserva las erratas.
- Cada bloque es autónomo: se puede leer sin contexto del índice.
