# corpus.md — Mapa acumulativo de taxonomía y linajes

> **Estado:** preview simulada — resultado de pasar 51 piezas del lore por pipeline Bartleby
> **Fecha de corte:** 18 de abril de 2026
> **Piezas procesadas:** 51 (P:9, S:13, N:5, T:14, R:10)
> **Nick corriente:** `[restitutiva-documental]`
> **Posición del corpus:** baseline completo del caso semilla

---

## I. Corriente detectada: herencia y linaje

### Linaje primario

| Eslabón | Texto/obra/actor | Función en el corpus |
|---------|------------------|----------------------|
| Stallman / GNU (1983) | Cuatro libertades | Fundamento ético: el código como habla `[R-03]` |
| Torvalds / Linux (1991) | Fork pragmático | Infraestructura alternativa funcional `[R-03]` |
| Lessig / Creative Commons (2001) | Gradación de licencias | Arquitecto jurídico: ni todo ni nada `[R-04]` |
| Aaron Swartz / JSTOR (2011) | Liberación de conocimiento | Coste personal de la posición `[R-03]` `[S-02]` |
| Thiel / *Zero to One* (2014) | Monopolio como eficiencia | Marco NRx del incumbente `[R-05]` |
| David Bravo / *Copia este libro* | Defensa jurídica del commons | Letrado del caso, diputado, precedente Soto `[P-02]` `[T-12]` |
| Rubén Sánchez / FACUA | Cronista y superviviente de AUSBANC | Amplificador mediático `[P-07]` |
| Facu | Divulgador / puente social→institucional | Canal hacia Bustinduy `[P-05]` `[S-05]` |
| Cristóbal | Jurista / analista en directo | Taxonomía jurídica del caso `[P-04]` `[S-03]` |
| Feo | Creador de Zoowoman, divulgador cinematográfico | Protagonista del caso `[P-01]` |
| Cerezo / EGEDA / Mercury / FlixOlé | Entramado audiovisual | Demandante, titular y plataforma comercial `[P-09]` |

**Nodos de linaje primario:** 11

### Linaje por exclusión

| Excluido | Qué ausencia revela |
|----------|---------------------|
| Fiscalía como actor con voz propia | Solo aparece mediada por la circular 1/2016; sin testimonio directo `[N-04]` |
| Cerezo como persona con declaración | Solo aparece como entramado corporativo; sin voz directa `[P-09]` |
| Grandes medios | El corpus registra su ausencia como dato: ningún gran medio cubrió el caso `[S-05]` |
| Audiencia del juicio | No hay crónica de sala; solo testimonios pre y post `[S-01]` `[S-02]` |
| La sentencia | No existe todavía; el corpus opera en el hueco entre juicio y veredicto |

**Nodos de linaje por exclusión:** 5

### Corriente resultante

El corpus opera dentro de una corriente `[restitutiva-documental]`: reconstrucción de un caso jurídico-cultural desde la preservación de la voz del acusado y su entorno mediático, enmarcada en tradiciones de commons digital, propiedad intelectual crítica y tensión institucional. No es periodismo (no verifica hechos nuevos). No es defensa jurídica (no argumenta ante tribunal). No es activismo (no pide resultado). Es cartografía documental de un conflicto en curso, sin sentencia.

---

## II. Taxonomía funcional acumulada

### Árbol funcional

```
CASO ZOOWOMAN
├── PRESERVACIÓN CULTURAL ── verbo: rescatar
│   ├── loss media ── verbo: desaparecer (fenómeno) `[T-05]`
│   ├── Zoowoman/Filmoteca ── verbo: alojar (respuesta) `[T-06]`
│   ├── distribuidora de emergentes ── verbo: ceder (autores → plataforma) `[S-01]`
│   ├── festival de cortos ── verbo: visibilizar `[S-02]`
│   └── Generación Maldita ── verbo: recopilar colectivamente `[S-02]`
│
├── ACUSACIÓN ── verbo: tipificar
│   ├── autorización ── verbo: exigir (licencia del titular) `[T-07]` `[T-08]`
│   ├── lucro directo ── verbo: monetizar (negado) `[T-09]`
│   ├── lucro indirecto ── verbo: beneficiarse (hipótesis ecosistema) `[T-09]` `[S-03]`
│   ├── lucro cesante ── verbo: cuantificar (870.000€) `[T-09]` `[T-13]`
│   └── ánimo/dolo ── verbo: probar (eje decisivo según S-03/N-04) `[N-04]`
│
├── DEFENSA ── verbo: desmontar
│   ├── ausencia de monetización ── verbo: demostrar (sin banners, sin suscripciones) `[S-01]` `[S-03]`
│   ├── prueba empírica ── verbo: medir (curvas de crecimiento sin inflexión) `[S-02]` `[S-03]`
│   ├── contraataque industrial ── verbo: invertir (¿quién copia a quién?) `[N-04]`
│   ├── estrategia de desgaste ── verbo: desgastar (hacer onerosa la propia reclamación) `[N-04]` `[S-10]`
│   ├── valor cultural ── verbo: establecer (bibliotecas, universidades) `[N-04]` `[S-01]`
│   └── ruta de asociación ── verbo: formalizar (lo que debería haberse hecho) `[N-04]`
│
├── ENCUADRE MEDIÁTICO ── verbo: enmarcar
│   ├── criminalizante ── verbo: señalar ("pirata", sucesos) `[N-03]`
│   ├── restitutivo ── verbo: escalar (capital vs preservación) `[N-02]`
│   ├── analítico ── verbo: desmenuzar (83 min de análisis jurídico) `[S-03]` `[N-04]`
│   └── institucional ── verbo: elevar (stream → gobierno) `[S-05]`
│
├── INFRAESTRUCTURA RENTISTA ── verbo: blindar
│   ├── EGEDA ── verbo: denunciar `[T-10]`
│   ├── Mercury Films ── verbo: acumular (+7.000 títulos) `[P-09]`
│   ├── FlixOlé ── verbo: monetizar ("Zoowoman de pago") `[S-03]`
│   └── Circular FGE 1/2016 ── verbo: ampliar (beneficio indirecto) `[N-04]`
│
├── PENAS ── verbo: solicitar (no impuestas)
│   ├── económico ── 870.000€ `[T-13]`
│   ├── prisión ── 2 años y medio `[T-13]`
│   └── social ── borrado del archivo → loss media recursivo `[T-13]` `[T-05]`
│
├── CONTEXTO ESTRUCTURAL ── verbo: enmarcar
│   ├── indignación → institucionalización `[T-01]` `[T-02]`
│   ├── FOSS/hacker ── cultura del commons digital `[R-03]` `[R-04]`
│   ├── monopolio como eficiencia `[R-05]`
│   ├── Thiel invertido ── contrapeso y enclosure `[R-10]`
│   ├── digitalización vs feudos analógicos `[R-06]`
│   ├── posesión vs suscripción `[R-07]`
│   ├── Windows vs Linux ── lawfare corporativo y supervivencia `[R-08]`
│   └── tensión judicial España ── sistema verificable `[R-09]`
│
└── EMERGENCIAS (+)
    ├── idea feliz ── prototipo nacido del análisis `[S-04]`
    ├── efecto Streisand ── disciplinamiento que amplifica `[S-02]`
    ├── segunda ola ── verbo: federar (de la plaza a la unidad de actividad) `[S-12]`
    ├── tándem legal ciudadano ── verbo: replicar (funciones, no personas) `[S-13]`
    └── triángulo Bravo→Rubén→caso ── cierre de red `[S-06]`..`[S-08]` (pendiente)
```

### Tabla de categorías

| Categoría | Definición en el corpus | Verbo | Nodo obligatorio | Piezas |
|-----------|-------------------------|-------|------------------|--------|
| Loss media | Obras sin soporte accesible | desaparecer | Sí | T-05 |
| Zoowoman | Repositorio comunal de preservación | alojar | Sí | T-06, S-01, S-03 |
| FlixOlé | Plataforma de pago sobre mismo catálogo | monetizar | Sí | S-03, P-09 |
| Lucro directo | Ingresos del acusado por Zoowoman | monetizar | Sí | T-09 |
| Lucro indirecto | Beneficio colateral (ecosistema YouTube/Patreon) | beneficiarse | Sí | T-09, S-02, S-03 |
| Lucro cesante | Pérdida hipotética del titular | cuantificar | Sí | T-09, T-13 |
| Ánimo/dolo | Intención demostrable de obtener beneficio | probar | Sí | N-04, S-03 |
| Beneficio económico inexistente | Posición de la defensa sobre el lucro | negar | Sí | N-02, S-01, S-02 |
| Encuadre criminalizante | Pirata, sucesos, lucro establecido | señalar | Sí | N-03 |
| Encuadre restitutivo | Capital vs preservación, disciplinamiento | escalar | Sí | N-02 |
| Efecto Streisand | Amplificación por intento de supresión | amplificar | No | S-02 |
| Contraataque industrial | Inversión de la demanda por modelo de utilidad | invertir | No | N-04 |
| Estrategia de desgaste | El tiempo y la carga de prueba se vuelven arma inversa | desgastar | No | N-04, S-10 |
| Ruta de asociación | Estructura legal no constituida | formalizar | No | N-04 |
| Valor cultural | Función preservadora como defensa | establecer | No | N-04, S-01 |
| Segunda ola | Retorno operativo de la indignación en forma de red territorial | federar | No | S-12 |
| Tándem legal ciudadano | Estructura mínima de defensa distribuida | replicar | No | S-13 |
| Tensión judicial | Sistema entre alumbrado y ceremonia | oscilar | No | R-01, R-02, R-09 |
| Ruido distribuido | Caso entra en institución por stream, no agenda | elevar | No | S-05 |

**Categorías taxonómicas totales:** 19

### Vista desde el hueco

Posiciones que no existen en esta taxonomía:

1. **La voz de Cerezo como persona** — el corpus solo lo registra como entramado corporativo. No hay declaración, entrevista ni posición articulada propia.
2. **La voz del tribunal** — no hay sentencia, no hay acta de sala, no hay motivación judicial. El corpus opera en el vacío entre juicio y veredicto.
3. **La posición del autor de las obras** — las obras preservadas en Zoowoman tienen titulares; ninguno habla en el corpus. Su posición (¿preferirían preservación o monetización?) no está.
4. **El espectador que pagó FlixOlé** — la infraestructura rentista tiene usuarios. Su experiencia no está en el corpus.
5. **El cálculo actuarial del lucro cesante** — los 870.000€ aparecen como cifra pero no como método. Cómo se calcularon no está en el corpus.

---

## III. Mecanismos retóricos acumulados

| Mecanismo | Descripción | Frecuencia | Piezas principales |
|-----------|-------------|------------|--------------------|
| Oposición binaria | Comunal vs rentista, preservar vs blindar, pirata vs archivero | ×12 | F, N-02, N-03, S-03 |
| Escalado del caso al sistema | Un caso particular como síntoma de estructura | ×8 | N-02, R-05, R-06, S-05 |
| Autorización por cifra | 870.000€, 12.000€, +7.000 títulos, 130k→400k seguidores | ×9 | T-09, T-13, S-02, P-09 |
| Criminalización por alias | "Pirata" como categoría previa al juicio | ×3 | N-03 |
| Desmontaje empírico | Gráficas sin inflexión, ausencia de banners, crecimiento post-cierre | ×5 | S-02, S-03, N-04 |
| Inversión de roles | ¿Quién copia a quién? FlixOlé como Zoowoman de pago | ×3 | S-03, N-04 |
| Consigna como cierre | "El cine es nuestro", "Solo la gente salva a la gente" | ×4 | S-01, S-02 |
| Referencia a precedente judicial | Caso Soto, series.ly, Indiceps2, STS 89/2023, Gil y Gil | ×6 | T-08, N-04, N-01 |
| Ejemplo y contraejemplo jurídico | Portero-camello, bibliotecas públicas, Archivo Nacional | ×4 | N-04 |
| Paradoja recursiva | Borrado del archivo = loss media del loss media | ×2 | T-13, F |
| Puente social→institucional | Stream como canal de agenda | ×2 | S-05 |
| Humildad performativa | "No conozco el caso, pero..." (Bustinduy) | ×1 | S-05 |

**Mecanismos retóricos distintos:** 12
**Frecuencia total:** ×59

---

## IV. Lo emergente — qué aporta sobre la tradición

### Diagnósticos que la tradición no tenía

1. **El ánimo como eje decisivo**: la tradición del commons digital discutía legalidad de la copia; este corpus desplaza el eje a la prueba del ánimo de lucro, no al acto de copia en sí `[N-04]` `[S-03]`
2. **Loss media como categoría jurídicamente vacía**: obras que no son dominio público ni son explotadas; su estatus legal no está resuelto `[T-05]` `[T-07]`
3. **El ruido distribuido como canal institucional**: un caso entra en la agenda del gobierno por stream, no por dossier ni cobertura de prensa `[S-05]`
4. **La segunda ola como forma operativa**: la indignación ya no solo escala a partido o ministerio; reaparece como filmoteca, archivo, despacho y red territorial `[S-12]`
5. **La replicación por funciones**: la estructura legal colectiva se deja leer mejor como tándem de roles que como alianza personalista `[S-13]`

### Operaciones que desplazan la herencia

1. **Inversión del vector de la demanda**: el corpus formula que el acusado podría demandar al demandante por propiedad industrial — el modelo de utilidad del repositorio `[N-04]`
2. **Paradoja del tercer eje penal**: si se destruye el archivo como pena, la preservación se convierte en su propio loss media — recursividad que la tradición penal no contempla `[T-13]`
3. **FlixOlé como apropiación rentista del commons**: no es solo competencia; es la materialización comercial de un modelo nacido como bien común `[S-03]`

### Ausencias estructurales

1. El corpus **no puede ver** al acusado como culpable porque opera en el hueco pre-sentencia; pero tampoco como inocente — la posición Bartleby es pre-resolución, no pro-defensa
2. El corpus **no puede contemplar** el caso desde la posición del titular que sí explota su catálogo legítimamente — esa voz no existe en las fuentes procesadas
3. El corpus **no puede medir** el daño cultural de la desaparición de Zoowoman porque el archivo ya fue destruido — solo quedan testimonios sobre lo que había

**Emergencias identificadas:** 8
**Ausencias estructurales:** 3

---

## V. Vista desde el hueco

El corpus entero opera desde una posición específica: la semana entre el juicio y el veredicto. Esa posición no es accidental — es constitutiva.

Desde el hueco se ve:

- Un sistema judicial que oscila entre alumbrado y ceremonia, y un caso que puede caer en cualquiera de los dos lados — sin que el corpus pueda predecir cuál.
- Un acusado cuya actividad cultural está documentada con más densidad que la hipótesis acusatoria — no porque la acusación sea débil, sino porque la voz del acusado y su entorno están preservadas y la de la acusación no.
- Una estructura económica donde el mismo catálogo de obras genera simultáneamente una acción penal (por alojar sin licencia) y una plataforma de pago (por alojar con licencia adquirida ex post) — y donde la pregunta de quién se apropió de qué modelo no tiene respuesta unívoca.
- Un mecanismo de amplificación que funciona al revés del diseño: la tentativa de disciplinamiento produce visibilidad, cobertura institucional y análisis jurídico público que no existían antes del caso.

Si el sistema de obligaciones del corpus ("debe preservarse", "debe probarse el ánimo", "debe establecerse el valor cultural") fuera exhaustivo, lo que queda fuera es: **la posibilidad de que el caso no importe**. El corpus no puede contemplar la irrelevancia del caso, porque su propia existencia es la evidencia de que importa.

---

## Metadatos acumulados

| Campo | Valor |
|---|---|
| Fecha de corte | 2026-04-18 |
| Piezas procesadas | 51 |
| Linaje primario (nodos) | 11 |
| Linaje por exclusión (nodos) | 5 |
| Categorías taxonómicas | 19 |
| Mecanismos retóricos distintos | 12 |
| Frecuencia total mecanismos | 59 |
| Emergencias identificadas | 8 |
| Ausencias estructurales | 3 |
| Nick corriente | `[restitutiva-documental]` |
| Posición en corpus | baseline completo del caso semilla |

---

## Registro de merges

| # | Fecha | Piezas incorporadas | Delta principal |
|---|-------|---------------------|-----------------|
| 1 | 2026-04-17 | P-01…P-09, S-01…S-08, N-01…N-04, T-01…T-14, R-01…R-09 | Baseline inicial: 44 piezas, 16 categorías, 12 mecanismos, corriente `[restitutiva-documental]` |
| 2 | 2026-04-18 | S-12, S-13, R-10, S-04, N-04, S-09, S-11 | Expansión v2: 51 piezas, 19 categorías, integración de nuevos verbos (`desgastar`, `federar`, `replicar`), fortalecimiento de matriz de lectura y tensiones emergentes. |
