# pages/4_arquitectura.py
import streamlit as st

st.set_page_config(page_title="Arquitectura DWH", page_icon="🏗️", layout="wide")

st.markdown("<h1 style='text-align:center; color:#ffffff;'>🏗️ Arquitectura de un Data Warehouse</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Capas y componentes de una arquitectura DWH completa</p>", unsafe_allow_html=True)

st.divider()

# --- Introducción ---
st.subheader("📝 Introducción")
st.write("""
La arquitectura de un **Data Warehouse** se compone de múltiples capas que trabajan en conjunto para 
extraer, transformar, almacenar y presentar datos de manera eficiente. Cada capa tiene un propósito específico
en el flujo de datos desde las fuentes hasta los usuarios finales.
""")

st.divider()

# --- Capas principales ---
st.subheader("🔷 Capas de la Arquitectura")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **1️⃣ Capa de Fuentes de Datos**
    - Sistemas operacionales (ERP, CRM)
    - Bases de datos transaccionales
    - Archivos externos (CSV, JSON, XML)
    - APIs y servicios web
    - Aplicaciones legacy
    """)
    
    st.success("""
    **2️⃣ Capa de Staging (Preparación)**
    - Área temporal de almacenamiento
    - Datos en formato crudo
    - Mínima transformación
    - Punto de recuperación ante errores
    """)
    
    st.warning("""
    **3️⃣ Capa ETL/ELT**
    - Extracción de datos
    - Transformación y limpieza
    - Validación de calidad
    - Carga al DWH
    """)

with col2:
    st.info("""
    **4️⃣ Capa de Almacenamiento**
    - Data Warehouse central
    - Data Marts departamentales
    - Modelos dimensionales
    - Datos históricos agregados
    """)
    
    st.success("""
    **5️⃣ Capa de Presentación**
    - Herramientas de BI
    - Reportes y dashboards
    - Consultas OLAP
    - Análisis ad-hoc
    """)
    
    st.warning("""
    **6️⃣ Capa de Metadatos**
    - Diccionario de datos
    - Linaje de datos
    - Reglas de negocio
    - Documentación técnica
    """)

st.divider()

# --- Tipos de Arquitectura ---
st.subheader("🏛️ Tipos de Arquitectura DWH")

tab1, tab2, tab3 = st.tabs(["📦 Arquitectura de 1 Capa", "📦📦 Arquitectura de 2 Capas", "📦📦📦 Arquitectura de 3 Capas"])

with tab1:
    st.markdown("""
    ### Arquitectura de Una Capa
    - **Descripción:** DWH y fuentes operacionales en el mismo sistema
    - **Ventajas:** 
        - Simple y económica
        - Fácil de implementar
    - **Desventajas:**
        - No separa operaciones de análisis
        - Impacta rendimiento de sistemas transaccionales
        - **❌ Raramente recomendada en producción**
    """)

with tab2:
    st.markdown("""
    ### Arquitectura de Dos Capas
    - **Descripción:** Separa fuentes de datos del DWH
    - **Componentes:**
        - Capa 1: Fuentes de datos
        - Capa 2: DWH + Herramientas BI
    - **Ventajas:**
        - Separa análisis de operaciones
        - Mejor rendimiento
    - **Desventajas:**
        - Sin área de staging
        - Dificultad en recuperación de errores
    """)

with tab3:
    st.markdown("""
    ### Arquitectura de Tres Capas (Más común)
    - **Descripción:** Arquitectura estándar de DWH empresarial
    - **Componentes:**
        - Capa 1: Fuentes de datos
        - Capa 2: Staging + DWH Central
        - Capa 3: Data Marts + BI Tools
    - **Ventajas:**
        - ✅ Máxima flexibilidad
        - ✅ Mejor manejo de errores
        - ✅ Escalable y mantenible
        - ✅ Separación clara de responsabilidades
    """)

st.divider()

# --- Componentes clave ---
with st.expander("🔧 Componentes Clave de la Arquitectura"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🗄️ Repositorio de Datos:**
        - Base de datos central
        - Almacenamiento optimizado para consultas
        - Particionamiento y clustering
        - Compresión de datos
        
        **🔄 Proceso ETL/ELT:**
        - Herramientas de integración
        - Orquestadores de workflows
        - Monitoreo y logging
        - Manejo de errores
        """)
    
    with col2:
        st.markdown("""
        **📊 Herramientas de Acceso:**
        - Reportes predefinidos
        - Dashboards interactivos
        - Consultas SQL directas
        - Análisis OLAP (cubos)
        
        **🔐 Seguridad y Gobernanza:**
        - Control de acceso
        - Encriptación de datos
        - Auditoría y compliance
        - Gestión de metadatos
        """)

st.divider()

# --- Ejemplo visual ---
st.subheader("🎯 Flujo de Datos en la Arquitectura")

st.markdown("""
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Fuentes    │ --> │   Staging   │ --> │     DWH     │ --> │  Data Marts │
│  de Datos   │     │    Area     │     │   Central   │     │  + BI Tools │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
      │                    │                    │                    │
   ERP, CRM          Datos Crudos         Datos Integrados    Análisis BI
   Archivos          Sin transformar      Modelos Dim.        Reportes
   APIs              Temporal             Histórico           Dashboards
```
""")

st.divider()

# --- Consideraciones ---
st.subheader("💡 Consideraciones de Diseño")

col1, col2 = st.columns(2)

col1.info("""
**Escalabilidad:**
- Diseño modular y extensible
- Capacidad de crecimiento horizontal
- Optimización de recursos
""")

col2.success("""
**Rendimiento:**
- Particionamiento de tablas
- Índices y estadísticas
- Consultas optimizadas
""")

col1.warning("""
**Disponibilidad:**
- Redundancia de componentes
- Backups automáticos
- Plan de recuperación ante desastres
""")

col2.error("""
**Mantenimiento:**
- Documentación completa
- Monitoreo proactivo
- Procesos automatizados
""")

st.divider()

# --- Arquitecturas Modernas ---
with st.expander("☁️ Arquitecturas Modernas en la Nube"):
    st.write("""
    Las arquitecturas DWH modernas aprovechan servicios en la nube para mayor flexibilidad:
    
    **AWS:**
    - Amazon Redshift (DWH)
    - AWS Glue (ETL)
    - Amazon S3 (Staging/Data Lake)
    
    **Azure:**
    - Azure Synapse Analytics
    - Azure Data Factory
    - Azure Data Lake Storage
    
    **Google Cloud:**
    - BigQuery (DWH serverless)
    - Cloud Dataflow (ETL)
    - Cloud Storage
    
    **Ventajas Cloud:**
    - Escalabilidad elástica
    - Pago por uso
    - Mantenimiento reducido
    - Alta disponibilidad
    """)

st.divider()

