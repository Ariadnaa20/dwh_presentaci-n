# pages/4_arquitectura.py
import streamlit as st

st.set_page_config(page_title="Arquitectura DWH", page_icon="🏗️", layout="wide")

# Header
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
    <div style='font-size: 4rem; margin-bottom: 20px;'>🏗️</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        Arquitectura de un Data Warehouse
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Capas y componentes de una arquitectura DWH completa
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
    <h2 style='color: #ffffff; margin-bottom: 20px;'>📝 Introducción</h2>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        La arquitectura de un <strong style='color: #fff;'>Data Warehouse</strong> se compone de múltiples capas que trabajan en conjunto 
        para extraer, transformar, almacenar y presentar datos de manera eficiente. Cada capa tiene un propósito específico en el flujo 
        de datos desde las fuentes hasta los usuarios finales.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# Capas principales
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🔷 Capas de la Arquitectura</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.info("""
    **1️⃣ Fuentes de Datos**
    - Sistemas operacionales (ERP, CRM)
    - Bases de datos transaccionales
    - Archivos externos (CSV, JSON, XML)
    - APIs y servicios web
    """)
    
    st.warning("""
    **4️⃣ Almacenamiento**
    - Data Warehouse central
    - Data Marts departamentales
    - Modelos dimensionales
    - Datos históricos agregados
    """)

with col2:
    st.success("""
    **2️⃣ Staging**
    - Área temporal de almacenamiento
    - Datos en formato crudo
    - Mínima transformación
    - Punto de recuperación ante errores
    """)
    
    st.success("""
    **5️⃣ Presentación**
    - Herramientas de BI
    - Reportes y dashboards
    - Consultas OLAP
    - Análisis ad-hoc
    """)

with col3:
    st.warning("""
    **3️⃣ ETL/ELT**
    - Extracción de datos
    - Transformación y limpieza
    - Validación de calidad
    - Carga al DWH
    """)
    
    st.info("""
    **6️⃣ Metadatos**
    - Diccionario de datos
    - Linaje de datos
    - Reglas de negocio
    - Documentación técnica
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Tipos de Arquitectura
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🏛️ Tipos de Arquitectura DWH</h2>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📦 1 Capa", "📦📦 2 Capas", "📦📦📦 3 Capas (Recomendada)"])

with tab1:
    st.markdown("""
    <div style="background: rgba(245, 101, 101, 0.1); padding: 30px; border-radius: 15px; border: 1px solid rgba(245, 101, 101, 0.3);">
        <h3 style="color: #fc8181; margin-bottom: 20px;">Arquitectura de Una Capa</h3>
        <p style="color: #d0dae8; line-height: 1.8;">
            <strong style='color: #fff;'>Descripción:</strong> DWH y fuentes operacionales en el mismo sistema
        </p>
        <h4 style="color: #9ae6b4; margin-top: 25px; margin-bottom: 15px;">Ventajas:</h4>
        <ul style="color: #b8c5d6; line-height: 2;">
            <li>✅ Simple y económica</li>
            <li>✅ Fácil de implementar</li>
        </ul>
        <h4 style="color: #fc8181; margin-top: 25px; margin-bottom: 15px;">Desventajas:</h4>
        <ul style="color: #b8c5d6; line-height: 2;">
            <li>❌ No separa operaciones de análisis</li>
            <li>❌ Impacta rendimiento de sistemas transaccionales</li>
            <li>❌ <strong style='color: #fff;'>Raramente recomendada en producción</strong></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div style="background: rgba(237, 137, 54, 0.1); padding: 30px; border-radius: 15px; border: 1px solid rgba(237, 137, 54, 0.3);">
        <h3 style="color: #fbd38d; margin-bottom: 20px;">Arquitectura de Dos Capas</h3>
        <p style="color: #d0dae8; line-height: 1.8;">
            <strong style='color: #fff;'>Descripción:</strong> Separa fuentes de datos del DWH
        </p>
        <h4 style="color: #9ae6b4; margin-top: 25px; margin-bottom: 15px;">Ventajas:</h4>
        <ul style="color: #b8c5d6; line-height: 2;">
            <li>✅ Separa análisis de operaciones</li>
            <li>✅ Mejor rendimiento</li>
        </ul>
        <h4 style="color: #fbd38d; margin-top: 25px; margin-bottom: 15px;">Desventajas:</h4>
        <ul style="color: #b8c5d6; line-height: 2;">
            <li>⚠️ Sin área de staging</li>
            <li>⚠️ Dificultad en recuperación de errores</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div style="background: rgba(72, 187, 120, 0.1); padding: 30px; border-radius: 15px; border: 1px solid rgba(72, 187, 120, 0.3);">
        <h3 style="color: #9ae6b4; margin-bottom: 20px;">Arquitectura de Tres Capas ⭐</h3>
        <p style="color: #d0dae8; line-height: 1.8;">
            <strong style='color: #fff;'>Descripción:</strong> Arquitectura estándar de DWH empresarial
        </p>
        <p style="color: #d0dae8; line-height: 1.8; margin-top: 15px;">
            <strong style='color: #fff;'>Componentes:</strong>
        </p>
        <ul style="color: #b8c5d6; line-height: 2; margin-top: 10px;">
            <li>📂 Capa 1: Fuentes de datos</li>
            <li>🔄 Capa 2: Staging + DWH Central</li>
            <li>📊 Capa 3: Data Marts + BI Tools</li>
        </ul>
        <h4 style="color: #9ae6b4; margin-top: 25px; margin-bottom: 15px;">Ventajas:</h4>
        <ul style="color: #b8c5d6; line-height: 2;">
            <li>✅ Máxima flexibilidad</li>
            <li>✅ Mejor manejo de errores</li>
            <li>✅ Escalable y mantenible</li>
            <li>✅ Separación clara de responsabilidades</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Flujo de datos
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🎯 Flujo de Datos</h2>
</div>
""", unsafe_allow_html=True)

st.code("""
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Fuentes    │ --> │   Staging   │ --> │     DWH     │ --> │  Data Marts │
│  de Datos   │     │    Area     │     │   Central   │     │  + BI Tools │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
      │                    │                    │                    │
   ERP, CRM          Datos Crudos         Datos Integrados    Análisis BI
   Archivos          Sin transformar      Modelos Dim.        Reportes
   APIs              Temporal             Histórico           Dashboards
""", language="text")

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
