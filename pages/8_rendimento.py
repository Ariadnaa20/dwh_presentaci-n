# pages/8_rendimento.py
import streamlit as st

st.set_page_config(page_title="Rendimiento DWH", page_icon="⚡", layout="wide")

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
    <div style='font-size: 4rem; margin-bottom: 20px;'>⚡</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        Optimización de Rendimiento
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Particiones, índices y técnicas para acelerar consultas
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
    <h2 style='color: #ffffff; margin-bottom: 20px;'>📝 ¿Por qué es crucial el rendimiento?</h2>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        Un <strong style='color: #fff;'>Data Warehouse</strong> puede contener terabytes o petabytes de datos. Sin optimización 
        adecuada, las consultas pueden tardar horas. Las técnicas de optimización son esenciales para respuestas en segundos 
        vs horas, reducción de costos y escalabilidad sostenible.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# Técnicas principales
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🎯 Técnicas Principales</h2>
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
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>📂</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Particionamiento</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Divide tablas grandes en fragmentos más pequeños basados en valores específicos (usualmente fecha)
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ Partition Pruning</li>
            <li>✅ Mejora 10x-100x</li>
            <li>✅ Mantenimiento más fácil</li>
            <li>✅ Paralelismo</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
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
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🔍</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Índices</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Estructuras auxiliares que permiten acceso rápido a datos mediante búsquedas eficientes
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ B-Tree Index</li>
            <li>✅ Bitmap Index</li>
            <li>✅ Columnstore Index</li>
            <li>✅ Covering Index</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
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
        <div style='font-size: 3rem; margin-bottom: 20px; text-align: center;'>🗂️</div>
        <h3 style='color: #ffffff; margin-bottom: 15px; font-size: 1.6rem; text-align: center;'>Clustering</h3>
        <p style='color: #d0dae8; line-height: 1.7; text-align: center; font-size: 1.05rem;'>
            Ordena físicamente los datos en disco según columnas específicas para mejorar localidad
        </p>
        <ul style='color: #b8c5d6; font-size: 0.95rem; line-height: 1.8; margin-top: 15px; list-style: none; padding-left: 0;'>
            <li>✅ Snowflake micro-partitions</li>
            <li>✅ BigQuery clustering</li>
            <li>✅ Redshift sort keys</li>
            <li>✅ Compresión mejorada</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Buenas Prácticas
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>✨ Mejores Prácticas</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.success("""
    ### ✅ DO - Hacer
    
    **Diseño:**
    - Particionar por fecha (casi siempre)
    - Usar clustering en columnas de filtro frecuentes
    - Implementar vistas materializadas para reportes comunes
    
    **Queries:**
    - Siempre incluir filtros de partición
    - Seleccionar solo columnas necesarias
    - Usar EXISTS en vez de COUNT cuando aplique
    
    **Mantenimiento:**
    - Analizar estadísticas regularmente (ANALYZE)
    - Monitorear queries lentas
    - Revisar y eliminar índices no usados
    """)

with col2:
    st.error("""
    ### ❌ DON'T - Evitar
    
    **Diseño:**
    - No sobre-indexar (overhead en writes)
    - No crear particiones demasiado pequeñas
    - No ignorar el plan de ejecución
    
    **Queries:**
    - No usar SELECT * en producción
    - No aplicar funciones sobre columnas indexadas en WHERE
    - No hacer JOINs sin filtros previos
    
    **Mantenimiento:**
    - No dejar estadísticas desactualizadas
    - No ignorar warnings del optimizer
    - No ejecutar VACUUM/ANALYZE en horas pico
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Ejemplo de optimización
with st.expander("💡 **Caso Real: E-commerce con 100TB de datos**", expanded=False):
    st.error("### Situación inicial:")
    st.write("""
    - 📊 Tabla fact_orders: 50 mil millones de filas
    - ⏰ Reportes diarios: 30 minutos
    - ❌ Análisis ad-hoc: imposibles
    - 💰 Costo cloud: $50K/mes
    """)
    
    st.info("### Optimizaciones aplicadas:")
    st.write("""
    - 📂 **Particionamiento por fecha (día):** Mejora 300x
    - 🗂️ **Clustering por (fecha, customer_country):** Compresión 5:1 → 12:1
    - 💾 **Vistas materializadas para reportes diarios:** 30 min → 10 seg
    - 🔍 **Columnstore indexes en dimensiones:** JOINs 5x más rápidos
    - ⚡ **Reescritura de queries top 10:** 10-50x por query
    """)
    
    st.success("### Resultados:")
    st.write("""
    - ⚡ Reportes: 30 min → 10 seg (180x más rápido)
    - 📊 Análisis ad-hoc: Ahora factibles (1-5 min)
    - 💰 Costo cloud: $50K → $18K/mes (64% reducción)
    - ⭐ Satisfacción usuarios: ⭐⭐ → ⭐⭐⭐⭐⭐
    """)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
