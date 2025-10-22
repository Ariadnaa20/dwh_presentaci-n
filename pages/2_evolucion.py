# pages/2_evolucion.py
import streamlit as st

st.set_page_config(page_title="Evolución del DWH", page_icon="📜", layout="wide")

st.markdown("<h1 style='text-align:center; color:#1e3d8f;'>📜 Evolución histórica del DWH</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Explora la evolución desde los primeros sistemas hasta la actualidad</p>", unsafe_allow_html=True)
st.divider()

eras = [
    {"title": "1980s - DSS", "icon": "📊", "subtitle": "Sistemas de soporte a decisiones",
     "points": ["Datos de sistemas transaccionales",
                "Reportes simples para gerentes",
                "Sistemas no estandarizados"]},
    
    {"title": "1990s - Bill Inmon & Kimball", "icon": "🏗️", "subtitle": "Nacimiento del DWH",
     "points": ["Repositorio centralizado, integrado y no volátil",
                "Modelado dimensional y Data Marts"]},

    {"title": "2000s - ETL & OLAP", "icon": "💻", "subtitle": "Herramientas comerciales",
     "points": ["ETL automatizado (Informatica, DataStage)",
                "Sistemas OLAP más eficientes"]},

    {"title": "2010s+ - Big Data & Cloud", "icon": "☁️", "subtitle": "Análisis avanzado",
     "points": ["DWH en la nube (Redshift, Snowflake)",
                "Integración con AI/ML",
                "Self-service analytics"]}
]

# Botones tipo carrusel
st.subheader("📅 Línea temporal interactiva")
selected = st.radio("Selecciona una época:", [f"{e['title']} {e['icon']}" for e in eras])

# Mostrar contenido de la época seleccionada
for era in eras:
    if f"{era['title']} {era['icon']}" == selected:
        st.markdown(f"### {era['title']} {era['icon']}")
        st.markdown(f"**{era['subtitle']}**")
        for point in era["points"]:
            st.write(f"- {point}")
        break

st.divider()

# Ejemplo práctico
with st.expander("💡 Ejemplo práctico: Análisis de ventas"):
    st.write("""
Antes, una empresa que quería analizar ventas tenía que esperar a que los reportes nocturnos se generaran.  
Hoy, con DWH modernos y en la nube:
- Analiza datos en tiempo casi real
- Compara tendencias históricas
- Aplica modelos de Machine Learning para predicciones
""")

# Impacto
st.subheader("🎯 Impacto de la evolución del DWH")
col1, col2 = st.columns(2)
col1.success("⚡ Mayor velocidad de análisis")
col1.info("📚 Consolidación de datos históricos")
col2.success("🔮 Analítica avanzada y predicciones")
col2.info("✅ Reducción de errores por manipulación manual")

st.divider()
