# Aurora v1 — Jhuza / Lab

Identidad compartida por ChatPDF, Visión y el portafolio. El tema pertenece a la capa de presentación; cada aplicación conserva su propósito y sus modelos.

## Archivos

- `.streamlit/config.toml`: tema oscuro nativo, tipografía de interfaz y colores de controles.
- `aurora.css`: tokens de color, retícula, vidrio, reflejos, tarjetas y adaptación móvil.
- `aurora.py`: navegación, portada, títulos de sección, estado inicial y pie.

Los tres repositorios incluyen copias idénticas de estos archivos para desplegarse de forma independiente, sin paquetes externos de diseño. Al modificar el sistema, sincronizar las tres copias. No usar clases generadas de Streamlit; los paneles propios tienen claves explícitas. Revisar los selectores `data-testid` al actualizar Streamlit.

## Reglas visuales

Fondo `#05070B`, superficie `#0D1420`, texto `#F4F6FA`, texto secundario `#A9B5C7`, azul `#4C8DFF` y naranja `#FF8A4C`. El azul da profundidad y el naranja destaca la acción. Mantener la mayor parte de la superficie oscura.

Serif de sistema para las portadas y sans serif nativa para lectura y controles. Paneles de 24 px de radio, bordes finos y fondos suficientemente opacos para leer. Escultura abstracta hecha con CSS, sin descargas de fuentes ni animaciones continuas. El efecto de vidrio tiene una alternativa legible si no existe `backdrop-filter`.

Conservar controles nativos, etiquetas visibles, foco de teclado y mensajes de validación. No ocultar herramientas de Streamlit mediante CSS. A 640 px se apilan portada y contenido; el catálogo cambia a dos columnas a 900 px y una a 640 px. Respetar `prefers-reduced-motion`.

## Revisión después de cambios

Comprobar escritorio y móvil, apertura de menús/ayudas, carga de archivos, formularios vacíos, resultado y error. Ejecutar las pruebas sin API y realizar una prueba de servicio con una clave válida cuando se necesite verificar el modelo. No añadir datos de precisión, porcentajes o evidencias de ejecución inventados.
