# pages/5_dimensiones.py
import streamlit as st

st.set_page_config(page_title="Dimensiones y SCD", page_icon="🔷", layout="wide")

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
    <div style='font-size: 4rem; margin-bottom: 20px;'>🔷</div>
    <h1 style='color: #ffffff; font-size: 3rem; margin-bottom: 15px; text-shadow: 0 4px 16px rgba(0, 0, 0, 0.6); font-weight: 800;'>
        Slowly Changing Dimensions
    </h1>
    <p style='color: #b8c5d6; font-size: 1.2rem; max-width: 700px; margin: 0 auto;'>
        Gestión de cambios históricos en dimensiones
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
    <h2 style='color: #ffffff; margin-bottom: 20px;'>📝 ¿Qué son las SCD?</h2>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9;'>
        Las <strong style='color: #fff;'>Slowly Changing Dimensions (SCD)</strong> son técnicas para gestionar cambios en los atributos 
        de las dimensiones a lo largo del tiempo. Permiten rastrear el historial de cambios y mantener la integridad de los análisis históricos.
    </p>
    <p style='color: #d0dae8; font-size: 1.15rem; line-height: 1.9; margin-top: 15px;'>
        <strong style='color: #fff;'>Problema:</strong> ¿Qué sucede cuando un cliente cambia de dirección o un producto cambia de categoría? 
        ¿Cómo mantenemos el historial sin perder la trazabilidad?
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

# Tipos de SCD
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>🎯 Tipos de SCD</h2>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📌 Tipo 0 y 1", "📊 Tipo 2 (Más Común)", "🔀 Tipo 3 y 6"])

with tab1:
    st.markdown("""
    <div style="background: rgba(237, 137, 54, 0.1); padding: 30px; border-radius: 15px; border: 1px solid rgba(237, 137, 54, 0.3); margin-bottom: 25px;">
        <h3 style="color: #fbd38d; margin-bottom: 20px;">📌 SCD Tipo 0 - Sin Cambios</h3>
        <p style="color: #d0dae8; line-height: 1.8;">
            Los datos <strong style='color: #fff;'>nunca cambian</strong>. Los valores originales se mantienen permanentemente.
        </p>
        <ul style="color: #b8c5d6; line-height: 2; margin-top: 15px;">
            <li>✅ Máxima simplicidad</li>
            <li>❌ No refleja la realidad si hay cambios</li>
        </ul>
        <p style="color: #90cdf4; margin-top: 15px;"><strong>Ejemplo:</strong> Fecha de nacimiento</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: rgba(245, 101, 101, 0.1); padding: 30px; border-radius: 15px; border: 1px solid rgba(245, 101, 101, 0.3);">
        <h3 style="color: #fc8181; margin-bottom: 20px;">🔄 SCD Tipo 1 - Sobrescribir</h3>
        <p style="color: #d0dae8; line-height: 1.8;">
            <strong style='color: #fff;'>Sobrescribe</strong> el valor antiguo con el nuevo. No mantiene historial.
        </p>
        <ul style="color: #b8c5d6; line-height: 2; margin-top: 15px;">
            <li>✅ Simple de implementar</li>
            <li>✅ No incrementa tamaño de tabla</li>
            <li>❌ Pierde historial completamente</li>
        </ul>
        <p style="color: #90cdf4; margin-top: 15px;"><strong>Ejemplo:</strong> Corrección de errores de captura</p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.success("### 📊 SCD Tipo 2 - Nueva Fila ⭐")
    
    st.write("""
    Crea una **nueva fila** para cada cambio. Mantiene **historial completo**. 
    Es el método más popular en DWH.
    """)
    
    st.write("**Implementación:**")
    st.write("""
    - 🔑 Clave subrogada (surrogate key)
    - 📅 Fecha inicio vigencia
    - 📅 Fecha fin vigencia
    - ✅ Flag de registro activo
    """)
    
    st.write("**Ventajas:**")
    st.write("""
    - ✅ Historial completo
    - ✅ Análisis punto en el tiempo
    - ✅ Auditoría completa
    - ✅ No se pierden datos
    """)
    
    st.write("**Desventajas:**")
    st.write("""
    - ⚠️ Crece el tamaño de la tabla
    - ⚠️ Consultas más complejas
    - ⚠️ Requiere gestión de claves
    """)

with tab3:
    st.markdown("""
    <div style="background: rgba(66, 153, 225, 0.1); padding: 30px; border-radius: 15px; border: 1px solid rgba(66, 153, 225, 0.3); margin-bottom: 25px;">
        <h3 style="color: #90cdf4; margin-bottom: 20px;">🔀 SCD Tipo 3 - Columnas Adicionales</h3>
        <p style="color: #d0dae8; line-height: 1.8;">
            Añade <strong style='color: #fff;'>columnas adicionales</strong> para valores anteriores. Historial <strong style='color: #fff;'>limitado</strong> 
            (típicamente 1-2 valores previos).
        </p>
        <ul style="color: #b8c5d6; line-height: 2; margin-top: 15px;">
            <li>✅ No aumenta filas</li>
            <li>✅ Fácil comparar actual vs anterior</li>
            <li>❌ Historial muy limitado</li>
        </ul>
        <p style="color: #90cdf4; margin-top: 15px;"><strong>Ejemplo:</strong> Ciudad_Actual, Ciudad_Anterior</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: rgba(167, 139, 250, 0.1); padding: 30px; border-radius: 15px; border: 1px solid rgba(167, 139, 250, 0.3);">
        <h3 style="color: #c4b5fd; margin-bottom: 20px;">🔀 SCD Tipo 6 - Híbrido (1+2+3)</h3>
        <p style="color: #d0dae8; line-height: 1.8;">
            Combina características de Tipo 1, 2 y 3. Nueva fila para cada cambio + columnas para valor actual y anterior.
        </p>
        <ul style="color: #b8c5d6; line-height: 2; margin-top: 15px;">
            <li>✅ Historial completo</li>
            <li>✅ Valor actual accesible desde cualquier registro</li>
            <li>❌ Complejidad alta</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 60px;'></div>", unsafe_allow_html=True)

# Comparativa
st.markdown("""
<div style="text-align: center; margin: 60px 0 40px 0;">
    <h2 style='color: #ffffff; font-size: 2.5rem; margin-bottom: 10px;'>⚖️ Comparativa de Tipos</h2>
</div>
""", unsafe_allow_html=True)

scd_comparison = {
    "Tipo": ["Tipo 0", "Tipo 1", "Tipo 2", "Tipo 3", "Tipo 6"],
    "Historial": ["❌ No", "❌ No", "✅ Completo", "⚠️ Limitado", "✅ Completo"],
    "Filas Adicionales": ["No", "No", "Sí", "No", "Sí"],
    "Complejidad": ["Muy Baja", "Baja", "Media", "Baja", "Alta"],
    "Uso Común": ["Raro", "Común", "Muy Común ⭐", "Ocasional", "Raro"]
}

st.table(scd_comparison)

st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
