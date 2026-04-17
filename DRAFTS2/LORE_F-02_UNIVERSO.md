# Universo: Caso Zoowoman — Segunda mitad (T=0 → X → T+∞)

> **Grafo semilla** inicializado desde [LORE_F-02_ARTEFACTO.md](LORE_F-02_ARTEFACTO.md)
> **Hilo narrativo fuente:** [LORE_F.md](LORE_F.md) — primera mitad (T-∞ → presente)
> **Corpus fuente:** [CORPUS_PREVIEW.md](CORPUS_PREVIEW.md)
> **Obra derivada existente:** [LORE_F-02_CORTO.md](LORE_F-02_CORTO.md) — *Tres Lunes Para Una Misma Sala*

---

## Estructura temporal

```
T=0 (presente)  ──→  T+0.5 (espacio nuevo si R4)  ──→  X (veredicto)  ──→  T+∞
     8 nodos            R4: contraataque               pivote              ramas
```

**X** no es una fecha fija. Es el evento de resolución judicial y su ejecución efectiva. La fecha candidata es 21-abr-2026 `[T-14]`, pero X puede desplazarse por eventos internos del caso o del aparato judicial `[R-09]`. En la rama R4, X se desplaza ~1 año por suspensión cautelar.

---

## T=0 — Estado del presente (17-abr-2026)

| ID | Nodo | Piezas ancla |
|----|------|-------------|
| 0.1 | Veredicto pendiente: fecha candidata 21-abr, desplazable | `[T-12]` `[T-14]` `[R-09]` |
| 0.2 | Archivo Zoowoman destruido: la web no existe. Canal YouTube replicado en al menos 4 copias independientes `[S-11]` | `[T-06]` `[S-01]` `[S-11]` |
| 0.3 | Amplificación mediática activa: Cristóbal, N-02, Facu→Bustinduy, Bizarro, Xataka | `[S-03]` `[S-05]` `[N-02]` `[S-09]` `[N-05]` |
| 0.4 | Ánimo/dolo ni probado ni descartado: eje decisivo sin resolución. Matiz: enlazaba, no alojaba | `[N-04]` `[S-03]` `[N-05]` |
| 0.5 | Pena solicitada: 3 ejes (económico, prisión, social) `[T-13]` | `[T-13]` `[T-09]` |
| 0.6 | Segunda cola mediática + datos duros de Cerezo | `[S-06]` `[S-07]` `[S-08]` `[S-09]` |
| 0.7 | Canal institucional abierto: Bustinduy reconoce el patrón | `[S-05]` `[P-08]` |
| 0.8 | Idea feliz + ecosistema distribuidora independiente + hydra archiving activo | `[S-04]` `[S-03]` `[N-04]` `[S-11]` |

---

## T=0 → X — Arcos hacia el pivote

| Origen | Destino | Peso | Justificación |
|--------|---------|------|---------------|
| 0.1 | X | — | Directo: el veredicto resuelve la espera |
| 0.4 | X | — | El ánimo/dolo determina la dirección del veredicto |
| 0.5 | X | — | El lucro cesante condiciona la magnitud de la resolución |
| 0.3 | X | — | La amplificación preexistente condiciona el contexto de recepción |
| 0.6 | X | `[?]` | Depende de si S-06…S-08 se materializan antes del veredicto |
| 0.7 | X | media | Canal institucional puede influir en el contexto |
| 0.2 | X | — | El archivo ya destruido condiciona qué puede ordenar la resolución |
| 0.6 | R4.1 | media | La 2ª cola + datos duros Cerezo alimentan el contraataque |
| 0.8 | R4.3 | media | La idea feliz + hydra archiving `[S-11]` son la semilla del ecosistema alternativo |
| 0.7 | R4.3 | media | El canal institucional habilita el apoyo a la conformación |

---

## X — Pivote: veredicto y ejecución

> Referencia: [LORE_F-02_ARTEFACTO.md § Nodos de bifurcación](LORE_F-02_ARTEFACTO.md)

| Dirección | Descripción | Plausibilidad | Piezas ancla |
|-----------|-------------|---------------|-------------|
| X-A | Salida favorable: no se encuentra ánimo de lucro suficiente | media | `[T-12]` `[T-13]` `[N-04]` |
| X-B | Condena ejemplarizante: el encuadre disciplinario prevalece | media | `[T-12]` `[T-13]` `[N-03]` |
| X-C | Salida recurrible: resolución intermedia que no cierra | alta | `[T-12]` `[R-09]` `[N-04]` |
| X-D | Suspensión cautelar: contraataque desplaza X ~1 año | baja→media | `[S-09]` `[S-03]` `[N-04]` `[R-05]` `[N-05]` |

---

## X → T+∞ — Ramas post-pivote

> Referencia: [LORE_F-02_ARTEFACTO.md § Escenarios considerados](LORE_F-02_ARTEFACTO.md)

| Rama | Nombre | Dirección de X | Plausibilidad | Estado |
|------|--------|----------------|---------------|--------|
| R1 | La absolución sin regreso | X-A | media | activa |
| R2 | La ceremonia ejemplar | X-B | media | activa |
| R3 | La sala sigue abierta | X-C | alta | activa |
| R4 | Contraataque: la posición de Cerezo se erosiona | X-D | baja | activa — [detalle](universo/universo-1.md) |

Caminos no tomados: NINGUNO

### R4 — Secuencia de nodos (T=0 → T+0.5 → X)

> Detalle completo en [universo/universo-1.md](universo/universo-1.md)

```
0.6 2ª cola + datos Cerezo ──→ R4.1 demanda contra Cerezo (Thiel invertido)
0.8 idea feliz ──────────────→         │
0.7 canal institucional ────→         │
                                      ├──→ R4.2 suspensión cautelar (X → ~abr-2027)
                                      │
                              ┌───────┴───────┐
                              │               │
                        R4.3 ecosistema    R4.4 estructura legal
                        · Filmoteca Esp.   · FACUA/Bravo
                        · red federada     · crowdfunding
                        · distribuidora    · investigación Mercury
                              │               │
                              └───────┬───────┘
                                      │
                                R4.5 retirada negociada
                                (Cerezo retira cargos, conserva FlixOlé)
                                      │
                                R4.6 red de filmotecas federada
                                (circulación: ocio + educación)
```

**Huecos abiertos:** 6 — ver [universo-1.md § Huecos](universo/universo-1.md)

### Ejes pendientes de expansión por rama (R1–R3)

Cada rama hereda 3 ejes abiertos (del artefacto) aún sin nodos propios:

| Eje | Tipo | Descripción | Piezas ancla |
|-----|------|-------------|-------------|
| Relato que se impone | Relato vs relato | ¿Preservación, piratería o relato dividido? | `[N-02]` `[N-03]` `[S-03]` `[S-05]` |
| Destino del archivo | Paradoja recursiva | ¿No vuelve, reaparece distribuido o queda suspendido? | `[S-01]` `[S-02]` `[T-13]` |
| Duración real del castigo | Estrategia de parte | ¿Cierre, amplificación o prolongación? | `[N-04]` `[T-12]` `[R-09]` |

*Nodos concretos por rama: vacío. Pendiente de diseño paso a paso.*

---

## Metadatos del universo

| Campo | Valor |
|---|---|
| Última actualización | 2026-04-17 (N-05 integrado) |
| Corpus fuente | DRAFTS2/CORPUS_PREVIEW.md |
| Hilo narrativo fuente | DRAFTS2/LORE_F.md |
| Nivel T=0 | Espera entre juicio (9-abr) y veredicto (21-abr-2026) |
| Pivote X | Veredicto y ejecución (fecha candidata 21-abr, desplazable; en R4 → ~abr-2027) |
| Nodos totales | 8 (T=0) + pivote X (4 direcciones) + 6 (R4) = 18 |
| Arcos totales | 10 (T=0→X/R4) |
| Ramas activas | 4 |
| Caminos no tomados | 0 |
| Nodos sin ancla [?] | 1 (arco 0.6→X) + 5 huecos R4 (H1 resuelto por `[S-10]`, H6 parcialmente resuelto por `[N-05]`) |
| Obras generadas | [LORE_F-02_CORTO.md](LORE_F-02_CORTO.md), [LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md](LORE_F-02_CORTO-universo-1-gemini-3.1-pro.md), [LORE_F-02_CORTO-universo-1-claude-opus-4.md](LORE_F-02_CORTO-universo-1-claude-opus-4.md), [LORE_F-02_CORTO-universo-1-gpt-5-4.md](LORE_F-02_CORTO-universo-1-gpt-5-4.md), [LORE_F-02_CORTO-universo-1-claude-opus-4-2.md](LORE_F-02_CORTO-universo-1-claude-opus-4-2.md) |
| Piezas diseñadas | [universo/universo-1.md](universo/universo-1.md) |
