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
    
    # Cargar y ejecutar el contenido de la página correspondiente
    page_file = pathlib.Path(__file__).parent / "pages" / f"{page_name}.py"
    
    if page_file.exists():
        # Leer el contenido del archivo
        with open(page_file, 'r', encoding='utf-8') as f:
            page_content = f.read()
        
        # Eliminar las líneas de configuración de página que causan conflicto
        lines_to_remove = [
            "import streamlit as st",
            "st.set_page_config"
        ]
        
        content_lines = page_content.split('\n')
        filtered_lines = []
        skip_next = False
        
        for line in content_lines:
            # Skip import streamlit y set_page_config
            if any(remove in line for remove in lines_to_remove):
                if "st.set_page_config" in line:
                    skip_next = True
                continue
            if skip_next and line.strip() == "":
                skip_next = False
                continue
            skip_next = False
            filtered_lines.append(line)
        
        # Ejecutar el código filtrado
        try:
            exec('\n'.join(filtered_lines))
        except Exception as e:
            st.error(f"Error al cargar el contenido: {str(e)}")
            st.code('\n'.join(filtered_lines[:50]))  # Mostrar primeras líneas para debug
    else:
        st.warning(f"📄 El archivo de la página ({page_name}.py) no existe.")
        st.info("Verifica que el archivo esté en la carpeta 'pages'.")

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
