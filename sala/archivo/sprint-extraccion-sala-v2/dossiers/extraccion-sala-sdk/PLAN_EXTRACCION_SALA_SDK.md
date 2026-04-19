# Dossier — extraccion-sala-sdk

> **Origen:** BL-02 del sprint-cristalizacion-v1
> **Prioridad:** alta
> **Tasks estimadas:** 5-7

## Contexto

La funcionalidad "sala de coordinación" (protocolo multi-agente orquestado) fue desarrollada en `mod/legislativa` como parte del lore legislativa. Pero es **genérica**: cualquier lore puede usarla. El SDK (`main`) no la tiene aún.

Según la regla fundamental del repo, el flujo es:
```
main (SDK) ──git pull──→ mod/[nombre]
```

Hay que **promover** los artefactos de sala a `.github/` en la rama `main`, y luego que `mod/legislativa` los herede.

## Inventario de artefactos a promover

### Prompts (7 ficheros)
| Origen (mod/) | Destino (.github/) |
|---|---|
| `mod/prompts/sala-entrar.prompt.md` | `.github/prompts/sala-entrar.prompt.md` |
| `mod/prompts/sala-seguir.prompt.md` | `.github/prompts/sala-seguir.prompt.md` |
| `mod/prompts/sala-aprobar.prompt.md` | `.github/prompts/sala-aprobar.prompt.md` |
| `mod/prompts/sala-reconectar.prompt.md` | `.github/prompts/sala-reconectar.prompt.md` |
| `mod/prompts/sala-salir.prompt.md` | `.github/prompts/sala-salir.prompt.md` |
| `mod/prompts/sala-archivar.prompt.md` | `.github/prompts/sala-archivar.prompt.md` |
| `mod/prompts/sala-aleph.prompt.md` | Revisar: ¿es genérico o específico del lore? |

### Instructions (2 ficheros)
| Origen (mod/) | Destino (.github/) |
|---|---|
| `mod/instructions/sala-protocolo.instructions.md` | `.github/instructions/sala-protocolo.instructions.md` |
| `mod/instructions/plan-attribution.instructions.md` | `.github/instructions/plan-attribution.instructions.md` |

### Templates (nuevo)
| Artefacto | Destino (.github/) |
|---|---|
| Plantilla tablero.md | `.github/templates/sala-tablero.template.md` |
| Plantilla carpetas dossier | `.github/templates/sala-dossier.template.md` |
| Plantilla carpetas agente | `.github/templates/sala-agente.template.md` |

### Lo que se queda en mod/ (específico del lore)
- `mod/instructions/legislativa-universo.instructions.md`
- `mod/instructions/lore-estado.instructions.md`
- `mod/instructions/lore-routing.instructions.md`
- `mod/instructions/lore-schema.instructions.md`
- `mod/instructions/onboarding-map.instructions.md`
- Agentes del mod, skills del mod, universos

## Operación

1. Crear rama desde `main` (ej. `feat/sala-sdk`)
2. Copiar artefactos a `.github/`
3. Generalizar: eliminar referencias específicas al lore legislativa
4. Crear templates de tablero, dossier, agente
5. Actualizar `copilot-instructions.md` de SDK con la sección "Sala"
6. Commit + merge a `main`
7. En `mod/legislativa`: `git merge main` — hereda los artefactos SDK
8. Eliminar duplicados en `mod/` que ahora vienen de `.github/`
9. Adaptar `mod/` para override/extend donde haga falta (ej. sala-aleph si es lore-specific)
