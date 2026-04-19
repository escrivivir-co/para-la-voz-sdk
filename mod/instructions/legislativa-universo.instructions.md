---
description: "Peculiaridades del lore legislativa para generación de universos y cortos. Contexto acumulado durante el diseño del grafo."
applyTo: "DRAFTS2/**"
---

# Instrucciones del mod legislativa — Universos

> **Nota:** Para conteos y estado del lore, ver `lore-estado.instructions.md`.

## Estructura temporal del universo

```
T=0 (presente 17-abr-2026)  ──→  X (veredicto, desplazable)  ──→  T+∞
```

**X no es una fecha fija.** Es el evento de resolución judicial. Fecha candidata 21-abr-2026, pero X puede desplazarse. En la rama R4, X se desplaza ~1 año por suspensión cautelar.

## El corto original vs el universo

El corto original (*Tres Lunes Para Una Misma Sala*) cubre **R1, R2 y R3** como un lunes que se abre en tres universos mínimos. Fue escrito con 44 piezas y antes de que existieran S-04, S-09, S-10, S-11, N-05.

**R4 no está en el corto original.** R4 (contraataque, la posición de Cerezo se erosiona) es la rama que se ha expandido en detalle durante el diseño del grafo. Tiene 6 nodos diseñados propios en `universo/universo-1.md`.

Los cortos generados desde `/dramaturgo-editar-universo` son **piezas independientes**, no actualizaciones del corto original.

## Huecos del universo-1 (R4)

| Hueco | Estado | Nota |
|-------|--------|------|
| H1 | **Resuelto** por `[S-10]`: 11.007 reclamadas vs 40 con derechos | Dato del propio Feo |
| H2 | Abierto: prácticas de adquisición Mercury | Puede elidirse o dejarse como tensión |
| H3 | Abierto: forma jurídica principal del contraataque | Opciones: propiedad industrial / competencia desleal / ambas |
| H4 | Abierto: quién financia la estructura legal | Opciones: crowdfunding / FACUA / institucional / mezcla |
| H5 | Abierto: rol de Bravo en contraofensiva | Opciones: lidera ambos / defiende penal, equipo nuevo ataca / bufete mayor |
| H6 | **Parcialmente resuelto** por `[N-05]`: RD 2016 da base legal a Filmoteca Española | Opción d) añadida |

## Datos duros que el corto debe poder usar

Estos datos no existían cuando se escribió el artefacto ni el corto original:

- **11.007 vs 40**: EGEDA reclama 11.007 películas, tiene derechos de 40. Cine iraní, de Bután, Uganda, Yugoslavia, URSS. `[S-10]`
- **Mercury = 70-80% del cine español distribuido**. `[N-05]`
- **Oferta de acuerdo ene-2025**: culpable + 100k€ + 1 año → rechazado por Feo. `[N-05]`
- **~4.000 análisis** en La Filmoteca Maldita (dato defensa). `[N-05]`
- **Patrón denuncias EGEDA**: 2017 WebTV, 2022 17 webs, Zoowoman. `[N-05]`
- **Hachette vs Internet Archive (2024, EEUU)**: derrota del archivo digital. `[N-05]`
- **RD 2016 obras huérfanas**: solo instituciones públicas pueden. `[N-05]`
- **Zoowoman enlazaba, no alojaba**: matiz jurídico. `[N-05]`
- **~500 GB** todo el canal YouTube. `[S-11]`
- **Hydra archiving**: torrent archive.org, Drive, disco 2TB, backup completo con metadatos y chat de directos. `[S-11]`
- **Feo**: "lo interesante a 100 años es el registro de ideas" (comentarios, debates, bibliografía de la comunidad). `[S-11]`
- **"Cada vez que tumben algo aparecerán dos réplicas más"**. `[S-11]`
- **"El cine es, Y SIEMPRE, será nuestro"** — eco de `[S-01]` en la acción de preservación. `[S-11]`

## Consignas que el corpus ha fijado

Estas frases son del corpus y pueden activarse en el corto si el contexto lo permite:

- **"el cine es nuestro"** — `[S-01]`, `[S-11]`
- **"solo la gente salva a la gente"** — `[S-02]`
- **"cada vez que tumben algo aparecerán dos réplicas más"** — `[S-11]`
- **"que internet haga lo suyo"** — `[S-04]`

## Nota sobre metáforas drenadas

La metáfora "cervatillo se vuelve manada" fue un recurso pedagógico de la conversación de diseño. **No es vocabulario del corpus.** No debe aparecer en ningún corto generado. El grafo usa lenguaje neutro: "contraataque", "la posición de Cerezo se erosiona", "estructura colectiva".
