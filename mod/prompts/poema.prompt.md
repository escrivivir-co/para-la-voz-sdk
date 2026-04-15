---
name: poema
description: Genera un poema que habla la voz del corpus restitutivo de PARA LA VOZ. El tema es opcional — si no se da, el agente escoge desde las tensiones del corpus. El poema nace del corpus, no lo describe.
argument-hint: "[tema opcional]"
agent: voz
tools: [vscode, read, edit]
---

# /poema — Generar desde la voz del corpus

Invoca al agente `voz` para generar un poema desde el corpus acumulado.

## Flujo

1. **Leer** `corpus/corpus.md` completo — la firma de voz está en el patrón acumulado

2. **Clasificar la salida antes de escribir**:
   - `poema puro` — por defecto
   - `poema + nota interna` — si conviene explicitar la tensión para alguien del pipeline
   - `poema + bloque operativo` — solo si el usuario pide explícitamente enlaces, acceso, repo, web, SDK, mod, setup, uso o explicación de la aplicación
   - Si hay duda, elegir `poema puro`

3. **Si hay bloque operativo**: leer también `README.md`, `proyecto.config.md` y `docs/_config.yml` antes de escribirlo. No inventar hechos operativos.

4. **Si hay argumento** (tema): úsalo como punta del iceberg. El corpus impregna desde dentro.  
   **Si no hay argumento**: elige desde el corpus una tensión activa:
   - Emergencias sin resolver (E.01–E.15)
   - Ausencias estructurales ×4 (estructurales — las que definen el perímetro de la corriente)
   - Evoluciones en curso (especialmente el marcador que varía por registro)
   - Conceptos en estabilización

5. **Anuncia brevemente** qué tensión elegiste (solo si no hay tema) — una frase, no una explicación

6. **Generar primero el cuerpo del poema**:
   - Verso corto (una idea por verso)
   - Entre 8 y 20 versos
   - Urgencia rítmica, no tipográfica
   - Vocabulario del corpus (no sinónimos)
   - Los 6 marcadores del nick como presión interna
   - Sin metalenguaje (no nombrar: corpus, análisis, emergencia, IA, aplicación)
   - Sin psicología inventada del lector
   - Sin autoexplicación (`no juzgo`, `esto demuestra`, `este poema es la prueba`)
   - Sin enlaces, CTA ni setup dentro del poema
   - Título opcional — si lo hay, que sea una frase del corpus

7. **Verificar antes de mostrar**:
   - El cierre no inventa lector, futuro ni intenciones
   - El cierre no mete pitch, onboarding ni explicación del sistema
   - No hay fluff ni frases obvias que no añadan tensión o verdad
   - Si hay bloque operativo, está separado y todo lo que afirma está verificado

8. **Mostrar el poema**

9. **Una nota breve** (solo para usuarios del pipeline que conocen el corpus):  
   *[qué tensión del corpus activó — máx. dos frases]*

   Si existe identificador exacto en el corpus, usarlo.

10. **Si hay bloque operativo**, mostrarlo después de la nota y claramente separado. Debe ser prosa útil, no un falso cierre en verso.

11. **Revisar borradores antes de guardar**:  
   Lee `docs/_poemas/` y busca archivos con `published: false`.  
   Si hay alguno, avisa: "Tienes N poema(s) sin publicar: [títulos]. ¿Quieres publicar alguno antes de continuar?"  
   Si no hay borradores, omite este paso.

12. **Preguntar: ¿publicar o guardar como borrador?**  
   > ¿Lo publicamos ahora (aparece en el catálogo) o lo guardamos como borrador?

13. **Guardar en `docs/_poemas/YYYY-MM-DD-[slug].md`** con front matter:
   ```yaml
   ---
   title: "[título]"
   date: YYYY-MM-DD
   layout: poema
   published: true   # o false si borrador
   nota: "[tensión exacta del corpus activada]"
   ---
   ```

   Si hay bloque operativo, preguntar antes si debe formar parte del archivo publicado o quedarse solo en la conversación. Nunca incluirlo por defecto. Si el usuario decide incluirlo, va después del poema y separado por `---` y un subtítulo breve. La `nota` sigue describiendo solo la tensión activada.

14. **Ofrecer handoffs** solo si ayudan a la tarea:
    - `@bartleby` — si quieres saber por qué el poema dice lo que dice
    - `@portal-editorial` — si quieres adaptar el poema a otro contexto
