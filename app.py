import streamlit as st
import pathlib

st.set_page_config(page_title="Presentación DWH", page_icon="📊", layout="wide")

# Cargar CSS
static_path = pathlib.Path(__file__).parent / "static"
with open(static_path / "styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Título y subtítulo
st.markdown("<h1>📊 Data Warehouse (DWH)</h1>", unsafe_allow_html=True)
st.markdown('<p class="sub">Explora los temas usando el sidebar o haciendo scroll por las cards</p>', unsafe_allow_html=True)

# Carrusel de cards
st.markdown("""
<div class="carousel">
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2942/2942821.png">
        <h3>Definición y propósito del DWH</h3>
        <p>Qué es un Data Warehouse y para qué se utiliza.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910768.png">
        <h3>Evolución histórica</h3>
        <p>Cómo ha cambiado el concepto de DWH con el tiempo.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2838/2838890.png">
        <h3>OLTP vs OLAP</h3>
        <p>Diferencias entre sistemas transaccionales y analíticos.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/4149/4149723.png">
        <h3>Arquitectura de un DWH</h3>
        <p>Staging, ETL/ELT y presentación.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910772.png">
        <h3>Modelado dimensional</h3>
        <p>Estrella, copo de nieve, dimensiones y hechos.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910778.png">
        <h3>Dimensiones, hechos y SCD</h3>
        <p>Tipos de dimensiones, hechos y Slowly Changing Dimensions.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3003/3003945.png">
        <h3>Herramientas y tecnologías</h3>
        <p>On-premise y cloud para DWH.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3003/3003940.png">
        <h3>ETL vs ELT</h3>
        <p>Procesos de extracción, transformación y carga de datos.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2921/2921828.png">
        <h3>Rendimiento</h3>
        <p>Particiones e índices para acelerar consultas.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910776.png">
        <h3>Ventajas y limitaciones</h3>
        <p>Fortalezas y debilidades de un DWH.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910780.png">
        <h3>Comparativa con Data Lake / Lakehouse</h3>
        <p>Relaciones y diferencias con otras arquitecturas.</p>
    </div>
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910785.png">
        <h3>Futuro del DWH</h3>
        <p>Tendencias y perspectivas futuras.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Creado por Ariadna, Gabriel, Teo y Oriol | Presentación DWH 2025</p>", unsafe_allow_html=True)
