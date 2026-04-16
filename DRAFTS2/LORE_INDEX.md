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
| C | Noticias / Casos oficiales | `[N-01]`…`[N-03]` (3) | [LORE_C.md](LORE_C.md) |
| D | Meta-fases cronológicas | `[T-01]`…`[T-14]` (14) | [LORE_D.md](LORE_D.md) |
| E | Recursos contextuales | `[R-01]`…`[R-08]` (8) | [LORE_E.md](LORE_E.md) |
| **F** | **Hilo narrativo — 1ª mitad (T-∞ → presente)** | todas (42) | [LORE_F.md](LORE_F.md) |

**Total:** 42 piezas

### Ficheros de soporte por pieza

- `[P-01]` → [LORE_P-01.md](LORE_P-01.md)
- `[P-09]` → [LORE_P-09.md](LORE_P-09.md)
- `[S-01]` → [LORE_S-01.md](LORE_S-01.md)
- `[S-02]` → [LORE_S-02.md](LORE_S-02.md)
- `[S-03]` → [LORE_S-03.md](LORE_S-03.md)
- `[N-02]` → [LORE_N-02.md](LORE_N-02.md)
- `[N-03]` → [LORE_N-03.md](LORE_N-03.md)
- `[T-09]` → [LORE_T-09.md](LORE_T-09.md)
- `[T-13]` → [LORE_T-13.md](LORE_T-13.md)

Estos ficheros no añaden piezas nuevas al conteo. Sirven para sacar del bloque la expansión, consolidación de material disperso o ficha derivada y dejarla reusable como soporte de trabajo.

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
