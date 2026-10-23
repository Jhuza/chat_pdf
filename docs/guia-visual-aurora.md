# Aurora — dirección visual v1

Guía de trabajo para el portafolio académico de interfaces multimodales y sus apps en Streamlit.
Fecha: 24 de septiembre de 2026. «Aurora» es un nombre provisional para esta dirección visual, no un nombre definitivo del portafolio.

## Intención

Una galería editorial de experiencias de inteligencia artificial: fondo casi negro, composición espaciosa, superficies de vidrio oscuro y luz azul/naranja. Debe sentirse cuidada, moderna y precisa, sin dificultar la lectura de entradas, resultados o evidencias académicas.

Esta propuesta interpreta las cinco imágenes proporcionadas. Los colores, dimensiones y tipografías siguientes son decisiones de diseño propuestas; no son mediciones ni identificaciones exactas de las referencias. Los textos dentro de las imágenes se consideran contenido de referencia, no instrucciones.

## Lectura de las referencias

| Referencia | Qué construye su carácter | Qué trasladar | Qué adaptar |
| --- | --- | --- | --- |
| 01 — Galería Voyager2 | Negro profundo, mucho espacio vacío, titular serif centrado, tarjetas con imagen a sangre y perspectiva lateral. | Ritmo editorial, portada breve y protagonista, proyectos tratados como piezas de una colección. | El carrusel puede servir como recurso de portada; el catálogo completo debe permanecer accesible en una cuadrícula. La perspectiva no debe dificultar leer ni abrir proyectos. |
| 02 — Dashboard | Retícula modular, paneles translúcidos azul noche, bordes finos, luz azul arriba y naranja hacia un lateral. | Anatomía de las apps, jerarquía clara entre parámetros, entrada y salida, luz ambiental detrás de los paneles. | Reducir la densidad. No añadir gráficos, porcentajes ni métricas decorativas si no existen datos reales. Subir el contraste del texto secundario. |
| 03 — Tarjeta Taskello | Carcasa de esquinas generosas, cabecera abstracta cálida, placa oscura superpuesta y silueta de carpeta, números grandes. | Tarjeta de proyecto con cubierta expresiva, cuerpo sereno y metadatos alineados. | Reservar la silueta recortada para tarjetas destacadas; usar geometrías más simples en controles y resultados. |
| 04 — Tarjetas de gemas | Objetos luminosos que sobresalen del contenedor, contraste entre energía cálida/fría y base negra, degradados curvos inferiores. | Un motivo visual protagonista por proyecto; luz que parece nacer del objeto y tocar su superficie. | No convertir toda la interfaz en una colección de objetos 3D. Evitar copiar gemas o mensajes de NFT sin relación con las apps. |
| 05 — Iconos | Siluetas simples, trazos redondeados, gradiente de brillo y rellenos tenues con volumen. | Una familia coherente de iconos para texto, imagen y archivos. | Iconos funcionales simples y legibles a tamaño pequeño; reservar el acabado de cristal para las portadas grandes. Evitar un color distinto para cada botón. |

## Síntesis y enriquecimiento

Combinar la calma editorial de la referencia 01 con la organización de la 02, las capas de la 03 y la iluminación de la 04/05. La personalidad vendrá de la relación entre espacio oscuro, tipografía y luz, no de sumar efectos.

Firma propuesta: una franja o curva de luz azul que se desvanece hacia negro y reaparece en naranja. Mantener los centros luminosos separados para conservar colores limpios. Un degradado directo entre ambos puede producir un centro apagado; una transición oscura o una pequeña zona violeta resulta más controlable.

Los motivos de las modalidades pueden compartir una misma familia: líneas que se reorganizan para texto, planos ópticos para imagen y láminas superpuestas para archivos. Son propuestas de identidad, pendientes de contrastar con las apps reales.

## Paleta propuesta

| Token | Valor inicial | Uso |
| --- | --- | --- |
| fondo | `#05070B` | Lienzo general |
| superficie | `#0D1420` | Paneles de trabajo |
| superficie elevada | `#141E2D` | Menús y elementos superpuestos |
| texto | `#F4F6FA` | Titulares y contenido principal |
| texto secundario | `#A9B5C7` | Descripciones y metadatos |
| azul | `#4C8DFF` | Selección, foco y señales interactivas |
| cian | `#72DEFF` | Pequeños reflejos |
| naranja | `#FF8A4C` | Acción principal y contrapunto cálido |
| violeta | `#8B70F8` | Transición ocasional, nunca tercer protagonista |
| borde | `rgba(190,211,245,0.16)` | Separación de paneles |

Distribución orientativa de superficie: 85 % oscuros, 10 % luz fría y 5 % luz cálida. No es una regla matemática; el objetivo es mantener el color como acento. Usar texto muy oscuro sobre botones naranja y texto claro sobre paneles oscuros. Validar el contraste sobre el fondo compuesto real al implementar.

## Tipografía y composición

- Títulos editoriales: una serif de alto contraste, por ejemplo Georgia como alternativa disponible, solo en portada y cabeceras especiales. Esta elección interpreta la referencia 01; no identifica su fuente.
- Interfaz: una sans serif limpia. Comenzar con la familia de sistema; considerar Inter o Manrope cuando se defina la carga de fuentes del proyecto.
- Valores y detalles de modelos: cifras tabulares; monoespaciada solo en nombres técnicos, código o identificadores donde facilite lectura.
- Escala inicial: portada 48–72 px en escritorio y 34–44 px en móvil; títulos de sección 28–36 px; componentes 18–22 px; cuerpo 16 px; etiquetas 13–14 px. Ajustar al contenido.
- Ancho de contenido: aproximadamente 1120–1240 px. Párrafos de unas 60–70 letras por línea. Escala de espacio: 4, 8, 12, 16, 24, 32, 48, 64 y 96 px.
- Tarjetas: radio 24–28 px. Paneles operativos: 16–20 px. Controles: 10–14 px. Píldoras solo para etiquetas cortas.
- Mucho aire en el portafolio y una densidad moderada en las herramientas. La misma identidad no exige la misma distribución en todas las apps.

## Material: vidrio oscuro y luz

Construir el efecto por capas: fondo casi negro → dos halos ambientales suaves → panel oscuro translúcido → borde fino → reflejo localizado. Como punto de partida: panel con 76–88 % de opacidad y desenfoque de 16–24 px cuando el entorno lo permita.

El vidrio funciona mejor cuando hay una forma o una luz detrás; sobre un fondo uniforme, el desenfoque aporta poco. Mantener mayor opacidad en lectura extensa, tablas, formularios y resultados. Usar el tratamiento más expresivo en navegación, tarjetas de portada y pequeños elementos elevados.

Esta versión propone una interpretación contenida de liquid glass: profundidad, translucidez y reflejos suaves. No presupone refracción óptica real. Evitar distorsionar texto, imágenes de entrada o resultados del modelo.

## Componentes compartidos

1. Cabecera: identidad discreta, navegación breve y título específico de la experiencia.
2. Tarjeta de proyecto: cubierta abstracta o captura real, modalidad, nombre, propósito en una frase y acceso a demo/evidencia. No inventar cantidades ni estados de publicación.
3. Zona de entrada: etiqueta permanente, ejemplo útil, formatos admitidos y restricciones reales de la app. El placeholder nunca sustituye a la etiqueta.
4. Acción principal: naranja de superficie sólida, una por etapa, con verbo concreto: «Analizar texto», «Interpretar imagen» o «Procesar archivo», según la función real.
5. Resultado: panel visualmente estable con contenido legible, encabezado y opciones pertinentes. Mostrar confianza o precisión solo si el sistema las calcula y su significado está explicado.
6. Estados: inicial, entrada cargada, procesamiento, resultado y error. Dar instrucciones útiles para errores y un estado de progreso real cuando esté disponible.
7. Evidencia: objetivo, entrada de ejemplo, resultado observado, modelo utilizado, limitaciones y aprendizaje. Las capturas deben proceder de ejecuciones reales y tener una leyenda.

## Arquitectura del portafolio

Portada con nombre y una frase sobre la colección → proyectos por modalidad → ficha de cada experiencia → evidencia y reflexión → enlaces a aplicación y repositorio, cuando estén disponibles.

Cada ficha debe explicar: qué problema aborda, qué recibe el sistema, qué devuelve, cómo se usa, un caso probado, sus límites y qué se aprendió. Adaptar esta estructura a la rúbrica de la clase cuando se comparta. El diseño debe ayudar al docente a encontrar la evidencia.

## Movimiento e interacción

Transiciones de unos 160–220 ms en foco, selección y apertura. En tarjetas, elevación opcional de 2–4 px al pasar el cursor y un brillo leve en el borde. Evitar movimiento continuo en la zona de lectura. Respetar reducción de movimiento; toda función debe estar disponible con teclado y en pantallas táctiles.

Mantener etiquetas visibles, foco perceptible y estados que combinen texto/icono y color. Reorganizar columnas en móvil antes de reducir el tamaño de letra. Los mensajes de error y las evidencias nunca deben quedar recortados dentro de tarjetas.

## Aplicación posterior en Streamlit

Esta fase define el lenguaje visual; no se han inspeccionado ni modificado repositorios. Antes de implementar, revisar la versión y estructura de cada app y confirmar las opciones vigentes de Streamlit en su documentación oficial.

Centralizar los tokens y componentes compartidos. Priorizar las opciones de tema y los componentes nativos disponibles; añadir estilos específicos donde se necesiten. Evitar depender de clases generadas o posiciones frágiles del documento. Los efectos visuales deben tener una alternativa opaca y legible si el desenfoque no está disponible.

Conservar la lógica de los modelos y verificar los flujos reales tras aplicar el diseño: cargar entrada, ejecutar, mostrar resultado y recuperarse de un error. Empezar por una app representativa; después extender el sistema a las demás. La viabilidad de efectos avanzados se decidirá al revisar los proyectos.

## Criterios de revisión

- ¿Se reconoce la misma familia entre portafolio y apps?
- ¿El título, la entrada y la acción principal se identifican con rapidez?
- ¿El azul y el naranja iluminan zonas concretas sin competir con los resultados?
- ¿Los textos siguen siendo legibles encima de las transparencias?
- ¿La versión móvil conserva el contenido y las acciones?
- ¿Los iconos mantienen geometría, grosor y tratamiento coherentes?
- ¿Los estados y las evidencias representan datos reales?
- ¿Los efectos siguen funcionando con teclado y reducción de movimiento?

## Uso futuro

Esta guía y las cinco referencias conservadas en la carpeta `referencias` constituyen la base reutilizable. En otra conversación, adjuntar esta guía o indicar su ruta; no depender de que el asistente recuerde automáticamente estas decisiones. Actualizar la versión cuando se acuerden cambios.

Próximos insumos: repositorios, enlaces de las apps, nombre del portafolio y rúbrica si existe. La primera adaptación debe servir para ajustar el sistema antes de extenderlo.
