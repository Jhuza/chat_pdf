import hashlib
import io
import platform
import streamlit as st
from aurora import empty_state, footer, hero, section, setup
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

setup("ChatPDF", "01 / DOCUMENTOS")
hero("CHATPDF · GENERACIÓN AUMENTADA POR RECUPERACIÓN", "Un documento.", "Una conversación.",
     "Carga un PDF, pregunta sobre su contenido y explora respuestas construidas a partir de sus fragmentos.")

with st.sidebar:
    st.subheader("Acerca de ChatPDF")
    st.write("Este agente te ayuda a realizar análisis sobre el PDF cargado.")
    st.markdown("**El recorrido**\n\n1. Carga un documento.\n2. Escribe tu pregunta.\n3. Revisa la respuesta.")
    st.caption("La extracción requiere texto seleccionable; no incluye reconocimiento de texto en imágenes.")
    st.caption(f"Python {platform.python_version()} · RAG / LangChain / FAISS")

left, right = st.columns([1, 1.15], gap="large")
with left:
    with st.container(key="input_panel"):
        section("01", "Tu documento", "PDF → contexto")
        ke = st.text_input("Clave de OpenAI", type="password", placeholder="Ingresa tu clave de API",
                           help="Se utiliza para procesar el documento y responder tus preguntas con OpenAI.")
        pdf = st.file_uploader("Carga tu archivo PDF", type=["pdf"])
        st.caption("Usa un PDF con texto seleccionable. El documento se prepara cuando envías tu primera pregunta.")
        user_question = st.text_area("¿Qué quieres saber del documento?", height=130,
                                    placeholder="Por ejemplo: ¿cuáles son las ideas principales?")
        ask = st.button("Consultar documento", type="primary", width="stretch")

# This index belongs to one user's session. Do not cache documents or credentials globally.
document_id = hashlib.sha256(pdf.getvalue()).hexdigest() if pdf else None
credential_id = hashlib.sha256(ke.encode()).hexdigest() if ke else None
context_id = (document_id, credential_id)
if st.session_state.get("context_id") != context_id:
    for key in ("knowledge_base", "answer", "answered_question", "document_stats"):
        st.session_state.pop(key, None)
    st.session_state.context_id = context_id

with right:
    with st.container(key="output_panel"):
        section("02", "Respuesta", "Contexto → comprensión")
        if ask:
            if not ke:
                st.warning("Ingresa tu clave de OpenAI para continuar.")
            elif pdf is None:
                st.warning("Carga un archivo PDF para continuar.")
            elif not user_question.strip():
                st.warning("Escribe una pregunta sobre el documento.")
            else:
                st.session_state.pop("answer", None)
                st.session_state.pop("answered_question", None)
                try:
                    with st.spinner("Buscando contexto en tu documento…"):
                        if "knowledge_base" not in st.session_state:
                            reader = PdfReader(io.BytesIO(pdf.getvalue()))
                            text = "\n".join(page.extract_text() or "" for page in reader.pages)
                            if not text.strip():
                                raise ValueError("El PDF no contiene texto extraíble. Prueba con un documento con texto seleccionable.")
                            splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=20, length_function=len)
                            chunks = splitter.split_text(text)
                            embeddings = OpenAIEmbeddings(openai_api_key=ke)
                            st.session_state.knowledge_base = FAISS.from_texts(chunks, embeddings)
                            st.session_state.document_stats = (len(text), len(chunks))
                        docs = st.session_state.knowledge_base.similarity_search(user_question)
                        llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini-2024-07-18", openai_api_key=ke)
                        chain = load_qa_chain(llm, chain_type="stuff")
                        st.session_state.answer = chain.run(input_documents=docs, question=user_question)
                        st.session_state.answered_question = user_question
                except Exception as exc:
                    st.error(f"No se pudo procesar la consulta: {exc}")

        if "answer" in st.session_state:
            st.caption(f"Pregunta: {st.session_state.answered_question}")
            st.markdown(st.session_state.answer)
            characters, chunks_count = st.session_state.document_stats
            with st.expander("Detalles del documento"):
                st.write(f"Texto extraído: {characters:,} caracteres")
                st.write(f"Documento dividido en {chunks_count} fragmentos")
            st.caption("Contrasta la respuesta con el documento original.")
        elif not ask:
            empty_state("Las respuestas empiezan aquí", "Carga tu documento y plantea una pregunta. Este espacio mostrará la respuesta del modelo.")

footer("DOCUMENTOS / TEXTO / CONTEXTO")
