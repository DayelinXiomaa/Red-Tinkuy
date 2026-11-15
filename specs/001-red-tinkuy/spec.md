# Spec 001: Red Tinkuy - Plataforma de Articulación y Financiamiento

> **Módulo:** Plataforma Web Integral para Organizaciones Juveniles Lideradas por Mujeres  
> **Estado:** Completo / Validado en Demo  
> **Evento:** Warmi Innovathon 2026 (Lead at Ulima & Makipuray · Reto ONG Ubuntu)

## 1. Contexto y objetivo
Las organizaciones juveniles y colectivas de base lideradas por mujeres en el Perú sufren aislamiento operativo: coordinan mediante chats dispersos, carecen de cuentas bancarias auditables para recaudación y no logran visibilidad ante donantes o convocatorias públicas (SENAJU, APCI). **Red Tinkuy** resuelve este problema centralizando comunicación, financiamiento transparente con Juntta y alianzas estratégicas asistidas por IA.

## 2. Propuesta de valor
* **Inclusión total:** Permite a colectivas sin RUC asociarse con ONGs formalizadas para co-postular a financiamiento.
* **Transparencia radical:** Donaciones directas vía Juntta con trazabilidad de metas y cero comisión de intermediación.
* **Seguridad jurídica:** Registro compatible con la Ley N° 29733 de Protección de Datos Personales de Perú.

## 3. Usuarias / Actores
* **Lideresas juveniles y miembros de colectivas:** Usuarias principales que acceden desde smartphones y necesitan coordinar asambleas, registrar proyectos y recibir micro-fondos.
* **ONGs formalizadas (con RUC / SUNARP / APCI):** Organizaciones con personería jurídica que actúan como madrinas/co-postulantes en desafíos de mayor escala.
* **Empresas donantes / RSE:** Organizaciones del sector privado que buscan proyectos verificados para canalizar inversión social con impacto cuantificable.

## 4. Requisitos Funcionales (EARS)

- **RF-01 (Mapa Nacional Interactivo):**  
  *CUANDO* la usuaria accede a la vista de mapa, *EL SISTEMA* debe renderizar un mapa departamental interactivo que permita filtrar organizaciones por región (Lima, Cusco, Junín, etc.) y causa social, mostrando tarjetas de perfil con enlace directo a WhatsApp.

- **RF-02 (Financiamiento Transparente Juntta):**  
  *CUANDO* la usuaria consulta un proyecto publicado, *EL SISTEMA* debe exhibir la meta recaudada en tiempo real, el porcentaje completado y un botón de redirección segura a Juntta para donar vía Yape, Plin o tarjeta.

- **RF-03 (Alianzas Estratégicas y Copostulación IA):**  
  *CUANDO* dos organizaciones con causas afines solicitan articulación, *EL SISTEMA* debe generar una propuesta de sinergia y un borrador estructurado de convenio interinstitucional para postulación conjunta.

- **RF-04 (Calendario Cruzado de Eventos):**  
  *CUANDO* se agendan talleres, asambleas o foros, *EL SISTEMA* debe consolidarlos en un calendario nacional visible para evitar cruces de fechas entre iniciativas comunitarias.

- **RF-05 (Registro y Protección de Datos Ley 29733):**  
  *MIENTRAS* se realiza el registro formal de una organización, *EL SISTEMA* debe solicitar el consentimiento explícito y documentado del tratamiento de datos personales conforme a la Ley N° 29733 antes de guardar la información.

- **RF-06 (Portal B2B de Inversión Social):**  
  *CUANDO* una empresa accede al portal corporativo, *EL SISTEMA* debe mostrar desafíos de financiamiento RSE y proyectos comunitarios verificados con trazabilidad de inversión.

## 5. Requisitos No Funcionales
* **Mobile-First & Ligereza:** La página debe cargar en menos de 2 segundos en conexiones móviles 3G/4G sin dependencias pesadas.
* **Cumplimiento legal peruano:** Cláusulas de consentimiento expreso para datos personales y validación de RUC de 11 dígitos.
* **Diseño accesible:** Tipografía legible, navegación por teclado y contraste cromático adecuado según lineamientos WCAG.
