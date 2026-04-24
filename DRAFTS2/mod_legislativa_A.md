# MOD/LEGISLATIVA — §1. BLOQUE A — Identidad del mod y separación del SDK

← [Índice](mod_legislativa_INDEX.md) · Siguiente: [Bloque B →](mod_legislativa_B.md)

> **Dependencia:** este bloque asume que el refactor ontológico del SDK
> ([§R — Bloque R](mod_legislativa_R.md)) ya se ha ejecutado en `main`.
> Las rutas y nombres genéricos del SDK reflejan la terminología post-refactor
> ("documental/documento" en lugar de "editorial").

---

### A-1. Invariante de aislamiento SDK/mod

El SDK core (`.github/`) NO DEBE ser modificado por ninguna operación del mod.
Todo artefacto generado por el cristalizador o por intervención manual DEBE
residir en `mod/` o en `corpus/`.

**Artefacto de verificación:**
- Fichero: [.github/copilot-instructions.md](.github/copilot-instructions.md), §Regla fundamental
- Condición: el flujo de actualización es estrictamente unidireccional (`main → mod`)
- Test: ningún commit en la rama `mod/legislativa` DEBE contener diff sobre `.github/`

**Artefacto de soporte existente:**
- Fichero: [.vscode/settings.json](.vscode/settings.json)
- Estado: ya configura `mod/agents`, `mod/skills`, `mod/prompts`, `mod/hooks`, `mod/instructions` como fuentes de artefactos Copilot
- Acción: ninguna. La infraestructura de resolución de rutas ya soporta el mod.

### A-2. Invariante de aislamiento mod/legislativa vs. mod/restitutiva

El mod `legislativa` DEBE ser operacionalmente independiente del mod `restitutiva`.
No comparten rama, no comparten corpus, no comparten artefactos en `mod/`.
Lo único compartido es el SDK en `.github/`.

**Verificación:** la rama `mod/legislativa` DEBE partir de `main`, no de `mod/restitutiva`.

### A-3. Estructura de directorios del mod

DEBERÁ crearse la siguiente estructura al inicializar el mod:

```
mod/
  agents/              ← agentes específicos del ámbito jurídico
  prompts/             ← comandos específicos (tipos documentales, etc.)
  skills/              ← taxonomía base jurídica y ejemplos
  hooks/               ← hooks del ciclo procesal
  instructions/        ← instrucciones de voz adaptadas al registro legal
corpus/
  actuaciones/         ← textos originales verbatim (sustituye a editoriales/)
  analisis/            ← informes Bartleby (.analisis.md)
  corpus.md            ← mapa acumulativo de taxonomía y linajes
guiones/               ← roadmaps de ciclo por actuación (.guion.md)
docs/
  _documentos/         ← colección Jekyll de documentos legales (sustituye a _poemas/)
```

| Directorio SDK (genérico post-refactor §R) | Directorio mod/legislativa | Motivo del cambio |
|---------------------------------------------|---------------------------|-------------------|
| `corpus/documentos/`                        | `corpus/actuaciones/`     | La unidad de input del mod es una actuación procesal; el SDK genérico dice "documentos" |
| `docs/_poemas/` (restitutiva)               | `docs/_documentos/`       | La unidad de output no es un poema sino un documento legal |

**Backlog item:**
- [ ] **TASK A-3.1** — Crear árbol de directorios `mod/` con subdirectorios vacíos + `.gitkeep`
- [ ] **TASK A-3.2** — Crear `corpus/` con subdirectorios `actuaciones/`, `analisis/`, y `corpus.md` vacío
- [ ] **TASK A-3.3** — Crear `docs/_documentos/` como colección Jekyll

### A-4. Fichero de configuración del proyecto

DEBERÁ crearse `proyecto.config.md` a partir de la plantilla SDK.

**Artefacto plantilla:** [proyecto.config.template.md](proyecto.config.template.md)

**Valores a instanciar:**

```yaml
nombre: "legislativa"
descripcion: |
  Mod jurídico-procesal del SDK para-la-voz. Analiza actuaciones
  procesales (declaraciones, partes, resoluciones) y cristaliza
  documentos normativos con trazabilidad al corpus.
idioma: "es"
version: "0.1.0"
fecha-inicio: "2026-04-16"
```

**Backlog item:**
- [ ] **TASK A-4.1** — Crear `proyecto.config.md` con los valores anteriores

### A-5. Configuración Jekyll del mod

DEBERÁ crearse `docs/_config.yml` a partir de la plantilla.

**Artefacto plantilla:** [docs/_config.yml.example](docs/_config.yml.example)

**Valores a instanciar:**

```yaml
mod_name:        "legislativa"
mod_branch:      "mod/legislativa"
mod_corriente:   "[pendiente de primer análisis]"
mod_description: "Documentos legales cristalizados desde el corpus procesal"

collections:
  documentos:           # ← sustituye 'poemas'
    output: true
    sort_by: date
```

**Dependencia:** la colección `documentos` exige que `docs/_documentos/` exista (TASK A-3.3).

**Backlog item:**
- [ ] **TASK A-5.1** — Crear `docs/_config.yml` con la colección `documentos`

### A-6. Workflow de despliegue

DEBERÁ copiarse la plantilla de GitHub Actions y configurarse para la rama del mod.

**Artefacto plantilla:** [.github/workflows/pages.template.yml](.github/workflows/pages.template.yml)

**Cambio requerido:** línea `branches:` → `["mod/legislativa"]`

**Backlog item:**
- [ ] **TASK A-6.1** — Crear `.github/workflows/pages.yml` en la rama `mod/legislativa`
