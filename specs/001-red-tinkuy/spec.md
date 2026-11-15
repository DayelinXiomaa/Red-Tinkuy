# Spec 001: Red Tinkuy - Plataforma de Articulación y Financiamiento

> **Módulo:** Plataforma Web Integral para Organizaciones Juveniles Lideradas por Mujeres  
> **Estado:** Completo / Validado en Demo  
> **Evento:** Warmi Innovathon 2026 (Lead at Ulima & Makipuray · Aliado Técnico: GitHub)  
> **Equipo:** Grupo 9

## 1. Contexto y objetivo
Según el diagnóstico de la Senaju (2022), las mujeres representan el 61% de los integrantes de organizaciones juveniles en el Perú y el 53% de las representaciones oficiales. Sin embargo, el **64.4% de las organizaciones juveniles no cuenta con personería jurídica (sin SUNARP ni RUC)** y el 53% se sostiene únicamente con aportes de sus propios miembros. Red Tinkuy resuelve esta fragilidad eliminando la barrera de formalización, articulando iniciativas georreferenciadas en un mapa nacional, canalizando micro-financiamiento transparente mediante Juntta y conectando alianzas estratégicas asistidas por Inteligencia Artificial.

## 2. Propuesta de valor
* **Inclusión total sin RUC:** Permite a colectivas sin personería jurídica visibilizarse y aliarse con organizaciones formalizadas.
* **Transparencia radical:** Donaciones directas vía Juntta con trazabilidad de metas y cero comisión de intermediación por Red Tinkuy.
* **Conexión asistida por IA:** Redacción de borradores formales de convenio y sincronización automática de calendarios compartidos.
* **Seguridad jurídica:** Registro compatible con la Ley N° 29733 de Protección de Datos Personales de Perú.

## 3. Usuarias / Actores
* **Lideresas juveniles y colectivas comunitarias:** Usuarias principales que acceden desde smartphones y necesitan coordinar asambleas, registrar proyectos y recibir micro-fondos.
* **Organizaciones aliadas y ONGs constituidas:** Organizaciones que actúan como co-postulantes en desafíos de mayor escala.
* **Empresas aliadas (Inversión Social / RSE):** Sector privado que busca proyectos verificados para canalizar financiamiento con impacto medible en las regiones donde operan.

## 4. Requisitos Funcionales (EARS)

- **RF-01 (Mapa Nacional Interactivo & Perfil Verificado):**  
  *CUANDO* la usuaria accede a la vista de mapa, *EL SISTEMA* debe renderizar un mapa departamental interactivo que permita filtrar organizaciones por región (Lima, Junín, Cusco, etc.) y causa social, mostrando tarjetas de perfil con enlace directo a WhatsApp y redes sociales.

- **RF-02 (Financiamiento Transparente con Juntta):**  
  *CUANDO* la usuaria consulta un proyecto publicado, *EL SISTEMA* debe exhibir la meta recaudada en tiempo real, el presupuesto desglosado y un botón de redirección segura a Juntta para donar vía Yape, Plin o tarjeta, con rendición de cuentas obligatoria al finalizar.

- **RF-03 (Alianzas Estratégicas y Copostulación IA):**  
  *CUANDO* dos organizaciones con causas afines solicitan articulación, *EL SISTEMA* debe generar una propuesta de sinergia, redactar un borrador estructurado de convenio y cruzar calendarios para coordinar la primera reunión.

- **RF-04 (Calendario Propio y Cruzado):**  
  *CUANDO* se agendan talleres, asambleas o foros, *EL SISTEMA* debe consolidarlos en un calendario nacional visible para evitar cruces de fechas entre iniciativas comunitarias.

- **RF-05 (Registro y Protección de Datos Ley 29733):**  
  *MIENTRAS* se realiza el registro formal de una organización, *EL SISTEMA* debe solicitar el consentimiento explícito y documentado del tratamiento de datos personales conforme a la Ley N° 29733 antes de guardar la información.

- **RF-06 (Portal Corporativo de Inversión Social):**  
  *CUANDO* una empresa accede al portal corporativo, *EL SISTEMA* debe mostrar desafíos de financiamiento RSE y proyectos comunitarios verificados con trazabilidad de inversión.

## 5. Requisitos No Funcionales
* **Mobile-First & Ultraligero:** La página debe cargar en menos de 2 segundos en conexiones móviles sin dependencias pesadas.
* **Cumplimiento legal peruano:** Cláusulas de consentimiento expreso para datos personales según Ley N° 29733.
* **Diseño accesible:** Tipografía legible, carrusel 3D Coverflow accesible y contraste adecuado (WCAG).
