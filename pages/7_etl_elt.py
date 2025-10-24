# pages/7_etl_elt.py
import streamlit as st

st.set_page_config(page_title="ETL vs ELT", page_icon="🔄", layout="wide")

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
    <div style='font-size: 4rem; margin-bottom: 20px;'>🔄</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        ETL vs ELT
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Procesos de extracción, transformación y carga de datos
    </p>
</div>
""", unsafe_allow_html=True)

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
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        <strong style='color: #fff;'>ETL</strong> y <strong style='color: #fff;'>ELT</strong> son enfoques para integrar datos 
        desde fuentes diversas hacia un sistema de análisis. La diferencia principal está en <strong style='color: #fff;'>dónde</strong> 
        y <strong style='color: #fff;'>cuándo</strong> se realizan las transformaciones.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# ETL
st.info("## 📤 ETL: Extract, Transform, Load")

st.write("""
El proceso **ETL** transforma los datos **antes** de cargarlos en el destino
""")

st.write("**🔄 Flujo ETL:**")
st.write("""
- **1️⃣ Extract:** Conectar a fuentes de datos y leer datos
- **2️⃣ Transform:** Limpiar, validar y aplicar reglas de negocio *(en servidor ETL intermedio)*
- **3️⃣ Load:** Escribir datos transformados al DWH
""")

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.success("""
    **✅ Ventajas:**
    - Datos llegan limpios al DWH
    - Menos carga en el DWH
    - Control total del proceso
    - Seguridad: datos sensibles transformados fuera
    """)

with col2:
    st.error("""
    **❌ Desventajas:**
    - Proceso más lento
    - Servidor ETL costoso
    - No guarda datos raw
    - Menos flexibilidad
    """)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# ELT
st.success("## 📥 ELT: Extract, Load, Transform")

st.write("""
El proceso **ELT** carga los datos primero y transforma **después**, dentro del DWH
""")

st.write("**🔄 Flujo ELT:**")
st.write("""
- **1️⃣ Extract:** Conectar a fuentes y leer datos
- **2️⃣ Load:** Cargar datos **RAW** directamente al DWH
- **3️⃣ Transform:** Transformaciones *dentro* del DWH con SQL
""")

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.success("""
    **✅ Ventajas:**
    - Carga mucho más rápida
    - Datos raw preservados
    - Flexibilidad: re-transformar fácilmente
    - Aprovecha poder del DWH cloud
    - Ideal para exploración
    """)

with col2:
    st.error("""
    **❌ Desventajas:**
    - Más carga en el DWH
    - Datos sensibles en raw
    - Requiere DWH potente
    - Costos de compute mayores
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Comparativa
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>⚖️ Comparativa Detallada</h2>
</div>
""", unsafe_allow_html=True)

comparison_data = {
    "Aspecto": [
        "Orden de Operaciones",
        "Transformaciones",
        "Velocidad de carga",
        "Datos raw",
        "Flexibilidad",
        "Ideal para"
    ],
    "ETL 📤": [
        "Extract → Transform → Load",
        "En servidor ETL",
        "Más lenta",
        "No se guardan",
        "Menos flexible",
        "On-premise, datos sensibles"
    ],
    "ELT 📥": [
        "Extract → Load → Transform",
        "Dentro del DWH",
        "Muy rápida",
        "Se preservan",
        "Muy flexible",
        "Cloud, big data, agilidad"
    ]
}

st.table(comparison_data)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Tendencias
col1, col2 = st.columns(2, gap="large")

with col1:
    st.warning("""
    ### 📈 Tendencia: ELT está ganando
    
    **Por qué ELT es el futuro:**
    
    1. ☁️ **Cloud DWH más potentes**
       - Snowflake, BigQuery, Redshift
       - Compute separado de storage
       - Escalado elástico
    
    2. 🚀 **Necesidad de agilidad**
       - Startups y empresas ágiles
       - Análisis exploratorio
       - Data science y ML
    
    3. 🏗️ **Arquitectura moderna**
       - Data Lakes (S3, ADLS, GCS)
       - Lakehouse (Delta, Iceberg)
       - Datos semi-estructurados
    """)

with col2:
    st.info("""
    ### 🏛️ ETL aún relevante
    
    **Casos donde ETL sigue siendo mejor:**
    
    1. 🏢 **Enterprise legacy**
       - Inversión en Informatica/DataStage
       - On-premise DWH (Oracle, Teradata)
       - Equipos expertos en ETL
    
    2. 🔐 **Compliance estricto**
       - Banca y finanzas
       - Salud (HIPAA)
       - Datos sensibles PII
    
    3. 🔧 **Transformaciones complejas**
       - Lógica propietaria compleja
       - Múltiples sistemas legacy
    """)

st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(167, 139, 250, 0.15) 0%, rgba(167, 139, 250, 0.05) 100%);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 40px;
    margin: 40px 0;
    border: 1px solid rgba(167, 139, 250, 0.3);
    text-align: center;
">
    <h3 style='color: #c4b5fd; margin-bottom: 20px; font-size: 1.8rem;'>💡 Recomendación 2025</h3>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        Para nuevos proyectos, empieza con <strong style='color: #fff;'>ELT</strong> (Fivetran/Airbyte + dbt) 
        a menos que tengas requisitos específicos que requieran ETL.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
