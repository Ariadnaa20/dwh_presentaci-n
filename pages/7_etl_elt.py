# pages/7_etl_elt.py
import streamlit as st

st.set_page_config(page_title="ETL vs ELT", page_icon="🔄", layout="wide")

st.markdown("<h1 style='text-align:center; color:#1e3d8f;'>🔄 ETL vs ELT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Procesos de extracción, transformación y carga de datos</p>", unsafe_allow_html=True)

st.divider()

# --- Introducción ---
st.subheader("📝 ¿Qué son ETL y ELT?")
st.write("""
**ETL** y **ELT** son enfoques para integrar datos desde fuentes diversas hacia un sistema de análisis.
La diferencia principal está en **dónde** y **cuándo** se realizan las transformaciones.
""")

st.divider()

# --- ETL ---
st.subheader("📤 ETL: Extract, Transform, Load")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    ### Flujo ETL Tradicional
    
    El proceso **ETL** transforma los datos **antes** de cargarlos en el destino:
    
    **1️⃣ Extract (Extraer):**
    - Conectar a fuentes de datos (BD, APIs, archivos)
    - Leer datos desde sistemas origen
    - Identificar datos nuevos/modificados (CDC)
    
    **2️⃣ Transform (Transformar):**
    - Limpiar datos (nulos, duplicados, inconsistencias)
    - Validar calidad de datos
    - Aplicar reglas de negocio
    - Enriquecer y combinar datos
    - Agregar y calcular métricas
    - **Todo esto en un servidor ETL intermedio**
    
    **3️⃣ Load (Cargar):**
    - Escribir datos transformados al DWH
    - Datos ya listos para consultas
    - Carga optimizada (bulk insert)
    """)

with col2:
    st.info("""
    **Ventajas ETL:**
    
    ✅ Datos llegan limpios al DWH
    ✅ Menos carga en el DWH
    ✅ Transformaciones complejas
    ✅ Control total del proceso
    ✅ Seguridad: datos sensibles transformados fuera
    
    **Desventajas:**
    
    ❌ Proceso más lento
    ❌ Servidor ETL costoso
    ❌ Menos flexibilidad
    ❌ No guarda datos raw
    ❌ Cambios requieren re-procesamiento
    """)

st.code("""
# Flujo ETL Visual

┌─────────┐      ┌─────────┐      ┌─────────┐
│ Source  │ ---> │ ETL     │ ---> │   DWH   │
│ Systems │      │ Server  │      │ (Clean) │
└─────────┘      └─────────┘      └─────────┘
   Extract       Transform           Load
                 (Staging)
                 
Datos transformados ANTES de llegar al DWH
""")

st.divider()

# --- ELT ---
st.subheader("📥 ELT: Extract, Load, Transform")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    ### Flujo ELT Moderno
    
    El proceso **ELT** carga los datos primero y transforma **después**, dentro del DWH:
    
    **1️⃣ Extract (Extraer):**
    - Conectar a fuentes de datos
    - Leer datos (igual que ETL)
    - Mínima transformación (solo formato)
    
    **2️⃣ Load (Cargar):**
    - Cargar datos **RAW** directamente al DWH
    - Área de staging en el propio DWH
    - Carga rápida y simple
    - **Se guardan los datos originales**
    
    **3️⃣ Transform (Transformar):**
    - Transformaciones **dentro** del DWH
    - Usar SQL o herramientas nativas
    - Aprovecha el poder de cómputo del DWH
    - Transformaciones bajo demanda
    - Datos raw siempre disponibles
    """)

with col2:
    st.success("""
    **Ventajas ELT:**
    
    ✅ Carga mucho más rápida
    ✅ Datos raw preservados
    ✅ Flexibilidad: re-transformar fácilmente
    ✅ Aprovecha poder del DWH cloud
    ✅ Menos infraestructura
    ✅ Ideal para exploración
    
    **Desventajas:**
    
    ❌ Más carga en el DWH
    ❌ Datos sensibles en raw
    ❌ Requiere DWH potente
    ❌ Costos de compute mayores
    ❌ Transformaciones menos portable
    """)

st.code("""
# Flujo ELT Visual

┌─────────┐      ┌──────────────────┐
│ Source  │ ---> │       DWH        │
│ Systems │      │ ┌─────┬────────┐ │
└─────────┘      │ │ Raw │Transformed│
   Extract       │ │Data │  Data   │ │
                 │ └─────┴────────┘ │
                 └──────────────────┘
                   Load → Transform
                   
Datos raw cargados primero, transformados después
""")

st.divider()

# --- Comparativa ---
st.subheader("⚖️ ETL vs ELT: Comparativa Detallada")

comparison = {
    "Aspecto": [
        "Orden de Operaciones",
        "Transformaciones",
        "Velocidad de carga",
        "Datos raw",
        "Flexibilidad",
        "Costo infraestructura",
        "Escalabilidad",
        "Mantenimiento",
        "Ideal para"
    ],
    "ETL": [
        "Extract → Transform → Load",
        "En servidor ETL",
        "Más lenta",
        "No se guardan",
        "Menos flexible",
        "Servidor ETL necesario",
        "Escalado vertical",
        "Más complejo",
        "On-premise, datos sensibles"
    ],
    "ELT": [
        "Extract → Load → Transform",
        "Dentro del DWH",
        "Muy rápida",
        "Se preservan",
        "Muy flexible",
        "Solo DWH necesario",
        "Escalado horizontal",
        "Más simple",
        "Cloud, big data, agilidad"
    ]
}

st.table(comparison)

st.divider()

# --- Casos de Uso ---
st.subheader("🎯 ¿Cuándo usar ETL vs ELT?")

tab1, tab2 = st.tabs(["📤 Usa ETL cuando...", "📥 Usa ELT cuando..."])

with tab1:
    st.markdown("""
    ### Situaciones ideales para ETL
    
    **1. Datos Sensibles:**
    - Necesitas enmascarar/encriptar datos antes de almacenar
    - Compliance requiere no guardar datos raw
    - PII (información personal) debe transformarse fuera
    
    **2. Transformaciones Complejas:**
    - Lógica de negocio muy compleja
    - Múltiples fuentes que combinar antes de cargar
    - Cálculos intensivos mejor fuera del DWH
    
    **3. Infraestructura Legacy:**
    - DWH on-premise con capacidad limitada
    - Herramientas ETL ya implementadas
    - Equipo experto en herramientas ETL tradicionales
    
    **4. Volúmenes Pequeños:**
    - Pocos datos para transformar
    - El tiempo de transformación no es crítico
    - No necesitas análisis exploratorio
    
    **5. Destinos Múltiples:**
    - Necesitas cargar a varios destinos
    - Transformaciones reutilizables
    - Data marts específicos
    """)
    
    st.info("""
    **💡 Ejemplo ETL:**
    
    Una empresa financiera que necesita:
    - Enmascarar números de cuenta antes de almacenar
    - Validar transacciones con reglas complejas
    - Combinar datos de 20 sistemas antes de cargar
    - No puede guardar datos raw por compliance
    
    → ETL es la mejor opción
    """)

with tab2:
    st.markdown("""
    ### Situaciones ideales para ELT
    
    **1. Cloud Data Warehouse:**
    - Usando Snowflake, BigQuery, Redshift
    - DWH con capacidad de cómputo elástica
    - Costo de storage bajo
    
    **2. Big Data:**
    - Volúmenes masivos de datos
    - Velocidad de carga es crítica
    - Datos de streaming o IoT
    
    **3. Agilidad y Exploración:**
    - Análisis exploratorio frecuente
    - Necesitas acceso a datos raw
    - Requisitos cambian frecuentemente
    - Data scientists explorando datos
    
    **4. Arquitectura Moderna:**
    - Data Lake + DWH (Lakehouse)
    - Microservicios y APIs
    - Datos semi-estructurados (JSON, logs)
    
    **5. Recursos Limitados:**
    - No quieres mantener servidores ETL
    - Prefieres serverless
    - Equipo pequeño de datos
    """)
    
    st.success("""
    **💡 Ejemplo ELT:**
    
    Una startup tech que necesita:
    - Cargar logs de aplicación rápidamente
    - Experimentar con diferentes transformaciones
    - Acceso a datos raw para ML
    - Escalar según demanda
    - Minimizar infraestructura
    
    → ELT es la mejor opción
    """)

st.divider()

# --- Herramientas ---
st.subheader("🛠️ Herramientas ETL vs ELT")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    ### Herramientas ETL Clásicas
    
    **Enterprise:**
    - Informatica PowerCenter
    - IBM DataStage
    - Oracle Data Integrator (ODI)
    - Microsoft SSIS
    
    **Open Source:**
    - Talend
    - Pentaho (Kettle)
    - Apache NiFi
    - Apache Hop
    
    **Características comunes:**
    - GUI drag-and-drop
    - Transformaciones visuales
    - Conectores pre-built
    - Orquestación integrada
    """)

with col2:
    st.success("""
    ### Herramientas ELT Modernas
    
    **Cloud ETL/ELT:**
    - AWS Glue
    - Azure Data Factory
    - Google Cloud Dataflow
    
    **Replicación ELT:**
    - Fivetran
    - Airbyte (open source)
    - Stitch (Talend)
    - Matillion
    
    **Transformación SQL:**
    - dbt (data build tool) ⭐
    - Dataform (Google)
    - SQLMesh
    
    **Características comunes:**
    - Cloud-native
    - Enfoque en carga rápida
    - Transformaciones en SQL
    - Versionado de código (Git)
    """)

st.divider()

# --- dbt Example ---
with st.expander("⭐ dbt (data build tool) - El estándar moderno para ELT"):
    st.markdown("""
    ### ¿Qué es dbt?
    
    **dbt** es la herramienta líder para transformaciones ELT en SQL. Permite:
    
    **Características:**
    - Transformaciones en SQL puro
    - Versionado con Git
    - Testing de datos integrado
    - Documentación automática
    - Linaje de datos visual
    - Modularidad y reutilización
    
    **Ejemplo de modelo dbt:**
    """)
    
    st.code("""
-- models/staging/stg_orders.sql
WITH source AS (
    SELECT * FROM {{ source('raw', 'orders') }}
),

cleaned AS (
    SELECT
        order_id,
        customer_id,
        order_date,
        CAST(amount AS DECIMAL(10,2)) AS amount,
        status
    FROM source
    WHERE order_date IS NOT NULL
)

SELECT * FROM cleaned

-- Este modelo crea una tabla/vista en el DWH
-- Se ejecuta con: dbt run
    """, language="sql")
    
    st.markdown("""
    **Workflow dbt:**
    ```
    Raw Data (loaded) → dbt models (SQL) → Transformed tables/views
    ```
    
    **Ventajas:**
    - ✅ Transformaciones legibles (SQL)
    - ✅ Control de versiones
    - ✅ Testing automático
    - ✅ Documentación viva
    - ✅ Compatible con todos los DWH modernos
    """)

st.divider()

# --- Tendencias ---
st.subheader("📈 Tendencias Actuales")

col1, col2 = st.columns(2)

with col1:
    st.warning("""
    ### El cambio hacia ELT
    
    **Por qué ELT está ganando:**
    
    1. **Cloud DWH más baratos y potentes**
       - Snowflake, BigQuery, Redshift
       - Compute separado de storage
       - Escalado elástico
    
    2. **Necesidad de agilidad**
       - Startups y empresas ágiles
       - Análisis exploratorio
       - Data science y ML
    
    3. **Arquitectura moderna**
       - Data Lakes (S3, ADLS, GCS)
       - Lakehouse (Delta, Iceberg)
       - Datos semi-estructurados
    
    4. **DevOps para datos (DataOps)**
       - Git, CI/CD
       - Testing automatizado
       - Infraestructura como código
    """)

with col2:
    st.info("""
    ### ETL aún relevante
    
    **Casos donde ETL sigue siendo mejor:**
    
    1. **Enterprise legacy**
       - Inversión en Informatica/DataStage
       - On-premise DWH (Oracle, Teradata)
       - Equipos expertos en ETL
    
    2. **Compliance estricto**
       - Banca y finanzas
       - Salud (HIPAA)
       - Datos sensibles PII
    
    3. **Transformaciones complejas**
       - Lógica propietaria compleja
       - Múltiples sistemas legacy
       - Integración tiempo real
    
    4. **Destinos múltiples**
       - Cargar a varios DWH
       - Sincronización entre sistemas
       - Data marts específicos
    """)

st.divider()

# --- Híbrido ---
with st.expander("🔀 Enfoque Híbrido: ETL + ELT"):
    st.markdown("""
    ### Lo mejor de ambos mundos
    
    Muchas organizaciones modernas usan un **enfoque híbrido**:
    
    **Arquitectura combinada:**
    ```
    ┌─────────┐      ┌─────────┐      ┌──────────────────┐
    │ Sources │ ---> │ ETL     │ ---> │       DWH        │
    │ Legacy  │      │ Light   │      │ ┌─────┬────────┐ │
    └─────────┘      └─────────┘      │ │ Raw │  ELT   │ │
                                      │ │     │ Trans. │ │
    ┌─────────┐                      │ └─────┴────────┘ │
    │ Modern  │ -------------------> │                  │
    │ APIs    │   Direct Load (ELT) └──────────────────┘
    └─────────┘
    ```
    
    **Estrategia:**
    - **ETL ligero:** Solo transformaciones esenciales de seguridad/compliance
    - **Carga rápida:** Datos raw al DWH
    - **ELT dentro del DWH:** Transformaciones de negocio con dbt/SQL
    
    **Beneficios:**
    - ✅ Seguridad de ETL
    - ✅ Flexibilidad de ELT
    - ✅ Datos raw disponibles
    - ✅ Transformaciones ágiles
    
    **Ejemplo:**
    1. ETL: Enmascarar PII de clientes al extraer
    2. Load: Cargar datos masked a staging
    3. ELT: Transformar con dbt para modelos analíticos
    """)

st.divider()

# --- Decisión ---
st.subheader("🤔 Guía de Decisión")

st.markdown("""
### Flowchart de Decisión

```
¿Usas Cloud DWH? (Snowflake, BigQuery, Redshift)
  │
  ├─ SÍ → ¿Tienes datos muy sensibles?
  │        │
  │        ├─ SÍ → ETL ligero + ELT
  │        └─ NO  → ELT puro (dbt)
  │
  └─ NO → ¿DWH on-premise con capacidad limitada?
           │
           ├─ SÍ → ETL clásico
           └─ NO  → Considera migrar a cloud + ELT
```

**Recomendación general 2025:**
Para nuevos proyectos, empieza con **ELT** (Fivetran/Airbyte + dbt) a menos que tengas 
requisitos específicos que requieran ETL.
""")

st.divider()

