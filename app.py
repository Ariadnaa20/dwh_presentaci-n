import streamlit as st
import streamlit.components.v1 as components
import pathlib

st.set_page_config(page_title="Presentación DWH", page_icon="📊", layout="wide")

# Cargar CSS
static_path = pathlib.Path(__file__).parent / "static"
css_file = static_path / "styles.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.error(f"CSS file not found at {css_file}")

# Inicializar session state
if 'show_modal' not in st.session_state:
    st.session_state.show_modal = False
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = None

# Título y subtítulo
st.markdown("<h1>📊 Data Warehouse (DWH)</h1>", unsafe_allow_html=True)
st.markdown('<p class="sub">Explora los temas haciendo clic en las cards</p>', unsafe_allow_html=True)

# Definir las cards con sus páginas correspondientes
cards_data = [
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/2942/2942821.png",
        "title": "Definición y propósito del DWH",
        "description": "Qué es un Data Warehouse y para qué se utiliza.",
        "page": "1_definicion"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/2910/2910768.png",
        "title": "Evolución histórica",
        "description": "Cómo ha cambiado el concepto de DWH con el tiempo.",
        "page": "2_evolucion"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/2838/2838890.png",
        "title": "OLTP vs OLAP",
        "description": "Diferencias entre sistemas transaccionales y analíticos.",
        "page": "3_oltp_olap"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/4149/4149723.png",
        "title": "Arquitectura de un DWH",
        "description": "Staging, ETL/ELT y presentación.",
        "page": "4_arquitectura"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/2910/2910772.png",
        "title": "Modelado dimensional",
        "description": "Estrella, copo de nieve, dimensiones y hechos.",
        "page": "5_modelado"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/2910/2910778.png",
        "title": "Dimensiones, hechos y SCD",
        "description": "Tipos de dimensiones, hechos y Slowly Changing Dimensions.",
        "page": "5_dimensiones"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/3003/3003945.png",
        "title": "Herramientas y tecnologías",
        "description": "On-premise y cloud para DWH.",
        "page": "6_herramientas"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/3003/3003940.png",
        "title": "ETL vs ELT",
        "description": "Procesos de extracción, transformación y carga de datos.",
        "page": "7_etl_elt"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/2921/2921828.png",
        "title": "Rendimiento",
        "description": "Particiones e índices para acelerar consultas.",
        "page": "8_rendimento"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/2910/2910776.png",
        "title": "Ventajas y limitaciones",
        "description": "Fortalezas y debilidades de un DWH.",
        "page": "9_ventajas"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/2910/2910780.png",
        "title": "Comparativa con Data Lake / Lakehouse",
        "description": "Relaciones y diferencias con otras arquitecturas.",
        "page": "10_comparativa"
    },
    {
        "icon": "https://cdn-icons-png.flaticon.com/512/2910/2910785.png",
        "title": "Futuro del DWH",
        "description": "Tendencias y perspectivas futuras.",
        "page": "11_futuro"
    }
]

# Verificar si hay un query param para seleccionar página
if 'page' in st.query_params:
    page_value = st.query_params.get('page')
    # Convertir a string si es una lista
    if isinstance(page_value, list):
        page_value = page_value[0]
    
    if page_value and not st.session_state.show_modal:
        st.session_state.selected_page = page_value
        st.session_state.show_modal = True

# Crear el carrusel HTML con las cards
st.markdown("""
<div class="carousel">
    <div class="card" id="card-0">
        <img src="https://cdn-icons-png.flaticon.com/512/2942/2942821.png" alt="icon">
        <h3>Definición y propósito del DWH</h3>
        <p>Qué es un Data Warehouse y para qué se utiliza.</p>
    </div>
    <div class="card" id="card-1">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910768.png" alt="icon">
        <h3>Evolución histórica</h3>
        <p>Cómo ha cambiado el concepto de DWH con el tiempo.</p>
    </div>
    <div class="card" id="card-2">
        <img src="https://cdn-icons-png.flaticon.com/512/2838/2838890.png" alt="icon">
        <h3>OLTP vs OLAP</h3>
        <p>Diferencias entre sistemas transaccionales y analíticos.</p>
    </div>
    <div class="card" id="card-3">
        <img src="https://cdn-icons-png.flaticon.com/512/4149/4149723.png" alt="icon">
        <h3>Arquitectura de un DWH</h3>
        <p>Staging, ETL/ELT y presentación.</p>
    </div>
    <div class="card" id="card-4">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910772.png" alt="icon">
        <h3>Modelado dimensional</h3>
        <p>Estrella, copo de nieve, dimensiones y hechos.</p>
    </div>
    <div class="card" id="card-5">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910778.png" alt="icon">
        <h3>Dimensiones, hechos y SCD</h3>
        <p>Tipos de dimensiones, hechos y Slowly Changing Dimensions.</p>
    </div>
    <div class="card" id="card-6">
        <img src="https://cdn-icons-png.flaticon.com/512/3003/3003945.png" alt="icon">
        <h3>Herramientas y tecnologías</h3>
        <p>On-premise y cloud para DWH.</p>
    </div>
    <div class="card" id="card-7">
        <img src="https://cdn-icons-png.flaticon.com/512/3003/3003940.png" alt="icon">
        <h3>ETL vs ELT</h3>
        <p>Procesos de extracción, transformación y carga de datos.</p>
    </div>
    <div class="card" id="card-8">
        <img src="https://cdn-icons-png.flaticon.com/512/2921/2921828.png" alt="icon">
        <h3>Rendimiento</h3>
        <p>Particiones e índices para acelerar consultas.</p>
    </div>
    <div class="card" id="card-9">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910776.png" alt="icon">
        <h3>Ventajas y limitaciones</h3>
        <p>Fortalezas y debilidades de un DWH.</p>
    </div>
    <div class="card" id="card-10">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910780.png" alt="icon">
        <h3>Comparativa con Data Lake / Lakehouse</h3>
        <p>Relaciones y diferencias con otras arquitecturas.</p>
    </div>
    <div class="card" id="card-11">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910785.png" alt="icon">
        <h3>Futuro del DWH</h3>
        <p>Tendencias y perspectivas futuras.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Crear botones invisibles para cada card usando CSS para ocultarlos
cols = st.columns(len(cards_data))
for idx, (col, card) in enumerate(zip(cols, cards_data)):
    with col:
        if st.button(f"Open {idx}", key=f"btn_{idx}", type="primary"):
            st.session_state.selected_page = card["page"]
            st.session_state.show_modal = True
            st.rerun()

# CSS para ocultar los botones
st.markdown("""
<style>
    button[kind="primary"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# JavaScript para conectar clicks de cards con botones
components.html(f"""
<script>
    // Esperar a que el DOM esté listo
    setTimeout(function() {{
        const cards = window.parent.document.querySelectorAll('.card');
        const buttons = window.parent.document.querySelectorAll('button[kind="secondary"]');
        
        console.log('Cards encontradas:', cards.length);
        console.log('Botones encontrados:', buttons.length);
        
        cards.forEach((card, index) => {{
            card.style.cursor = 'pointer';
            card.addEventListener('click', function(e) {{
                console.log('Click en card', index);
                e.preventDefault();
                e.stopPropagation();
                
                // Buscar el botón correspondiente
                const allButtons = Array.from(window.parent.document.querySelectorAll('button'));
                const targetButton = allButtons.find(btn => btn.textContent.includes('Open ' + index));
                
                if (targetButton) {{
                    console.log('Haciendo click en botón', index);
                    targetButton.click();
                }} else {{
                    console.log('No se encontró el botón', index);
                }}
            }});
        }});
    }}, 500);
</script>
""", height=0)

# Función para renderizar el contenido de cada página
@st.dialog("📚 Contenido del tema", width="large")
def show_page_content(page_name):
    """Muestra el contenido de la página seleccionada en un modal"""
    
    # CSS para ajustar el ancho del diálogo
    st.markdown("""
    <style>
        section[data-testid="stDialog"] {
            width: 85vw !important;
            max-width: 1600px !important;
        }
        section[data-testid="stDialog"] > div {
            width: 85vw !important;
            max-width: 1600px !important;
            overflow-y: auto !important;
            max-height: 90vh !important;
        }
        section[data-testid="stDialog"] > div > div {
            width: 100% !important;
            max-width: 1600px !important;
        }
        [role="dialog"] {
            width: 85vw !important;
            max-width: 1600px !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Script separado para scroll al principio
    components.html("""
    <script>
        setTimeout(function() {
            const dialog = window.parent.document.querySelector('section[data-testid="stDialog"] > div');
            if (dialog) {
                dialog.scrollTop = 0;
            }
            // También hacer scroll en la página principal
            window.parent.scrollTo(0, 0);
        }, 150);
    </script>
    """, height=0)
    
    if page_name == "1_definicion":
        st.markdown("<h1 style='text-align:center; color:#1e3d8f;'>📊 Definición y propósito del DWH</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Explora cada sección interactuando con los bloques y expanders</p>", unsafe_allow_html=True)
        st.divider()
        
        st.subheader("📝 Introducción")
        st.write("""
        Un **Data Warehouse (DWH)** es un sistema que recopila, integra y organiza datos provenientes de distintas fuentes
        para facilitar la **toma de decisiones estratégicas** en una organización.  
        Su propósito es centralizar la información para que los analistas puedan obtener **insights valiosos** sin afectar los sistemas operacionales.
        """)
        st.divider()
        
        st.subheader("✨ Características principales")
        col1, col2, col3 = st.columns(3)
        col1.success("🧩 Integración de datos\nCombina información de múltiples sistemas (ERP, CRM, bases de datos).")
        col2.info("📂 Orientado a temas\nLos datos se organizan según áreas de interés: ventas, clientes, inventario.")
        col3.warning("⏳ No volátil\nLos datos históricos se mantienen sin alteraciones frecuentes.")
        
        col1, col2, col3 = st.columns(3)
        col1.success("📊 Variedad histórica\nPermite analizar tendencias y comparativas a lo largo del tiempo.")
        col2.info("⚡ Optimizado para consultas\nDiseñado para responder consultas analíticas complejas.")
        col3.warning("💡 Escalable\nSe puede ampliar según crecimiento de la organización.")
        st.divider()
        
        with st.expander("💡 Ejemplo práctico: Retail"):
            st.write("""
            Imaginemos una empresa de retail que tiene:
            - 🏬 Un sistema ERP para gestión de inventario.
            - 📇 Un CRM que almacena datos de clientes.
            - 🛒 Una plataforma de ventas online.
            
            El **DWH** recopila información de todos estos sistemas, organiza los datos por categorías
            (ventas, clientes, productos), y permite que el equipo de marketing analice:
            """)
            col1, col2 = st.columns(2)
            col1.metric(label="📈 Productos más vendidos", value="5000 unidades/mes")
            col2.metric(label="👥 Clientes más leales", value="1.200 clientes")
        
        st.divider()
        st.subheader("🎯 Beneficios de usar un DWH")
        col1, col2 = st.columns(2)
        col1.success("✅ Decisiones basadas en datos: fundamentadas en información consolidada.")
        col1.info("⚡ Análisis más rápido: evita consultas directas a sistemas transaccionales lentos.")
        col2.success("📚 Histórico confiable: mantiene datos para reportes y proyecciones.")
        col2.info("🚀 Mejora la eficiencia operativa: reduce preparación manual de reportes.")
        
        st.divider()
        with st.expander("📌 Conceptos relacionados"):
            st.write("""
            - **ETL (Extract, Transform, Load):** Extraer, transformar y cargar datos al DWH.
            - **OLAP (Online Analytical Processing):** Análisis multidimensional sobre los datos.
            - **Data Mart:** Subconjunto del DWH enfocado en un área específica de negocio.
            - **BI (Business Intelligence):** Herramientas para análisis y visualización de datos.
            """)
    
    elif page_name == "2_evolucion":
        st.markdown("<h1 style='text-align:center; color:#1e3d8f;'>📜 Evolución histórica del DWH</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size:16px; color:gray;'>Explora la evolución desde los primeros sistemas hasta la actualidad</p>", unsafe_allow_html=True)
        st.divider()
        
        eras = [
            {"title": "1980s - DSS", "icon": "📊", "subtitle": "Sistemas de soporte a decisiones",
             "points": ["Datos de sistemas transaccionales",
                        "Reportes simples para gerentes",
                        "Sistemas no estandarizados"]},
            
            {"title": "1990s - Bill Inmon & Kimball", "icon": "🏗️", "subtitle": "Nacimiento del DWH",
             "points": ["Repositorio centralizado, integrado y no volátil",
                        "Modelado dimensional y Data Marts"]},

            {"title": "2000s - ETL & OLAP", "icon": "💻", "subtitle": "Herramientas comerciales",
             "points": ["ETL automatizado (Informatica, DataStage)",
                        "Sistemas OLAP más eficientes"]},

            {"title": "2010s+ - Big Data & Cloud", "icon": "☁️", "subtitle": "Análisis avanzado",
             "points": ["DWH en la nube (Redshift, Snowflake)",
                        "Integración con AI/ML",
                        "Self-service analytics"]}
        ]
        
        st.subheader("📅 Línea temporal interactiva")
        selected = st.radio("Selecciona una época:", [f"{e['title']} {e['icon']}" for e in eras])
        
        for era in eras:
            if f"{era['title']} {era['icon']}" == selected:
                st.markdown(f"### {era['title']} {era['icon']}")
                st.markdown(f"**{era['subtitle']}**")
                for point in era["points"]:
                    st.write(f"- {point}")
                break
        
        st.divider()
        with st.expander("💡 Ejemplo práctico: Análisis de ventas"):
            st.write("""
            Antes, una empresa que quería analizar ventas tenía que esperar a que los reportes nocturnos se generaran.  
            Hoy, con DWH modernos y en la nube:
            - Analiza datos en tiempo casi real
            - Compara tendencias históricas
            - Aplica modelos de Machine Learning para predicciones
            """)
        
        st.subheader("🎯 Impacto de la evolución del DWH")
        col1, col2 = st.columns(2)
        col1.success("⚡ Mayor velocidad de análisis")
        col1.info("📚 Consolidación de datos históricos")
        col2.success("🔮 Analítica avanzada y predicciones")
        col2.info("✅ Reducción de errores por manipulación manual")
    
    elif page_name == "3_oltp_olap":
        st.title("⚙️ OLTP vs OLAP")
        st.write("""
        En el mundo de la gestión de datos, es esencial distinguir entre **OLTP** (*Online Transaction Processing*) y **OLAP** (*Online Analytical Processing*).  
        Aunque ambos manejan información, tienen **objetivos y estructuras completamente diferentes** dentro de una organización.
        """)
        st.divider()
        
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
        
        st.subheader("🔗 Relación entre OLTP y OLAP")
        st.write("""
        Los **sistemas OLTP alimentan los Data Warehouse (DWH)**, que luego son la base de los entornos **OLAP**.  
        Esta separación garantiza un **rendimiento óptimo**:  
        - Los sistemas operativos no se ven afectados por consultas analíticas.  
        - Los datos se transforman y consolidan antes del análisis.
        """)
        st.image("https://upload.wikimedia.org/wikipedia/commons/8/88/OLTP_OLAP_diagram_en.png", 
                 caption="Esquema simplificado de la relación OLTP ↔ OLAP", use_container_width=True)
    
    else:
        st.warning(f"📄 El contenido de esta página ({page_name}) aún no está disponible.")
        st.info("Esta página está en construcción. Pronto estará disponible con contenido completo.")

# Mostrar el modal si está activo
if st.session_state.show_modal and st.session_state.selected_page:
    show_page_content(st.session_state.selected_page)
    # Resetear el estado después de mostrar el modal
    st.session_state.show_modal = False
    # Limpiar la URL después de mostrar el modal
    if 'page' in st.query_params:
        st.query_params.clear()

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Creado por Ariadna, Gabriel, Teo y Oriol | Presentación DWH 2025</p>", unsafe_allow_html=True)
