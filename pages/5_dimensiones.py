# pages/5_dimensiones.py
import streamlit as st

st.set_page_config(page_title="Dimensiones y SCD", page_icon="🔷", layout="wide")

st.markdown("<h1 style='text-align:center; color:#ffffff;'>🔷 Dimensiones, Hechos y SCD</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Slowly Changing Dimensions y gestión de cambios históricos</p>", unsafe_allow_html=True)

st.divider()

# --- Introducción ---
st.subheader("📝 ¿Qué son las Slowly Changing Dimensions (SCD)?")
st.write("""
Las **Slowly Changing Dimensions (SCD)** son técnicas para gestionar cambios en los atributos de las dimensiones 
a lo largo del tiempo. Permiten rastrear el historial de cambios y mantener la integridad de los análisis históricos.

**Problema:** ¿Qué sucede cuando un cliente cambia de dirección o un producto cambia de categoría?
¿Cómo mantenemos el historial sin perder la trazabilidad?
""")

st.divider()

# --- Tipos de SCD ---
st.subheader("🎯 Tipos de Slowly Changing Dimensions")

# SCD Tipo 0
with st.expander("📌 SCD Tipo 0 - Sin cambios"):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Tipo 0: Retener Original
        
        **Descripción:**
        - Los datos **nunca cambian**
        - Los valores originales se mantienen permanentemente
        - Ignora cualquier actualización
        
        **Cuándo usar:**
        - Datos que no deben cambiar (ej: fecha de nacimiento)
        - Referencias fijas
        - Códigos inmutables
        
        **Ventajas:**
        - ✅ Máxima simplicidad
        - ✅ Sin overhead de procesamiento
        
        **Desventajas:**
        - ❌ No refleja la realidad si hay cambios
        - ❌ Puede causar inconsistencias
        """)
    
    with col2:
        st.code("""
Cliente ID: 1001
Nombre: Juan Pérez
Nacimiento: 1985-03-15

↓ (Nunca cambia)

Cliente ID: 1001
Nombre: Juan Pérez
Nacimiento: 1985-03-15
        """)

# SCD Tipo 1
with st.expander("🔄 SCD Tipo 1 - Sobrescribir"):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Tipo 1: Sobrescribir
        
        **Descripción:**
        - **Sobrescribe** el valor antiguo con el nuevo
        - No mantiene historial
        - Actualización simple (UPDATE)
        
        **Cuándo usar:**
        - Corrección de errores
        - Datos donde el historial no importa
        - Cambios que deben reflejarse retroactivamente
        
        **Ventajas:**
        - ✅ Simple de implementar
        - ✅ No incrementa tamaño de tabla
        - ✅ Siempre muestra valor actual
        
        **Desventajas:**
        - ❌ Pierde historial completamente
        - ❌ No permite análisis temporal
        - ❌ Los reportes históricos cambian
        """)
    
    with col2:
        st.code("""
ANTES:
ID | Nombre | Ciudad
1  | Ana    | Madrid

↓ UPDATE

DESPUÉS:
ID | Nombre | Ciudad
1  | Ana    | Barcelona

(Madrid se pierde)
        """)

# SCD Tipo 2
with st.expander("📊 SCD Tipo 2 - Nueva fila (MÁS COMÚN)"):
    st.markdown("""
    ### Tipo 2: Añadir Nueva Fila (Historical Tracking)
    
    **Descripción:**
    - Crea una **nueva fila** para cada cambio
    - Mantiene **historial completo**
    - Usa fechas de vigencia o versiones
    - El método más popular en DWH
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Implementación común:**
        - Clave subrogada (surrogate key)
        - Fecha inicio vigencia
        - Fecha fin vigencia
        - Flag de registro activo
        
        **Ventajas:**
        - ✅ Historial completo
        - ✅ Análisis punto en el tiempo
        - ✅ Auditoría completa
        - ✅ No se pierden datos
        
        **Desventajas:**
        - ⚠️ Crece el tamaño de la tabla
        - ⚠️ Consultas más complejas
        - ⚠️ Requiere gestión de claves
        """)
    
    with col2:
        st.code("""
ID_SK | ID_NK | Nombre | Ciudad    | Inicio     | Fin        | Activo
1     | 100   | Ana    | Madrid    | 2020-01-01 | 2023-05-31 | N
2     | 100   | Ana    | Barcelona | 2023-06-01 | NULL       | S

Consulta actual: WHERE Activo = 'S'
Consulta histórica: WHERE '2022-03-15' 
                    BETWEEN Inicio AND Fin
        """)
    
    st.info("""
    **💡 Ejemplo de consulta:**
    ```sql
    -- Obtener ventas con ciudad del cliente en el momento de la venta
    SELECT 
        v.fecha,
        c.nombre,
        c.ciudad,
        v.importe
    FROM fact_ventas v
    JOIN dim_cliente c 
        ON v.cliente_id = c.id_sk
        AND v.fecha BETWEEN c.fecha_inicio AND COALESCE(c.fecha_fin, '9999-12-31')
    ```
    """)

# SCD Tipo 3
with st.expander("🔀 SCD Tipo 3 - Columnas adicionales"):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Tipo 3: Añadir Columna
        
        **Descripción:**
        - Añade **columnas adicionales** para valores anteriores
        - Mantiene historial **limitado** (típicamente 1-2 valores previos)
        - No aumenta filas
        
        **Cuándo usar:**
        - Solo necesitas valor actual y anterior
        - Cambios muy poco frecuentes
        - Análisis de "antes vs después"
        
        **Ventajas:**
        - ✅ No aumenta filas
        - ✅ Fácil comparar actual vs anterior
        - ✅ Consultas simples
        
        **Desventajas:**
        - ❌ Historial muy limitado
        - ❌ Estructura rígida
        - ❌ Necesita cambios de esquema
        """)
    
    with col2:
        st.code("""
ID | Nombre | Ciudad_Actual | Ciudad_Anterior
1  | Ana    | Barcelona     | Madrid

Permite analizar:
- ¿De dónde venían?
- Migración entre ciudades
        """)

# SCD Tipo 4
with st.expander("📑 SCD Tipo 4 - Tabla histórica separada"):
    st.markdown("""
    ### Tipo 4: Mini-Dimension / Tabla Histórica
    
    **Descripción:**
    - Mantiene datos **actuales** en dimensión principal
    - Mueve **historial** a tabla separada
    - Combina Tipo 1 y Tipo 2
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code("""
dim_cliente (ACTUAL):
ID | Nombre | Ciudad
1  | Ana    | Barcelona

dim_cliente_history (HISTÓRICO):
ID | Nombre | Ciudad | Inicio     | Fin
1  | Ana    | Madrid | 2020-01-01 | 2023-05-31
1  | Ana    | Barcelona | 2023-06-01 | NULL
        """)
    
    with col2:
        st.markdown("""
        **Ventajas:**
        - ✅ Dimensión actual pequeña y rápida
        - ✅ Historial completo en tabla aparte
        - ✅ Mejor rendimiento en consultas actuales
        
        **Desventajas:**
        - ⚠️ Dos tablas que mantener
        - ⚠️ Más complejo de gestionar
        """)

# SCD Tipo 6
with st.expander("🔀 SCD Tipo 6 - Híbrido (1+2+3)"):
    st.markdown("""
    ### Tipo 6: Híbrido (También llamado Tipo 1+2+3)
    
    **Descripción:**
    - Combina características de Tipo 1, 2 y 3
    - Nueva fila para cada cambio (Tipo 2)
    - Columnas para valor actual y anterior (Tipo 3)
    - Sobrescribe valor actual en todas las filas (Tipo 1)
    """)
    
    st.code("""
ID_SK | ID_NK | Nombre | Ciudad_Historica | Ciudad_Actual | Inicio     | Fin        | Activo
1     | 100   | Ana    | Madrid          | Barcelona     | 2020-01-01 | 2023-05-31 | N
2     | 100   | Ana    | Barcelona       | Barcelona     | 2023-06-01 | NULL       | S

Permite:
- Ver valor en cualquier momento (Tipo 2)
- Ver valor actual desde cualquier registro (Tipo 1)
- Comparar histórico vs actual (Tipo 3)
    """)

st.divider()

# --- Comparativa ---
st.subheader("⚖️ Comparativa de Tipos de SCD")

scd_comparison = {
    "Tipo": ["Tipo 0", "Tipo 1", "Tipo 2", "Tipo 3", "Tipo 4", "Tipo 6"],
    "Historial": ["❌ No", "❌ No", "✅ Completo", "⚠️ Limitado", "✅ Completo", "✅ Completo"],
    "Filas Adicionales": ["No", "No", "Sí", "No", "Sí (otra tabla)", "Sí"],
    "Complejidad": ["Muy Baja", "Baja", "Media", "Baja", "Alta", "Alta"],
    "Uso Común": ["Raro", "Común", "Muy Común", "Ocasional", "Poco Común", "Raro"]
}

st.table(scd_comparison)

st.divider()

# --- Implementación Tipo 2 ---
st.subheader("💻 Implementación Práctica - SCD Tipo 2")

tab1, tab2, tab3 = st.tabs(["📝 Diseño de Tabla", "🔄 INSERT de Cambio", "🔍 Consultas"])

with tab1:
    st.code("""
CREATE TABLE dim_cliente (
    cliente_sk INT PRIMARY KEY AUTO_INCREMENT,  -- Surrogate Key
    cliente_id INT NOT NULL,                     -- Natural Key / Business Key
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(100),
    ciudad VARCHAR(50),
    segmento VARCHAR(20),
    
    -- Campos de control SCD Tipo 2
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NULL,                         -- NULL = registro activo
    version INT NOT NULL DEFAULT 1,
    registro_activo CHAR(1) DEFAULT 'S',         -- 'S' = activo, 'N' = histórico
    
    INDEX idx_natural_key (cliente_id, registro_activo),
    INDEX idx_fechas (fecha_inicio, fecha_fin)
);
    """, language="sql")

with tab2:
    st.code("""
-- Proceso ETL para actualizar dimensión con SCD Tipo 2

-- 1. Cerrar registro actual (marcar como histórico)
UPDATE dim_cliente
SET fecha_fin = CURRENT_DATE - 1,
    registro_activo = 'N'
WHERE cliente_id = 1001 
  AND registro_activo = 'S';

-- 2. Insertar nuevo registro con los datos actualizados
INSERT INTO dim_cliente (
    cliente_id, nombre, apellido, email, ciudad, segmento,
    fecha_inicio, fecha_fin, version, registro_activo
)
VALUES (
    1001, 'Ana', 'García', 'ana@email.com', 'Barcelona', 'Premium',
    CURRENT_DATE, NULL, 2, 'S'
);
    """, language="sql")

with tab3:
    st.code("""
-- Consulta 1: Obtener solo registros actuales
SELECT cliente_id, nombre, ciudad
FROM dim_cliente
WHERE registro_activo = 'S';

-- Consulta 2: Ver historial completo de un cliente
SELECT cliente_sk, nombre, ciudad, fecha_inicio, fecha_fin, version
FROM dim_cliente
WHERE cliente_id = 1001
ORDER BY version;

-- Consulta 3: Estado de cliente en una fecha específica (Point-in-Time)
SELECT nombre, ciudad, segmento
FROM dim_cliente
WHERE cliente_id = 1001
  AND '2022-06-15' BETWEEN fecha_inicio AND COALESCE(fecha_fin, '9999-12-31');

-- Consulta 4: Análisis de migración de clientes entre ciudades
SELECT 
    ciudad_antigua,
    ciudad_nueva,
    COUNT(*) as cantidad_migraciones
FROM (
    SELECT 
        c1.cliente_id,
        c1.ciudad as ciudad_antigua,
        c2.ciudad as ciudad_nueva
    FROM dim_cliente c1
    JOIN dim_cliente c2 ON c1.cliente_id = c2.cliente_id
    WHERE c1.fecha_fin = c2.fecha_inicio - 1
      AND c1.ciudad <> c2.ciudad
) migraciones
GROUP BY ciudad_antigua, ciudad_nueva;
    """, language="sql")

st.divider()

# --- Mejores Prácticas ---
st.subheader("✨ Mejores Prácticas para SCD")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    **✅ DO - Hacer:**
    
    - Usar claves subrogadas (surrogate keys)
    - Documentar qué tipo de SCD usa cada atributo
    - Implementar Tipo 2 para atributos críticos
    - Incluir campos de auditoría (usuario, fecha)
    - Usar índices en fechas de vigencia
    - Validar que solo haya un registro activo por entidad
    """)

with col2:
    st.error("""
    **❌ DON'T - Evitar:**
    
    - Mezclar tipos de SCD sin documentar
    - Usar claves naturales en tablas de hechos
    - Ignorar el impacto en el rendimiento
    - Olvidar cerrar registros antiguos
    - Tener múltiples registros activos
    - Implementar SCD en todas las dimensiones innecesariamente
    """)

st.divider()

# --- Decisión de Tipo SCD ---
with st.expander("🤔 ¿Qué tipo de SCD elegir?"):
    st.markdown("""
    ### Guía de Decisión
    
    **Usa SCD Tipo 0 cuando:**
    - Los datos nunca deben cambiar (ej: fecha de nacimiento)
    - Son códigos o identificadores fijos
    
    **Usa SCD Tipo 1 cuando:**
    - Solo importa el valor actual
    - Son correcciones de errores de captura
    - El historial no tiene valor de negocio
    - Ejemplo: Corrección de typos en nombres
    
    **Usa SCD Tipo 2 cuando:** ⭐ **MÁS RECOMENDADO**
    - Necesitas análisis histórico completo
    - Los cambios son significativos para el negocio
    - Requieres auditoría completa
    - Ejemplo: Cambios de categoría de cliente, cambios de precio
    
    **Usa SCD Tipo 3 cuando:**
    - Solo necesitas comparar actual vs anterior
    - Los cambios son muy poco frecuentes
    - El análisis es "antes/después" simple
    - Ejemplo: Reestructuración organizacional (división antigua vs nueva)
    
    **Usa SCD Tipo 4 cuando:**
    - La dimensión tiene millones de registros
    - El rendimiento es crítico
    - Rara vez necesitas datos históricos
    
    **Usa SCD Tipo 6 cuando:**
    - Necesitas lo mejor de todos los mundos
    - Tienes casos de uso muy complejos
    - Vale la pena la complejidad adicional
    """)

st.divider()

# --- Ejemplo Real ---
with st.expander("💡 Ejemplo del Mundo Real: Dimensión Producto"):
    st.markdown("""
    ### Caso: Gestión de Productos en Retail
    
    **Escenario:**
    Un producto cambia de categoría y precio a lo largo del tiempo.
    
    **Atributos y sus tipos de SCD:**
    
    | Atributo | Tipo SCD | Razón |
    |----------|----------|-------|
    | código_producto | Tipo 0 | Nunca cambia |
    | nombre | Tipo 1 | Correcciones solo |
    | categoría | Tipo 2 | Análisis histórico crucial |
    | precio | Tipo 2 | Análisis de tendencias |
    | proveedor | Tipo 2 | Trazabilidad requerida |
    | código_barras | Tipo 1 | Correcciones solo |
    | estado | Tipo 1 | Solo importa si está activo ahora |
    
    **Tabla resultante:**
    ```sql
    producto_sk | producto_id | nombre      | categoria    | precio | fecha_inicio | fecha_fin  | activo
    ------------|-------------|-------------|-------------|--------|--------------|------------|-------
    1           | P1001       | Laptop Pro  | Electrónica | 999.00 | 2023-01-01   | 2023-06-30 | N
    2           | P1001       | Laptop Pro  | Informática | 949.00 | 2023-07-01   | 2024-12-31 | N
    3           | P1001       | Laptop Pro  | Informática | 899.00 | 2025-01-01   | NULL       | S
    ```
    
    **Análisis posibles:**
    - Ventas por categoría en cada período
    - Impacto de cambios de precio en ventas
    - Migración de productos entre categorías
    """)

st.divider()

