"""Self-contained Aurora presentation layer; no model or credential logic."""
from html import escape
from pathlib import Path
import streamlit as st

PORTFOLIO = "https://jhginterfacesmultimodalesportfolio.streamlit.app/"


def setup(title, section):
    st.set_page_config(page_title=f"{title} · Jhuza", page_icon="◈", layout="wide", initial_sidebar_state="collapsed")
    css = Path(__file__).with_name("aurora.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.markdown(f'<nav class="aurora-nav" aria-label="Navegación principal"><a class="aurora-brand" href="{PORTFOLIO}" target="_self">JHUZA<span> / LAB</span></a><span class="aurora-nav-section">{escape(section)}</span><a class="aurora-back" href="{PORTFOLIO}" target="_self">Portafolio ↗</a></nav>', unsafe_allow_html=True)


def hero(eyebrow, title, accent, description, kind="document"):
    st.markdown(f'<header class="aurora-hero"><div class="aurora-hero-copy"><p class="aurora-eyebrow">{escape(eyebrow)}</p><h1>{escape(title)}<br><em>{escape(accent)}</em></h1><p class="aurora-intro">{escape(description)}</p></div><div class="aurora-sculpture {escape(kind)}" aria-hidden="true"><div class="aurora-orbit orbit-one"></div><div class="aurora-orbit orbit-two"></div><div class="aurora-orbit orbit-three"></div><div class="aurora-core"></div><span class="aurora-sculpture-label">INPUT / INSIGHT</span></div></header>', unsafe_allow_html=True)


def section(number, title, note=""):
    st.markdown(f'<div class="aurora-section"><span>{escape(number)}</span><h2>{escape(title)}</h2><p>{escape(note)}</p></div>', unsafe_allow_html=True)


def empty_state(title, description):
    st.markdown(f'<div class="aurora-empty"><div class="aurora-empty-mark" aria-hidden="true">◈</div><h3>{escape(title)}</h3><p>{escape(description)}</p></div>', unsafe_allow_html=True)


def footer(label):
    st.markdown(f'<footer class="aurora-footer"><span>JHUZA / INTERFACES MULTIMODALES</span><span>{escape(label)}</span></footer>', unsafe_allow_html=True)
