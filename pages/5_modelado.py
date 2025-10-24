# pages/5_modelado.py
import streamlit as st

st.set_page_config(page_title="Modelado Dimensional", page_icon="⭐", layout="wide")

st.markdown("<h1 style='text-align:center; color:#ffffff;'>⭐ Modelado Dimensional</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Esquema Estrella, Copo de Nieve y técnicas de modelado</p>", unsafe_allow_html=True)

st.divider()

# --- Introducción ---
st.subheader("📝 ¿Qué es el Modelado Dimensional?")
st.write("""
El **modelado dimensional** es una técnica de diseño de bases de datos optimizada para consultas y análisis
en Data Warehouses. A diferencia de la normalización tradicional, prioriza la **simplicidad de consultas** 
y el **rendimiento analítico** sobre la eficiencia de almacenamiento.
""")

st.divider()

# --- Conceptos Básicos ---
st.subheader("🎯 Conceptos Fundamentales")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **📊 Tabla de Hechos (Fact Table)**
    
    Contiene las **métricas cuantitativas** del negocio:
    - Ventas, ingresos, cantidades
    - Eventos o transacciones
    - Medidas numéricas agregables
    - Claves foráneas a dimensiones
    
    **Características:**
    - ✅ Muchas filas (millones/billones)
    - ✅ Pocas columnas
    - ✅ Principalmente valores numéricos
    - ✅ Actualizaciones frecuentes
    """)

with col2:
    st.success("""
    **🔷 Tablas de Dimensiones (Dimension Tables)**
    
    Contienen **información descriptiva** del contexto:
    - Quién, qué, cuándo, dónde, por qué, cómo
    - Atributos textuales
    - Categorías y jerarquías
    - Datos de referencia
    
    **Características:**
    - ✅ Menos filas que hechos
    - ✅ Muchas columnas descriptivas
    - ✅ Principalmente texto
    - ✅ Actualizaciones menos frecuentes
    """)

st.divider()

# --- Esquema Estrella ---
st.subheader("⭐ Esquema Estrella (Star Schema)")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    El **esquema estrella** es el modelo dimensional más común y simple:
    
    **Estructura:**
    - Una tabla de hechos central
    - Múltiples tablas de dimensiones conectadas directamente
    - Las dimensiones NO están normalizadas
    - Forma visual de estrella
    
    **Ventajas:**
    - ✅ Consultas simples y rápidas
    - ✅ Fácil de entender para usuarios
    - ✅ Mejor rendimiento de consultas
    - ✅ Menos JOINs necesarios
    
    **Desventajas:**
    - ⚠️ Redundancia de datos en dimensiones
    - ⚠️ Mayor espacio de almacenamiento
    """)

with col2:
    st.code("""
    Ejemplo Ventas:
    
         Tiempo
           |
    Cliente - VENTAS - Producto
           |
        Tienda
        
    VENTAS (Hechos):
    - fecha_id
    - cliente_id
    - producto_id
    - tienda_id
    - cantidad
    - importe
    """)

st.divider()

# --- Esquema Copo de Nieve ---
st.subheader("❄️ Esquema Copo de Nieve (Snowflake Schema)")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    El **esquema copo de nieve** es una variación normalizada del esquema estrella:
    
    **Estructura:**
    - Tabla de hechos central
    - Dimensiones normalizadas en múltiples tablas
    - Jerarquías explícitas
    - Forma visual de copo de nieve
    
    **Ventajas:**
    - ✅ Menor redundancia de datos
    - ✅ Menos espacio de almacenamiento
    - ✅ Mejor integridad referencial
    - ✅ Mantenimiento más sencillo de jerarquías
    
    **Desventajas:**
    - ⚠️ Consultas más complejas
    - ⚠️ Más JOINs = Menor rendimiento
    - ⚠️ Más difícil de entender
    """)

with col2:
    st.code("""
    Ejemplo Normalizado:
    
    Año - Mes - Día
              |
           VENTAS - Categoría
              |         |
          Producto   Subcategoría
    
    Más niveles de
    normalización en
    las dimensiones
    """)

st.divider()

# --- Comparativa ---
st.subheader("⚖️ Estrella vs Copo de Nieve")

comparison_data = {
    "Característica": ["Complejidad", "Rendimiento", "Espacio", "Mantenimiento", "Comprensión", "JOINs"],
    "⭐ Estrella": ["Simple", "Alto", "Más espacio", "Fácil", "Intuitivo", "Pocos"],
    "❄️ Copo Nieve": ["Compleja", "Medio", "Menos espacio", "Complejo", "Técnico", "Muchos"]
}

st.table(comparison_data)

st.divider()

# --- Tipos de Tablas de Hechos ---
st.subheader("📊 Tipos de Tablas de Hechos")

tab1, tab2, tab3 = st.tabs(["📝 Transaccionales", "📸 Snapshot", "📈 Acumulativas"])

with tab1:
    st.markdown("""
    ### Tablas de Hechos Transaccionales
    
    **Descripción:** Registran eventos individuales en el momento que ocurren.
    
    **Características:**
    - Una fila por transacción
    - Grano más detallado
    - Crece continuamente
    
    **Ejemplo - Ventas:**
    | fecha_id | producto_id | cliente_id | cantidad | precio |
    |----------|-------------|------------|----------|--------|
    | 20250124 | 101         | 5001       | 2        | 49.99  |
    | 20250124 | 102         | 5002       | 1        | 89.99  |
    
    **Casos de uso:**
    - Ventas por ticket
    - Transacciones bancarias
    - Clicks en website
    """)

with tab2:
    st.markdown("""
    ### Tablas de Hechos Snapshot (Instantáneas)
    
    **Descripción:** Capturan el estado en momentos específicos del tiempo.
    
    **Características:**
    - Una fila por período
    - Registro periódico (diario, mensual)
    - Tamaño predecible
    
    **Ejemplo - Inventario Diario:**
    | fecha_id | producto_id | almacen_id | stock | valor |
    |----------|-------------|------------|-------|-------|
    | 20250124 | 101         | 1          | 150   | 7500  |
    | 20250125 | 101         | 1          | 145   | 7250  |
    
    **Casos de uso:**
    - Saldo de cuentas bancarias
    - Niveles de inventario
    - Estado de procesos
    """)

with tab3:
    st.markdown("""
    ### Tablas de Hechos Acumulativas
    
    **Descripción:** Siguen un proceso con múltiples etapas a lo largo del tiempo.
    
    **Características:**
    - Una fila por proceso
    - Se actualiza a medida que progresa
    - Múltiples fechas por fila
    
    **Ejemplo - Procesamiento de Pedidos:**
    | pedido_id | fecha_pedido | fecha_envio | fecha_entrega | días_envío |
    |-----------|--------------|-------------|---------------|------------|
    | 1001      | 2025-01-20   | 2025-01-22  | 2025-01-24    | 4          |
    
    **Casos de uso:**
    - Pipeline de ventas
    - Procesamiento de pedidos
    - Ciclo de vida de productos
    """)

st.divider()

# --- Granularidad ---
with st.expander("🔍 Granularidad de los Hechos"):
    st.write("""
    La **granularidad** define el nivel de detalle de las mediciones en la tabla de hechos.
    
    **Niveles comunes:**
    
    1. **Grano Atómico (Más detallado):**
       - Una fila por transacción individual
       - Ejemplo: Cada producto en cada ticket de venta
       - ✅ Máxima flexibilidad de análisis
       - ⚠️ Mayor volumen de datos
    
    2. **Grano Agregado:**
       - Una fila por grupo o período
       - Ejemplo: Ventas totales por día y producto
       - ✅ Menos espacio
       - ⚠️ Pierde detalle para análisis específicos
    
    **Recomendación:** 
    Siempre diseñar al **grano más atómico posible** y crear agregaciones cuando sea necesario.
    """)

st.divider()

# --- Dimensiones Especiales ---
st.subheader("🎭 Dimensiones Especiales")

col1, col2 = st.columns(2)

with col1:
    st.warning("""
    **📅 Dimensión Tiempo**
    - La más importante
    - Presente en casi todos los modelos
    - Contiene: fecha, día semana, mes, trimestre, año
    - Facilita análisis temporales
    - Incluye festivos y períodos fiscales
    """)
    
    st.info("""
    **🔢 Dimensión Degenerada**
    - Atributo dimensional sin tabla propia
    - Se almacena en la tabla de hechos
    - Ejemplo: Número de ticket, ID de pedido
    - Útil para referencias únicas
    """)

with col2:
    st.success("""
    **⚙️ Dimensión Conformada**
    - Compartida entre múltiples tablas de hechos
    - Significado consistente en todo el DWH
    - Ejemplo: Dimensión Cliente usada en Ventas y Soporte
    - Permite análisis cruzado (drill-across)
    """)
    
    st.error("""
    **👻 Dimensión Junk (Basura)**
    - Agrupa indicadores y flags de baja cardinalidad
    - Evita muchas columnas booleanas en hechos
    - Ejemplo: Tipo envío, método pago, indicadores varios
    - Reduce tamaño de tabla de hechos
    """)

st.divider()

# --- Ejemplo Práctico ---
with st.expander("💡 Ejemplo Completo: Sistema de Ventas Retail"):
    st.markdown("""
    ### Modelo Estrella para Ventas
    
    **Tabla de Hechos - VENTAS:**
    ```sql
    CREATE TABLE fact_ventas (
        fecha_id INT,
        producto_id INT,
        cliente_id INT,
        tienda_id INT,
        promocion_id INT,
        cantidad INT,
        importe_venta DECIMAL(10,2),
        descuento DECIMAL(10,2),
        costo DECIMAL(10,2),
        beneficio DECIMAL(10,2)
    );
    ```
    
    **Dimensiones:**
    
    **dim_tiempo:** fecha, día_semana, mes, trimestre, año, festivo
    
    **dim_producto:** id, nombre, categoría, marca, precio_base
    
    **dim_cliente:** id, nombre, edad, género, ciudad, segmento
    
    **dim_tienda:** id, nombre, dirección, región, tamaño
    
    **dim_promocion:** id, nombre, tipo, descuento_pct
    
    **Consulta de ejemplo:**
    ```sql
    SELECT 
        t.año,
        t.mes,
        p.categoria,
        SUM(v.importe_venta) as ventas_totales,
        SUM(v.cantidad) as unidades_vendidas
    FROM fact_ventas v
    JOIN dim_tiempo t ON v.fecha_id = t.id
    JOIN dim_producto p ON v.producto_id = p.id
    WHERE t.año = 2025
    GROUP BY t.año, t.mes, p.categoria;
    ```
    """)

st.divider()

