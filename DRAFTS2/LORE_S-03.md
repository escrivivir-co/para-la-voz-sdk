# `[S-03]` — Analisis del caso (Cristobal)

> ← [LORE_B.md](LORE_B.md)
> ← [LORE_INDEX.md](LORE_INDEX.md)

---

## Identificacion

| Campo | Valor |
|-------|-------|
| Marca | `[S-03]` |
| Emisor | `[P-04]` Cristobal |
| Tipo | Analisis/comentario |
| Fuente principal | <https://www.twitch.tv/videos/2747836356> |
| VOD | *❄️ELMAÑANEO#1241. Hoy, TRUMP ORMUZ, M. Rajoy el Asturiano, Filmoteca vs Cerezo, Vito Judicial, Begoña Imputati, Plus Ultra, Juicio Koldo,* |
| Duracion total del VOD | `12501s` (`3:28:21`) |
| Ventana preservada | `01:15:00` -> `02:22:00` |
| Duracion transcrita | `4020s` (`1:07:00`) |
| Estado | Transcripcion GPU completa recuperada y archivada como soporte |

## Artefactos preservados

- Audio largo de trabajo: `tmp/media-cache/S-03-cristobal-caso-long-twitch.aac`
- Transcripcion GPU completa: `tmp/media-cache/S-03-cristobal-caso-GPU-int8.txt`
- Estado reanudable: `tmp/media-cache/S-03-cristobal-caso-GPU-int8.state.json`
- Chunks previos de referencia: `tmp/media-cache/S-03-cristobal-0115-0120.aac`, `S-03-cristobal-0120-0125.aac`, `S-03-cristobal-0125-0130.aac`, `S-03-cristobal-0130-0135.aac`

## Anclajes utiles

| Eje | Dato util | Conecta con |
|-----|-----------|-------------|
| Encuadre narrativo | Cristobal define el episodio como **"lore profundo de internet"** antes que noticia aislada | `[R-03]`, `[S-01]`, `[S-02]` |
| Naturaleza de Zoowoman | La presenta como repositorio de *loss media*, usado por universidad, academia, guionistas y publico cinefilo | `[T-04]`, `[T-05]`, `[T-06]` |
| Ausencia de lucro directo | Repite que Zoowoman no tenia publicidad ni suscripciones y se mantenia desde el bolsillo del Feo | `[T-09]` |
| Hipotesis acusatoria | Situa el centro juridico en el **beneficio indirecto** y en la adquisicion posterior de derechos por parte de Cerezo | `[T-09]`, `[T-10]`, `[T-13]` |
| Lectura de infraestructura | Formula FlixOle como **"Zoowoman, de pago"**, es decir, apropiacion mercantil del mismo terreno cultural | `[P-09]`, `[T-06]` |
| Debate doctrinal | Abre dos porros centrales: autorizacion de titulares y estatuto legal del *loss media* / dominio publico | `[T-07]`, `[R-07]` |
| Contraataque especulativo | Llega a plantear si Cerezo copia el modelo de utilidad de Zoowoman al monetizarlo en FlixOle | `[S-04]` |

## Extractos a preservar

> "esto ha sido este caso mas bien el lore internet... el lore profundo de internet"

> "No habia ni suscripciones, no habia absolutamente nada... lo mantenia el de su bolsillo"

> "Flixole es... literalmente, Zoowoman, de pago"

> "El porro de beneficio indirecto"

> "la peticion de carcel para un divulgador... supone en la practica un mecanismo de vigilancia y control social"

> "Solamente lo que le libra al feo ahora mismo es establecer el valor cultural de lo que estaba haciendo"

## Nota de soporte

- La transcripcion completa se recupero en GPU el `2026-04-16` con `faster-whisper`, modelo `small`, `cuda`, `int8`.
- La pasada cubre la ventana completa `01:15:00` -> `02:22:00` en `14` chunks de `300` segundos.
- El raw completo vive en cache para futuras pasadas o verificacion manual; este fichero condensa los puntos utiles para el lore y deja trazada la existencia del transcript entero.
