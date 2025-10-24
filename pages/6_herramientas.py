# pages/6_herramientas.py
import streamlit as st

st.set_page_config(page_title="Herramientas DWH", page_icon="🛠️", layout="wide")

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
    <div style='font-size: 4rem; margin-bottom: 20px;'>🛠️</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        Herramientas y Tecnologías
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Plataformas On-Premise y Cloud para Data Warehouses
    </p>
</div>
""", unsafe_allow_html=True)

# On-Premise vs Cloud
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🏢 On-Premise vs ☁️ Cloud</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.info("""
    ### 🏢 On-Premise (Local)
    
    **Características:**
    - Infraestructura propia
    - Control total sobre hardware y software
    - Instalación en servidores propios
    
    **Ventajas:**
    - ✅ Control total de la infraestructura
    - ✅ Cumplimiento regulatorio estricto
    - ✅ Sin dependencia de internet
    - ✅ Costos predecibles a largo plazo
    
    **Desventajas:**
    - ❌ Alta inversión inicial (CAPEX)
    - ❌ Mantenimiento manual
    - ❌ Escalabilidad limitada
    - ❌ Requiere equipo técnico dedicado
    """)

with col2:
    st.success("""
    ### ☁️ Cloud (Nube)
    
    **Características:**
    - Infraestructura gestionada por proveedor
    - Acceso vía internet
    - Modelo de pago por uso
    
    **Ventajas:**
    - ✅ Sin inversión inicial (OPEX)
    - ✅ Escalabilidad elástica
    - ✅ Actualizaciones automáticas
    - ✅ Alta disponibilidad
    - ✅ Despliegue rápido
    
    **Desventajas:**
    - ❌ Dependencia de internet
    - ❌ Costos variables
    - ❌ Menor control sobre infraestructura
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Cloud DWH
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>☁️ Cloud Data Warehouses</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(237, 137, 54, 0.2) 0%, rgba(237, 137, 54, 0.05) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(237, 137, 54, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
    ">
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🔶</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Amazon Redshift</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Servicio DWH de AWS
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ Almacenamiento columnar</li>
            <li>✅ Integración con S3, Glue</li>
            <li>✅ Redshift Spectrum</li>
            <li>💰 Pago por nodo/hora</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(66, 153, 225, 0.2) 0%, rgba(66, 153, 225, 0.05) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(66, 153, 225, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
    ">
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🔷</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Google BigQuery</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            DWH Serverless de Google
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ 100% Serverless</li>
            <li>✅ ML integrado (BigQuery ML)</li>
            <li>✅ Consultas en segundos</li>
            <li>💰 Pago por TB procesado</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
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
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>❄️</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Snowflake</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            DWH Multi-Cloud
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ Multi-cloud (AWS, Azure, GCP)</li>
            <li>✅ Separación compute/storage</li>
            <li>✅ Time Travel & Data Sharing</li>
            <li>💰 Compute + Storage</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Comparativa
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>⚖️ Comparativa Cloud DWH</h2>
</div>
""", unsafe_allow_html=True)

comparison_data = {
    "Característica": ["Serverless", "Multi-Cloud", "ML Integrado", "Pricing", "Escalabilidad"],
    "Redshift": ["Opcional", "❌", "Limitado", "Por nodo", "⭐⭐⭐⭐"],
    "BigQuery": ["✅", "❌", "✅✅", "Por consulta", "⭐⭐⭐⭐⭐"],
    "Snowflake": ["✅", "✅", "Via partners", "Compute+Storage", "⭐⭐⭐⭐⭐"]
}

st.table(comparison_data)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Herramientas BI
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>📊 Herramientas de BI</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.info("""
    **Tableau**
    - Visualizaciones interactivas
    - Drag-and-drop intuitivo
    - Gran comunidad
    - 💰 $$$ (Salesforce)
    """)
    
    st.success("""
    **Power BI**
    - Integración Microsoft
    - DAX para cálculos
    - Excelente relación calidad/precio
    - 💲 $ - $$
    """)

with col2:
    st.warning("""
    **Looker**
    - Basado en LookML
    - Embedded analytics
    - Modelo semántico fuerte
    - 💰 $$ (Google)
    """)
    
    st.info("""
    **Qlik Sense**
    - Motor asociativo único
    - Análisis exploratorio
    - Self-service BI
    - 💰 $$
    """)

with col3:
    st.success("""
    **Apache Superset**
    - Open source
    - Dashboards modernos
    - SQL Lab integrado
    - 🆓 Gratuito
    """)
    
    st.warning("""
    **Metabase**
    - Open source
    - Simple y fácil de usar
    - Perfecto para startups
    - 🆓 Gratuito
    """)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
