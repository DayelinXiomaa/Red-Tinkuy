# Tareas: Spec 001 - Red Tinkuy

> **Metodología Spec-Driven Development (SDD)**  
> Cada tarea corresponde a uno o más Requisitos Funcionales (RF) de `specs/001-red-tinkuy/spec.md`.  
> Regla: **Una tarea = un área = una persona = una rama = un PR**.

---

## Tareas por Módulos y Áreas

### 🗺️ Módulo 1: Mapa Interactivo y Directorio Georreferenciado (RF-01)
- [x] **T1.1 - [Diseño] Boceto de mapa vectorial de Perú y fichas de iniciativas**
  * Área: `área: diseño`
  * Cumple: RF-01
  * Hecho cuando: El diseño define la paleta morada `#6d2867`, estados hover/active de cada departamento y la estructura de la tarjeta de contacto.
- [x] **T1.2 - [Frontend] Implementación del mapa SVG interactivo y filtros por causa**
  * Área: `área: frontend`
  * Cumple: RF-01
  * Hecho cuando: Al hacer clic en un departamento o causa social, se filtran las organizaciones en tiempo real sin recargar la página.
- [x] **T1.3 - [Backend-Datos] Estructura de datos JSON de organizaciones verificadas**
  * Área: `área: backend-datos`
  * Cumple: RF-01
  * Hecho cuando: Cada organización cuenta con departamento, causa, enlace directo a WhatsApp y sello de formalidad SUNARP/RENOJ.

---

### 💳 Módulo 2: Financiamiento Transparente con Juntta (RF-02)
- [x] **T2.1 - [Diseño] Tarjeta de recaudación y barra de progreso de metas**
  * Área: `área: diseño`
  * Cumple: RF-02
  * Hecho cuando: La barra de progreso refleja visualmente el % alcanzado con contraste legible y tipografía jerárquica.
- [x] **T2.2 - [Frontend] Integración del botón de donaciones y flujo Juntta**
  * Área: `área: frontend`
  * Cumple: RF-02
  * Hecho cuando: El botón de aporte despliega el modal interactivo con opciones de Yape/Plin/Tarjeta y conciliación en tiempo real.
- [x] **T2.3 - [Pruebas] Validación del flujo de aporte y reporte de gastos**
  * Área: `área: pruebas`
  * Cumple: RF-02
  * Hecho cuando: Se comprueba que la meta se actualiza correctamente y los reportes de egresos son descargables en PDF.

---

### 🤝 Módulo 3: Alianzas y Co-postulación asistida por IA (RF-03)
- [x] **T3.1 - [Lógica] Algoritmo de emparejamiento por afinidad de misión**
  * Área: `área: backend-datos`
  * Cumple: RF-03
  * Hecho cuando: La función cruza la causa de una colectiva de base con una ONG acreditada y calcula el porcentaje de compatibilidad.
- [x] **T3.2 - [Frontend] Generador visual de borradores de convenios con IA**
  * Área: `área: frontend`
  * Cumple: RF-03
  * Hecho cuando: Al pulsar "Generar Alianza IA", se redacta el borrador formal con cláusulas de postulación conjunta y sincronización de agendas.

---

### 🗓️ Módulo 4: Calendario Cruzado de Actividades (RF-04)
- [x] **T4.1 - [Frontend] Visualizador de calendario nacional y eventos compartidos**
  * Área: `área: frontend`
  * Cumple: RF-04
  * Hecho cuando: El calendario muestra las actividades del mes distinguiendo talleres abiertos, asambleas y convocatorias.

---

### 🛡️ Módulo 5: Registro y Protección de Datos Ley N° 29733 (RF-05)
- [x] **T5.1 - [Diseño / Legal] Modal de términos y consentimiento expreso informado**
  * Área: `área: diseño`
  * Cumple: RF-05
  * Hecho cuando: El modal contiene la política de privacidad conforme a la Ley N° 29733 de Perú y exige confirmación obligatoria.
- [x] **T5.2 - [Frontend] Formulario de registro escalonado con validación de RUC**
  * Área: `área: frontend`
  * Cumple: RF-05
  * Hecho cuando: El formulario valida formato de 11 dígitos numéricos para organizaciones formales y permite registro comunitario a colectivas de base.

---

### 🏢 Módulo 6: Portal Corporativo B2B para Empresas (RF-06)
- [x] **T6.1 - [Frontend] Vista B2B de Desafíos de Sostenibilidad y RSE**
  * Área: `área: frontend`
  * Cumple: RF-06
  * Hecho cuando: Las empresas visualizan indicadores de inversión, trazabilidad de impacto y convocatorias corporativas abiertas.

---

### 🚀 Despliegue, Calidad y Pitch
- [x] **T7.1 - [Despliegue] Pipeline de CI/CD y publicación en Vercel**
  * Área: `área: despliegue`
  * Hecho cuando: La web está desplegada en `https://red-tinkuy.vercel.app` con certificado SSL y responde en dispositivos móviles.
- [x] **T7.2 - [Docs] Documentación oficial, README y Guion de Pitch**
  * Área: `área: docs-pitch`
  * Hecho cuando: `README.md` y `docs/pitch.md` están listos con datos de la encuesta y guion de 5 minutos para la sustentación.
