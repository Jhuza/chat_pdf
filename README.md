# ChatPDF · Interfaces multimodales

Consulta documentos PDF mediante extracción de texto, fragmentación, embeddings de OpenAI, recuperación con FAISS y una cadena de preguntas y respuestas. Interfaz Aurora: fondo oscuro, luz azul/naranja, paneles de vidrio y jerarquía editorial.

## Ejecutar

Python 3.10 o posterior. Validación local realizada con Python 3.12.

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Introduce tu clave de OpenAI en el campo de contraseña, carga un PDF con texto seleccionable, escribe una pregunta y pulsa **Consultar documento**. El texto del documento se envía a OpenAI para generar embeddings y responder. La clave y el índice se mantienen en la sesión; no se usa una caché global para documentos ni se escriben claves en el repositorio.

El índice se reutiliza al consultar el mismo documento y se invalida al cambiar de archivo o clave. La respuesta queda identificada con la pregunta que la produjo. Los PDF escaneados sin texto requieren OCR previo.

## Lógica conservada

- Fragmentos de 500 caracteres, solapamiento de 20 y separador de salto de línea.
- OpenAI embeddings, FAISS similarity search y cadena `stuff`.
- Modelo `gpt-4o-mini-2024-07-18`, temperatura 0. Se usa `ChatOpenAI` para enviar el modelo a la interfaz de chat apropiada.
- Extracción con PyPDF2 y acceso a estadísticas del documento.

Se actualizaron Streamlit y FAISS para la presentación y la compatibilidad del entorno. Se retiraron dependencias visuales sin uso, incluido el pin antiguo de Altair incompatible con el nuevo Streamlit. LangChain y OpenAI conservan sus versiones originales.

## Verificación

```sh
python -m pip install -r requirements-dev.txt
python -m pytest tests -q
```

Las pruebas usan el PDF del repositorio, la extracción, el fragmentador, FAISS y la cadena QA reales, con embeddings y respuesta remota simulados. Cubren validación, reutilización del índice, cambio de clave/documento y PDF vacío o corrupto. No consumen API. La disponibilidad y calidad de la respuesta del servicio requieren una prueba con una clave válida.

Consulta `AURORA.md` para mantener el sistema visual. El archivo de entrada en Streamlit Cloud sigue siendo `app.py`.
