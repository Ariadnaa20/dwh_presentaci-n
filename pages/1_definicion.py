# pages/1_definicion.py
import streamlit as st

st.set_page_config(page_title="Definición del DWH", page_icon="📊", layout="wide")

# --- Título ---
st.markdown("<h1 style='text-align:center; color:#ffffff;'>📊 Definición y propósito del DWH</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Explora cada sección interactuando con los bloques y expanders</p>", unsafe_allow_html=True)

st.divider()

# --- Introducción ---
st.subheader("📝 Introducción")
st.write("""
Un **Data Warehouse (DWH)** es un sistema que recopila, integra y organiza datos provenientes de distintas fuentes
para facilitar la **toma de decisiones estratégicas** en una organización.  
Su propósito es centralizar la información para que los analistas puedan obtener **insights valiosos** sin afectar los sistemas operacionales.
""")

st.divider()

# --- Características ---
st.subheader("✨ Características principales")
st.columns([1, 1, 1])
col1, col2, col3 = st.columns(3)
col1.success("🧩 Integración de datos\nCombina información de múltiples sistemas (ERP, CRM, bases de datos).")
col2.info("📂 Orientado a temas\nLos datos se organizan según áreas de interés: ventas, clientes, inventario.")
col3.warning("⏳ No volátil\nLos datos históricos se mantienen sin alteraciones frecuentes.")

col1, col2, col3 = st.columns(3)
col1.success("📊 Variedad histórica\nPermite analizar tendencias y comparativas a lo largo del tiempo.")
col2.info("⚡ Optimizado para consultas\nDiseñado para responder consultas analíticas complejas.")
col3.warning("💡 Escalable\nSe puede ampliar según crecimiento de la organización.")

st.divider()

# --- Ejemplo práctico interactivo ---
with st.expander("💡 Ejemplo práctico: Retail"):
    st.write("""
Imaginemos una empresa de retail que tiene:
- 🏬 Un sistema ERP para gestión de inventario.
- 📇 Un CRM que almacena datos de clientes.
- 🛒 Una plataforma de ventas online.

El **DWH** recopila información de todos estos sistemas, organiza los datos por categorías
(ventas, clientes, productos), y permite que el equipo de marketing analice:
""")
    st.columns([1, 1])
    col1, col2 = st.columns(2)
    col1.metric(label="📈 Productos más vendidos", value="5000 unidades/mes")
    col2.metric(label="👥 Clientes más leales", value="1.200 clientes")

st.divider()

# --- Beneficios ---
st.subheader("🎯 Beneficios de usar un DWH")
col1, col2 = st.columns(2)
col1.success("✅ Decisiones basadas en datos: fundamentadas en información consolidada.")
col1.info("⚡ Análisis más rápido: evita consultas directas a sistemas transaccionales lentos.")
col2.success("📚 Histórico confiable: mantiene datos para reportes y proyecciones.")
col2.info("🚀 Mejora la eficiencia operativa: reduce preparación manual de reportes.")

st.divider()

# --- Conceptos relacionados ---
with st.expander("📌 Conceptos relacionados"):
    st.write("""
- **ETL (Extract, Transform, Load):** Extraer, transformar y cargar datos al DWH.
- **OLAP (Online Analytical Processing):** Análisis multidimensional sobre los datos.
- **Data Mart:** Subconjunto del DWH enfocado en un área específica de negocio.
- **BI (Business Intelligence):** Herramientas para análisis y visualización de datos.
""")

st.divider()

