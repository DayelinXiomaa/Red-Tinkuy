"""
Pruebas Automatizadas de Requisitos Funcionales (Spec-Driven Development)
Proyecto: Red Tinkuy - Warmi Innovathon 2026 (Grupo 9)
Requisitos evaluados: RF-01 al RF-06 de specs/001-red-tinkuy/spec.md
"""

import os
import re
import pytest
from bs4 import BeautifulSoup

@pytest.fixture(scope="module")
def html_soup():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(base_dir, "index.html")
    assert os.path.exists(index_path), f"No se encontró index.html en {index_path}"
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    return soup, content

# RF-01: Directorio Georreferenciado con Mapa Interactivo Departamental
def test_rf01_mapa_interactivo_y_directorio(html_soup):
    soup, content = html_soup
    # Verificar existencia de sección de mapa o SVG
    svg_maps = soup.find_all("svg")
    assert len(svg_maps) > 0, "RF-01 Falló: No se encontró gráfico SVG interactivo"
    
    # Verificar mención a departamentos clave
    assert "Cusco" in content or "Lima" in content, "RF-01 Falló: Faltan regiones en el mapa"
    
    # Verificar botón o enlace a WhatsApp directo
    wa_elements = [el for el in soup.find_all(["a", "button"]) if "wa.me" in str(el) or "whatsapp" in str(el).lower()]
    assert len(wa_elements) > 0, "RF-01 Falló: No se encontró botón directo a WhatsApp"

# RF-02: Módulo de Transparencia y Micro-recaudación con Juntta
def test_rf02_financiamiento_juntta_y_transparencia(html_soup):
    soup, content = html_soup
    # Verificar integración visual y conceptual de Juntta
    assert "juntta" in content.lower(), "RF-02 Falló: No se menciona la plataforma Juntta"
    
    # Verificar proyecto Warmikuna Puririsun y meta de fondos
    assert "Warmikuna" in content or "Puririsun" in content, "RF-02 Falló: Falta proyecto ancla de financiamiento"
    assert "84%" in content or "S/." in content or "S/ 1." in content, "RF-02 Falló: Falta indicador de recaudación"

# RF-03: Motor de Alianzas y Generación de Convenios con IA
def test_rf03_alianzas_estrategicas_e_ia(html_soup):
    soup, content = html_soup
    # Verificar presencia de módulo de alianzas con IA
    assert "alianzas" in content.lower() and "ia" in content.lower(), "RF-03 Falló: No se encontró el módulo de Alianzas IA"
    
    # Verificar función de emparejamiento o compatibilidad
    assert "sinergia" in content.lower() or "compatibilidad" in content.lower() or "alianza" in content.lower()

# RF-04: Calendario Cruzado de Actividades y Eventos Nacionales
def test_rf04_calendario_eventos_y_cruce(html_soup):
    soup, content = html_soup
    # Verificar visualizador de calendario
    calendar_elements = soup.find_all(attrs={"class": re.compile(r"calendar|event", re.I)})
    assert len(calendar_elements) > 0 or "calendario" in content.lower(), "RF-04 Falló: No se encontró el módulo de calendario"

# RF-05: Formulario de Registro Escalonado con Protección de Datos Ley N° 29733
def test_rf05_registro_y_proteccion_datos_ley_29733(html_soup):
    soup, content = html_soup
    # Verificar formulario de registro
    reg_form = soup.find(id="view-register")
    assert reg_form is not None, "RF-05 Falló: No se encontró la vista de registro"
    
    # Verificar cláusula obligatoria de la Ley N° 29733
    assert "29733" in content, "RF-05 Falló: Falta la referencia a la Ley N° 29733 de Protección de Datos Personales"
    
    # Verificar campo RUC (11 dígitos)
    ruc_input = soup.find(attrs={"id": re.compile(r"ruc", re.I)})
    assert ruc_input is not None, "RF-05 Falló: Falta el campo de validación de RUC"

# RF-06: Portal Corporativo B2B de Inversión Social y Desafíos RSE
def test_rf06_portal_b2b_empresas_y_rse(html_soup):
    soup, content = html_soup
    # Verificar vista de empresas
    emp_view = soup.find(id="view-empresas")
    assert emp_view is not None, "RF-06 Falló: No se encontró la vista B2B de empresas"
    
    # Verificar acordeón de preguntas frecuentes y desafíos RSE
    assert "rse" in content.lower() or "preguntas frecuentes" in content.lower(), "RF-06 Falló: Faltan desafíos RSE o FAQs"

# Prueba de Calidad e Identidad de Marca
def test_calidad_e_identidad_de_marca(html_soup):
    soup, content = html_soup
    # Verificar paleta institucional #6d2867
    assert "#6d2867" in content.lower(), "Calidad Falló: Falta el color primario de marca #6d2867"
    
    # Verificar eslogan
    assert "donde las iniciativas se encuentran" in content.lower()

# Prueba de Carrusel Coverflow 3D
def test_carrusel_coverflow_3d(html_soup):
    soup, content = html_soup
    # Verificar que el carrusel cuenta con las 6 tarjetas de características
    carousel_cards = soup.find_all(attrs={"class": re.compile(r"feature-card-carousel")})
    assert len(carousel_cards) == 6, f"Coverflow Falló: Se esperaban 6 tarjetas en el carrusel, se encontraron {len(carousel_cards)}"
