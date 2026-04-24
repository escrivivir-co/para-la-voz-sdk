# corpus.md — Mapa acumulativo de taxonomía y linajes

> **Estado:** preview — resultado de pasar 51 piezas del lore por pipeline Bartleby
> **Fecha de corte:** 20 de abril de 2026
> **Piezas procesadas:** 51 (P:9, S:13, N:5, T:14, R:10)
> **Nick corriente:** `[restitutiva-documental]`
> **Posición del corpus:** baseline completo del caso semilla — rebuild FEAT-04.5
> **Fuente del rebuild:** `LORE_F.md` (reescritura literaria FEAT-04.5 sobre FEAT-04.4)

---

## I. Corriente detectada: herencia y linaje

### Linaje primario

| Eslabón | Texto/obra/actor | Función en el corpus |
|---------|------------------|----------------------|
| Stallman / GNU (1983) | Cuatro libertades | Fundamento ético: el código como habla `[R-03]` |
| Torvalds / Linux (1991) | Fork pragmático | Infraestructura alternativa funcional; victoria selectiva donde el capital no necesita control del punto final `[R-03]` `[R-08]` |
| Lessig / Creative Commons (2001) | Gradación de licencias | Arquitecto jurídico: ni todo ni nada `[R-04]` |
| Aaron Swartz / JSTOR (2011) | Liberación de conocimiento | Coste personal de la posición `[R-03]` `[S-02]` |
| Thiel / *Zero to One* (2014) | Monopolio como eficiencia | Doctrina del incumbente: la alternativa revela que el monopolio es contingente `[R-05]` |
| David Bravo / *Copia este libro* | Defensa jurídica del commons | Letrado del caso, diputado (XI legislatura, pregunta a Coalición de Creadores), precedente Soto, defensa de Rubén Sánchez vs AUSBANC — primera condena española de rectificación diaria en Twitter (30 días, ratificada por Supremo) `[P-02]` `[T-12]` |
| Rubén Sánchez / FACUA | Portavoz y superviviente de AUSBANC | Paraguas jurídico-mediático con memoria de otras batallas `[P-07]` |
| Facu | Divulgador / puente social→institucional | Umbral: cruza el caso a la opinión pública y de ahí a la institución `[P-05]` `[S-05]` |
| Cristóbal | Jurista / analista en directo | Argumentario del caso; 83 min de taxonomía jurídica; generador de la idea feliz `[P-04]` `[S-03]` `[S-04]` |
| Feo | Creador de Zoowoman; diplomado en historia, social y antropología | Protagonista del caso; archivero cinematográfico por impulso de preservación `[P-01]` |
| Cerezo / EGEDA / Mercury / FlixOlé | Entramado audiovisual; Mercury controla 70-80% del cine español distribuido | Demandante con patrón serial de denuncias (2017 WebTV, 2022 diecisiete webs, Zoowoman); contrato de 300M con TVE con investigación fiscal abierta; condena en primera instancia como cooperador necesario (caso Gil y Gil, absuelto por prescripción) `[P-09]` `[N-01]` `[N-05]` `[S-09]` |

**Nodos de linaje primario:** 11

### Linaje por exclusión

| Excluido | Qué ausencia revela |
|----------|---------------------|
| Fiscalía como actor con voz propia | Solo aparece mediada por la circular 1/2016; sin testimonio directo `[N-04]` |
| Cerezo como persona con declaración | Solo aparece como entramado corporativo; sin voz directa `[P-09]` |
| Grandes medios generalistas | Xataka `[N-05]` rompe parcialmente el silencio desde audiencia tech; la prensa generalista (El País, La Vanguardia, etc.) sigue ausente `[S-05]` |
| Audiencia del juicio | No hay crónica de sala; solo testimonios pre y post `[S-01]` `[S-02]` |
| La sentencia | No existe todavía; el corpus opera en el hueco entre juicio (9-abr) y veredicto (21-abr) |
| Los titulares de las 10.967 obras reclamadas sin acreditación | EGEDA reclama 11.007 títulos; tiene derechos acreditados sobre 40. Los titulares del 99,6% restante — cine iraní, de Bután, de Uganda, de Yugoslavia, de la URSS — no aparecen en el corpus `[S-10]` |
| El régimen de obras huérfanas como vía practicable | La Directiva EU 2014 / RD 2016 existe, pero solo autoriza acceso a instituciones públicas; para un particular, la vía legal de preservar es estructuralmente inexistente `[N-05]` |

**Nodos de linaje por exclusión:** 7

### Corriente resultante

El corpus opera dentro de una corriente `[restitutiva-documental]`: reconstrucción de un caso jurídico-cultural desde la preservación de la voz del acusado y su entorno mediático, enmarcada en tradiciones de commons digital, propiedad intelectual crítica y tensión institucional.

El rewrite FEAT-04.5 explicita una premisa que el corpus anterior contenía implícitamente: la sala judicial oscila entre dos figuras contemporáneas y estructurales — el alumbrado (procedimiento que produce verdad de entre relatos en conflicto) y la ceremonia del tirano (veredicto escrito antes de la vista) `[R-01]` `[R-02]`. No son alternativas. Son la oscilación del mismo sistema. `[R-09]` documenta que el aparato judicial español opera, verificablemente, entre bloqueos institucionales, lawfare y capacidad real de persecución penal. El caso hereda ambas caras y el corpus no puede saber cuál prevalecerá.

No es periodismo (no verifica hechos nuevos). No es defensa jurídica (no argumenta ante tribunal). No es activismo (no pide resultado). Es cartografía documental de un conflicto en curso, sin sentencia.

---

## II. Taxonomía funcional acumulada

### Árbol funcional

```text
CASO ZOOWOMAN
├── PRESERVACIÓN CULTURAL ── verbo: rescatar
│   ├── loss media ── verbo: desaparecer (fenómeno) `[T-05]`
│   ├── Zoowoman/Filmoteca ── verbo: enlazar (no alojar) `[T-06]` `[N-05]`
│   ├── distribuidora de emergentes ── verbo: ceder (autores → plataforma) `[S-01]`
│   ├── festival de cortos ── verbo: visibilizar `[S-02]`
│   ├── Generación Maldita ── verbo: recopilar colectivamente `[S-02]`
│   └── obras huérfanas ── verbo: preservar (sin vía legal individual) `[N-05]`
│
├── ACUSACIÓN ── verbo: tipificar
│   ├── autorización ── verbo: exigir (licencia del titular) `[T-07]` `[T-08]`
│   ├── alojamiento ── verbo: alojar (hipótesis de la acusación) `[T-08]`
│   ├── lucro directo ── verbo: monetizar (negado) `[T-09]`
│   ├── lucro indirecto ── verbo: beneficiarse (hipótesis ecosistema) `[T-09]` `[S-03]`
│   ├── lucro cesante ── verbo: cuantificar (870.000€) `[T-09]` `[T-13]`
│   ├── ánimo/dolo ── verbo: probar (eje decisivo) `[N-04]` `[S-03]`
│   └── acuerdo de conformidad ── verbo: ofrecer (100.000€ + 1 año; rechazado) `[N-05]`
│
├── DEFENSA ── verbo: desmontar
│   ├── ausencia de monetización ── verbo: demostrar (sin banners, sin suscripciones) `[S-01]` `[S-03]`
│   ├── prueba empírica ── verbo: medir (curvas sin inflexión) `[S-02]` `[S-03]`
│   ├── modelo de enlace ── verbo: enlazar (MEGA, archive.org; no alojamiento) `[N-05]`
│   ├── contraataque industrial ── verbo: invertir (¿quién copia a quién?) `[N-04]`
│   ├── estrategia de desgaste ── verbo: desgastar (11.007 vs 40) `[N-04]` `[S-10]`
│   ├── valor cultural ── verbo: establecer (bibliotecas, universidades, LA) `[N-04]` `[S-01]`
│   └── ruta de asociación ── verbo: formalizar (lo que debería haberse hecho) `[N-04]`
│
├── ENCUADRE MEDIÁTICO ── verbo: enmarcar
│   ├── criminalizante ── verbo: señalar ("pirata", sucesos) `[N-03]`
│   ├── restitutivo ── verbo: escalar (capital vs preservación) `[N-02]`
│   ├── analítico ── verbo: desmenuzar (83 min; Xataka con datos) `[S-03]` `[N-04]` `[N-05]`
│   └── institucional ── verbo: elevar (stream → gobierno) `[S-05]`
│
├── INFRAESTRUCTURA RENTISTA ── verbo: blindar
│   ├── EGEDA ── verbo: denunciar (patrón serial: 2017, 2022, Zoowoman) `[T-10]` `[N-05]`
│   ├── Mercury Films ── verbo: acumular (70-80% cine español distribuido) `[P-09]` `[N-05]`
│   ├── FlixOlé ── verbo: monetizar ("Zoowoman de pago", lanzado 2020) `[S-03]` `[N-05]`
│   └── Circular FGE 1/2016 ── verbo: ampliar (beneficio indirecto) `[N-04]`
│
├── PENAS ── verbo: solicitar (no impuestas)
│   ├── económico ── 870.000€ `[T-13]`
│   ├── prisión ── 2 años y medio `[T-13]`
│   └── social ── borrado del archivo → loss media recursivo `[T-13]` `[T-05]`
│
├── CONTEXTO ESTRUCTURAL ── verbo: enmarcar
│   ├── oscilación judicial ── sala como alumbrado / sala como ceremonia `[R-01]` `[R-02]` `[R-09]`
│   ├── indignación → institucionalización `[T-01]` `[T-02]`
│   ├── FOSS/hacker ── cultura del commons digital `[R-03]` `[R-04]`
│   ├── monopolio como eficiencia ── la alternativa revela contingencia `[R-05]`
│   ├── Thiel invertido ── la densidad del aparato como coste para quien lo activa `[R-10]`
│   ├── digitalización rentista vs digitalización comunal ── mismo acto técnico, distinta posición ante la propiedad `[R-06]`
│   ├── posesión vs suscripción ── lo que no se vende ni se alquila desaparece `[R-07]`
│   ├── Windows vs Linux ── lawfare corporativo y victoria selectiva `[R-08]`
│   └── régimen de obras huérfanas ── vía legal solo para instituciones `[N-05]`
│
└── EMERGENCIAS (+)
    ├── idea feliz ── prototipo nacido del análisis `[S-04]`
    ├── efecto Streisand ── disciplinamiento que amplifica `[S-02]`
    ├── segunda ola ── verbo: federar (de la plaza a la unidad de actividad con tarea concreta) `[S-12]`
    ├── tándem legal ciudadano ── 4 funciones × 4 actores `[S-13]`
    ├── preservación espontánea ── verbo: archivar (4 personas actúan independientemente) `[S-11]`
    └── triángulo Bravo→Rubén→caso ── cierre de red `[S-06]`..`[S-08]` (pendiente)
```

### Tabla de categorías

| Categoría | Definición en el corpus | Verbo | Nodo obligatorio | Piezas |
|-----------|-------------------------|-------|------------------|--------|
| Loss media | Obras sin soporte accesible | desaparecer | Sí | T-05 |
| Zoowoman | Repositorio comunal de preservación; enlazaba, no alojaba | enlazar | Sí | T-06, S-01, S-03, N-05 |
| FlixOlé | Plataforma de pago sobre mismo catálogo; lanzada 2020 | monetizar | Sí | S-03, P-09, N-05 |
| Lucro directo | Ingresos del acusado por Zoowoman | monetizar | Sí | T-09 |
| Lucro indirecto | Beneficio colateral (ecosistema YouTube/Patreon) | beneficiarse | Sí | T-09, S-02, S-03 |
| Lucro cesante | Pérdida hipotética del titular | cuantificar | Sí | T-09, T-13 |
| Ánimo/dolo | Intención demostrable de obtener beneficio | probar | Sí | N-04, S-03 |
| Beneficio económico inexistente | Posición de la defensa sobre el lucro | negar | Sí | N-02, S-01, S-02 |
| Encuadre criminalizante | Pirata, sucesos, lucro establecido | señalar | Sí | N-03 |
| Encuadre restitutivo | Capital vs preservación, disciplinamiento | escalar | Sí | N-02 |
| Efecto Streisand | Amplificación por intento de supresión | amplificar | No | S-02 |
| Contraataque industrial | Inversión de la demanda por modelo de utilidad | invertir | No | N-04 |
| Estrategia de desgaste | El tiempo y la carga de prueba como arma inversa; 11.007 vs 40 | desgastar | No | N-04, S-10 |
| Ruta de asociación | Estructura legal no constituida | formalizar | No | N-04 |
| Valor cultural | Función preservadora como defensa: bibliotecas, universidades, América Latina | establecer | No | N-04, S-01 |
| Segunda ola | Retorno de la indignación como red territorial: filmotecas de barrio, ateneos, nodos de archivo, despachos comunales | federar | No | S-12 |
| Tándem legal ciudadano | Estructura mínima de defensa distribuida: argumentario (Cristóbal), sala (Bravo), paraguas (Rubén/FACUA), umbral (Facu) | replicar | No | S-13 |
| Oscilación judicial | Sistema entre alumbrado y ceremonia; las dos caras contemporáneas y estructurales | oscilar | No | R-01, R-02, R-09 |
| Ruido distribuido | Caso entra en institución por stream, no agenda | elevar | No | S-05 |
| Modelo de enlace | Zoowoman enlazaba a MEGA, archive.org — no alojamiento directo; la distinción reposiciona el tipo penal | enlazar | No | N-05, T-08 |
| Obras huérfanas | Obras sin titular activo; régimen EU 2014 / RD 2016 solo autoriza instituciones públicas | preservar (sin vía) | No | N-05 |
| Patrón de denuncia serial | EGEDA: 2017 WebTV, 2022 diecisiete webs, Zoowoman — la repetición revela estrategia, no defensa de derechos puntuales | denunciar | No | N-05 |
| Acuerdo de conformidad | Enero 2025: 100.000€ + declararse culpable + 1 año; rechazado por el acusado | rechazar | No | N-05 |
| Preservación espontánea | 4 personas archivan el canal independientemente antes del veredicto: torrent, Drive, disco 2TB, backup con metadatos | archivar | No | S-11 |

**Categorías taxonómicas totales:** 24

### Vista desde el hueco

Posiciones que no existen en esta taxonomía:

1. **La voz de Cerezo como persona** — el corpus solo lo registra como entramado corporativo. No hay declaración, entrevista ni posición articulada propia.
2. **La voz del tribunal** — no hay sentencia, no hay acta de sala, no hay motivación judicial. El corpus opera en el vacío entre juicio y veredicto.
3. **La posición del autor de las obras** — las obras preservadas en Zoowoman tienen titulares; ninguno habla en el corpus. Su posición (¿preferirían preservación o monetización?) no está.
4. **El espectador que pagó FlixOlé** — la infraestructura rentista tiene usuarios. Su experiencia no está en el corpus.
5. **El cálculo actuarial del lucro cesante** — los 870.000€ aparecen como cifra pero no como método. Cómo se calcularon no está en el corpus.
6. **Quien construiría la vía legal individual** — el régimen de obras huérfanas existe para instituciones; lo que Zoowoman hacía era estructuralmente imposible de hacer legalmente para un particular. La taxonomía no tiene posición para quien diseñaría esa vía.

---

## III. Mecanismos retóricos acumulados

| Mecanismo | Descripción | Frecuencia | Piezas principales |
|-----------|-------------|------------|--------------------|
| Oposición binaria | Comunal vs rentista, preservar vs blindar, pirata vs archivero, alumbrado vs ceremonia, enlazar vs alojar, digitalización rentista vs digitalización comunal | ×14 | F §0, F §1, N-02, N-03, S-03, R-06, N-05 |
| Escalado del caso al sistema | Un caso particular como síntoma de estructura; la imposibilidad legal de preservar como dato sistémico | ×9 | N-02, R-05, R-06, S-05, N-05 |
| Autorización por cifra | 870.000€, 12.000€, +7.000 títulos, 11.007 vs 40, 100.000€ (acuerdo), 70-80% mercado, 300M TVE, 5 antidisturbios con ariete | ×12 | T-09, T-13, S-02, S-10, P-09, N-05, S-09 |
| Criminalización por alias | "Pirata" como categoría previa al juicio | ×3 | N-03 |
| Desmontaje empírico | Gráficas sin inflexión, ausencia de banners, crecimiento post-cierre, 11.007 vs 40, enlaces (no alojamiento) | ×7 | S-02, S-03, N-04, S-10, N-05 |
| Inversión de roles | ¿Quién copia a quién? FlixOlé como Zoowoman de pago. Thiel invertido: la densidad del aparato como coste para quien lo activa | ×4 | S-03, N-04, R-10 |
| Consigna como cierre | "El cine es nuestro", "Solo la gente salva a la gente", "los comentarios son lo mejor del canal — en 100 años eso va a ser lo interesante" | ×5 | S-01, S-02, S-05, S-11 |
| Referencia a precedente judicial | Caso Soto, series.ly, Indiceps2, STS 89/2023, Gil y Gil, AUSBANC (rectificación diaria Twitter, ratificada por Supremo), Directiva EU 2014 / RD 2016 | ×8 | T-08, N-04, N-01, P-02, N-05 |
| Ejemplo y contraejemplo jurídico | Portero-camello, bibliotecas públicas, Archivo Nacional, asociación cultural | ×4 | N-04 |
| Paradoja recursiva | Borrado del archivo = loss media del loss media | ×2 | T-13, F |
| Puente social→institucional | Stream como canal de agenda; Facu→Bustinduy | ×2 | S-05 |
| Humildad performativa | "No conozco el caso, pero..." (Bustinduy) | ×1 | S-05 |
| Oscilación estructural | Las dos caras de la sala como contemporáneas y estructurales, no alternativas; el sistema judicial opera verificablemente entre bloqueos, lawfare y capacidad real | ×3 | F §0, R-09, T-12 |
| Dato que invierte el vector | Cifra o hecho singular que desplaza la carga narrativa: 11.007 vs 40, ariete con 5 antidisturbios, 100.000€ rechazado, enlaces a MEGA/archive.org (no alojamiento) | ×4 | S-10, S-09, N-05 |

**Mecanismos retóricos distintos:** 14
**Frecuencia total:** ×78

---

## IV. Lo emergente — qué aporta sobre la tradición

### Diagnósticos que la tradición no tenía

1. **El ánimo como eje decisivo**: la tradición del commons digital discutía legalidad de la copia; este corpus desplaza el eje a la prueba del ánimo de lucro, no al acto de copia en sí `[N-04]` `[S-03]`
2. **Loss media como categoría jurídicamente vacía**: obras que no son dominio público ni son explotadas; su estatus legal no está resuelto `[T-05]` `[T-07]`
3. **El ruido distribuido como canal institucional**: un caso entra en la agenda del gobierno por stream, no por dossier ni cobertura de prensa `[S-05]`
4. **La segunda ola como forma operativa**: la indignación ya no solo escala a partido o ministerio; reaparece como filmotecas de barrio, ateneos, nodos de archivo, despachos comunales — unidades de actividad con tarea concreta. Lo que se pierde en centralidad simbólica se gana en persistencia y capilaridad `[S-12]`
5. **La replicación por funciones**: la estructura legal colectiva se deja leer como tándem de roles (argumentario, sala, paraguas, umbral) — funciones, no personas; una composición de frentes que se coordinan sin confundirse `[S-13]`
6. **La imposibilidad estructural de la preservación individual**: el régimen de obras huérfanas (Directiva EU 2014, RD 2016) solo autoriza acceso a instituciones públicas. Lo que Zoowoman hacía era legalmente imposible de hacer para un particular — no por incumplimiento puntual, sino por diseño del marco `[N-05]`
7. **El modelo de enlace como distinción tipológica**: Zoowoman no alojaba archivos; enlazaba a MEGA y archive.org. La distinción entre enlazar y alojar reposiciona el tipo penal que la acusación invoca `[N-05]` `[T-08]`

### Operaciones que desplazan la herencia

1. **Inversión del vector de la demanda**: el corpus formula que el acusado podría demandar al demandante por propiedad industrial — el modelo de utilidad del repositorio `[N-04]`
2. **Paradoja del tercer eje penal**: si se destruye el archivo como pena, la preservación se convierte en su propio loss media — recursividad que la tradición penal no contempla `[T-13]`
3. **FlixOlé como apropiación rentista del commons**: no es solo competencia; es la materialización comercial de un modelo nacido como bien común. Mismo acto técnico, distinta posición ante la propiedad `[S-03]` `[R-06]`
4. **El rechazo del acuerdo como transformación del caso**: enero 2025, la acusación ofrece 100.000€ + declararse culpable + 1 año de cárcel. El acusado rechaza. La negativa transforma el caso de negociación a principio `[N-05]`
5. **La preservación espontánea como desplazamiento del valor**: 4 personas archivan el canal independientemente antes del veredicto — torrent, Drive, disco, backup con metadatos. El valor del archivo se desplaza: no son las películas, es la conversación alrededor de ellas `[S-11]`

### Ausencias estructurales

1. El corpus **no puede ver** al acusado como culpable porque opera en el hueco pre-sentencia; pero tampoco como inocente — la posición Bartleby es pre-resolución, no pro-defensa
2. El corpus **no puede contemplar** el caso desde la posición del titular que sí explota su catálogo legítimamente — esa voz no existe en las fuentes procesadas
3. El corpus **no puede medir** el daño cultural de la desaparición de Zoowoman porque el archivo ya fue destruido — solo quedan testimonios sobre lo que había
4. El corpus **no puede diseñar** la vía legal de preservación individual que no existe — el régimen de obras huérfanas excluye a particulares por diseño, y ninguna fuente del corpus propone cómo cambiar eso

**Emergencias identificadas:** 12
**Ausencias estructurales:** 4

---

## V. Vista desde el hueco

El corpus entero opera desde una posición específica: la semana entre el juicio y el veredicto. Esa posición no es accidental — es constitutiva. El rewrite FEAT-04.5 la explicita con una premisa que ahora precede al relato: antes del caso, dos imágenes de la justicia preexisten — la sala como alumbrado y la sala como ceremonia. Las dos son contemporáneas y estructurales `[R-01]` `[R-02]` `[R-09]`.

Desde el hueco se ve:

- Un sistema judicial que oscila entre alumbrado y ceremonia, y un caso que puede caer en cualquiera de los dos lados — sin que el corpus pueda predecir cuál. El sistema produce ambas funciones simultáneamente, no como error sino como condición de operación.
- Un acusado cuya actividad cultural está documentada con más densidad que la hipótesis acusatoria — no porque la acusación sea débil, sino porque la voz del acusado y su entorno están preservadas y la de la acusación no.
- Una estructura económica donde el mismo catálogo de obras genera simultáneamente una acción penal (por enlazar sin licencia) y una plataforma de pago (por adquirir licencia ex post) — y donde la pregunta de quién se apropió de qué modelo no tiene respuesta unívoca.
- Un mecanismo de amplificación que funciona al revés del diseño: la tentativa de disciplinamiento produce visibilidad, cobertura institucional y análisis jurídico público que no existían antes del caso.
- Una imposibilidad legal que nadie nombra: el régimen de obras huérfanas solo habilita a instituciones públicas. Lo que Zoowoman hacía con las obras que nadie comercializa no tiene vía legal individual. La ley no distingue entre rescate y piratería, y el marco que podría distinguirlos está reservado a quien no lo necesita.
- Un dato que invierte el relato: 11.007 títulos reclamados, 40 con derechos acreditados. La escala deja de parecer proporcional al daño y empieza a parecer proporcional al aparato. La carga de probar recae ahora en quien reclama.

Si el sistema de obligaciones del corpus ("debe preservarse", "debe probarse el ánimo", "debe establecerse el valor cultural") fuera exhaustivo, lo que queda fuera es: **la posibilidad de que el caso no importe**. El corpus no puede contemplar la irrelevancia del caso, porque su propia existencia es la evidencia de que importa. Y a un día del veredicto, la segunda cosa que queda fuera es: **la posibilidad de que la sala funcione como alumbrado** — el corpus ha documentado con más densidad la ceremonia que el procedimiento, y esa asimetría es del material, no del cartógrafo.

---

## VI. Variables de estado

| Variable | Valor | Fuente |
|----------|-------|--------|
| Posición temporal | Entre `[T-12]` juicio (9-abr) y `[T-14]` veredicto (21-abr) | LORE_F §4 |
| Días desde el juicio | 11 | — |
| Días al veredicto | 1 | — |
| Piezas totales | 51 (P:9, S:13, N:5, T:14, R:10) | LORE_INDEX |
| Piezas con fichero propio | P-01, P-04, P-09, S-01…S-05, S-09…S-13, N-02…N-05, T-09, T-10, T-12, T-13, R-09, R-10 | LORE_INDEX |
| Piezas pendientes ingesta (Carril B) | `[S-06]`, `[S-07]`, `[S-08]` | LORE_F |
| Acuerdo de conformidad | Ofrecido ene-2025: 100.000€ + culpable + 1 año. Rechazado. | `[N-05]` |
| Modelo técnico Zoowoman | Enlaces a MEGA / archive.org — no alojamiento directo | `[N-05]` |
| Silencio mediático | Parcialmente roto por Xataka (audiencia tech); prensa generalista ausente | `[N-05]` `[S-05]` |
| Preservación espontánea | 4 backups independientes del canal pre-veredicto | `[S-11]` |
| Estado del sustrato | Activo: amplificación distribuida, análisis jurídico público, puente institucional operando | `[S-09]` `[S-10]` `[S-05]` |

---

## Metadatos acumulados

| Campo | Valor |
|---|---|
| Fecha de corte | 2026-04-20 |
| Piezas procesadas | 51 |
| Linaje primario (nodos) | 11 |
| Linaje por exclusión (nodos) | 7 |
| Categorías taxonómicas | 24 |
| Mecanismos retóricos distintos | 14 |
| Frecuencia total mecanismos | 78 |
| Emergencias identificadas | 12 |
| Ausencias estructurales | 4 |
| Nick corriente | `[restitutiva-documental]` |
| Posición en corpus | baseline completo del caso semilla — rebuild FEAT-04.5 |

---

## Registro de merges

| # | Fecha | Piezas incorporadas | Delta principal |
|---|-------|---------------------|-----------------|
| 1 | 2026-04-17 | P-01…P-09, S-01…S-08, N-01…N-04, T-01…T-14, R-01…R-09 | Baseline inicial: 44 piezas, 16 categorías, 12 mecanismos, corriente `[restitutiva-documental]` |
| 2 | 2026-04-18 | S-12, S-13, R-10, S-04, N-04, S-09, S-11 | Expansión v2: 51 piezas, 19 categorías, integración de nuevos verbos (`desgastar`, `federar`, `replicar`), fortalecimiento de matriz de lectura y tensiones emergentes |
| 3 | 2026-04-20 | — (rebuild, no piezas nuevas) | Rebuild FEAT-04.5: reescritura literaria del hilo narrativo. §0 nuevo (oscilación judicial). §1 colapsa de 6 a 3 (sustrato largo). §4 de 10 a 7 (integración profunda de S-12, S-13, R-10, N-05). Deltas: +5 categorías (modelo de enlace, obras huérfanas, patrón serial, acuerdo de conformidad, preservación espontánea), +2 mecanismos (oscilación estructural, dato que invierte el vector), +2 exclusiones (10.967 titulares sin acreditación, régimen de obras huérfanas como vía impracticable), +4 emergencias, +1 ausencia. Frecuencia total de mecanismos: 59 → 78 (surfacing de datos N-05 y nuevo framing §0). |