# ENTREGA — CU-01 + ES-04

**Agente:** Sony (Claude Sonnet 4.6)
**Fecha:** 2026-04-19 06:25
**Tasks:** CU-01 + ES-04 (bloque)

---

## Resumen

**CU-01** — Creado prompt `corto-universo.prompt.md` que activa al Dramaturgo Cortos para generar piezas literarias desde ramas del grafo de universos. Cubre plan → aprobación → escritura → guardado con sufijo de modelo. Autocontenido y portable (no hardcodea rutas del lore salvo los ficheros de referencia).

**ES-04** — Creados 3 templates para infraestructura de sala, con placeholders `{{NOMBRE}}`. Cubren: tablero de tareas (tracks, resumen, backlog), carpeta de dossier (estructura completa con tasks/), y carpeta de agente (estado.md con log, handoff y comentarios de formato).

---

## Ficheros producidos

| Fichero | Destino definitivo |
|---------|-------------------|
| `sala/agente-sony/candidato-corto-universo.prompt.md` | `mod/prompts/corto-universo.prompt.md` |
| `sala/agente-sony/candidato-sala-tablero.template.md` | `.github/templates/sala-tablero.template.md` |
| `sala/agente-sony/candidato-sala-dossier.template.md` | `.github/templates/sala-dossier.template.md` |
| `sala/agente-sony/candidato-sala-agente.template.md` | `.github/templates/sala-agente.template.md` |

---

## Pasos que Aleph debe ejecutar

1. **Revisar** los 4 candidatos en `DRAFTS2/sala/agente-sony/`.
2. Si aprueba CU-01: copiar `candidato-corto-universo.prompt.md` → `mod/prompts/corto-universo.prompt.md`.
3. Si aprueba ES-04: copiar los 3 `candidato-sala-*.template.md` → `.github/templates/sala-{tablero,dossier,agente}.template.md`.
4. Cerrar CU-01 y ES-04 en el tablero. Actualizar resumen.
5. Actualizar `estado.md` de Sony con línea `ALEPH: entrega aprobada`.

---

## Notas de diseño

- **corto-universo.prompt.md**: El prompt es una versión portabilizada de `dramaturgo-editar-universo.prompt.md` — elimina referencias hardcodeadas a `LORE_F-02` y reutiliza el argumento `{{universo}}` como variable dinámica. La naming convention de salida usa kebab-case del modelo para trazabilidad multi-modelo.
- **sala-tablero.template.md**: Incluye solo los estados que el protocolo define. El backlog post-sprint y el resumen de conteos son secciones fijas (Aleph siempre las necesita). Los tracks se añaden como bloques copiables.
- **sala-dossier.template.md**: Refleja la estructura real del dossier `extraccion-sala-sdk` + `gap-corto-universo`. Incluye `activacion.prompt.md` como fichero estándar del dossier.
- **sala-agente.template.md**: El bloque de comentarios de log documenta los formatos de línea que usa el protocolo — ayuda a agentes nuevos a entender la convención sin leer el README.
