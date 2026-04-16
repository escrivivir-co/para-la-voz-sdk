# MOD/LEGISLATIVA — §6. BLOQUE F — Ciclo de vida: archivar y reiniciar

← [Bloque E](mod_legislativa_E.md) · [Índice](mod_legislativa_INDEX.md)

---

### F-1. Patrón de uso del mod

El mod/legislativa opera por casos. Cada caso tiene un ciclo de vida finito:

```
INICIO → ingesta de actuaciones → acumulación en corpus → cristalización
       → generación de catálogo → CIERRE del caso → archivo → reinicio
```

Este patrón NO existe en el mod/restitutiva (donde el corpus crece indefinidamente).
Es una funcionalidad nueva del SDK.

### F-2. Operación `/archive` (nuevo prompt SDK)

DEBERÁ crearse un prompt a nivel de SDK (reutilizable por cualquier mod) que
ejecute el cierre de un caso.

**Ubicación propuesta:** `.github/prompts/archive.prompt.md`

> **Nota:** este es uno de los pocos casos donde el mod necesita un artefacto en el SDK core.
> La decisión de si se sube a main (PR al SDK) o se mantiene temporalmente en `mod/prompts/`
> queda a criterio del mantenedor del SDK. Para el MVP, PODRÁ residir en `mod/prompts/`.

**Operación archive — pasos:**

1. Verificar que el caso tiene al menos un ciclo completo (feed + diff + merge + documento).
2. Generar un manifiesto del caso:
   ```
   caso: [referencia del procedimiento]
   fecha-inicio: YYYY-MM-DD
   fecha-cierre: YYYY-MM-DD
   actuaciones: N
   analisis: N
   documentos-cristalizados: N
   artefactos-mod: [lista de ficheros en mod/ creados para este caso]
   ```
3. Comprimir en ZIP:
   - `corpus/` completo
   - `guiones/` completo
   - `docs/_documentos/` completo
   - Manifiesto del caso
   - Opcionalmente: `mod/` completo (si el usuario lo solicita)
4. Guardar el ZIP en `archivo/YYYY-MM-DD_caso-[referencia].zip`

### F-3. Operación `/reset` (nuevo prompt)

DEBERÁ crearse un prompt que reinicie el mod para un nuevo caso.

**Ubicación propuesta:** `mod/prompts/reset.prompt.md` (específico del mod, ya que
el mod/restitutiva no necesita reinicio).

**Operación reset — pasos:**

1. Verificar que existe un archivo del caso anterior (TASK F-2). Si no existe, AVISAR y pedir confirmación.
2. Solicitar al usuario qué artefactos de `mod/` conservar:
   - `mod/instructions/` → probablemente SÍ (son genéricos del ámbito jurídico)
   - `mod/skills/` → probablemente SÍ
   - `mod/prompts/` → probablemente SÍ
   - `mod/agents/` → EVALUAR caso a caso
   - `mod/hooks/` → probablemente SÍ
3. Limpiar:
   - `corpus/actuaciones/` → vaciar
   - `corpus/analisis/` → vaciar
   - `corpus/corpus.md` → reiniciar a plantilla vacía
   - `guiones/` → vaciar
   - `docs/_documentos/` → vaciar
4. Mantener intactos:
   - `mod/` (según selección del usuario)
   - `docs/_config.yml`
   - `docs/_layouts/`, `docs/_includes/`, `docs/_sass/`
   - `proyecto.config.md` (actualizar `fecha-inicio` al nuevo caso)
5. Informar del estado post-reset vía `/status`.

### F-4. Directorio de archivo

DEBERÁ crearse `archivo/` como directorio de nivel raíz para almacenar los ZIPs
de casos cerrados. Este directorio DEBERÁ añadirse a `.gitignore` si los ZIPs
no deben subir al repositorio (decisión pendiente del promotor).

**Backlog item:**
- [ ] **TASK F-2.1** — Crear `mod/prompts/archive.prompt.md` (MVP en mod; evaluar migración a SDK)
- [ ] **TASK F-3.1** — Crear `mod/prompts/reset.prompt.md`
- [ ] **TASK F-4.1** — Crear directorio `archivo/` + decidir política de `.gitignore`
- [ ] **TASK F-4.2** — Evaluar si `/archive` y `/reset` deben ser prompts SDK (`.github/prompts/`) o mod (`mod/prompts/`)
