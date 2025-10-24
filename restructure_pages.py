#!/usr/bin/env python3
"""
Script para reestructurar todas las páginas con diseño glassmorphism moderno
"""

import re
from pathlib import Path

def create_header(title, subtitle):
    """Crea un header glassmorphism"""
    return f'''st.markdown("""
<div style="
    text-align: center;
    padding: 40px 20px;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    margin: 20px 0 40px 0;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    <h1 style='color: #ffffff; font-size: 2.8rem; margin-bottom: 10px; text-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);'>
        {title}
    </h1>
    <p style='color: #b8c5d6; font-size: 1.1rem;'>
        {subtitle}
    </p>
</div>
""", unsafe_allow_html=True)
'''

def wrap_section_title(title):
    """Envuelve un título de sección en un card glassmorphism"""
    return f'''st.markdown("""
<div style="
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 30px;
    margin: 40px 0 30px 0;
    border: 1px solid rgba(255, 255, 255, 0.1);
">
    <h2 style='color: #ffffff; text-align: center;'>{title}</h2>
</div>
""", unsafe_allow_html=True)
'''

def wrap_content_card(content):
    """Envuelve contenido en un card glassmorphism"""
    return f'''st.markdown("""
<div style="
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 30px;
    margin: 20px 0;
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
">
    {content}
</div>
""", unsafe_allow_html=True)
'''

def process_page(file_path):
    """Procesa un archivo de página"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer el título principal
    title_match = re.search(r'st\.markdown\(["\']<h1[^>]*>([^<]+)</h1>', content)
    if not title_match:
        title_match = re.search(r'st\.title\(["\']([^"\']+)["\']', content)
    
    if title_match:
        title = title_match.group(1).strip()
        print(f"✅ Procesando: {file_path.name} - {title}")
    else:
        print(f"⚠️  No se encontró título en: {file_path.name}")
        return False
    
    return True

# Procesar todas las páginas
pages_dir = Path(__file__).parent / "pages"

print("🎨 Iniciando reestructuración de páginas...\n")

for page_file in sorted(pages_dir.glob("*.py")):
    process_page(page_file)

print("\n✨ Proceso completado!")

