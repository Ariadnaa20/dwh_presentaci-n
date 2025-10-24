# pages/9_ventajas.py
import streamlit as st

st.set_page_config(page_title="Ventajas y Limitaciones", page_icon="⚖️", layout="wide")

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
    <div style='font-size: 4rem; margin-bottom: 20px;'>⚖️</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        Ventajas y Limitaciones del DWH
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Fortalezas, debilidades y cuándo usar un Data Warehouse
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
        Un <strong style='color: #fff;'>Data Warehouse</strong> no es una solución universal. Es importante entender tanto sus 
        <strong style='color: #fff;'>fortalezas</strong> como sus <strong style='color: #fff;'>limitaciones</strong> para tomar 
        decisiones arquitectónicas informadas.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# Ventajas
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>✅ Ventajas y Fortalezas</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.success("""
    ### 1️⃣ Separación de Análisis y Operaciones
    - Los sistemas OLTP no se sobrecargan
    - Análisis complejos sin impactar producción
    - Diferentes patrones de acceso optimizados
    
    ### 2️⃣ Datos Históricos y Trazabilidad
    - Mantiene historial completo (SCD)
    - Permite análisis de tendencias
    - Auditoría y compliance
    
    ### 3️⃣ Calidad y Consistencia
    - Datos limpios y validados (ETL)
    - Modelo único y coherente
    - "Single source of truth"
    """)

with col2:
    st.info("""
    ### 4️⃣ Rendimiento Optimizado
    - Diseñado para queries analíticas
    - Índices, particionamiento, compresión
    - Modelos dimensionales eficientes
    
    ### 5️⃣ Integración de Múltiples Fuentes
    - Combina datos de ERP, CRM, web
    - Vista 360° del negocio
    - Enriquecimiento de datos
    
    ### 6️⃣ Facilita Business Intelligence
    - Herramientas BI conectan fácilmente
    - Modelo dimensional intuitivo
    - Self-service analytics
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Limitaciones
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>❌ Limitaciones y Desafíos</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.error("""
    ### 1️⃣ Complejidad de Implementación
    - Requiere diseño cuidadoso
    - ETL complejos de desarrollar
    - Tiempo hasta valor (6-12 meses típico)
    
    ### 2️⃣ Costos Iniciales Altos
    - Inversión en infraestructura
    - Licencias software
    - Equipos especializados necesarios
    
    ### 3️⃣ Latencia de Datos
    - ETL típicamente batch (nocturno)
    - Datos no en tiempo real
    - Puede ser horas/días desactualizado
    """)

with col2:
    st.warning("""
    ### 4️⃣ Rigidez del Esquema
    - Cambios de esquema son costosos
    - Requiere rehacer ETL
    - Difícil para datos no estructurados
    
    ### 5️⃣ Mantenimiento Continuo
    - ETL fallan y necesitan monitoreo
    - Datos de calidad pobre en origen
    - Performance degradation
    
    ### 6️⃣ Duplicación de Datos
    - Copia datos desde fuentes
    - Mayor uso de storage
    - Sincronización necesaria
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Cuándo usar
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🤔 ¿Cuándo usar un DWH?</h2>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["✅ Usar DWH", "❌ No usar DWH"])

with tab1:
    st.success("""
    ### Situaciones donde un DWH es ideal
    
    **1. Análisis Histórico y Reporting:**
    - Necesitas analizar tendencias en años de datos
    - Reportes ejecutivos periódicos
    - Comparativas año sobre año
    
    **2. Integración de Múltiples Fuentes:**
    - Tienes 5+ sistemas que necesitas correlacionar
    - Necesitas vista única del cliente/producto
    
    **3. Business Intelligence:**
    - Dashboards para ejecutivos
    - Self-service analytics para analistas
    - KPIs estandarizados
    
    **4. Datos Estructurados:**
    - Ventas, inventario, finanzas, HR
    - Esquema relativamente estable
    
    **5. Rendimiento Crítico:**
    - Queries complejas sobre TB de datos
    - Usuarios concurrentes (100+)
    
    **💡 Ejemplos perfectos:**
    - Retail: Análisis de ventas, inventario
    - Banca: Análisis de riesgo, detección fraude
    - Salud: Análisis de pacientes, costos
    """)

with tab2:
    st.error("""
    ### Situaciones donde un DWH NO es adecuado
    
    **1. Datos en Tiempo Real:**
    - Necesitas latencia < 1 segundo
    - Trading, alertas críticas, IoT
    - → **Usar:** Stream processing (Kafka, Flink)
    
    **2. Datos No Estructurados:**
    - Logs, JSON variado, texto libre
    - Imágenes, videos, audio
    - → **Usar:** Data Lake (S3, ADLS) + Spark
    
    **3. Machine Learning en Desarrollo:**
    - Experimentación rápida con features
    - Modelos que requieren datos raw
    - → **Usar:** Data Lake + notebooks
    
    **4. Startup en Fase Temprana:**
    - Pocos datos (< 100GB)
    - Requisitos cambian semanalmente
    - Presupuesto limitado
    - → **Usar:** PostgreSQL + Metabase
    
    **5. Transacciones Operacionales:**
    - Necesitas UPDATE/DELETE frecuente
    - ACID transactions
    - → **Usar:** Base de datos OLTP
    """)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Matriz de decisión
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>📊 Matriz de Decisión</h2>
    <p style='color: #b8c5d6; font-size: 1.1rem;'>Evalúa tu situación</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.metric("Volumen de datos", "> 1TB", help="¿Más de 1TB de datos?")
    st.metric("Fuentes de datos", "> 5", help="¿Más de 5 sistemas?")
    st.metric("Usuarios analistas", "> 20", help="¿Más de 20 usuarios?")
    st.metric("Presupuesto anual", "> $100K", help="¿Más de $100K?")
    st.metric("Latencia aceptable", "> 1 hora", help="¿Datos pueden tener >1h retraso?")

with col2:
    st.info("""
    **Scoring:**
    
    - **5 SÍ:** DWH es probablemente necesario ✅
    - **3-4 SÍ:** DWH puede ser beneficioso ⚠️
    - **0-2 SÍ:** Considera alternativas más simples ❌
    
    **A favor de DWH:**
    - ✅ Industria regulada (banca, salud)
    - ✅ Necesidad de auditoría histórica
    - ✅ Múltiples departamentos necesitan datos
    - ✅ Reporting ejecutivo crítico
    
    **En contra de DWH:**
    - ❌ Startup en growth stage
    - ❌ Datos principalmente no estructurados
    - ❌ Necesidad de real-time (<1 min)
    - ❌ Presupuesto/recursos limitados
    """)

st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(167, 139, 250, 0.15) 0%, rgba(167, 139, 250, 0.05) 100%);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 40px;
    margin: 60px 0;
    border: 1px solid rgba(167, 139, 250, 0.3);
    text-align: center;
">
    <h3 style='color: #c4b5fd; margin-bottom: 20px; font-size: 1.8rem;'>💡 Recomendación Final</h3>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        Un Data Warehouse no es obsoleto, pero tampoco es la única solución. Evalúa tus necesidades, recursos y madurez 
        organizacional antes de decidir. Muchas veces, un <strong style='color: #fff;'>enfoque híbrido</strong> (Lake + Warehouse + Streaming) 
        es la mejor opción.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
