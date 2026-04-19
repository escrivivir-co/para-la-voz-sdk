# Plan — future-machine-sdk

> **Fecha:** 19-abr-2026
> **Autor:** GPT-5.4
> **Dossier:** `sala/dossiers/future-machine-sdk/`

## 1. Contexto

El dossier archivado `future-machine-universo-1` nació como cierre del feature sobre `universo-1`, pero el trabajo real quedó repartido en los dossiers hermanos que ya hemos ido separando:

- `lore-db-sdk` — piezas y `@Loreador`
- `corpus-sdk` — capa corpus y `@Archivero`
- `grafo-sdk` — contrato portable de grafo
- `universos-sdk` — persistencia de universos
- `cortos-sdk` — persistencia de obras derivadas

Esa separación era correcta para limpiar responsabilidades, pero dejó un hueco nuevo: **falta la carcasa compositiva** que convierta esas capas en una máquina reconocible y portable.

Eso era, en el fondo, la intuición útil de `future-machine`: no otra capa de datos, sino la **estructura que ensambla el ciclo entero** y lo vuelve navegable desde:

- `@Portal` — puerta de entrada
- `@Pipeline` — orquestación técnica
- prompts de onboarding y status
- una inicialización reproducible cuando exista el lore exportado en `{{LORE_DIR}}`

Este dossier exporta esa carcasa a `main`.

Relación con otros dossiers:

| Dossier | Branch | Qué hace | Relación |
|---------|--------|----------|----------|
| `lore-db-sdk` | main | Piezas y scaffold `lore/` | Slot upstream |
| `corpus-sdk` | main | Capa corpus | Slot upstream |
| `grafo-sdk` | main | Contrato de grafo | Slot intermedio |
| `universos-sdk` | main | Contrato de universo | Slot downstream |
| `cortos-sdk` | main | Contrato de obra derivada | Slot downstream |
| **future-machine-sdk** | main | **Carcasa compositiva + entrypoints** | Este dossier |
| `future-machine-legislativa` | mod/legislativa | Instancia la máquina con el caso Feo | Hereda este contrato |

## 2. Anclas

| Artefacto | Ubicación | Estado |
|-----------|-----------|--------|
| Dossier archivado | `sala/archivo/sprint-cristalizacion-v1/dossiers/future-machine-universo-1/` | Referencia histórica |
| Portal SDK | `.github/agents/portal.agent.md` | Ya existe como puerta de entrada genérica |
| Archivero SDK | `.github/agents/archivero.agent.md` | Slot corpus |
| Dramaturgo SDK | `.github/agents/dramaturgo.agent.md` | Slot downstream de creación |
| lore-db-sdk | `sala/dossiers/lore-db-sdk/` | Slot piezas |
| corpus-sdk | `sala/dossiers/corpus-sdk/` | Slot corpus |
| grafo-sdk | `sala/dossiers/grafo-sdk/` | Slot grafo |
| universos-sdk | `sala/dossiers/universos-sdk/` | Slot universos |
| cortos-sdk | `sala/dossiers/cortos-sdk/` | Slot obras |

## 3. Restricciones

- `future-machine` **no duplica** los contratos de piezas, corpus, grafo, universos ni cortos
- `future-machine` **no crea un agente nuevo** por defecto: `Portal` sigue siendo la puerta de entrada y `Pipeline` el orquestador cuando el mod lo provea
- El SDK no impone nombres concretos como `/user-empieza-aqui` o `/lore-status`; define **slots de entrypoint** que cada mod puede materializar con sus prompts
- Debe convivir con la inicialización de `lore/` prevista en `lore-db-sdk`
- Tiene que servir tanto para mods simples como para mods con Portal, Pipeline y dashboard ricos

## 4. Propuesta

### 4.1. Contrato de slots de la machine

Crear `.github/instructions/future-machine-schema.instructions.md`.

La machine se define como un ensamblaje de slots:

- `slot_lore_db`
- `slot_corpus`
- `slot_grafo`
- `slot_universos`
- `slot_obras`
- `slot_pipeline`
- `slot_portal`
- `slot_entry_start`
- `slot_entry_status`
- `slot_entry_refresh`

Slots opcionales:

- `slot_sala`
- `slot_dashboard_cliente`
- `slot_generacion_obra`

Cada slot declara:

- ruta canónica
- agente o prompt propietario
- dependencia upstream/downstream
- estado (`pendiente`, `operativo`, `legacy`, `workaround`)

### 4.2. Template de manifest

Crear `.github/templates/future-machine.template.md` para instanciar como:

```text
{{LORE_DIR}}/FUTURE_MACHINE.md
```

Ese manifest no duplica datos del lore. Solo registra:

- qué slots existen
- qué rutas ocupan
- qué agentes los sirven
- cuáles son las puertas de entrada del usuario

### 4.3. Integración con Portal

Ampliar el Portal SDK para que, si el mod declara una `future-machine`, pueda presentarla como cierre del ciclo en vez de quedarse solo en corpus.

El Portal SDK debe reconocer el patrón:

```text
start here -> status -> pipeline refresh -> universo -> obra
```

sin imponer nombres de prompts. Solo detecta y documenta los entrypoints declarados por el mod.

### 4.4. Integración con la inicialización del lore

Extender la documentación de inicialización para que el scaffold de `lore/` pueda incluir un `FUTURE_MACHINE.md` vacío o de ejemplo cuando el mod quiera operar el ciclo completo.

### 4.5. Documentar la machine como cierre de ciclo

Actualizar `.github/copilot-instructions.md` para dejar explícito que la machine es la composición portable:

```text
lore-db -> corpus -> grafo -> universos -> cortos
           ↑                     ↓
         Portal              Pipeline
```

No es una capa más. Es la forma de **navegar y orquestar** el conjunto.

## 5. Salida operativa

- Tracking: [BACKLOG.md](./BACKLOG.md)
- Decisiones del PO: [RESPUESTAS.md](./RESPUESTAS.md)
- Tasks: carpeta [tasks](./tasks)