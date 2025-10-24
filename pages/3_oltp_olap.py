# pages/3_oltp_olap.py
import streamlit as st

st.set_page_config(page_title="OLTP vs OLAP", page_icon="⚖️", layout="wide")

# --- Header Glassmorphism ---
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
        OLTP vs OLAP
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Diferencias entre sistemas transaccionales y analíticos
    </p>
</div>
""", unsafe_allow_html=True)

# Introducción
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
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9; margin-bottom: 20px;'>
        En el mundo de la gestión de datos, es esencial distinguir entre <strong style='color: #ffffff; font-weight: 700;'>OLTP</strong> 
        (<em>Online Transaction Processing</em>) y <strong style='color: #ffffff; font-weight: 700;'>OLAP</strong> 
        (<em>Online Analytical Processing</em>).
    </p>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        Aunque ambos manejan información, tienen <strong style='color: #ffffff;'>objetivos y estructuras completamente diferentes</strong> 
        dentro de una organización.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# OLTP Section
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(66, 153, 225, 0.2) 0%, rgba(66, 153, 225, 0.05) 100%);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 45px;
    margin: 30px 0;
    border: 1px solid rgba(66, 153, 225, 0.4);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    <div style="display: flex; align-items: center; gap: 25px; margin-bottom: 30px;">
        <div style="font-size: 4rem;">🔹</div>
        <h2 style="color: #90cdf4; margin: 0; font-size: 2.5rem; font-weight: 700;">OLTP</h2>
    </div>
    <h3 style="color: #ffffff; margin-bottom: 20px; font-size: 1.8rem;">Online Transaction Processing</h3>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.8; margin-bottom: 30px;'>
        Los sistemas <strong style='color: #fff;'>OLTP</strong> se utilizan en el <strong style='color: #fff;'>día a día operativo</strong> 
        de las empresas. Están optimizados para manejar muchas transacciones pequeñas en tiempo real.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div style="
        background: rgba(66, 153, 225, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 30px;
        border: 1px solid rgba(66, 153, 225, 0.3);
        height: 100%;
    ">
        <h4 style="color: #90cdf4; margin-bottom: 20px; font-size: 1.4rem;">📦 Ejemplos Comunes</h4>
        <ul style="color: #d0dae8; font-size: 1.05rem; line-height: 2; list-style: none; padding-left: 0;">
            <li>🛒 Ventas en tiendas</li>
            <li>✈️ Reservas de vuelos</li>
            <li>💳 Pagos en línea</li>
            <li>📦 Control de inventario</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background: rgba(66, 153, 225, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 30px;
        border: 1px solid rgba(66, 153, 225, 0.3);
        height: 100%;
    ">
        <h4 style="color: #90cdf4; margin-bottom: 20px; font-size: 1.4rem;">⚙️ Características Clave</h4>
        <ul style="color: #d0dae8; font-size: 1.05rem; line-height: 2; list-style: none; padding-left: 0;">
            <li>⚡ Alta frecuencia de operaciones</li>
            <li>🔄 Datos <strong style='color: #fff;'>normalizados</strong></li>
            <li>🎯 Prioridad en rapidez y consistencia</li>
            <li>📝 Registra cada transacción individual</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.success("🎯 **Objetivo:** Registrar operaciones en tiempo real de forma eficiente y segura.")

st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

# OLAP Section
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(167, 139, 250, 0.2) 0%, rgba(167, 139, 250, 0.05) 100%);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 45px;
    margin: 30px 0;
    border: 1px solid rgba(167, 139, 250, 0.4);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    <div style="display: flex; align-items: center; gap: 25px; margin-bottom: 30px;">
        <div style="font-size: 4rem;">🔸</div>
        <h2 style="color: #c4b5fd; margin: 0; font-size: 2.5rem; font-weight: 700;">OLAP</h2>
    </div>
    <h3 style="color: #ffffff; margin-bottom: 20px; font-size: 1.8rem;">Online Analytical Processing</h3>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.8; margin-bottom: 30px;'>
        Los sistemas <strong style='color: #fff;'>OLAP</strong> se usan para <strong style='color: #fff;'>analizar grandes volúmenes 
        de datos históricos</strong> y generar conocimiento estratégico. A diferencia de OLTP, priorizan la velocidad en las 
        consultas analíticas sobre millones de registros.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div style="
        background: rgba(167, 139, 250, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 30px;
        border: 1px solid rgba(167, 139, 250, 0.3);
        height: 100%;
    ">
        <h4 style="color: #c4b5fd; margin-bottom: 20px; font-size: 1.4rem;">📊 Ejemplos Comunes</h4>
        <ul style="color: #d0dae8; font-size: 1.05rem; line-height: 2; list-style: none; padding-left: 0;">
            <li>📈 Análisis de ventas por región</li>
            <li>👥 Comportamiento de clientes</li>
            <li>📊 Indicadores de rendimiento (KPIs)</li>
            <li>📅 Comparativas anuales</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background: rgba(167, 139, 250, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 30px;
        border: 1px solid rgba(167, 139, 250, 0.3);
        height: 100%;
    ">
        <h4 style="color: #c4b5fd; margin-bottom: 20px; font-size: 1.4rem;">🧩 Características Clave</h4>
        <ul style="color: #d0dae8; font-size: 1.05rem; line-height: 2; list-style: none; padding-left: 0;">
            <li>📚 Datos <strong style='color: #fff;'>históricos y consolidados</strong></li>
            <li>⭐ Estructura <strong style='color: #fff;'>desnormalizada</strong></li>
            <li>🔍 Consultas <strong style='color: #fff;'>complejas y multidimensionales</strong></li>
            <li>🎯 Permite análisis predictivo y estratégico</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.info("🎯 **Objetivo:** Facilitar el análisis y la toma de decisiones empresariales.")

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Tabla Comparativa
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>⚖️ Comparativa Rápida</h2>
    <p style='color: #b8c5d6; font-size: 1.1rem;'>Las diferencias clave entre ambos sistemas</p>
</div>
""", unsafe_allow_html=True)

comparison_table = {
    "Característica": [
        "Propósito",
        "Tipo de datos",
        "Transacciones",
        "Estructura",
        "Ejemplo típico",
        "Usuarios",
        "Volumen",
        "Actualizaciones"
    ],
    "OLTP 🧾": [
        "Operaciones diarias",
        "Actual y detallado",
        "Muchas, pequeñas y rápidas",
        "Normalizada",
        "Registro de ventas",
        "Operadores, cajeros",
        "Miles/millones de transacciones",
        "Continuas (INSERT, UPDATE, DELETE)"
    ],
    "OLAP 📈": [
        "Análisis y decisiones",
        "Histórico y resumido",
        "Pocas, pero complejas",
        "Desnormalizada",
        "Reporte de ventas mensuales",
        "Analistas, ejecutivos",
        "Millones/billones de registros históricos",
        "Periódicas (batch)"
    ]
}

st.table(comparison_table)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Relación entre OLTP y OLAP
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🔗 Relación entre OLTP y OLAP</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 40px;
    margin: 30px 0;
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9; margin-bottom: 20px;'>
        Los <strong style='color: #ffffff;'>sistemas OLTP alimentan los Data Warehouse (DWH)</strong>, que luego son la base 
        de los entornos <strong style='color: #ffffff;'>OLAP</strong>.
    </p>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        Esta separación garantiza un <strong style='color: #ffffff;'>rendimiento óptimo</strong>:
    </p>
    <ul style='color: #b8c5d6; font-size: 1.05rem; line-height: 2; margin-top: 20px; list-style: none; padding-left: 0;'>
        <li>✅ Los sistemas operativos no se ven afectados por consultas analíticas</li>
        <li>✅ Los datos se transforman y consolidan antes del análisis</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Diagrama de flujo
st.code("""
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│  OLTP Systems   │         │   Data Warehouse │         │  OLAP Systems   │
│                 │         │       (DWH)      │         │                 │
│  🏪 Ventas      │  ═════> │                  │  ═════> │  📊 Analytics   │
│  🛒 Inventario  │  ETL    │  📦 Consolidado  │  Query  │  📈 Reports     │
│  💳 Pagos       │         │  🧹 Limpio       │         │  🎯 Dashboards  │
│  ✈️ Reservas    │         │  📅 Histórico    │         │  🔍 BI Tools    │
└─────────────────┘         └──────────────────┘         └─────────────────┘
   (Operacional)              (Almacenamiento)              (Analítico)
""", language="text")

st.caption("📌 Los datos fluyen desde sistemas operativos (OLTP) → Data Warehouse → Análisis (OLAP)")

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
