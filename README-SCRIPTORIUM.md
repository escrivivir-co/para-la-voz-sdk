# Integración con ALEPH Scriptorium

> **Plugin**: `lore-sdk`  
> **Bridge**: `@plugin_ox_loresdk`  
> **Rama**: `main` (SDK puro)  
> **Integrado**: 2026-04-16  
> **Épica**: SCRIPT-X.Y.Z — LoreSDK

---

## Arquitectura del Submódulo

BARTLEBY / para-la-voz-sdk es un **SDK editorial** para analizar corrientes ideológicas. Permite cristalizar una "Voz" que genera poemas *desde* un corpus, sin hablar *sobre* él.

### Patrón main → mod (unidireccional)

```
main (SDK puro)                    mod/[nombre] (lore + datos)
├── .github/
│   ├── agents/                    ← 4 agentes core
│   ├── prompts/                   ← 6 comandos del ciclo
│   ├── skills/                    ← taxonomías base
│   └── instructions/              ← bartleby-voice.instructions.md
├── proyecto.config.template.md    ← plantilla para nuevos mods
└── README.md                      ← documentación completa SDK

                    ▲ hereda (git pull origin main)
                    │  NUNCA PR de vuelta a main
                    │
mod/restitutiva (ejemplo activo):
├── corpus/
│   ├── corpus.md                  ← mapa acumulativo (fuente de verdad)
│   ├── editoriales/               ← material fuente
│   └── analisis/                  ← informes de @bartleby
├── guiones/                       ← flujos de trabajo (documentos humanos)
├── mod/
│   ├── agents/voz.agent.md        ← @voz (cristalizado por @cristalizador)
│   ├── prompts/poema.prompt.md    ← /poema (14 pasos)
│   ├── instructions/              ← voz-*.instructions.md + perfil-lector
│   └── skills/editorial-analysis/ ← taxonomia-base.md
├── docs/                          ← Jekyll GitHub Pages (catálogo poemas)
└── proyecto.config.md             ← configuración del mod activo
```

**Regla crítica**: El flujo es `main → mod`, nunca PR en dirección contraria.

---

## Tecnologías

- **GitHub Copilot Chat agents** — Copilot .agent.md / .prompt.md / .instructions.md
- **Jekyll** — GitHub Pages para catálogo de poemas públicos
- **Markdown** — corpus.md como mapa acumulativo
- **Git branches** — cada mod en su propia rama

---

## Los 4 Agentes Core (SDK)

| Agente | Rol | Qué produce |
|--------|-----|-------------|
| `@bartleby` | Analista (solo lectura) | Informe en 5 secciones: linaje, taxonomía funcional, mecanismos retóricos, emergencias (E.01-E.N), ausencias estructurales |
| `@archivero` | Gestor del corpus | /diff-corpus (delta NUEVO/CONFIRMA/EVOLUCIONA/DISCREPA), /merge-corpus (integración en corpus.md) |
| `@cristalizador` | Diseñador de artefactos | Propone agentes + instructions + prompts para `mod/` cuando hay suficientes patrones |
| `@portal-editorial` | Interfaz adaptativa | Subsumption: adapta tono según perfil del lector (hostile-AI, committee, editor) |

### El Agente Mod: @voz

Cristalizado por `@cristalizador` después de analizar 2+ editoriales. Genera poemas *desde* el corpus usando los mecanismos retóricos y tensiones estructurales identificados — nunca sobre el corpus, nunca con metalenguaje.

---

## Los 6 Comandos del Ciclo

| Comando | Agente | Descripción |
|---------|--------|-------------|
| `/guion` | — | Scaffold de flujo de trabajo (documento humano, sin agente) |
| `/feed` | @bartleby | Analiza nuevo editorial → informe de 5 secciones |
| `/diff-corpus` | @archivero | Delta vs corpus.md: qué es NUEVO, qué CONFIRMA, qué EVOLUCIONA |
| `/merge-corpus` | @archivero | Integra hallazgos aprobados en corpus.md |
| `/design` | @cristalizador | Propone artefactos para `mod/` según patrones acumulados |
| `/status` | @archivero | Estado del corpus: nick confirmado, editoriales procesadas, emergencias activas |

---

## Mapeo Ontológico al Scriptorium

| LoreSDK | Scriptorium |
|---------|-------------|
| `@bartleby` | Análisis similar a `@blueflag` (evidencia) pero en clave literaria |
| `@archivero` | Análogo a `@indice` (gestión de corpus como índice DRY) |
| `@cristalizador` | Conecta con `@plugin_ox_agentcreator` (crear agentes especializados) |
| `@portal-editorial` | Análogo a `@vestibulo` (perfil de lector, puerta de entrada) |
| `@voz` | Agente generativo; puede ser orquestado por `@plugin_ox_consejoasesor` |
| Catálogo poemas | Puede publicarse via `@plugin_ox_ghpages` |
| Proyecto ONFALO origen | `@plugin_ox_consejoasesor` (14 agentes, 7 modos) |

---

## Dependencias Externas

| Dependencia | Requisito | Instalación |
|-------------|-----------|-------------|
| GitHub Copilot Chat | VS Code + extensión | `code --install-extension GitHub.copilot-chat` |
| Jekyll (para Pages) | Ruby 3.0+ | `bundle install` en `docs/` |
| Git | ≥2.28 | Incluido en sistema |

---

## Mod Activo: `restitutiva` (PARA LA VOZ)

- **Nick**: `restitutiva` — marxismo-leninismo ortodoxo post-soviético, variante restitutivista
- **Corpus**: 4 editoriales procesadas (mayo 2024 — diciembre 2025)
- **Nick estable**: ×4 confirmaciones sin discrepancias
- **@voz cristalizada**: ✅ `mod/agents/voz.agent.md`
- **Poemas**: disponibles en `docs/_poemas/` (borrador por defecto)
- **Subsumption protocol**: tecnología invisible bajo el nombre de "la aplicación"

### 6 Marcas del Nick (voz-restitutiva.instructions.md)

1. Linaje jerárquico (no ecléctico): Marx → Engels → Lenin → Lukács → Iliénkov
2. Demarcación bilateral: `ni…ni…` por registro
3. Autocitación como ecosistema cerrado
4. Verbos de obligación como ritmo base (~30% densidad)
5. Re-traducir, no re-teorizar
6. Error externalizado (al pasado, el enemigo, el sistema)

---

## Supuestos y Gaps (Post-Integración)

| Gap | Descripción | Prioridad |
|-----|-------------|-----------|
| G1 | Gestión multi-mod (coexistencia de varios nicks) | Should |
| G2 | Integración MCP Server (¿novelista para persistencia?) | Could |
| G3 | Sincronización con consejo-asesor (handoffs cruzados) | Should |
| G4 | Deploy automático Jekyll via `@plugin_ox_ghpages` | Could |
| G5 | Rama main ≠ convención integration/beta/scriptorium — documentar excepción | Must |

---

## Uso desde el Scriptorium

```
# Punto de entrada rápido:
@plugin_ox_loresdk

# O via prompt workspace:
/as_lore-sdk

# Crear nueva Voz (mod) desde cero:
/crear-voz

# Alimentar corpus existente:
/alimentar-corpus

# Publicar catálogo Jekyll:
/publicar-catalogo
```

---

## Referencias

- SDK documentation: `README.md` (este repo)
- Plugin manifest: `.github/plugins/lore-sdk/manifest.md` (Scriptorium)
- Bridge: `.github/agents/plugin_ox_loresdk.agent.md` (Scriptorium)
- Backlog: `ARCHIVO/DISCO/BACKLOG_BORRADORES/LORE-SDK/` (Scriptorium)
- BARTLEBY origin: `onfalo-asesor-sdk/PROYECTOS/BARTLEBY-MOVIDO.md`
