# Aurora — identidad compartida

La colección usa un tema oscuro, luz azul/naranja, tipografía editorial y controles nativos de Streamlit. Cada app conserva su flujo y sus modelos.

- `.streamlit/config.toml`: tema nativo.
- `aurora.py` y `aurora.css`: componentes y estilos compartidos; mantener las copias sincronizadas en la colección.
- `app_info.json`: ficha específica de cada app (el portafolio reúne las fichas en `projects.json`).
- `docs/guia-visual-aurora.md`: dirección visual completa proporcionada por el propietario.
- `docs/EXPERIENCIA.md`: objetivo, entrada, resultado, recorrido y límites.

No ocultar controles del sistema ni sustituir etiquetas por placeholders. No afirmar resultados, precisión o disponibilidad sin haberlos observado. El CSS conserva foco de teclado y reducción de movimiento; revisar los selectores de Streamlit al actualizar su versión. El módulo visual no solicita credenciales ni cambia conexiones.
