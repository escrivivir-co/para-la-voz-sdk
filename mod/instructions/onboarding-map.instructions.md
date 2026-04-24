---
description: "Mapa visual de onboarding del mod legislativa. Referencia rápida de directorios, agentes, protocolo y fases del pipeline. Cualquier agente puede presentarlo."
applyTo: "mod/**"
---

# Big Picture — mod/legislativa

## Mapa de directorios

```
 ┌─────────────────────────────────────────────────────────────────┐
 │  para-la-voz-sdk                                               │
 │                                                                 │
 │  .github/          SDK puro (inmutable desde el mod)            │
 │  ├── agents/       5 agentes core (Bartleby, Archivero,        │
 │  │                 Cristalizador, Dramaturgo, Portal)           │
 │  ├── prompts/      7 comandos core (/feed, /status, /guion…)   │
 │  ├── skills/       Protocolos portables (futures-engine,        │
 │  │                 documental-analysis, voice-crystallization)  │
 │  └── instructions/ Reglas de voz Bartleby                      │
 │                                                                 │
 │  mod/              ◀── TU TALLER: artefactos del mod            │
 │  ├── agents/       Puzzle, Archivero Lore, Grafista,            │
 │  │                 Demiurgo, Dramaturgo Cortos, Pipeline        │
 │  ├── prompts/      /user-empieza-aqui, /lore-status,            │
 │  │                 /dramaturgo-editar-universo, /lore-ingest,   │
 │  │                 /pipeline-refresh                             │
 │  ├── instructions/ Schema, estado, routing, universo            │
 │  ├── skills/       Cristalización de features                   │
 │  └── universos/    Vista canónica de universos                  │
 │                                                                 │
 │  DRAFTS2/          ◀── DATOS VIVOS del caso Feo                 │
 │  ├── LORE_*.md     51 piezas tipadas (P, S, N, T, R + F)       │
 │  ├── universo/     Ramas expandidas (universo-1, r1, r2)       │
 │  ├── grafo/        Grafo JSON (nodos, arcos, huecos)            │
 │  └── cristalizacion-*/  Dossiers de feature activos             │
 │                                                                 │
 │  corpus/           Redirect → DRAFTS2/CORPUS_PREVIEW.md         │
 └─────────────────────────────────────────────────────────────────┘
```

## La cadena de 5 agentes

```
  ╔═══════════╗    ╔════════════════╗    ╔══════════╗    ╔══════════╗    ╔═══════════════╗
  ║  Puzzle   ║───▶║ Archivero Lore ║───▶║ Grafista ║───▶║ Demiurgo ║───▶║ Dramaturgo    ║
  ║           ║    ║                ║    ║          ║    ║          ║    ║ Cortos        ║
  ╚═══════════╝    ╚════════════════╝    ╚══════════╝    ╚══════════╝    ╚═══════════════╝
   Valida piezas    Reduce a corpus       Estructura     Diseña          Genera obra
   contra schema    vía Bartleby          el grafo       universos       literaria

  Entrada:          Entrada:              Entrada:       Entrada:        Entrada:
  LORE_*.md         Pack verificado       CORPUS +       Grafo           Universo
  + LORE_INDEX      del Puzzle            LORE_F         completo        instanciado

  Salida:           Salida:               Salida:        Salida:         Salida:
  Pack verificado   CORPUS_PREVIEW.md     grafo/*.json   universo-N.md   CORTO-*.md
```

**Orquestador:** `@Pipeline` — refresca la cadena cuando cambian piezas base.

## Protocolo en 4 movimientos

```
  ┌─────────────────────────────────────────────────────────────┐
  │  1. INGESTAR        /lore-ingest                             │
  │     Puzzle valida → Archivero reduce → corpus actualizado   │
  │     ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤│
  │  2. ESTRUCTURAR     @Grafista generar grafo                 │
  │     Corpus → bifurcaciones → grafo JSON                     │
  │     ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤│
  │  3. BIFURCAR        @Demiurgo crear universo                │
  │     Grafo → ramas → universo instanciado (conversacional)   │
  │     ⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤⏤│
  │  4. NARRAR          /dramaturgo-editar-universo              │
  │     Universo → pieza literaria → CORTO-*.md                 │
  └─────────────────────────────────────────────────────────────┘

  En cualquier momento: @Pipeline /pipeline-refresh para sincronizar todo
```

## Dónde buscar cada cosa

| Necesitas… | Ve a… |
|------------|-------|
| Las piezas del lore (datos) | `DRAFTS2/LORE_*.md` |
| El hilo narrativo | `DRAFTS2/LORE_F.md` |
| El corpus acumulativo | `DRAFTS2/CORPUS_PREVIEW.md` |
| El grafo de futuros | `DRAFTS2/grafo/` (JSON) o `DRAFTS2/LORE_F-02_UNIVERSO.md` (legacy) |
| Las ramas de universo | `DRAFTS2/universo/` |
| Los cortos generados | `DRAFTS2/LORE_F-02_CORTO-*.md` |
| El plan de producción | `DRAFTS2/LORE_PLAN.md` |
| Los dossiers activos | `sala/dossiers/` |
| El esquema de tipos | `mod/instructions/lore-schema.instructions.md` |
| El estado del lore | `mod/instructions/lore-estado.instructions.md` |
| Las rutas canónicas | `mod/instructions/lore-routing.instructions.md` |
| Las reglas de universo | `mod/instructions/legislativa-universo.instructions.md` |

## Comandos rápidos

| Comando | Qué hace | Agente |
|---------|----------|--------|
| `/user-empieza-aqui` | Este mapa | Portal |
| `/lore-status` | Estado concreto del lore cargado | Portal |
| `/lore-ingest` | Ingestar pack completo | Archivero Lore |
| `/dramaturgo-editar-universo` | Generar corto desde rama | Dramaturgo Cortos |
| `/pipeline-refresh` | Sincronizar la cadena | Pipeline |
