# pages/10_comparativa.py
import streamlit as st

st.set_page_config(page_title="DWH vs Lake vs Lakehouse", page_icon="🔄", layout="wide")

st.markdown("<h1 style='text-align:center; color:#1e3d8f;'>🔄 Data Warehouse vs Data Lake vs Lakehouse</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Comparativa de arquitecturas de datos modernas</p>", unsafe_allow_html=True)

st.divider()

# --- Introducción ---
st.subheader("📝 Tres Enfoques para Gestión de Datos")
st.write("""
En el ecosistema moderno de datos, existen tres arquitecturas principales que a menudo se comparan y confunden:
**Data Warehouse**, **Data Lake** y **Data Lakehouse**. Cada una tiene sus propósitos, fortalezas y casos de uso ideales.
""")

st.divider()

# --- Las Tres Arquitecturas ---
st.subheader("🏗️ Las Tres Arquitecturas")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    ### 🏢 Data Warehouse
    
    **Qué es:**
    Sistema optimizado para análisis
    de datos **estructurados** e **históricos**
    
    **Origen:** Años 90 (Inmon, Kimball)
    
    **Tecnología:**
    - Base de datos relacional
    - Esquema definido (schema-on-write)
    - Modelo dimensional (estrella/copo)
    
    **Datos:**
    - Estructurados y limpios
    - ETL antes de cargar
    - Formato tabular
    
    **Ejemplos:**
    - Snowflake
    - BigQuery
    - Redshift
    - Synapse Analytics
    """)

with col2:
    st.success("""
    ### 🌊 Data Lake
    
    **Qué es:**
    Repositorio centralizado para almacenar
    datos **raw en cualquier formato**
    
    **Origen:** ~2010 (Era Big Data)
    
    **Tecnología:**
    - Object storage (S3, ADLS, GCS)
    - Schema-on-read
    - Formatos: Parquet, JSON, CSV, logs
    
    **Datos:**
    - Estructurados, semi-estructurados, no estructurados
    - Guardados en formato original
    - Sin transformación previa
    
    **Ejemplos:**
    - AWS S3 + Athena/Glue
    - Azure Data Lake + Synapse
    - Google Cloud Storage + Dataproc
    """)

with col3:
    st.warning("""
    ### 🏠 Data Lakehouse
    
    **Qué es:**
    Arquitectura híbrida que combina
    **flexibilidad de Lake** + **estructura de Warehouse**
    
    **Origen:** ~2020 (Databricks)
    
    **Tecnología:**
    - Storage de Lake
    - ACID transactions
    - Metadata layer (Delta, Iceberg)
    
    **Datos:**
    - Todos los tipos
    - Schema enforcement opcional
    - Versionado de datos
    
    **Ejemplos:**
    - Databricks (Delta Lake)
    - Apache Iceberg
    - Apache Hudi
    """)

st.divider()

# --- Comparativa Detallada ---
st.subheader("⚖️ Comparativa Detallada")

comparison_data = {
    "Característica": [
        "Tipo de datos",
        "Esquema",
        "Formato de almacenamiento",
        "Procesamiento",
        "Calidad de datos",
        "Performance consultas",
        "Costo de storage",
        "Flexibilidad",
        "Time-to-insight",
        "Governance",
        "ACID transactions",
        "Casos de uso principales"
    ],
    "🏢 Data Warehouse": [
        "Estructurados",
        "Schema-on-write (rígido)",
        "Tablas relacionales",
        "SQL",
        "Alta (ETL)",
        "Muy rápido (optimizado)",
        "$$ Alto",
        "Baja",
        "Lento (ETL)",
        "Fuerte",
        "✅ Sí",
        "BI, Reporting"
    ],
    "🌊 Data Lake": [
        "Todos (sin límite)",
        "Schema-on-read (flexible)",
        "Archivos (Parquet, JSON)",
        "Spark, Presto, Athena",
        "Variable (datos raw)",
        "Medio-Lento",
        "$ Bajo",
        "Muy alta",
        "Rápido (carga directa)",
        "Débil",
        "❌ No (originalmente)",
        "ML, Exploración, Archiving"
    ],
    "🏠 Data Lakehouse": [
        "Todos",
        "Híbrido (ambos)",
        "Archivos con metadata",
        "SQL + Spark",
        "Alta (enforced)",
        "Rápido",
        "$ Bajo-Medio",
        "Alta",
        "Medio",
        "Fuerte",
        "✅ Sí",
        "BI + ML + Exploración"
    ]
}

st.table(comparison_data)

st.divider()

# --- Deep Dive ---
st.subheader("🔍 Análisis Profundo")

tab1, tab2, tab3 = st.tabs(["🏢 Data Warehouse", "🌊 Data Lake", "🏠 Data Lakehouse"])

with tab1:
    st.markdown("""
    ### Data Warehouse - El Clásico
    
    **Historia:**
    Concepto introducido en los años 90 por Bill Inmon y Ralph Kimball.
    Revolucionó el análisis de datos empresariales al separar OLTP de OLAP.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Fortalezas:**
        
        ✅ **Rendimiento excepcional** para queries SQL
        - Optimizado específicamente para análisis
        - Índices, particionamiento, compresión
        - Queries complejas en segundos
        
        ✅ **Calidad de datos garantizada**
        - ETL valida y limpia antes de cargar
        - Esquema definido evita errores
        - Consistencia enforced
        
        ✅ **Modelo dimensional intuitivo**
        - Fácil de entender para analistas
        - Estrella/copo de nieve familiar
        - Herramientas BI integran perfecto
        
        ✅ **Gobierno y auditoría**
        - Control de acceso granular
        - Historial de cambios (SCD)
        - Compliance y regulación
        """)
    
    with col2:
        st.error("""
        **Limitaciones:**
        
        ❌ **Solo datos estructurados**
        - No puede almacenar JSON variado
        - Logs, imágenes, videos = No
        - Esquema rígido
        
        ❌ **Rigidez del esquema**
        - Cambios requieren rediseño ETL
        - Lento para adaptarse a cambios
        - No apto para exploración ágil
        
        ❌ **Costo**
        - Storage más caro que Data Lake
        - Compute dedicado costoso
        - Licencias (on-premise)
        
        ❌ **Latencia de carga**
        - ETL batch (horas/días)
        - No real-time
        - Duplicación de datos
        """)
    
    st.info("""
    **Mejor para:**
    - Reporting ejecutivo y KPIs
    - BI y dashboards empresariales
    - Análisis histórico de datos transaccionales
    - Cumplimiento regulatorio
    - Organizaciones maduras con datos estables
    """)

with tab2:
    st.markdown("""
    ### Data Lake - El Flexible
    
    **Historia:**
    Surgió ~2010 con el auge de Hadoop y Big Data. Prometía almacenar "todos los datos" 
    a bajo costo sin necesidad de estructura previa.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Fortalezas:**
        
        ✅ **Almacena cualquier tipo de dato**
        - Estructurado, semi-estructurado, no estructurado
        - JSON, CSV, Parquet, logs, imágenes, videos
        - Sin límites de esquema
        
        ✅ **Costo de storage muy bajo**
        - S3: ~$0.023/GB/mes
        - 10-20x más barato que DWH
        - Ideal para Big Data
        
        ✅ **Flexibilidad máxima**
        - Schema-on-read
        - Experimentación ágil
        - Ideal para data scientists
        
        ✅ **Escalabilidad ilimitada**
        - Petabytes sin problema
        - Separación compute/storage
        - Pay-as-you-go
        """)
    
    with col2:
        st.error("""
        **Limitaciones:**
        
        ❌ **"Data Swamp" (pantano de datos)**
        - Sin gobierno = caos
        - Datos duplicados/inconsistentes
        - Difícil encontrar datos útiles
        
        ❌ **Performance pobre para BI**
        - Queries SQL lentos
        - Sin índices/optimización
        - Escaneo full de archivos
        
        ❌ **Sin ACID transactions**
        - No updates atómicos
        - Inconsistencias posibles
        - Difícil mantener calidad
        
        ❌ **Complejidad técnica**
        - Requiere Spark/Presto
        - Curva de aprendizaje alta
        - No self-service para analistas
        """)
    
    st.info("""
    **Mejor para:**
    - Machine Learning (datos raw necesarios)
    - Análisis exploratorio de data scientists
    - Archiving de datos históricos
    - IoT y streaming data
    - Datos no estructurados (logs, clickstream)
    """)

with tab3:
    st.markdown("""
    ### Data Lakehouse - Lo Mejor de Ambos Mundos
    
    **Historia:**
    Concepto popularizado por Databricks en 2020. Promete unificar Data Lake y Data Warehouse
    en una sola arquitectura, eliminando la necesidad de duplicar datos.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Fortalezas:**
        
        ✅ **Unifica BI y ML**
        - Un solo lugar para todos los datos
        - SQL para BI + Spark para ML
        - No duplicación Lake → Warehouse
        
        ✅ **ACID sobre Data Lake**
        - Delta Lake/Iceberg añaden transacciones
        - Updates, deletes, merges posibles
        - Versionado de datos (time travel)
        
        ✅ **Performance mejorado**
        - Metadata layer optimiza queries
        - Caching inteligente
        - Mejor que Lake puro, cerca de DWH
        
        ✅ **Flexibilidad + Gobierno**
        - Schema enforcement opcional
        - Governance sobre archivos
        - Calidad de datos enforced
        
        ✅ **Costo reducido**
        - Storage de Lake (barato)
        - Compute solo cuando necesario
        - Sin duplicación de datos
        """)
    
    with col2:
        st.error("""
        **Limitaciones:**
        
        ❌ **Tecnología relativamente nueva**
        - Menos maduro que DWH
        - Menos herramientas integradas
        - Expertise menos común
        
        ❌ **Complejidad de setup**
        - Requiere configuración cuidadosa
        - Delta Lake/Iceberg/Hudi diferentes
        - Curva de aprendizaje
        
        ❌ **Performance aún no igual a DWH**
        - Para queries muy complejas
        - DWH dedicado sigue siendo más rápido
        - Aunque la brecha se cierra
        
        ❌ **Vendor lock-in posible**
        - Delta Lake (Databricks)
        - Aunque hay open source options
        """)
    
    st.info("""
    **Mejor para:**
    - Organizaciones que quieren unificar Lake + Warehouse
    - Casos de uso de BI + ML simultáneos
    - Empresas cloud-native modernas
    - Reducir duplicación y costos
    - Equipos ágiles con requisitos cambiantes
    """)

st.divider()

# --- Arquitecturas en Práctica ---
st.subheader("🏗️ Arquitecturas en Práctica")

st.markdown("""
### Cómo se usan en el mundo real
""")

col1, col2 = st.columns(2)

with col1:
    st.warning("""
    ### Arquitectura Tradicional (Separada)
    
    ```
    ┌──────────────┐
    │   Sources    │
    │  (OLTP DBs)  │
    └──────┬───────┘
           │ ETL
           ↓
    ┌──────────────┐      ┌──────────────┐
    │ Data Lake    │      │ Data         │
    │ (S3)         │ ───→ │ Warehouse    │
    │              │ ELT  │ (Snowflake)  │
    │ - Raw data   │      │              │
    │ - ML         │      │ - BI/Reports │
    │ - Archive    │      │ - KPIs       │
    └──────────────┘      └──────────────┘
           ↓                      ↓
    ML/Data Science        Dashboards/BI
    ```
    
    **Pros:**
    - Especialización (cada uno optimizado)
    - Herramientas maduras
    
    **Cons:**
    - Duplicación de datos
    - Dos sistemas que mantener
    - Sincronización necesaria
    """)

with col2:
    st.success("""
    ### Arquitectura Lakehouse (Unificada)
    
    ```
    ┌──────────────┐
    │   Sources    │
    │  (OLTP DBs)  │
    └──────┬───────┘
           │ Ingestion
           ↓
    ┌──────────────────────────────┐
    │      Data Lakehouse          │
    │      (Databricks)            │
    │                              │
    │  ┌────────┐   ┌───────────┐ │
    │  │  Raw   │ → │ Curated   │ │
    │  │(Bronze)│   │ (Silver)  │ │
    │  └────────┘   └─────┬─────┘ │
    │                     ↓        │
    │              ┌───────────┐  │
    │              │ Analytics │  │
    │              │  (Gold)   │  │
    │              └───────────┘  │
    └──────────────┬───────────────┘
                   ↓
         BI Tools + ML Notebooks
    ```
    
    **Pros:**
    - Un solo sistema
    - No duplicación
    - BI y ML sobre mismos datos
    
    **Cons:**
    - Menos maduro
    - Requiere expertise
    """)

st.divider()

# --- Migración ---
st.subheader("🔄 Rutas de Migración")

st.markdown("""
### ¿Cómo evolucionar tu arquitectura?
""")

tab1, tab2, tab3 = st.tabs(["DWH → Lakehouse", "Lake → Lakehouse", "Híbrido"])

with tab1:
    st.code("""
Migración: Data Warehouse → Data Lakehouse

Paso 1: Agregar Data Lake
├─ Mantener DWH existente (no apagar)
├─ Crear Data Lake (S3/ADLS)
└─ Cargar datos raw al Lake

Paso 2: Implementar Lakehouse layer
├─ Delta Lake/Iceberg sobre el Lake
├─ Migrar transformaciones ETL → ELT (dbt)
└─ Validar performance

Paso 3: Migración gradual de casos de uso
├─ Empezar con casos de uso nuevos
├─ Migrar reportes menos críticos
└─ Finalmente, reportes ejecutivos

Paso 4: Deprecar DWH
├─ Solo cuando todo migrado y validado
├─ Mantener período de rollback posible
└─ Liberar recursos del DWH antiguo

Timeline típico: 12-18 meses
Risk: Medio-Alto
Beneficio: Reducción costos 30-50%
    """)

with tab2:
    st.code("""
Migración: Data Lake → Data Lakehouse

Paso 1: Implementar metadata layer
├─ Instalar Delta Lake/Iceberg
├─ Convertir Parquet → Delta format
└─ No cambiar ubicación de datos

Paso 2: Agregar schema enforcement
├─ Definir esquemas para tablas principales
├─ Implementar validaciones de calidad
└─ Habilitar ACID transactions

Paso 3: Optimizar para queries
├─ Clustering y partitioning
├─ Z-ordering (Delta)
├─ Compaction de archivos pequeños

Paso 4: Conectar herramientas BI
├─ Tableau/Power BI sobre Lakehouse
├─ Crear vistas materializadas
└─ Habilitar SQL endpoint

Timeline típico: 3-6 meses
Risk: Bajo
Beneficio: Habilitar BI sin duplicar datos
    """)

with tab3:
    st.code("""
Enfoque Híbrido (mejor para muchos)

Arquitectura:
┌────────────┐
│  Sources   │
└─────┬──────┘
      ↓
┌─────────────────────────────────┐
│     Data Lakehouse (Unified)    │
│  ┌─────────┐  ┌──────────────┐ │
│  │   Raw   │→ │   Curated    │ │
│  │ (Bronze)│  │   (Silver)   │ │
│  └─────────┘  └───────┬──────┘ │
└────────────────────────┼────────┘
                         ↓
         ┌───────────────┴────────────────┐
         │                                │
    ┌────▼────┐                    ┌─────▼────┐
    │   DWH   │                    │ ML/Data  │
    │ (Legacy)│                    │ Science  │
    │         │                    │          │
    │ Reportes│                    │ Notebooks│
    │ críticos│                    │ Spark    │
    └─────────┘                    └──────────┘

Estrategia:
├─ Lakehouse para nuevos use cases
├─ DWH mantiene reportes críticos legacy
├─ Migración gradual según ROI
└─ Ambos coexisten largo plazo

Ventaja: Minimiza riesgo, maximiza beneficios
    """)

st.divider()

# --- Casos de Uso ---
st.subheader("🎯 Qué Usar Cuándo")

cases = {
    "Caso de Uso": [
        "Reportes ejecutivos (dashboards)",
        "KPIs y métricas de negocio",
        "Análisis financiero/compliance",
        "Machine Learning",
        "Exploración de datos (data scientists)",
        "Almacenamiento logs/clickstream",
        "Análisis en tiempo real",
        "Datos históricos (archiving)",
        "Análisis ad-hoc por analistas",
        "BI self-service"
    ],
    "🏢 DWH": ["✅ Ideal", "✅ Ideal", "✅ Ideal", "❌ No", "⚠️ Limitado", "❌ No", "❌ No", "✅ Sí", "✅ Sí", "✅ Ideal"],
    "🌊 Lake": ["❌ Lento", "❌ Lento", "⚠️ Posible", "✅ Ideal", "✅ Ideal", "✅ Ideal", "✅ Sí (Streaming)", "✅ Ideal", "✅ Sí", "❌ Difícil"],
    "🏠 Lakehouse": ["✅ Bien", "✅ Bien", "✅ Bien", "✅ Ideal", "✅ Ideal", "✅ Ideal", "✅ Sí", "✅ Ideal", "✅ Ideal", "✅ Bien"]
}

st.table(cases)

st.divider()

# --- Recomendación ---
st.subheader("💡 Recomendación Final")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    ### Elige DWH si...
    
    ✅ Tu organización es madura
    
    ✅ Datos son 100% estructurados
    
    ✅ BI/Reporting es el 90% de uso
    
    ✅ Performance crítico
    
    ✅ Ya tienes DWH y funciona bien
    
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
    ### Usa ambos (híbrido) si...
    
    ✅ Gran empresa con legacy
    
    ✅ No puedes migrar todo ya
    
    ✅ Riesgo debe ser mínimo
    
    ✅ Casos de uso muy diversos
    
    ✅ Transición gradual necesaria
    
    **Ejemplos:** Fortune 500 migrando
    """)

st.success("""
**💡 Tendencia 2025:**

El futuro es **Lakehouse** para la mayoría de organizaciones nuevas.  
Para empresas existentes, un **enfoque híbrido** minimiza riesgo mientras se moderniza.  
Data Warehouses tradicionales no desaparecen, pero su rol se especializa.
""")

st.divider()

