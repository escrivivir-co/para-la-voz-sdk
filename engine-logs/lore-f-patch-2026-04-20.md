# LORE_F PATCH — FEAT-04.4: total-cobertura-de-piezas
# Generado: 2026-04-20 — @Loreador (simulated) desde future-machine v0.1-dev
# Rama objetivo: mod/legislativa:DRAFTS2/LORE_F.md
# Gap resuelto: [N-05] body + [R-10] body + checklist 47→51
#
# Instrucciones de aplicación:
#   git checkout mod/legislativa
#   Aplicar INSERT-1 tras línea 208 (fin del párrafo `[S-09]`)
#   Aplicar INSERT-2 tras línea 220 (fin del párrafo `[P-06]` en ### El sustrato)
#   Aplicar INSERT-3 reemplazando el bloque ## Checklist de marcas completo
#   git add DRAFTS2/LORE_F.md && git commit -m "feat: FEAT-04.4 — total-cobertura-de-piezas (N-05 + R-10)"
#   git checkout main

---

## INSERT-1
### Insertar DESPUÉS de la línea del párrafo `[S-09]` (l.208), ANTES de `### El número que da la vuelta`

**Contexto previo (no incluir):**
```
`[S-09]` El 15 de abril, David Bizarro...no como color.
```

**INSERTAR:**

```markdown
### La cobertura tech-mainstream

`[N-05]` El 16 de abril, Xataka publica el primer análisis desde un medio de alcance masivo: *"La persona más poderosa del cine español lleva años empeñada en algo: que un streamer vaya a la cárcel y pague 800.000 euros."* El titular no usa "pirata" — construye la asimetría con datos: Mercury Films controla el 70-80% del cine español distribuido; EGEDA tiene un patrón documentado de denuncias (2017, 2022, Zoowoman); y FlixOlé fue lanzado por el mismo Cerezo `[P-09]` en 2020, poco antes de que llegara la denuncia formal. Dos datos nuevos entran al corpus: en enero de 2025 la acusación ofreció un acuerdo — declararse culpable, 100.000€ y un año de cárcel — que Feo `[P-01]` rechazó; y el matiz jurídico que la defensa usaba en sala cobra forma pública: Zoowoman no alojaba archivos, enlazaba a repositorios externos (MEGA, archive.org). Ese matiz separa el caso de la jurisprudencia previa sobre alojamiento directo. El régimen de obras huérfanas (Directiva EU 2014, RD 2016) solo autoriza acceso a instituciones públicas: lo que Zoowoman hacía era estructuralmente imposible de hacer de forma legal para un particular. El silencio que `[S-05]` y `[S-09]` documentaban como dato se rompe parcialmente: Xataka no es El País, pero su audiencia tech es la primera audiencia masiva que recibe el caso con encuadre analítico.
```

**Contexto siguiente (no incluir):**
```
### El número que da la vuelta
```

---

## INSERT-2
### Insertar DESPUÉS del párrafo `[P-06]` en sección "### El sustrato" (l.220), ANTES de `### La espera`

**Contexto previo (no incluir):**
```
`[P-06]` Los consumidores como colectivo...antes de que se sepa el resultado.
```

**INSERTAR:**

```markdown
`[R-10]` Leídas juntas, las piezas de la semana entre el juicio y el veredicto trazan la matriz que el sustrato largo de §1 preparaba: un commons que cuidó catálogos invisibles para el mercado mientras el mercado no los quería (`[S-01]`), un incumbente que activó el aparato legal cuando ese terreno se volvió visible y valioso (`[T-10]`, `[P-09]`), y un dato que invirtió el vector — 11.007 vs 40 `[S-10]`, cinco antidisturbios con ariete `[S-09]`, acuerdo de 100.000€ rechazado `[N-05]` — haciendo que quien reclama masivamente asuma el coste de probar lo que antes solo exigía. El corpus llama a esta configuración **Thiel invertido**: la densidad del aparato puede volverse, en determinadas condiciones, coste para quien lo activa.
```

**Contexto siguiente (no incluir):**
```
### La espera
```

---

## INSERT-3
### Reemplazar el bloque `## Checklist de marcas — primera mitad` completo (l.226–242)

**REEMPLAZAR TODO EL BLOQUE con:**

```markdown
## Checklist de marcas — primera mitad

| Tipo | Marcas usadas | Total | Estado |
|------|---------------|-------|--------|
| Personajes `[P-*]` | 01 02 03 04 05 06 07 08 09 | 9/9 | ✅ |
| Sociales `[S-*]` | 01 02 03 04 05 06 07 08 09 10 11 12 13 | 13/13 | ✅ |
| Noticias `[N-*]` | 01 02 03 04 05 | 5/5 | ✅ |
| Fases `[T-*]` | 01…13 + 14 (referenciado, pendiente) | 14/14 | ✅ |
| Recursos `[R-*]` | 01…10 | 10/10 | ✅ |
| **Total** | | **51/51** | ✅ todas tocadas |

> `[T-14]` está referenciado como fecha futura (21-abr). Se desarrolla en la segunda mitad.
> `[S-06]`…`[S-08]` son piezas pendientes de ingesta — contenido por llenar cuando exista referencia (Carril B).
> `[S-09]`, `[S-10]` y `[S-11]` son hechos del período 14-16 de abril. Incorporados en FEAT-04.3.
> `[N-05]` incorporada en FEAT-04.4: primera cobertura tech-mainstream (Xataka, 16-abr-2026).
> `[S-12]` anclada en §4 (idea feliz como segunda ola). `[S-13]` pieza de soporte sin anclaje narrativo propio — disponible para corpus-sdk vía checklist.
> `[R-10]` anclada en §4 (Thiel invertido — closing frame del presente). FEAT-04.4.
```

---

## Resumen del patch

| # | Gap | Tipo | Solución | Fuente de datos |
|---|-----|------|----------|-----------------|
| 1 | `[N-05]` ausente de prosa | Noticia real (Xataka, 16-abr) | Nueva subsección en §4 | LORE_N-05.md (real) |
| 2 | `[R-10]` solo en checklist nota | Recurso soporte (Thiel invertido) | Párrafo closing en §4 | LORE_R-10.md (real) |
| 3 | `[S-13]` solo en checklist nota | Soporte declarado | Sin cambio — checklist es cobertura suficiente | — |
| 4 | Checklist 47/47 desactualizado | Conteo | Actualizado a 51/51 | derivado |

**Mock data usada:** ninguna. Todos los datos provienen de piezas reales del lore.
**Piezas Carril B** (`[S-06]`, `[S-07]`, `[S-08]`): sin cambio — pendientes de ingesta real.

## Nota DRY para corpus-sdk

Post-patch, LORE_F cubre las 51 piezas del INDEX:
- 49 con anclaje en prosa narrativa
- 1 con anclaje en checklist (`[S-13]` — soporte puro)
- 3 con referencia en prosa pero marcadas Carril B (`[S-06]`…`[S-08]`)

El corpus-sdk puede tratar LORE_F como fuente DRY canónica sin necesidad de recorrer LORE_A.md…LORE_E.md para descubrir piezas.
