# pages/1_definicion.py
import streamlit as st

st.set_page_config(page_title="Definición del DWH", page_icon="📊", layout="wide")

# --- Header con Glassmorphism ---
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
    <div style='font-size: 4rem; margin-bottom: 20px;'>📊</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        Definición y Propósito del DWH
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Explora los fundamentos y características esenciales de un Data Warehouse
    </p>
</div>
""", unsafe_allow_html=True)

# --- Introducción con Card Glassmorphism ---
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
    <h2 style='color: #ffffff; margin-bottom: 25px; font-size: 2rem;'>📝 ¿Qué es un Data Warehouse?</h2>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9; margin-bottom: 20px;'>
        Un <strong style='color: #ffffff; font-weight: 700;'>Data Warehouse (DWH)</strong> es un sistema centralizado que 
        recopila, integra y organiza datos provenientes de múltiples fuentes para facilitar la 
        <strong style='color: #ffffff; font-weight: 700;'>toma de decisiones estratégicas</strong> en una organización.
    </p>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        Su propósito principal es centralizar la información empresarial para que los analistas y ejecutivos puedan obtener 
        <strong style='color: #ffffff; font-weight: 700;'>insights valiosos</strong> sin afectar el rendimiento de los sistemas operacionales.
    </p>
</div>
""", unsafe_allow_html=True)

# --- Características en Grid Glassmorphism ---
st.markdown("""
<div style="
    text-align: center;
    margin: 60px 0 40px 0;
">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>✨ Características Principales</h2>
    <p style='color: #b8c5d6; font-size: 1.1rem;'>Las cualidades que hacen único a un Data Warehouse</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(72, 187, 120, 0.25) 0%, rgba(72, 187, 120, 0.08) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(72, 187, 120, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
        transition: all 0.4s ease;
    " onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 12px 40px rgba(72, 187, 120, 0.4)';" 
       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 32px rgba(0, 0, 0, 0.3)';">
        <div style='font-size: 3.5rem; margin-bottom: 20px; text-align: center;'>🧩</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.5rem; text-align: center;'>Integración de Datos</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Combina información de múltiples sistemas como ERP, CRM y bases de datos transaccionales.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(72, 187, 120, 0.25) 0%, rgba(72, 187, 120, 0.08) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(72, 187, 120, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
        transition: all 0.4s ease;
    " onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 12px 40px rgba(72, 187, 120, 0.4)';" 
       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 32px rgba(0, 0, 0, 0.3)';">
        <div style='font-size: 3.5rem; margin-bottom: 20px; text-align: center;'>📊</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.5rem; text-align: center;'>Variedad Histórica</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Permite analizar tendencias y realizar comparativas a lo largo del tiempo.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(66, 153, 225, 0.25) 0%, rgba(66, 153, 225, 0.08) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(66, 153, 225, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
        transition: all 0.4s ease;
    " onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 12px 40px rgba(66, 153, 225, 0.4)';" 
       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 32px rgba(0, 0, 0, 0.3)';">
        <div style='font-size: 3.5rem; margin-bottom: 20px; text-align: center;'>📂</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.5rem; text-align: center;'>Orientado a Temas</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Los datos se organizan según áreas de interés: ventas, clientes, inventario, productos.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(66, 153, 225, 0.25) 0%, rgba(66, 153, 225, 0.08) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(66, 153, 225, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
        transition: all 0.4s ease;
    " onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 12px 40px rgba(66, 153, 225, 0.4)';" 
       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 32px rgba(0, 0, 0, 0.3)';">
        <div style='font-size: 3.5rem; margin-bottom: 20px; text-align: center;'>⚡</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.5rem; text-align: center;'>Optimizado para Consultas</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Diseñado específicamente para responder consultas analíticas complejas de manera eficiente.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(237, 137, 54, 0.25) 0%, rgba(237, 137, 54, 0.08) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(237, 137, 54, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
        transition: all 0.4s ease;
    " onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 12px 40px rgba(237, 137, 54, 0.4)';" 
       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 32px rgba(0, 0, 0, 0.3)';">
        <div style='font-size: 3.5rem; margin-bottom: 20px; text-align: center;'>⏳</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.5rem; text-align: center;'>No Volátil</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Los datos históricos se mantienen estables sin alteraciones frecuentes.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(237, 137, 54, 0.25) 0%, rgba(237, 137, 54, 0.08) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(237, 137, 54, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
        transition: all 0.4s ease;
    " onmouseover="this.style.transform='translateY(-10px)'; this.style.boxShadow='0 12px 40px rgba(237, 137, 54, 0.4)';" 
       onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 8px 32px rgba(0, 0, 0, 0.3)';">
        <div style='font-size: 3.5rem; margin-bottom: 20px; text-align: center;'>💡</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.5rem; text-align: center;'>Escalable</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Se puede ampliar según el crecimiento y necesidades de la organización.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# --- Ejemplo Práctico ---
with st.expander("💡 **Ejemplo Práctico: Retail**", expanded=False):
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 15px; margin: 10px 0;'>
        <p style='color: #d0dae8; font-size: 1.05rem; line-height: 1.8;'>
            Imaginemos una empresa de retail que gestiona:
        </p>
        <ul style='color: #b8c5d6; font-size: 1.05rem; line-height: 2; margin: 20px 0;'>
            <li>🏬 <strong style='color: #fff;'>Sistema ERP</strong> para gestión de inventario</li>
            <li>📇 <strong style='color: #fff;'>CRM</strong> que almacena datos de clientes</li>
            <li>🛒 <strong style='color: #fff;'>Plataforma e-commerce</strong> para ventas online</li>
        </ul>
        <p style='color: #d0dae8; font-size: 1.05rem; line-height: 1.8; margin-top: 20px;'>
            El <strong style='color: #fff;'>Data Warehouse</strong> recopila toda esta información, la organiza por categorías temáticas 
            (ventas, clientes, productos) y permite que el equipo de marketing y dirección analice:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.metric(
            label="📈 Productos más vendidos",
            value="5,000",
            delta="unidades/mes"
        )
    with col2:
        st.metric(
            label="👥 Clientes más leales",
            value="1,200",
            delta="clientes recurrentes"
        )

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# --- Beneficios ---
st.markdown("""
<div style="
    text-align: center;
    margin: 60px 0 40px 0;
">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🎯 Beneficios Clave</h2>
    <p style='color: #b8c5d6; font-size: 1.1rem;'>Ventajas de implementar un Data Warehouse</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.success("""
    **✅ Decisiones Basadas en Datos**  
    Fundamentadas en información consolidada y verificada de toda la organización.
    """)
    st.info("""
    **⚡ Análisis Más Rápido**  
    Evita consultas directas a sistemas transaccionales lentos y sobrecargados.
    """)

with col2:
    st.success("""
    **📚 Histórico Confiable**  
    Mantiene datos históricos para reportes retrospectivos y proyecciones futuras.
    """)
    st.info("""
    **🚀 Eficiencia Operativa**  
    Reduce significativamente el tiempo de preparación manual de reportes.
    """)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# --- Conceptos Relacionados ---
with st.expander("📌 **Conceptos Relacionados**", expanded=False):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔄 ETL (Extract, Transform, Load)**  
        Proceso de extracción, transformación y carga de datos al Data Warehouse.
        
        **📊 OLAP (Online Analytical Processing)**  
        Análisis multidimensional y complejo sobre los datos almacenados.
        """)
    
    with col2:
        st.markdown("""
        **📦 Data Mart**  
        Subconjunto del DWH enfocado en un área específica de negocio o departamento.
        
        **💡 BI (Business Intelligence)**  
        Herramientas y tecnologías para análisis y visualización de datos empresariales.
        """)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
