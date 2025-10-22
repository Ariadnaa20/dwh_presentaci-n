import streamlit as st

# 🌐 Título principal
st.title("⚙️ OLTP vs OLAP")

st.write("""
En el mundo de la gestión de datos, es esencial distinguir entre **OLTP** (*Online Transaction Processing*) y **OLAP** (*Online Analytical Processing*).  
Aunque ambos manejan información, tienen **objetivos y estructuras completamente diferentes** dentro de una organización.
""")

st.divider()

# 🧩 Sección 1: OLTP
st.subheader("🔹 OLTP — Online Transaction Processing")

st.write("""
Los sistemas **OLTP** se utilizan en el **día a día operativo** de las empresas.  
Están optimizados para manejar muchas transacciones pequeñas en tiempo real.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **📦 Ejemplos comunes:**
    - Ventas en tiendas
    - Reservas de vuelos
    - Pagos en línea
    - Control de inventario
    """)

with col2:
    st.markdown("""
    **⚙️ Características clave:**
    - Alta frecuencia de operaciones  
    - Datos **normalizados** para evitar duplicidades  
    - Prioridad en **rapidez y consistencia**  
    - Registra cada transacción individual  
    """)

st.success("🎯 Objetivo: Registrar operaciones en tiempo real de forma eficiente y segura.")

st.divider()

# 🧠 Sección 2: OLAP
st.subheader("🔸 OLAP — Online Analytical Processing")

st.write("""
Los sistemas **OLAP** se usan para **analizar grandes volúmenes de datos históricos** y generar conocimiento estratégico.  
A diferencia de OLTP, priorizan la velocidad en las consultas analíticas sobre millones de registros.
""")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    **📊 Ejemplos comunes:**
    - Análisis de ventas por región  
    - Comportamiento de clientes  
    - Indicadores de rendimiento (KPIs)  
    - Comparativas anuales  
    """)

with col4:
    st.markdown("""
    **🧩 Características clave:**
    - Datos **históricos y consolidados**  
    - Estructura **desnormalizada** (modelo estrella o copo de nieve)  
    - Consultas **complejas y multidimensionales**  
    - Permite análisis predictivo y estratégico  
    """)

st.info("🎯 Objetivo: Facilitar el análisis y la toma de decisiones empresariales.")

st.divider()

# 📊 Tabla comparativa
st.subheader("⚖️ Comparativa rápida")

st.markdown("""
| **Característica**      | **OLTP** 🧾 | **OLAP** 📈 |
|--------------------------|--------------|--------------|
| Propósito                | Operaciones diarias | Análisis y decisiones |
| Tipo de datos            | Actual y detallado | Histórico y resumido |
| Transacciones            | Muchas, pequeñas y rápidas | Pocas, pero complejas |
| Estructura               | Normalizada | Desnormalizada |
| Ejemplo típico           | Registro de ventas | Reporte de ventas mensuales |
""")

st.divider()

# 🔄 Conexión
st.subheader("🔗 Relación entre OLTP y OLAP")

st.write("""
Los **sistemas OLTP alimentan los Data Warehouse (DWH)**, que luego son la base de los entornos **OLAP**.  
Esta separación garantiza un **rendimiento óptimo**:  
- Los sistemas operativos no se ven afectados por consultas analíticas.  
- Los datos se transforman y consolidan antes del análisis.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/8/88/OLTP_OLAP_diagram_en.png", caption="Esquema simplificado de la relación OLTP ↔ OLAP", use_container_width=True)

st.divider()

