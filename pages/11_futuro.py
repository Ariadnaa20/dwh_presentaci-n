# pages/11_futuro.py
import streamlit as st

st.set_page_config(page_title="Futuro del DWH", page_icon="🔮", layout="wide")

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
    <div style='font-size: 4rem; margin-bottom: 20px;'>🔮</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        Futuro del Data Warehouse
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Tendencias, tecnologías emergentes y el camino hacia adelante
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
    <h2 style='color: #ffffff; margin-bottom: 20px;'>🌟 Perspectiva General</h2>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        El Data Warehouse <strong style='color: #fff;'>NO está muriendo</strong>, está <strong style='color: #fff;'>evolucionando</strong>. 
        La convergencia de tecnologías (Cloud, AI, Lakehouse) está redefiniendo qué significa ser un "warehouse" en 2025 y más allá.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# Tendencias principales
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🚀 Tendencias Clave</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
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
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🤖</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>AI Integrada</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Machine Learning nativo dentro del DWH
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ BigQuery ML, Snowflake ML</li>
            <li>✅ Entrenar modelos con SQL</li>
            <li>✅ Predicciones en queries</li>
            <li>✅ AutoML integrado</li>
            <li>✅ GenAI para queries (NL2SQL)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(72, 187, 120, 0.2) 0%, rgba(72, 187, 120, 0.05) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(72, 187, 120, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
    ">
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>⚡</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Real-Time</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            De batch nocturno a streaming continuo
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ Change Data Capture (CDC)</li>
            <li>✅ Kafka → DWH en segundos</li>
            <li>✅ Materialized views actualizadas</li>
            <li>✅ Latencia < 1 minuto</li>
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
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🏠</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Lakehouse Architecture</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Convergencia de Lake + Warehouse
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ Un solo repositorio</li>
            <li>✅ Delta Lake, Iceberg, Hudi</li>
            <li>✅ ACID en object storage</li>
            <li>✅ BI + ML en mismos datos</li>
            <li>✅ Elimina duplicación</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
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
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🌐</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Data Mesh</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Descentralización de propiedad de datos
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ Equipos poseen sus dominios</li>
            <li>✅ Data as a product</li>
            <li>✅ Self-serve platform</li>
            <li>✅ Federated governance</li>
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
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🔐</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Data Governance</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Privacidad, calidad y lineage
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ GDPR, CCPA compliance</li>
            <li>✅ Automated data lineage</li>
            <li>✅ Quality checks integrados</li>
            <li>✅ Data discovery AI-powered</li>
            <li>✅ Column-level security</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(240, 147, 251, 0.2) 0%, rgba(240, 147, 251, 0.05) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 35px 30px;
        border: 1px solid rgba(240, 147, 251, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        height: 100%;
    ">
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>💬</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Conversational BI</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Queries en lenguaje natural con LLMs
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ "Show me top sellers this week"</li>
            <li>✅ ChatGPT → SQL automático</li>
            <li>✅ Democratización extrema</li>
            <li>✅ Análisis para todos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Tecnologías emergentes
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🔬 Tecnologías Emergentes</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.info("""
    ### 🌟 Activamente en Desarrollo
    
    **1. Serverless Everything:**
    - No gestión de infraestructura
    - Pago estricto por uso
    - Auto-scaling infinito
    - BigQuery ya lo hace, otros siguen
    
    **2. Multi-Cloud / Cloud Agnostic:**
    - Snowflake en AWS, Azure, GCP
    - Starburst (query federation)
    - Evita vendor lock-in
    
    **3. Separación Compute-Storage:**
    - Escalar independientemente
    - Múltiples engines en mismos datos
    - Costos optimizados
    """)

with col2:
    st.success("""
    ### 🔮 En el Horizonte (2-5 años)
    
    **1. Quantum Query Optimization:**
    - Optimización de queries con quantum
    - Experimental (IBM, Google)
    
    **2. Autonomous DWH:**
    - Self-tuning completo
    - Self-repair
    - Oracle Autonomous DWH es inicio
    
    **3. Blockchain para Lineage:**
    - Trazabilidad inmutable
    - Data provenance certificado
    - Todavía muy experimental
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Skills del futuro
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>📚 Skills para el Futuro</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.warning("""
    ### 🔴 Menos Relevantes (Declive)
    
    - ETL manual con GUIs (Informatica drag-drop)
    - Administración de servidores on-premise
    - Tuning manual de índices tradicionales
    - OLAP Cubes clásicos (SSAS)
    - Reportes estáticos predefinidos
    """)

with col2:
    st.success("""
    ### 🟢 Más Relevantes (Crecimiento)
    
    - **SQL avanzado** (siempre relevante++)
    - Python para data engineering (Pandas, PySpark)
    - **dbt** (Analytics Engineering)
    - **Infraestructura como código** (Terraform, Pulumi)
    - **Observability** (Datadog, Monte Carlo)
    - Git/CI/CD para data pipelines
    - LLM prompting para análisis
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Predicciones
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🎯 Predicciones 2025-2030</h2>
</div>
""", unsafe_allow_html=True)

predictions_data = {
    "Predicción": [
        "Cloud DWH domina el mercado",
        "On-premise DWH en declive",
        "Lakehouse se vuelve mainstream",
        "Real-time es el nuevo estándar",
        "AI-native DWH (ML integrado)",
        "Conversational BI generalizado",
        "Data Mesh adoptado en Fortune 500",
        "Costo por TB almacenado"
    ],
    "2025": ["75%", "Nicho", "Early adopters", "30% casos", "Disponible", "15% uso", "5%", "$20/TB/mes"],
    "2030": ["90%", "Legacy", "Estándar", "70% casos", "Estándar", "50% uso", "30%", "$5/TB/mes"]
}

st.table(predictions_data)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Conclusión
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>💡 Conclusión Final</h2>
</div>
""", unsafe_allow_html=True)

st.success("""
### El Data Warehouse no está muriendo, está transformándose

De sistemas monolíticos on-premise a **plataformas cloud elásticas** con ML integrado,
el concepto fundamental de "un lugar centralizado para análisis de datos" sigue siendo válido.

La convergencia con **Data Lakes** (Lakehouse), la integración de **AI/ML**, y la democratización 
vía **conversational interfaces** están redefiniendo el espacio, pero la necesidad subyacente permanece.
""")

st.info("""
### ⭐ Mensaje para profesionales de datos:

Aprende los **fundamentos** (modelado dimensional, SQL, arquitectura), 
pero mantente **flexible y curioso**. Las herramientas cambian, 
pero los principios perduran. El futuro pertenece a quienes pueden **adaptarse**.
""")

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
