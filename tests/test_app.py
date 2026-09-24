"""Exercise actual PDF extraction, splitting, FAISS and QA with offline model doubles."""
import io
from pathlib import Path
from unittest.mock import MagicMock
import openai
import streamlit as st
from streamlit.testing.v1 import AppTest
from PyPDF2 import PdfWriter
import langchain.embeddings

ROOT = Path(__file__).resolve().parents[1]


class OfflineEmbeddings:
    builds = 0

    def __init__(self, **kwargs):
        pass

    def embed_documents(self, texts):
        type(self).builds += 1
        return [[float(len(text)), float(text.count("a")), 1.0] for text in texts]

    def embed_query(self, text):
        return [float(len(text)), float(text.count("a")), 1.0]


def pdf_file(data=None):
    value = io.BytesIO(data if data is not None else (ROOT / "example.pdf").read_bytes())
    value.name = "example.pdf"
    return value


def test_initial_state_and_missing_input_validation():
    app = AppTest.from_file(str(ROOT / "app.py")).run(timeout=30)
    assert not app.exception
    app.button[0].click().run()
    assert "clave" in app.warning[0].value
    app.text_input[0].set_value("offline-key").run()
    app.button[0].click().run()
    assert "PDF" in app.warning[0].value


def test_rag_reuses_index_and_resets_on_key_or_document_change(monkeypatch):
    monkeypatch.setattr(st, "file_uploader", lambda *a, **kw: pdf_file())
    OfflineEmbeddings.builds = 0
    monkeypatch.setattr(langchain.embeddings, "OpenAIEmbeddings", OfflineEmbeddings)
    completion = MagicMock(return_value={"choices": [{"message": {"role": "assistant", "content": "Respuesta de prueba sobre el documento."}, "finish_reason": "stop"}], "usage": {"prompt_tokens": 10, "completion_tokens": 10, "total_tokens": 20}})
    monkeypatch.setattr(openai.ChatCompletion, "create", completion)
    app = AppTest.from_file(str(ROOT / "app.py")).run(timeout=30)
    app.text_input[0].set_value("offline-key").run()
    app.text_area[0].set_value("¿Cuál es el tema principal?").run()
    app.button[0].click().run(timeout=30)
    assert not app.exception and not app.error
    assert "Respuesta de prueba" in app.session_state["answer"]
    assert OfflineEmbeddings.builds == 1
    assert completion.call_args.kwargs["model"] == "gpt-4o-mini-2024-07-18"
    assert len(completion.call_args.kwargs["messages"][0]["content"]) > 100
    app.text_area[0].set_value("Dame un resumen.").run()
    app.button[0].click().run(timeout=30)
    assert OfflineEmbeddings.builds == 1 and completion.call_count == 2
    app.text_input[0].set_value("another-offline-key").run()
    assert "answer" not in app.session_state and "knowledge_base" not in app.session_state
    monkeypatch.setattr(st, "file_uploader", lambda *a, **kw: None)
    app.run()
    assert "answer" not in app.session_state


def test_empty_pdf_and_corrupt_pdf_show_recoverable_errors(monkeypatch):
    writer = PdfWriter()
    writer.add_blank_page(width=100, height=100)
    content = io.BytesIO()
    writer.write(content)
    monkeypatch.setattr(st, "file_uploader", lambda *a, **kw: pdf_file(content.getvalue()))
    app = AppTest.from_file(str(ROOT / "app.py")).run(timeout=30)
    app.text_input[0].set_value("offline-key").run()
    app.text_area[0].set_value("Resume el archivo.").run()
    app.button[0].click().run(timeout=30)
    assert not app.exception
    assert "texto extraíble" in app.error[0].value
    assert "knowledge_base" not in app.session_state
    monkeypatch.setattr(st, "file_uploader", lambda *a, **kw: pdf_file(b"not a PDF"))
    app.button[0].click().run()
    assert not app.exception and app.error
