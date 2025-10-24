# pages/8_rendimento.py
import streamlit as st

st.set_page_config(page_title="Rendimiento DWH", page_icon="⚡", layout="wide")

st.markdown("<h1 style='text-align:center; color:#1e3d8f;'>⚡ Optimización de Rendimiento</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Particiones, índices y técnicas para acelerar consultas</p>", unsafe_allow_html=True)

st.divider()

# --- Introducción ---
st.subheader("📝 ¿Por qué es crucial el rendimiento en DWH?")
st.write("""
Un **Data Warehouse** puede contener **terabytes o petabytes** de datos. Sin optimización adecuada,
las consultas pueden tardar horas en ejecutarse. Las técnicas de optimización son esenciales para:
- Respuestas en segundos vs horas
- Experiencia de usuario ágil
- Reducción de costos de compute
- Escalabilidad sostenible
""")

st.divider()

# --- Técnicas Principales ---
st.subheader("🎯 Técnicas Principales de Optimización")

# Particionamiento
with st.expander("📂 Particionamiento (Partitioning)"):
    st.markdown("""
    ### ¿Qué es el Particionamiento?
    
    **Particionamiento** divide una tabla grande en fragmentos más pequeños basados en valores de columnas específicas.
    Cada partición se almacena y gestiona independientemente.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Tipos de Particionamiento:**
        
        **1. Particionamiento por Rango (Range Partitioning)**
        - Más común en DWH
        - Basado en fechas típicamente
        - Ejemplo: Una partición por día/mes/año
        
        **2. Particionamiento por Lista (List Partitioning)**
        - Basado en valores discretos
        - Ejemplo: Por país, región, categoría
        
        **3. Particionamiento por Hash**
        - Distribución uniforme
        - Útil para balanceo de carga
        
        **4. Particionamiento Compuesto**
        - Combina múltiples estrategias
        - Ejemplo: Por año + por región
        """)
    
    with col2:
        st.code("""
-- Ejemplo PostgreSQL
CREATE TABLE ventas (
    fecha DATE,
    producto_id INT,
    cantidad INT,
    importe DECIMAL
)
PARTITION BY RANGE (fecha);

-- Particiones mensuales
CREATE TABLE ventas_2024_01
PARTITION OF ventas
FOR VALUES FROM ('2024-01-01') 
TO ('2024-02-01');

CREATE TABLE ventas_2024_02
PARTITION OF ventas
FOR VALUES FROM ('2024-02-01') 
TO ('2024-03-01');
        """, language="sql")
    
    st.success("""
    **Ventajas del Particionamiento:**
    
    ✅ **Partition Pruning:** Solo escanea particiones relevantes
    - Query: `WHERE fecha = '2024-01-15'` → Solo escanea partición enero
    - Mejora rendimiento 10x-100x en queries con filtros de fecha
    
    ✅ **Mantenimiento más fácil:**
    - Eliminar datos antiguos: DROP partition (instantáneo vs DELETE lento)
    - Backup/restore por partición
    
    ✅ **Paralelismo:**
    - Consultas pueden ejecutarse en paralelo por partición
    
    ✅ **Gestión de almacenamiento:**
    - Particiones antiguas en storage más barato
    - Compresión diferenciada
    """)
    
    st.warning("""
    **Consideraciones:**
    
    ⚠️ Elegir columna de partición correcta (usualmente fecha)
    
    ⚠️ Demasiadas particiones = overhead de metadatos
    
    ⚠️ Consultas sin filtro de partición escanean todo
    """)

# Índices
with st.expander("🔍 Índices (Indexes)"):
    st.markdown("""
    ### Índices en Data Warehouses
    
    **Índices** aceleran búsquedas al crear estructuras de datos auxiliares que permiten acceso rápido.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Tipos de Índices:**
        
        **1. B-Tree Index (Tradicional)**
        - Para búsquedas exactas y rangos
        - Útil en dimensiones
        - WHERE, JOIN, ORDER BY
        
        **2. Bitmap Index**
        - Ideal para DWH
        - Columnas con baja cardinalidad
        - Muy eficiente para AND/OR/NOT
        - Ejemplo: género (M/F), estado (activo/inactivo)
        
        **3. Columnstore Index**
        - Almacenamiento columnar
        - Compresión excelente
        - Perfecto para agregaciones
        - Usado en SQL Server, Synapse
        
        **4. Covering Index**
        - Incluye todas las columnas necesarias
        - Evita acceso a tabla principal
        - Index-only scan
        """)
    
    with col2:
        st.code("""
-- B-Tree index
CREATE INDEX idx_cliente_id 
ON fact_ventas(cliente_id);

-- Bitmap index (Oracle)
CREATE BITMAP INDEX idx_estado 
ON dim_cliente(estado);

-- Columnstore (SQL Server)
CREATE COLUMNSTORE INDEX idx_cs_ventas
ON fact_ventas;

-- Covering index
CREATE INDEX idx_fecha_producto_amount
ON fact_ventas(fecha, producto_id)
INCLUDE (cantidad, importe);
        """, language="sql")
    
    st.info("""
    **Cuándo usar índices:**
    
    ✅ Columnas frecuentemente en WHERE
    
    ✅ Columnas de JOIN
    
    ✅ Dimensiones (tablas pequeñas)
    
    ✅ Claves foráneas en tablas de hechos
    
    **Cuándo NO usar índices:**
    
    ❌ Tablas de hechos con full table scans frecuentes
    
    ❌ Columnas que cambian constantemente
    
    ❌ Índices que no se usan (overhead en writes)
    """)

# Clustering
with st.expander("🗂️ Clustering (Ordenamiento físico)"):
    st.markdown("""
    ### Clustering Keys
    
    **Clustering** ordena físicamente los datos en disco según columnas específicas.
    Similar a particionamiento pero más granular.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Cómo funciona:**
        - Los datos se ordenan físicamente en storage
        - Mejora la localidad de datos
        - Reduce I/O al leer datos relacionados
        
        **Especialmente útil en:**
        - Snowflake (micro-partitions automáticas)
        - BigQuery (clustering columns)
        - Redshift (sort keys)
        
        **Beneficios:**
        - Partition pruning más efectivo
        - Compresión mejorada (datos similares juntos)
        - Queries con filtros más rápidas
        """)
    
    with col2:
        st.code("""
-- Snowflake
CREATE TABLE ventas (
    fecha DATE,
    region VARCHAR,
    importe NUMBER
)
CLUSTER BY (fecha, region);

-- BigQuery
CREATE TABLE `project.dataset.ventas`
PARTITION BY DATE(fecha)
CLUSTER BY region, categoria;

-- Redshift
CREATE TABLE ventas (
    fecha DATE,
    producto_id INT,
    importe DECIMAL
)
SORTKEY (fecha, producto_id);
        """, language="sql")

# Compresión
with st.expander("📦 Compresión de Datos"):
    st.markdown("""
    ### Compresión en Data Warehouses
    
    **Compresión** reduce el tamaño de almacenamiento y mejora rendimiento (menos I/O).
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Tipos de Compresión:**
        
        **1. Row-level Compression**
        - Comprime filas completas
        - GZIP, LZ4, Snappy
        - Bueno para storage, malo para queries selectivas
        
        **2. Columnar Compression**
        - Comprime cada columna independientemente
        - Mucho más eficiente (valores similares juntos)
        - Dictionary encoding, Run-length encoding
        
        **3. Dictionary Encoding**
        - Sustituye valores repetidos por códigos
        - Perfecto para strings con baja cardinalidad
        - Ejemplo: "España" → 1, "Francia" → 2
        
        **4. Run-Length Encoding (RLE)**
        - Almacena (valor, cuenta) en vez de repetir
        - Ideal para columnas ordenadas
        - Ejemplo: [A,A,A,A,B,B] → [(A,4), (B,2)]
        """)
    
    with col2:
        st.success("""
        **Ratios de Compresión típicos:**
        
        📊 Sin compresión: 1:1
        
        📊 Row compression: 2-3:1
        
        📊 Columnar compression: 5-10:1
        
        📊 Columnar + ordenamiento: 10-50:1
        
        **Beneficios:**
        
        ✅ Menos storage (cost savings)
        
        ✅ Menos I/O → queries más rápidas
        
        ✅ Más datos en memoria caché
        
        ✅ Transferencia de red más rápida
        """)

# Materialización
with st.expander("💾 Vistas Materializadas (Materialized Views)"):
    st.markdown("""
    ### Vistas Materializadas
    
    **Vistas Materializadas** pre-calculan y almacenan resultados de queries complejas.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Diferencia con vistas normales:**
        
        | Aspecto | Vista Normal | Vista Materializada |
        |---------|--------------|---------------------|
        | Almacenamiento | Solo definición SQL | Resultados físicos |
        | Rendimiento | Ejecuta query cada vez | Instantáneo |
        | Actualización | Siempre actual | Requiere refresh |
        | Uso de espacio | Mínimo | Duplica datos |
        
        **Cuándo usar:**
        - Queries complejas ejecutadas frecuentemente
        - Agregaciones pesadas (SUM, AVG, COUNT)
        - JOINs de muchas tablas
        - Reportes ejecutivos diarios/semanales
        
        **Estrategias de Refresh:**
        - **COMPLETE:** Reconstruye todo
        - **FAST:** Solo cambios incrementales
        - **ON DEMAND:** Manual
        - **ON COMMIT:** Automático (OLTP)
        - **SCHEDULED:** Cada X horas/días
        """)
    
    with col2:
        st.code("""
-- Crear vista materializada
CREATE MATERIALIZED VIEW mv_ventas_mensuales
AS
SELECT 
    DATE_TRUNC('month', fecha) as mes,
    producto_id,
    SUM(cantidad) as total_cantidad,
    SUM(importe) as total_importe,
    COUNT(*) as num_transacciones
FROM fact_ventas
GROUP BY 1, 2;

-- Refresh
REFRESH MATERIALIZED VIEW 
mv_ventas_mensuales;

-- Con índice
CREATE INDEX idx_mv_mes_producto
ON mv_ventas_mensuales(mes, producto_id);
        """, language="sql")

st.divider()

# --- Optimización de Queries ---
st.subheader("🔬 Optimización de Queries SQL")

tab1, tab2, tab3 = st.tabs(["❌ Antipatrones", "✅ Buenas Prácticas", "📊 Ejemplo Optimización"])

with tab1:
    st.markdown("""
    ### Antipatrones comunes que matan el rendimiento
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. SELECT * en tablas grandes**
        ```sql
        -- MAL ❌
        SELECT * FROM fact_ventas;
        
        -- BIEN ✅
        SELECT fecha, producto_id, importe 
        FROM fact_ventas;
        ```
        
        **2. Funciones en WHERE sobre columnas indexadas**
        ```sql
        -- MAL ❌ (no usa índice)
        SELECT * FROM ventas 
        WHERE YEAR(fecha) = 2024;
        
        -- BIEN ✅ (usa índice)
        SELECT * FROM ventas 
        WHERE fecha >= '2024-01-01' 
          AND fecha < '2025-01-01';
        ```
        
        **3. OR en vez de IN**
        ```sql
        -- MAL ❌
        WHERE pais = 'España' 
           OR pais = 'Francia' 
           OR pais = 'Italia';
        
        -- BIEN ✅
        WHERE pais IN ('España', 'Francia', 'Italia');
        ```
        """)
    
    with col2:
        st.error("""
        **4. Subconsultas correlacionadas**
        ```sql
        -- MAL ❌ (ejecuta subquery por cada fila)
        SELECT c.nombre,
            (SELECT SUM(importe) FROM ventas v 
             WHERE v.cliente_id = c.cliente_id)
        FROM clientes c;
        
        -- BIEN ✅ (un solo scan)
        SELECT c.nombre, SUM(v.importe)
        FROM clientes c
        LEFT JOIN ventas v ON c.cliente_id = v.cliente_id
        GROUP BY c.nombre;
        ```
        
        **5. DISTINCT innecesario**
        ```sql
        -- MAL ❌ (sort caro)
        SELECT DISTINCT cliente_id FROM ventas;
        
        -- BIEN ✅ (si ya es único)
        SELECT cliente_id FROM ventas 
        GROUP BY cliente_id;
        ```
        
        **6. COUNT(*) cuando solo necesitas EXISTS**
        ```sql
        -- MAL ❌
        IF (SELECT COUNT(*) FROM ventas 
            WHERE cliente_id = 123) > 0
        
        -- BIEN ✅
        IF EXISTS (SELECT 1 FROM ventas 
                   WHERE cliente_id = 123 LIMIT 1)
        ```
        """)

with tab2:
    st.markdown("""
    ### Buenas prácticas para queries rápidas
    """)
    
    st.success("""
    **1. Usa columnas de partición en WHERE**
    ```sql
    SELECT * FROM ventas
    WHERE fecha BETWEEN '2024-01-01' AND '2024-01-31'  -- Partition pruning
      AND region = 'EU';
    ```
    
    **2. JOIN en el orden correcto (pequeña → grande)**
    ```sql
    SELECT v.*, p.nombre
    FROM dim_producto p  -- Tabla pequeña primero
    JOIN fact_ventas v ON p.producto_id = v.producto_id
    WHERE p.categoria = 'Electronics';
    ```
    
    **3. Filtra antes de JOINs cuando sea posible**
    ```sql
    SELECT v.*, c.nombre
    FROM (
        SELECT * FROM fact_ventas 
        WHERE fecha >= '2024-01-01'  -- Reduce antes de JOIN
    ) v
    JOIN dim_cliente c ON v.cliente_id = c.cliente_id;
    ```
    
    **4. Usa agregaciones incrementales**
    ```sql
    -- En vez de recalcular todo, usa tablas resumen
    SELECT DATE_TRUNC('month', fecha) as mes,
           SUM(importe)
    FROM ventas_diarias_summary  -- Tabla pre-agregada
    GROUP BY 1;
    ```
    
    **5. Aprovecha CTE (WITH) para legibilidad y reutilización**
    ```sql
    WITH ventas_2024 AS (
        SELECT * FROM ventas WHERE YEAR(fecha) = 2024
    ),
    top_productos AS (
        SELECT producto_id, SUM(importe) as total
        FROM ventas_2024
        GROUP BY producto_id
        ORDER BY total DESC
        LIMIT 10
    )
    SELECT p.nombre, tp.total
    FROM top_productos tp
    JOIN productos p ON tp.producto_id = p.id;
    ```
    """)

with tab3:
    st.markdown("""
    ### Caso real: Optimización de query lenta
    """)
    
    st.code("""
-- QUERY ORIGINAL (lenta: 45 segundos) ❌
SELECT 
    c.nombre_cliente,
    p.nombre_producto,
    SUM(v.cantidad) as total_vendido,
    SUM(v.importe) as ingresos_totales
FROM fact_ventas v
JOIN dim_cliente c ON v.cliente_id = c.cliente_id
JOIN dim_producto p ON v.producto_id = p.producto_id
WHERE v.fecha >= '2023-01-01'
  AND c.pais = 'España'
GROUP BY c.nombre_cliente, p.nombre_producto
ORDER BY ingresos_totales DESC;

-- PROBLEMAS:
-- 1. fact_ventas tiene 500M filas, filtra después de JOIN
-- 2. No usa índices eficientemente
-- 3. GROUP BY en columnas sin índice
    """, language="sql")
    
    st.code("""
-- QUERY OPTIMIZADA (rápida: 3 segundos) ✅

-- Paso 1: Pre-filtrar ventas (usa partition pruning)
WITH ventas_filtradas AS (
    SELECT 
        cliente_id,
        producto_id,
        cantidad,
        importe
    FROM fact_ventas
    WHERE fecha >= '2023-01-01'  -- Partition pruning reduce a 50M filas
),

-- Paso 2: Filtrar clientes españoles primero (tabla pequeña)
clientes_spain AS (
    SELECT cliente_id, nombre_cliente
    FROM dim_cliente
    WHERE pais = 'España'  -- Solo 100K clientes en vez de 5M
)

-- Paso 3: JOIN solo con datos filtrados
SELECT 
    cs.nombre_cliente,
    p.nombre_producto,
    SUM(vf.cantidad) as total_vendido,
    SUM(vf.importe) as ingresos_totales
FROM ventas_filtradas vf
JOIN clientes_spain cs ON vf.cliente_id = cs.cliente_id
JOIN dim_producto p ON vf.producto_id = p.producto_id
GROUP BY cs.nombre_cliente, p.nombre_producto
ORDER BY ingresos_totales DESC;

-- MEJORAS APLICADAS:
-- ✅ Partition pruning reduce 10x datos escaneados
-- ✅ Filtra dimensión antes de JOIN (100K vs 5M)
-- ✅ JOINs sobre datasets reducidos
-- ✅ Usa índices en claves de JOIN
-- RESULTADO: 15x más rápido
    """, language="sql")

st.divider()

# --- Mejores Prácticas ---
st.subheader("✨ Mejores Prácticas Generales")

col1, col2 = st.columns(2)

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
    - Analizar estadísticas regularmente (ANALYZE/UPDATE STATISTICS)
    - Monitorear queries lentas
    - Revisar y eliminar índices no usados
    
    **Datos:**
    - Comprimir tablas grandes
    - Archivar datos antiguos
    - Limpiar datos duplicados
    """)

with col2:
    st.error("""
    ### ❌ DON'T - Evitar
    
    **Diseño:**
    - No sobre-indexar (cada índice = overhead en writes)
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
    
    **Datos:**
    - No mezclar datos hot y cold en misma partición
    - No mantener índices en datos históricos de solo lectura
    """)

st.divider()

# --- Monitoreo ---
with st.expander("📊 Monitoreo de Rendimiento"):
    st.markdown("""
    ### Métricas clave a monitorear
    
    **1. Query Performance:**
    - Tiempo de ejecución promedio/percentil 95
    - Queries más lentas (top 10)
    - Queries más frecuentes
    - Query plans que hacen full table scans
    
    **2. Recursos:**
    - CPU utilization
    - Memory usage
    - Disk I/O (IOPS)
    - Network throughput
    
    **3. Storage:**
    - Tamaño de tablas y crecimiento
    - Ratio de compresión
    - Uso de particiones (skew)
    
    **4. Concurrencia:**
    - Queries concurrentes
    - Queue time (espera)
    - Lock contention
    
    **Herramientas:**
    - **AWS:** CloudWatch + Performance Insights
    - **Snowflake:** Query Profile, Account Usage views
    - **BigQuery:** Query execution details, INFORMATION_SCHEMA
    - **SQL Server:** Query Store, DMVs
    """)

st.divider()

# --- Ejemplo Final ---
with st.expander("💡 Caso de estudio completo"):
    st.markdown("""
    ### Optimización real: E-commerce con 100TB de datos
    
    **Situación inicial:**
    - Tabla fact_orders: 50 mil millones de filas
    - Reportes diarios: 30 minutos
    - Análisis ad-hoc: imposibles
    - Costo cloud: $50K/mes
    
    **Optimizaciones aplicadas:**
    
    **1. Particionamiento por fecha (día)**
    - Antes: Full table scan 50B filas
    - Después: Scan de 1 día = 150M filas
    - **Mejora: 300x**
    
    **2. Clustering por (fecha, customer_country)**
    - Mejora compresión: 5:1 → 12:1
    - Reduce I/O en queries de país específico
    - **Mejora: 2.4x adicional**
    
    **3. Vistas materializadas para reportes diarios**
    - Pre-agrega daily_sales, daily_customers
    - Refresh incremental cada hora
    - **Mejora: Reportes de 30 min → 10 segundos**
    
    **4. Columnstore indexes en dimensiones**
    - dim_product, dim_customer
    - JOINs 5x más rápidos
    
    **5. Reescritura de queries top 10**
    - Aplicar mejores prácticas SQL
    - Filtros antes de JOINs
    - **Mejora: 10-50x por query**
    
    **Resultados:**
    - Reportes: 30 min → 10 seg (180x más rápido)
    - Análisis ad-hoc: Ahora factibles (1-5 min)
    - Costo cloud: $50K → $18K/mes (64% reducción)
    - Satisfacción usuarios: ⭐⭐ → ⭐⭐⭐⭐⭐
    """)

st.divider()

