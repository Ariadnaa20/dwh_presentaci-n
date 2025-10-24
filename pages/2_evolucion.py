# pages/2_evolucion.py
import streamlit as st

st.set_page_config(page_title="Evolución del DWH", page_icon="📜", layout="wide")

st.markdown("<h1 style='text-align:center; color:#ffffff;'>📜 Evolución histórica del DWH</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Desde los primeros sistemas hasta la era del Cloud y Big Data</p>", unsafe_allow_html=True)
st.divider()

# 📅 Línea temporal con cards
st.subheader("📅 Línea Temporal del Data Warehouse")

# 1980s
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("### 📊")
    st.markdown("**1980s**")
with col2:
    st.markdown("### Sistemas DSS (Decision Support Systems)")
    st.write("Los primeros intentos de análisis de datos empresariales")
    st.markdown("""
    - 📂 Datos extraídos manualmente de sistemas transaccionales
    - 📋 Reportes simples para ejecutivos
    - ⚠️ Sistemas no estandarizados y difíciles de mantener
    - 💾 Almacenamiento limitado y procesamiento lento
    """)

st.divider()

# 1990s
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("### 🏗️")
    st.markdown("**1990s**")
with col2:
    st.markdown("### Nacimiento del Data Warehouse Moderno")
    st.write("**Bill Inmon** y **Ralph Kimball** definen las bases del DWH")
    
    tab1, tab2 = st.tabs(["📘 Bill Inmon", "📗 Ralph Kimball"])
    
    with tab1:
        st.markdown("""
        **Enfoque: Corporate Information Factory (CIF)**
        - 🏛️ Repositorio centralizado, integrado y no volátil
        - 📊 Datos normalizados (3NF)
        - 🎯 Enfoque "top-down": primero el DWH, luego los Data Marts
        - 🔍 Una sola fuente de verdad para toda la organización
        """)
    
    with tab2:
        st.markdown("""
        **Enfoque: Dimensional Modeling**
        - ⭐ Modelo dimensional (Star Schema)
        - 📦 Data Marts por área de negocio
        - 🎯 Enfoque "bottom-up": primero los Data Marts
        - 👥 Orientado a usuarios de negocio (fácil de entender)
        """)

st.divider()

# 2000s
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("### 💻")
    st.markdown("**2000s**")
with col2:
    st.markdown("### Era de las Herramientas Comerciales")
    st.write("Automatización y madurez de procesos ETL y OLAP")
    st.markdown("""
    - 🔄 **ETL automatizado**: Informatica PowerCenter, IBM DataStage, Oracle ODI
    - 📊 **OLAP Cubes**: Microsoft Analysis Services, Oracle Essbase
    - 🗄️ **Bases de datos columnares**: Teradata, Vertica, Netezza
    - 📈 **BI Tools**: Business Objects, Cognos, MicroStrategy
    - ⚡ Mayor rendimiento en consultas analíticas
    """)

st.divider()

# 2010s+
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("### ☁️")
    st.markdown("**2010s+**")
with col2:
    st.markdown("### Revolución Cloud, Big Data y AI")
    st.write("La era moderna del análisis de datos")
    st.markdown("""
    - ☁️ **Cloud Data Warehouses**: Amazon Redshift (2012), Snowflake (2014), Google BigQuery
    - 🌊 **Data Lakes**: Hadoop, S3, Azure Data Lake
    - ⚡ **Procesamiento distribuido**: Spark, Presto, Databricks
    - 🤖 **Integración con AI/ML**: TensorFlow, scikit-learn integrados
    - 📊 **Self-service BI**: Tableau, Power BI, Looker
    - 🔄 **Tiempo real**: Streaming con Kafka, Kinesis
    - 💰 **Modelo de pago por uso**: Escalabilidad elástica
    """)

st.divider()

# 🔮 Hoy y Futuro
st.subheader("🔮 La Actualidad (2020s)")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🏠 Lakehouse")
    st.write("""
    Unificación de Data Lake + Data Warehouse
    - Delta Lake, Apache Iceberg
    - Un solo repositorio para todo
    """)

with col2:
    st.markdown("#### 🧠 IA Integrada")
    st.write("""
    Machine Learning nativo en DWH
    - Snowflake ML, BigQuery ML
    - Predicciones con SQL
    """)

with col3:
    st.markdown("#### 🌐 Data Mesh")
    st.write("""
    Descentralización de datos
    - Propiedad por dominio
    - Data as a Product
    """)

st.divider()

# 📊 Comparativa: Antes vs Ahora
st.subheader("📊 Transformación: Antes vs Ahora")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ❌ Antes (1990s-2000s)")
    st.markdown("""
    - 🐌 Procesamiento nocturno (batch)
    - 💰 Hardware caro y on-premise
    - 👨‍💻 Solo para expertos técnicos
    - 📆 Datos con días de retraso
    - 🔧 Mantenimiento complejo
    - 💾 Capacidad fija y limitada
    - 📊 Reportes estáticos predefinidos
    """)

with col2:
    st.markdown("### ✅ Ahora (2020s)")
    st.markdown("""
    - ⚡ Análisis en tiempo real
    - ☁️ Cloud escalable (pago por uso)
    - 👥 Self-service para todos
    - 🔄 Datos actualizados al segundo
    - 🤖 Automatización y IA integrada
    - 📈 Escalabilidad elástica infinita
    - 🎨 Visualizaciones interactivas dinámicas
    """)

st.divider()

# Ejemplo práctico
st.subheader("💡 Ejemplo Práctico: Análisis de Ventas")

with st.expander("👉 Haz clic para ver la evolución"):
    st.markdown("#### 📅 1990s: Análisis Manual")
    st.code("""
    1. Extraer datos de múltiples sistemas (días)
    2. Limpiar en Excel (horas)
    3. Consolidar manualmente (horas)
    4. Generar reporte en PowerPoint (horas)
    5. Presentar a gerencia (una vez al mes)
    
    ⏰ Tiempo total: Semanas | Datos: Desactualizados
    """)
    
    st.markdown("#### 📅 2000s: ETL y DWH")
    st.code("""
    1. ETL nocturno automatizado
    2. Datos en DWH central
    3. Reportes OLAP predefinidos
    4. Acceso via BI Tool
    
    ⏰ Tiempo total: Horas | Datos: 24h de retraso
    """)
    
    st.markdown("#### 📅 2020s: Cloud + Real-Time")
    st.code("""
    1. Streaming en tiempo real (Kafka → Snowflake)
    2. Dashboard self-service actualizado al segundo
    3. Alertas automáticas con ML (predicción de anomalías)
    4. Acceso desde móvil, compartible en Slack
    
    ⏰ Tiempo total: Segundos | Datos: En tiempo real
    """)

st.divider()

# 🎯 Impacto de la evolución
st.subheader("🎯 Impacto de la Evolución del DWH")

metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)

with metrics_col1:
    st.metric("Velocidad", "1000x", delta="vs 1990s", delta_color="normal")
    
with metrics_col2:
    st.metric("Costo/TB", "90%", delta="reducción", delta_color="inverse")
    
with metrics_col3:
    st.metric("Usuarios", "100x", delta="más acceso", delta_color="normal")
    
with metrics_col4:
    st.metric("Capacidad", "∞", delta="ilimitada", delta_color="normal")

st.divider()

# Beneficios clave
col1, col2 = st.columns(2)

with col1:
    st.success("⚡ **Mayor velocidad de análisis**: De semanas a segundos")
    st.success("☁️ **Democratización**: Todos pueden analizar datos")
    st.success("🤖 **IA Integrada**: ML nativo para predicciones")

with col2:
    st.info("💰 **Reducción de costos**: Pago por uso vs servidores caros")
    st.info("📈 **Escalabilidad infinita**: Crece según necesidades")
    st.info("✅ **Calidad de datos**: ETL automatizado reduce errores")

st.divider()
