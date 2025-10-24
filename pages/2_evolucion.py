# pages/2_evolucion.py
import streamlit as st

st.set_page_config(page_title="Evolución del DWH", page_icon="📜", layout="wide")

# --- Header Glassmorphism ---
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
    <div style='font-size: 4rem; margin-bottom: 20px;'>📜</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        Evolución Histórica del DWH
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Desde los primeros sistemas hasta la era del Cloud y Big Data
    </p>
</div>
""", unsafe_allow_html=True)

# Timeline Header
st.markdown("""
<div style="text-align: center; margin: 60px 0 50px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>📅 Línea Temporal</h2>
    <p style='color: #b8c5d6; font-size: 1.1rem;'>De 1980 hasta hoy: La evolución del Data Warehouse</p>
</div>
""", unsafe_allow_html=True)

# 1980s - Era DSS
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 40px;
    margin: 30px 0;
    border-left: 5px solid rgba(66, 153, 225, 0.8);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    <div style="display: flex; align-items: center; gap: 30px; margin-bottom: 25px;">
        <div style="font-size: 4rem;">📊</div>
        <div>
            <h2 style="color: #90cdf4; margin: 0; font-size: 2.5rem; font-weight: 700;">1980s</h2>
            <p style="color: #b8c5d6; margin: 5px 0 0 0; font-size: 1.1rem;">Los Primeros Pasos</p>
        </div>
    </div>
    <h3 style="color: #ffffff; margin-bottom: 15px; font-size: 1.8rem;">Sistemas DSS (Decision Support Systems)</h3>
    <p style="color: #d0dae8; font-size: 1.1rem; line-height: 1.8; margin-bottom: 20px;">
        Los primeros intentos de análisis de datos empresariales
    </p>
    <ul style="color: #b8c5d6; font-size: 1.05rem; line-height: 2; list-style: none; padding-left: 0;">
        <li>📂 Datos extraídos <strong style='color: #fff;'>manualmente</strong> de sistemas transaccionales</li>
        <li>📋 Reportes simples para ejecutivos</li>
        <li>⚠️ Sistemas no estandarizados y difíciles de mantener</li>
        <li>💾 Almacenamiento limitado y procesamiento lento</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# 1990s - Nacimiento del DWH Moderno
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 40px;
    margin: 30px 0;
    border-left: 5px solid rgba(72, 187, 120, 0.8);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    <div style="display: flex; align-items: center; gap: 30px; margin-bottom: 25px;">
        <div style="font-size: 4rem;">🏗️</div>
        <div>
            <h2 style="color: #9ae6b4; margin: 0; font-size: 2.5rem; font-weight: 700;">1990s</h2>
            <p style="color: #b8c5d6; margin: 5px 0 0 0; font-size: 1.1rem;">El Nacimiento</p>
        </div>
    </div>
    <h3 style="color: #ffffff; margin-bottom: 15px; font-size: 1.8rem;">Nacimiento del Data Warehouse Moderno</h3>
    <p style="color: #d0dae8; font-size: 1.1rem; line-height: 1.8; margin-bottom: 25px;">
        <strong style='color: #fff;'>Bill Inmon</strong> y <strong style='color: #fff;'>Ralph Kimball</strong> definen las bases del DWH
    </p>
</div>
""", unsafe_allow_html=True)

# Tabs para Inmon vs Kimball
tab1, tab2 = st.tabs(["📘 Bill Inmon - Top-Down", "📗 Ralph Kimball - Bottom-Up"])

with tab1:
    st.markdown("""
    <div style="
        background: rgba(66, 153, 225, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 30px;
        border: 1px solid rgba(66, 153, 225, 0.3);
    ">
        <h4 style="color: #90cdf4; margin-bottom: 20px; font-size: 1.5rem;">Enfoque: Corporate Information Factory (CIF)</h4>
        <ul style="color: #d0dae8; font-size: 1.05rem; line-height: 2; list-style: none; padding-left: 0;">
            <li>🏛️ Repositorio <strong style='color: #fff;'>centralizado</strong>, integrado y no volátil</li>
            <li>📊 Datos normalizados (3NF)</li>
            <li>🎯 Enfoque <strong style='color: #fff;'>"top-down"</strong>: primero el DWH, luego los Data Marts</li>
            <li>🔍 Una sola fuente de verdad para toda la organización</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div style="
        background: rgba(72, 187, 120, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 30px;
        border: 1px solid rgba(72, 187, 120, 0.3);
    ">
        <h4 style="color: #9ae6b4; margin-bottom: 20px; font-size: 1.5rem;">Enfoque: Dimensional Modeling</h4>
        <ul style="color: #d0dae8; font-size: 1.05rem; line-height: 2; list-style: none; padding-left: 0;">
            <li>⭐ Modelo dimensional (<strong style='color: #fff;'>Star Schema</strong>)</li>
            <li>📦 Data Marts por área de negocio</li>
            <li>🎯 Enfoque <strong style='color: #fff;'>"bottom-up"</strong>: primero los Data Marts</li>
            <li>👥 Orientado a usuarios de negocio (fácil de entender)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

# 2000s
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 40px;
    margin: 30px 0;
    border-left: 5px solid rgba(237, 137, 54, 0.8);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    <div style="display: flex; align-items: center; gap: 30px; margin-bottom: 25px;">
        <div style="font-size: 4rem;">💻</div>
        <div>
            <h2 style="color: #fbd38d; margin: 0; font-size: 2.5rem; font-weight: 700;">2000s</h2>
            <p style="color: #b8c5d6; margin: 5px 0 0 0; font-size: 1.1rem;">Madurez Tecnológica</p>
        </div>
    </div>
    <h3 style="color: #ffffff; margin-bottom: 15px; font-size: 1.8rem;">Era de las Herramientas Comerciales</h3>
    <p style="color: #d0dae8; font-size: 1.1rem; line-height: 1.8; margin-bottom: 20px;">
        Automatización y madurez de procesos ETL y OLAP
    </p>
    <ul style="color: #b8c5d6; font-size: 1.05rem; line-height: 2; list-style: none; padding-left: 0;">
        <li>🔄 <strong style='color: #fff;'>ETL automatizado:</strong> Informatica PowerCenter, IBM DataStage, Oracle ODI</li>
        <li>📊 <strong style='color: #fff;'>OLAP Cubes:</strong> Microsoft Analysis Services, Oracle Essbase</li>
        <li>🗄️ <strong style='color: #fff;'>Bases columnares:</strong> Teradata, Vertica, Netezza</li>
        <li>📈 <strong style='color: #fff;'>BI Tools:</strong> Business Objects, Cognos, MicroStrategy</li>
        <li>⚡ Mayor rendimiento en consultas analíticas</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# 2010s+
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 40px;
    margin: 30px 0;
    border-left: 5px solid rgba(167, 139, 250, 0.8);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    <div style="display: flex; align-items: center; gap: 30px; margin-bottom: 25px;">
        <div style="font-size: 4rem;">☁️</div>
        <div>
            <h2 style="color: #c4b5fd; margin: 0; font-size: 2.5rem; font-weight: 700;">2010s+</h2>
            <p style="color: #b8c5d6; margin: 5px 0 0 0; font-size: 1.1rem;">Revolución Cloud</p>
        </div>
    </div>
    <h3 style="color: #ffffff; margin-bottom: 15px; font-size: 1.8rem;">Revolución Cloud, Big Data y AI</h3>
    <p style="color: #d0dae8; font-size: 1.1rem; line-height: 1.8; margin-bottom: 20px;">
        La era moderna del análisis de datos
    </p>
    <ul style="color: #b8c5d6; font-size: 1.05rem; line-height: 2; list-style: none; padding-left: 0;">
        <li>☁️ <strong style='color: #fff;'>Cloud Data Warehouses:</strong> Amazon Redshift (2012), Snowflake (2014), Google BigQuery</li>
        <li>🌊 <strong style='color: #fff;'>Data Lakes:</strong> Hadoop, S3, Azure Data Lake</li>
        <li>⚡ <strong style='color: #fff;'>Procesamiento distribuido:</strong> Spark, Presto, Databricks</li>
        <li>🤖 <strong style='color: #fff;'>Integración con AI/ML:</strong> TensorFlow, scikit-learn integrados</li>
        <li>📊 <strong style='color: #fff;'>Self-service BI:</strong> Tableau, Power BI, Looker</li>
        <li>🔄 <strong style='color: #fff;'>Tiempo real:</strong> Streaming con Kafka, Kinesis</li>
        <li>💰 <strong style='color: #fff;'>Modelo de pago por uso:</strong> Escalabilidad elástica</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# Actualidad (2020s)
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🔮 La Actualidad (2020s)</h2>
    <p style='color: #b8c5d6; font-size: 1.1rem;'>Las tendencias que están definiendo el presente</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(102, 126, 234, 0.05) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(102, 126, 234, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
    ">
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🏠</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Lakehouse</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Unificación de Data Lake + Data Warehouse
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>• Delta Lake, Apache Iceberg</li>
            <li>• Un solo repositorio para todo</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(167, 139, 250, 0.2) 0%, rgba(167, 139, 250, 0.05) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(167, 139, 250, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
    ">
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🧠</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>IA Integrada</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Machine Learning nativo en DWH
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>• Snowflake ML, BigQuery ML</li>
            <li>• Predicciones con SQL</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(245, 101, 101, 0.2) 0%, rgba(245, 101, 101, 0.05) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(245, 101, 101, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
    ">
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🌐</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Data Mesh</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Descentralización de datos
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>• Propiedad por dominio</li>
            <li>• Data as a Product</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Comparativa Antes vs Ahora
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>📊 Transformación: Antes vs Ahora</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(245, 101, 101, 0.15) 0%, rgba(245, 101, 101, 0.05) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px;
        border: 1px solid rgba(245, 101, 101, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    ">
        <h3 style='color: #fc8181; margin-bottom: 25px; font-size: 1.8rem; text-align: center;'>❌ Antes (1990s-2000s)</h3>
        <ul style='color: #d0dae8; font-size: 1.05rem; line-height: 2.2; list-style: none; padding-left: 0;'>
            <li>🐌 Procesamiento nocturno (batch)</li>
            <li>💰 Hardware caro y on-premise</li>
            <li>👨‍💻 Solo para expertos técnicos</li>
            <li>📆 Datos con días de retraso</li>
            <li>🔧 Mantenimiento complejo</li>
            <li>💾 Capacidad fija y limitada</li>
            <li>📊 Reportes estáticos predefinidos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(72, 187, 120, 0.15) 0%, rgba(72, 187, 120, 0.05) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px;
        border: 1px solid rgba(72, 187, 120, 0.3);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    ">
        <h3 style='color: #9ae6b4; margin-bottom: 25px; font-size: 1.8rem; text-align: center;'>✅ Ahora (2020s)</h3>
        <ul style='color: #d0dae8; font-size: 1.05rem; line-height: 2.2; list-style: none; padding-left: 0;'>
            <li>⚡ Análisis en tiempo real</li>
            <li>☁️ Cloud escalable (pago por uso)</li>
            <li>👥 Self-service para todos</li>
            <li>🔄 Datos actualizados al segundo</li>
            <li>🤖 Automatización y IA integrada</li>
            <li>📈 Escalabilidad elástica infinita</li>
            <li>🎨 Visualizaciones interactivas dinámicas</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Métricas de impacto
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🎯 Impacto de la Evolución</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, gap="medium")

with col1:
    st.metric("⚡ Velocidad", "1000x", delta="vs 1990s")
with col2:
    st.metric("💰 Costo/TB", "↓ 90%", delta="reducción")
with col3:
    st.metric("👥 Usuarios", "100x", delta="más acceso")
with col4:
    st.metric("📈 Capacidad", "∞", delta="ilimitada")

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
