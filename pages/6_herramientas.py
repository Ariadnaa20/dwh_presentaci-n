# pages/6_herramientas.py
import streamlit as st

st.set_page_config(page_title="Herramientas DWH", page_icon="🛠️", layout="wide")

st.markdown("<h1 style='text-align:center; color:#ffffff;'>🛠️ Herramientas y Tecnologías</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Plataformas On-Premise y Cloud para Data Warehouses</p>", unsafe_allow_html=True)

st.divider()

# --- Introducción ---
st.subheader("📝 Panorama de Herramientas DWH")
st.write("""
El ecosistema de **Data Warehouse** incluye múltiples categorías de herramientas:
almacenamiento, ETL/ELT, modelado, visualización y gobierno. Podemos clasificarlas
en soluciones **On-Premise** (locales) y **Cloud** (nube).
""")

st.divider()

# --- On-Premise vs Cloud ---
st.subheader("🏢 On-Premise vs ☁️ Cloud")

col1, col2 = st.columns(2)

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
    - ❌ Mantenimiento y actualizaciones manuales
    - ❌ Escalabilidad limitada
    - ❌ Requiere equipo técnico dedicado
    """)

with col2:
    st.success("""
    ### ☁️ Cloud (Nube)
    
    **Características:**
    - Infraestructura gestionada por proveedor
    - Acceso via internet
    - Modelo de pago por uso
    
    **Ventajas:**
    - ✅ Sin inversión inicial (OPEX)
    - ✅ Escalabilidad elástica
    - ✅ Actualizaciones automáticas
    - ✅ Alta disponibilidad y disaster recovery
    - ✅ Despliegue rápido
    
    **Desventajas:**
    - ❌ Dependencia de conexión a internet
    - ❌ Costos variables
    - ❌ Menor control sobre infraestructura
    - ❌ Posibles preocupaciones de seguridad
    """)

st.divider()

# --- Bases de Datos DWH ---
st.subheader("🗄️ Bases de Datos para Data Warehousing")

tab1, tab2 = st.tabs(["🏢 On-Premise", "☁️ Cloud"])

with tab1:
    st.markdown("""
    ### Soluciones On-Premise Populares
    """)
    
    with st.expander("🔷 Oracle Database & Exadata"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Oracle Database** con **Exadata** es una solución empresarial completa.
            
            **Características:**
            - Motor de BD relacional robusto
            - Exadata: appliance optimizado para DWH
            - Compresión avanzada (Hybrid Columnar Compression)
            - Particionamiento inteligente
            - In-Memory Column Store
            
            **Casos de uso:**
            - Empresas grandes con infraestructura Oracle
            - Cargas de trabajo mixtas (OLTP + OLAP)
            - Requisitos de máximo rendimiento
            """)
        with col2:
            st.metric("Tipo", "Relacional")
            st.metric("Licencia", "Comercial $$$")
            st.metric("Escalabilidad", "Alta")
    
    with st.expander("🔷 Microsoft SQL Server"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **SQL Server** es la solución DWH de Microsoft.
            
            **Características:**
            - Integration Services (SSIS) para ETL
            - Analysis Services (SSAS) para OLAP
            - Reporting Services (SSRS) para reportes
            - Columnstore indexes para DWH
            - Integración con ecosistema Microsoft
            
            **Casos de uso:**
            - Entornos Windows/.NET
            - Integración con Power BI
            - SMB a Enterprise
            """)
        with col2:
            st.metric("Tipo", "Relacional")
            st.metric("Licencia", "Comercial $$")
            st.metric("Escalabilidad", "Media-Alta")
    
    with st.expander("🔷 IBM Db2 Warehouse"):
        st.markdown("""
        **IBM Db2** con extensiones de warehousing.
        
        **Características:**
        - BLU Acceleration (columnar)
        - Compresión adaptativa
        - Workload management avanzado
        - Integración con IBM Cloud Pak
        
        **Casos de uso:**
        - Empresas con infraestructura IBM
        - Mainframe integration
        - Entornos híbridos
        """)
    
    with st.expander("🔶 Teradata"):
        st.markdown("""
        **Teradata** - Pionero en DWH empresarial.
        
        **Características:**
        - Arquitectura MPP (Massively Parallel Processing)
        - Optimizado para consultas complejas
        - Gestión automática de datos
        - Escalabilidad masiva
        
        **Casos de uso:**
        - Enterprise DWH de gran escala
        - Telecomunicaciones, banca, retail
        - Petabytes de datos
        
        💰 **Nota:** Muy costoso, perdiendo mercado frente a cloud
        """)
    
    with st.expander("🟢 PostgreSQL + Greenplum"):
        st.markdown("""
        **PostgreSQL** con **Greenplum** para análisis masivo.
        
        **Características:**
        - Open source y gratuito
        - Greenplum: MPP sobre PostgreSQL
        - Compatible con herramientas SQL estándar
        - Comunidad activa
        
        **Casos de uso:**
        - Empresas que buscan alternativa open source
        - Presupuestos limitados
        - Flexibilidad y personalización
        """)

with tab2:
    st.markdown("""
    ### Soluciones Cloud Populares
    """)
    
    with st.expander("☁️ Amazon Redshift"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Amazon Redshift** - Servicio DWH de AWS.
            
            **Características:**
            - Almacenamiento columnar
            - Compresión automática
            - Distribución de datos (DIST KEYS)
            - Integración con S3, Glue, QuickSight
            - Redshift Spectrum (consultas en S3)
            - Concurrency Scaling automático
            
            **Pricing:**
            - Pago por nodo/hora
            - Serverless disponible
            
            **Casos de uso:**
            - Empresas en ecosistema AWS
            - Data Lakes en S3
            - Análisis de petabytes
            """)
        with col2:
            st.metric("Proveedor", "AWS")
            st.metric("Pricing", "Node-based")
            st.metric("⭐ Rating", "4.5/5")
    
    with st.expander("☁️ Google BigQuery"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Google BigQuery** - DWH serverless de Google.
            
            **Características:**
            - **Serverless** (sin gestión de infraestructura)
            - Almacenamiento columnar (Capacitor)
            - Escalado automático masivo
            - Consultas en segundos sobre TB/PB
            - ML integrado (BigQuery ML)
            - Separación de compute y storage
            - Streaming insert en tiempo real
            
            **Pricing:**
            - Pago por consulta ($ por TB procesado)
            - Flat-rate para uso predecible
            
            **Casos de uso:**
            - Startups y empresas cloud-native
            - Análisis ad-hoc masivo
            - ML sobre datos warehouse
            """)
        with col2:
            st.metric("Proveedor", "Google Cloud")
            st.metric("Pricing", "Por consulta")
            st.metric("⭐ Rating", "4.7/5")
    
    with st.expander("☁️ Snowflake"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Snowflake** - DWH cloud-native multi-cloud.
            
            **Características:**
            - **Multi-cloud** (AWS, Azure, GCP)
            - Separación total compute/storage
            - Virtual Warehouses independientes
            - Zero-copy cloning
            - Time Travel (acceso a datos históricos)
            - Data Sharing entre cuentas
            - Escalado instantáneo
            
            **Pricing:**
            - Storage: $ por TB/mes
            - Compute: $ por segundo de uso (créditos)
            
            **Casos de uso:**
            - Empresas multi-cloud
            - Data sharing entre organizaciones
            - Workloads con demanda variable
            """)
        with col2:
            st.metric("Proveedor", "Multi-cloud")
            st.metric("Pricing", "Compute+Storage")
            st.metric("⭐ Rating", "4.8/5")
    
    with st.expander("☁️ Azure Synapse Analytics"):
        st.markdown("""
        **Azure Synapse Analytics** - Plataforma DWH unificada de Microsoft.
        
        **Características:**
        - Unifica DWH y Big Data analytics
        - Pools SQL dedicados y serverless
        - Integración con Power BI
        - Spark integrado para big data
        - Data Explorer para series temporales
        - Pipelines (similar a ADF)
        
        **Pricing:**
        - DWU (Data Warehouse Units)
        - Pay-as-you-go o reservado
        
        **Casos de uso:**
        - Empresas en ecosistema Microsoft
        - Análisis unificado SQL + Spark
        - Integración con Office 365
        """)
    
    with st.expander("☁️ Databricks SQL (Lakehouse)"):
        st.markdown("""
        **Databricks SQL** - Análisis SQL sobre Data Lakehouse.
        
        **Características:**
        - Basado en Apache Spark
        - Delta Lake para ACID en Data Lake
        - Photon engine (motor vectorizado)
        - BI integrado (Databricks SQL)
        - Unity Catalog para governance
        
        **Casos de uso:**
        - Arquitectura Data Lakehouse
        - Empresas con Spark existente
        - ML + Analytics unificado
        """)

st.divider()

# --- Herramientas ETL/ELT ---
st.subheader("🔄 Herramientas ETL/ELT")

tab1, tab2 = st.tabs(["🏢 On-Premise", "☁️ Cloud"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Informatica PowerCenter**
        - Líder histórico en ETL empresarial
        - GUI drag-and-drop
        - Conectores para 100+ fuentes
        - Data quality integrado
        - 💰 Muy costoso
        """)
        
        st.success("""
        **Microsoft SSIS**
        - Incluido con SQL Server
        - Integración con Visual Studio
        - Transformaciones visuales
        - 💲 Económico para clientes Microsoft
        """)
    
    with col2:
        st.warning("""
        **Talend**
        - Open source y versión enterprise
        - Generación de código Java
        - Big Data support
        - 💡 Buena relación calidad/precio
        """)
        
        st.info("""
        **Pentaho Data Integration (Kettle)**
        - Open source
        - GUI intuitivo (Spoon)
        - Comunidad activa
        - 🆓 Gratuito (versión community)
        """)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **AWS Glue**
        - Serverless ETL
        - Basado en Spark
        - Data Catalog automático
        - Integración con ecosistema AWS
        """)
        
        st.info("""
        **Azure Data Factory**
        - Servicio de integración cloud
        - Pipelines visuales
        - Mapping Data Flows
        - Integración con Synapse
        """)
    
    with col2:
        st.warning("""
        **Google Cloud Dataflow**
        - Basado en Apache Beam
        - Streaming y batch unificado
        - Escalado automático
        - Procesamiento distribuido
        """)
        
        st.success("""
        **Fivetran / Airbyte**
        - ELT moderno (cloud → cloud)
        - Conectores pre-built
        - Replicación automática
        - Low-code / No-code
        """)

st.divider()

# --- Herramientas BI ---
st.subheader("📊 Herramientas de Business Intelligence")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **Tableau**
    - Visualizaciones interactivas
    - Drag-and-drop intuitivo
    - Gran comunidad
    - 💰 $$$ (ahora Salesforce)
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
    - 💰 $$ (ahora Google)
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

st.divider()

# --- Comparativa Cloud DWH ---
st.subheader("⚖️ Comparativa Cloud Data Warehouses")

comparison_data = {
    "Característica": ["Serverless", "Multi-Cloud", "ML Integrado", "Pricing", "Escalabilidad", "Facilidad Uso"],
    "Redshift": ["Opcional", "❌", "Limitado", "Por nodo", "⭐⭐⭐⭐", "⭐⭐⭐"],
    "BigQuery": ["✅", "❌", "✅✅", "Por consulta", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
    "Snowflake": ["✅", "✅", "Via partners", "Compute+Storage", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐"],
    "Synapse": ["Opcional", "❌", "Limitado", "DWU/Serverless", "⭐⭐⭐⭐", "⭐⭐⭐"]
}

st.table(comparison_data)

st.divider()

# --- Selección de Herramientas ---
with st.expander("🤔 ¿Cómo elegir la herramienta adecuada?"):
    st.markdown("""
    ### Criterios de Selección
    
    **1. Presupuesto:**
    - 💰💰💰 Enterprise: Oracle, Teradata, Informatica
    - 💰💰 Medio: SQL Server, Snowflake, Tableau
    - 💰 Económico: BigQuery (pay-per-query), Power BI
    - 🆓 Open Source: PostgreSQL, Pentaho, Superset
    
    **2. Volumen de Datos:**
    - < 1 TB: Cualquier solución funciona
    - 1-10 TB: SQL Server, Redshift, BigQuery
    - 10-100 TB: Snowflake, BigQuery, Redshift
    - > 100 TB: BigQuery, Snowflake, Synapse con Spark
    
    **3. Experiencia del Equipo:**
    - Microsoft shop → SQL Server, Power BI, Synapse
    - AWS shop → Redshift, Glue, QuickSight
    - Google shop → BigQuery, Dataflow, Looker Studio
    - Open source → PostgreSQL, Pentaho, Superset
    
    **4. Casos de Uso:**
    - Analytics simple → BigQuery serverless
    - Workloads variables → Snowflake
    - ML integrado → BigQuery ML
    - Multi-cloud → Snowflake
    - Tiempo real → Databricks, Synapse
    
    **5. Compliance y Seguridad:**
    - Datos muy sensibles → On-premise (Oracle, SQL Server)
    - Regulaciones específicas → Verificar certificaciones cloud
    - Datos en EU → Verificar GDPR compliance
    """)

st.divider()

# --- Arquitectura Moderna ---
st.subheader("🚀 Stack Moderno Recomendado")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    ### Stack Cloud-Native (Startup/Mediana)
    
    **Ingesta:**
    - Fivetran / Airbyte (ELT)
    
    **Storage:**
    - Snowflake o BigQuery
    
    **Transformación:**
    - dbt (data build tool)
    
    **Orquestación:**
    - Airflow / Prefect
    
    **BI:**
    - Looker / Metabase
    
    **💡 Ventajas:** Moderno, escalable, costo-efectivo
    """)

with col2:
    st.info("""
    ### Stack Enterprise (Gran Empresa)
    
    **Ingesta:**
    - Informatica / Talend
    
    **Storage:**
    - Snowflake / Synapse
    
    **Transformación:**
    - DBT + Stored Procedures
    
    **Orquestación:**
    - Control-M / Airflow
    
    **BI:**
    - Tableau / Power BI
    
    **💡 Ventajas:** Robusto, soporte enterprise, probado
    """)

st.divider()

