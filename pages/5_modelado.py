# pages/5_modelado.py
import streamlit as st

st.set_page_config(page_title="Modelado Dimensional", page_icon="⭐", layout="wide")

st.markdown("""
<div style="
    text-align: center;
    padding: 50px 20px;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
    backdrop-filter: blur(20px);
    border-radius: 25px;
    margin: 0 0 50px 0;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
">
    <div style='font-size: 4rem; margin-bottom: 20px;'>⭐</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        Modelado Dimensional
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Esquema Estrella, Copo de Nieve y técnicas de modelado
    </p>
</div>
""", unsafe_allow_html=True)

# Introducción
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 40px;
    margin: 40px 0;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    <h2 style='color: #ffffff; margin-bottom: 20px;'>📝 ¿Qué es el Modelado Dimensional?</h2>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        El <strong style='color: #fff;'>modelado dimensional</strong> es una técnica de diseño de bases de datos optimizada para 
        consultas y análisis en Data Warehouses. A diferencia de la normalización tradicional, prioriza la <strong style='color: #fff;'>
        simplicidad de consultas</strong> y el <strong style='color: #fff;'>rendimiento analítico</strong> sobre la eficiencia de almacenamiento.
    </p>
</div>
""", unsafe_allow_html=True)

# Conceptos Básicos
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🎯 Conceptos Fundamentales</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.info("""
    **📊 Tabla de Hechos (Fact Table)**
    
    Contiene las **métricas cuantitativas** del negocio:
    - Ventas, ingresos, cantidades
    - Eventos o transacciones
    - Medidas numéricas agregables
    - Claves foráneas a dimensiones
    
    **Características:**
    - ✅ Muchas filas (millones/billones)
    - ✅ Pocas columnas
    - ✅ Principalmente valores numéricos
    - ✅ Actualizaciones frecuentes
    """)

with col2:
    st.success("""
    **🔷 Tablas de Dimensiones**
    
    Contienen **información descriptiva** del contexto:
    - Quién, qué, cuándo, dónde, por qué, cómo
    - Atributos textuales
    - Categorías y jerarquías
    - Datos de referencia
    
    **Características:**
    - ✅ Menos filas que hechos
    - ✅ Muchas columnas descriptivas
    - ✅ Principalmente texto
    - ✅ Actualizaciones menos frecuentes
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Esquemas
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>📐 Tipos de Esquemas</h2>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["⭐ Esquema Estrella", "❄️ Esquema Copo de Nieve"])

with tab1:
    st.success("### ⭐ Star Schema - El Más Común")
    
    st.write("**Estructura:**")
    st.write("""
    - ⭐ Una tabla de hechos central
    - 📂 Múltiples tablas de dimensiones conectadas directamente
    - 📊 Las dimensiones NO están normalizadas
    - 🌟 Forma visual de estrella
    """)
    
    st.write("**Ventajas:**")
    st.write("""
    - ✅ Consultas simples y rápidas
    - ✅ Fácil de entender para usuarios
    - ✅ Mejor rendimiento de consultas
    - ✅ Menos JOINs necesarios
    """)
    
    st.write("**Desventajas:**")
    st.write("""
    - ⚠️ Redundancia de datos en dimensiones
    - ⚠️ Mayor espacio de almacenamiento
    """)

with tab2:
    st.info("### ❄️ Snowflake Schema - Normalizado")
    
    st.write("**Estructura:**")
    st.write("""
    - ⭐ Tabla de hechos central
    - 🔗 Dimensiones normalizadas en múltiples tablas
    - 📊 Jerarquías explícitas
    - ❄️ Forma visual de copo de nieve
    """)
    
    st.write("**Ventajas:**")
    st.write("""
    - ✅ Menor redundancia de datos
    - ✅ Menos espacio de almacenamiento
    - ✅ Mejor integridad referencial
    - ✅ Mantenimiento más sencillo de jerarquías
    """)
    
    st.write("**Desventajas:**")
    st.write("""
    - ❌ Consultas más complejas
    - ❌ Más JOINs = Menor rendimiento
    - ❌ Más difícil de entender
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Comparativa
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>⚖️ Comparativa</h2>
</div>
""", unsafe_allow_html=True)

comparison_data = {
    "Característica": ["Complejidad", "Rendimiento", "Espacio", "Mantenimiento", "Comprensión", "JOINs"],
    "⭐ Estrella": ["Simple", "Alto", "Más espacio", "Fácil", "Intuitivo", "Pocos"],
    "❄️ Copo Nieve": ["Compleja", "Medio", "Menos espacio", "Complejo", "Técnico", "Muchos"]
}

st.table(comparison_data)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
