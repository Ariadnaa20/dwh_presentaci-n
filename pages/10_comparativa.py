# pages/10_comparativa.py
import streamlit as st

st.set_page_config(page_title="DWH vs Lake vs Lakehouse", page_icon="🔀", layout="wide")

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
    <div style='font-size: 4rem; margin-bottom: 20px;'>🔀</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        Data Warehouse vs Data Lake vs Lakehouse
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Comparativa de arquitecturas de datos modernas
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
        En el ecosistema moderno de datos, existen tres arquitecturas principales: <strong style='color: #fff;'>Data Warehouse</strong>, 
        <strong style='color: #fff;'>Data Lake</strong> y <strong style='color: #fff;'>Data Lakehouse</strong>. Cada una tiene sus 
        propósitos, fortalezas y casos de uso ideales.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# Las tres arquitecturas
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🏗️ Las Tres Arquitecturas</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.info("""
    ### 🏢 Data Warehouse
    
    **Qué es:**
    Sistema optimizado para análisis
    de datos **estructurados** e **históricos**
    
    **Origen:** Años 90
    
    **Tecnología:**
    - Base de datos relacional
    - Schema-on-write
    - Modelo dimensional
    
    **Datos:**
    - Estructurados y limpios
    - ETL antes de cargar
    - Formato tabular
    
    **Ejemplos:**
    - Snowflake
    - BigQuery
    - Redshift
    """)

with col2:
    st.success("""
    ### 🌊 Data Lake
    
    **Qué es:**
    Repositorio para almacenar
    datos **raw en cualquier formato**
    
    **Origen:** ~2010 (Big Data)
    
    **Tecnología:**
    - Object storage (S3, ADLS)
    - Schema-on-read
    - Parquet, JSON, CSV
    
    **Datos:**
    - Todos los tipos
    - Formato original
    - Sin transformación previa
    
    **Ejemplos:**
    - AWS S3 + Athena
    - Azure Data Lake
    - Google Cloud Storage
    """)

with col3:
    st.warning("""
    ### 🏠 Data Lakehouse
    
    **Qué es:**
    Híbrido que combina
    **Lake** + **Warehouse**
    
    **Origen:** ~2020 (Databricks)
    
    **Tecnología:**
    - Storage de Lake
    - ACID transactions
    - Metadata layer
    
    **Datos:**
    - Todos los tipos
    - Schema enforcement opcional
    - Versionado de datos
    
    **Ejemplos:**
    - Databricks (Delta Lake)
    - Apache Iceberg
    - Apache Hudi
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Comparativa detallada
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>⚖️ Comparativa Detallada</h2>
</div>
""", unsafe_allow_html=True)

comparison_data = {
    "Característica": [
        "Tipo de datos",
        "Esquema",
        "Performance consultas",
        "Costo storage",
        "Flexibilidad",
        "ACID transactions",
        "Casos de uso"
    ],
    "🏢 Data Warehouse": [
        "Estructurados",
        "Schema-on-write",
        "Muy rápido",
        "$$ Alto",
        "Baja",
        "✅ Sí",
        "BI, Reporting"
    ],
    "🌊 Data Lake": [
        "Todos",
        "Schema-on-read",
        "Medio-Lento",
        "$ Bajo",
        "Muy alta",
        "❌ No",
        "ML, Exploración"
    ],
    "🏠 Lakehouse": [
        "Todos",
        "Híbrido",
        "Rápido",
        "$ Bajo-Medio",
        "Alta",
        "✅ Sí",
        "BI + ML"
    ]
}

st.table(comparison_data)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Qué usar cuándo
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🎯 Qué Usar Cuándo</h2>
</div>
""", unsafe_allow_html=True)

cases = {
    "Caso de Uso": [
        "Reportes ejecutivos",
        "KPIs y métricas",
        "Machine Learning",
        "Exploración de datos",
        "Logs/clickstream",
        "Análisis ad-hoc",
        "BI self-service"
    ],
    "🏢 DWH": ["✅ Ideal", "✅ Ideal", "❌ No", "⚠️ Limitado", "❌ No", "✅ Sí", "✅ Ideal"],
    "🌊 Lake": ["❌ Lento", "❌ Lento", "✅ Ideal", "✅ Ideal", "✅ Ideal", "✅ Sí", "❌ Difícil"],
    "🏠 Lakehouse": ["✅ Bien", "✅ Bien", "✅ Ideal", "✅ Ideal", "✅ Ideal", "✅ Ideal", "✅ Bien"]
}

st.table(cases)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Recomendación
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>💡 Recomendación Final</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.info("""
    ### Elige DWH si...
    
    ✅ Tu organización es madura
    
    ✅ Datos 100% estructurados
    
    ✅ BI/Reporting es el 90% de uso
    
    ✅ Performance crítico
    
    ✅ Ya tienes DWH funcionando
    
    **Ejemplos:** Banca, retail tradicional
    """)

with col2:
    st.success("""
    ### Elige Lakehouse si...
    
    ✅ Necesitas BI + ML
    
    ✅ Datos estructurados + no estructurados
    
    ✅ Cloud-native
    
    ✅ Quieres reducir duplicación
    
    ✅ Flexibilidad importante
    
    **Ejemplos:** Tech companies, startups
    """)

with col3:
    st.warning("""
    ### Usa ambos si...
    
    ✅ Gran empresa con legacy
    
    ✅ No puedes migrar todo ya
    
    ✅ Riesgo debe ser mínimo
    
    ✅ Casos de uso diversos
    
    ✅ Transición gradual
    
    **Ejemplos:** Fortune 500 migrando
    """)

st.success("""
**💡 Tendencia 2025:**

El futuro es **Lakehouse** para la mayoría de organizaciones nuevas.  
Para empresas existentes, un **enfoque híbrido** minimiza riesgo mientras se moderniza.  
Data Warehouses tradicionales no desaparecen, pero su rol se especializa.
""")

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
