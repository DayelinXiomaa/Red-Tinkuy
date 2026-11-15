# Red-Tinkuy

> **Donde las iniciativas se encuentran y multiplican.**  
> Una plataforma web para que las organizaciones juveniles lideradas por mujeres se comuniquen, se financien y se organicen en un solo lugar.

**Warmi Innovathon 2026** · Reto de la ONG · **Equipo:** Red Tinkuy · **Demo:** [red-tinkuy.vercel.app](https://red-tinkuy.vercel.app)

*Evento organizado por **Lead at Ulima** y **Makipuray**, con la **ONG Ubuntu** como autora del reto y **GitHub** como aliado técnico.*

---

## 📌 El problema

En el Perú, decenas de colectivas comunitarias y organizaciones juveniles lideradas por mujeres trabajan de forma aislada, dependiendo de herramientas fragmentadas: grupos de WhatsApp saturados, correos que nadie responde, formularios manuales y publicaciones efímeras en redes sociales. 

Esta desconexión genera tres barreras críticas:
1. **Pérdida de alcance y visibilidad:** Sus actividades y convocatorias no llegan más allá de su círculo inmediato de contactos.
2. **Brecha de financiamiento y formalidad:** Carecen de canales auditables para recaudar micro-donaciones y quedan descalificadas de fondos corporativos o de cooperación internacional por no contar con RUC o personería jurídica consolidada.
3. **Descoordinación de agendas:** Se cruzan talleres y asambleas entre organizaciones con objetivos afines, duplicando esfuerzos y agotando a sus lideresas.

### 📊 Lo que escuchamos (Validación de campo)
Aplicamos una encuesta a **20 lideresas y miembros de organizaciones juveniles** (principalmente en Lima y Junín), obteniendo los siguientes hallazgos clave:
* **85%** coordina sus actividades únicamente por mensajería instantánea, perdiendo convocatorias, actas y acuerdos importantes.
* **90%** reporta dificultades críticas para financiar sus eventos y depende de aportes personales o rifas sin trazabilidad para donantes externos.
* **75%** no postula a fondos institucionales por trabas burocráticas y falta de alianzas con ONGs de mayor trayectoria.

---

## 💡 Nuestra solución

**Red Tinkuy** es una plataforma web integral, ligera y pensada especialmente para lideresas de organizaciones pequeñas que acceden principalmente desde el celular:

1. **🗺️ Mapa Nacional Interactivo & Directorio Verificado:** Permite georreferenciar a cada organización por región y causa social (igualdad de género, educación, medio ambiente, derechos juveniles), con perfil verificado y enlace directo a WhatsApp.
2. **💳 Micro-Recaudación Transparente con Juntta:** Módulo de financiamiento colectivo con metas claras, seguimiento de gastos en tiempo real y recaudación directa mediante pasarelas (Yape, Plin y tarjeta) con **cero comisiones retenidas por Red Tinkuy**.
3. **🤝 Alianzas y Co-postulación asistida por IA:** Motor de emparejamiento que conecta colectivas de base con ONGs formalizadas, permitiéndoles postular en conjunto a fondos corporativos y generando borradores automáticos de convenios de alianza.
4. **🗓️ Calendario Propio y Cruzado:** Agenda comunitaria compartida que evita cruces de fechas y facilita la asistencia mutua a foros, talleres y asambleas.
5. **🏢 Portal de Inversión Social (RSE para Empresas):** Espacio B2B para que empresas aliadas canalicen financiamiento a proyectos auditables con impacto medible en las regiones donde operan.

### 🎯 ¿Para quién es?
Lideresas, voluntarias y miembros de organizaciones juveniles del Perú, activas tanto en Lima como en regiones, que necesitan una herramienta intuitiva desde su smartphone sin requerir conocimientos técnicos avanzados.

### 🌟 ¿Qué la hace distinta?
* **Diseño inclusivo y sin barreras burocráticas:** Permite participar tanto a colectivas no formalizadas como a ONGs constituidas mediante el mecanismo de alianzas estratégicas.
* **Cumplimiento estricto de la Ley N° 29733 (Protección de Datos Personales):** Consentimiento informado, explícito y auditable en el registro de voluntarias y lideresas.
* **Arquitectura ultra ligera (Mobile-First):** Carga instantánea en cualquier teléfono móvil, carrusel 3D Coverflow accesible y mapa SVG vectorial sin consumo excesivo de datos móviles.

---

## 🚀 Demo en vivo

* **Enlace de Producción:** [https://red-tinkuy.vercel.app](https://red-tinkuy.vercel.app)
* **Código fuente en GitHub:** [https://github.com/DayelinXiomaa/Red-Tinkuy](https://github.com/DayelinXiomaa/Red-Tinkuy)

### Pruébala en 3 pasos:
1. **Explora el Mapa:** Ingresa a la plataforma y filtra por departamentos (ej. Cusco, Lima, Junín) o selecciona una causa para ver las iniciativas en acción.
2. **Conoce el Financiamiento Juntta:** Revisa la tarjeta de recaudación en vivo de la organización *Warmikuna Puririsun*, con su meta de financiamiento y botón de aporte directo.
3. **Simula una Alianza Estratégica:** Visita la sección de alianzas para ver cómo la IA detecta sinergias y co-diseña propuestas de financiamiento conjunto.

---

## ⚙️ Funcionalidades y Requisitos (Spec-Driven)

Cada funcionalidad responde a un Requisito Funcional (RF) especificado en la arquitectura:

- [x] **RF-01:** Directorio Georreferenciado con Mapa Interactivo Departamental (`specs/001-red-tinkuy/spec.md`)
- [x] **RF-02:** Módulo de Transparencia y Micro-recaudación con Juntta (`specs/001-red-tinkuy/spec.md`)
- [x] **RF-03:** Motor de Alianzas y Generación de Convenios con IA (`specs/001-red-tinkuy/spec.md`)
- [x] **RF-04:** Calendario Cruzado de Actividades y Eventos Nacionales (`specs/001-red-tinkuy/spec.md`)
- [x] **RF-05:** Formulario de Registro Escalonado con Protección de Datos Ley N° 29733 (`specs/001-red-tinkuy/spec.md`)
- [x] **RF-06:** Portal Corporativo B2B de Inversión Social y Desafíos RSE (`specs/001-red-tinkuy/spec.md`)

El detalle completo se encuentra documentado en [`specs/001-red-tinkuy/spec.md`](specs/001-red-tinkuy/spec.md).

---

## 🛠️ Tecnologías utilizadas

| Área | Herramienta / Tecnología | Justificación técnica |
|---|---|---|
| **Frontend** | **HTML5 Semántico + CSS3 Moderno** | Flexbox, CSS Grid, variables CSS fluidas y animaciones nativas sin dependencias pesadas. |
| **Lógica e Interactividad** | **JavaScript ES6+ (SPA)** | Lógica reactiva en cliente, carrusel 3D Coverflow táctil, cálculo de estados y filtros instantáneos. |
| **Cartografía** | **SVG Vectorial Interactivo** | Mapa geográfico de los 24 departamentos sin peso de librerías externas para carga móvil rápida. |
| **Despliegue y Hosting** | **Vercel + GitHub Actions** | Integración continua (CI/CD), despliegue automático ante cada `push` a `main` y CDN con SSL. |
| **Inteligencia Artificial** | **GitHub Copilot + Modelos Asistentes** | Asistencia en la arquitectura de especificaciones, optimización de código y diseño responsivo. |
| **Control de Versiones** | **Git & GitHub** | Flujo de trabajo colaborativo mediante Pull Requests, ramas y revisiones de código. |

---

## 🤖 Uso de IA y originalidad

En **Red Tinkuy** utilizamos Inteligencia Artificial de forma ética y responsable como herramienta de aceleración durante el hackathon:
* **La IA propone, el equipo decide:** La IA se empleó como apoyo técnico para la redacción de especificaciones, depuración de estilos y optimización del código.
* **Originalidad:** El concepto, la investigación con lideresas de Lima y Junín, la propuesta de valor social y el modelo de alianza informales-formales para resolver el reto de la **ONG Ubuntu** fueron ideados y validados íntegramente por el equipo.

---

## 💻 Cómo ejecutar el proyecto localmente

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/DayelinXiomaa/Red-Tinkuy.git
   cd Red-Tinkuy
   ```

2. **Ejecutar la aplicación:**
   Al ser una aplicación web estandarizada, puedes abrirla de inmediato de cualquiera de las siguientes formas:
   * **Opción A (Directa):** Abre el archivo `index.html` en tu navegador favorito haciendo doble clic.
   * **Opción B (Servidor local ligero con Node.js):**
     ```bash
     npx serve .
     ```
   * **Opción C (Servidor local con Python):**
     ```bash
     python -m http.server 8000
     ```
     Luego ingresa a `http://localhost:8000`.

---

## 🏗️ Cómo lo construimos (Spec-Driven Development)

Seguimos una metodología guiada por especificaciones (**SDD**), asegurando orden desde la formulación del problema hasta la entrega final:

| Fase | Archivo de referencia |
|---|---|
| **Reto de la ONG** | [docs/RETO.md](docs/RETO.md) |
| **Principios y Constitución** | [docs/constitution.md](docs/constitution.md) |
| **Especificaciones y Requisitos** | [specs/001-red-tinkuy/spec.md](specs/001-red-tinkuy/spec.md) |
| **Plan y Tareas** | [specs/001-red-tinkuy/plan.md](specs/001-red-tinkuy/plan.md) |
| **Código Principal** | `index.html` y carpeta `assets/` |
| **Despliegue Continuo** | Vercel CI / GitHub Pages |
| **Guion de Pitch** | [docs/pitch.md](docs/pitch.md) |

---

## 👥 Equipo

Equipo multidisciplinario del **Warmi Innovathon 2026**:

| Nombre | Rol / Especialidad | Responsabilidades en el proyecto | GitHub |
|---|---|---|---|
| **Dayelin Xiomara** | Líder Técnica / Frontend Developer | Arquitectura web, desarrollo responsive, integración de vistas y despliegue Vercel | [@DayelinXiomaa](https://github.com/DayelinXiomaa) |
| **Kely Isabel** | UX Research & Validación de Impacto | Investigación de usuarias, diseño de encuestas en Lima/Junín y propuesta social | — |
| **Equipo Red Tinkuy** | Negocio & Pitch | Modelo de sostenibilidad, propuesta de valor para empresas y preparación de la presentación final | — |

---

## 📅 Fechas clave del evento

| Fecha | Hito |
|---|---|
| Jueves 12 de noviembre | Capacitación 1 (virtual): Ideación y definición del problema |
| Viernes 13 de noviembre | Capacitación 2 (virtual): Desarrollo técnico con GitHub e IA |
| Sábado 14 de noviembre | Capacitación 3 (virtual): Modelo de negocio y pitch |
| **Domingo 15, 11:59 p. m.** | **Entrega oficial: Repositorio GitHub y demo desplegada** |
| **Lunes 16, 3:00 a 7:00 p. m.** | **Final presencial en las oficinas de Microsoft:** Ajustes, pitch de 5 minutos ante el jurado y premiación |

---

## ✅ Checklist de entrega

- [x] **README completo:** Problema validado, solución, demo en vivo, tecnologías y equipo.
- [x] **Rama `main` operativa:** Probada, limpia y ejecutable en cualquier máquina.
- [x] **Especificaciones técnicas:** Carpeta `specs/` documentando requisitos funcionales (RF).
- [x] **Demo publicada:** Desplegada en Vercel con certificado SSL y accesible vía web y móvil.
- [x] **Privacidad y Seguridad:** Sin credenciales expuestas y con cláusulas de la Ley N° 29733.
- [x] **Repositorio público:** Abierto para revisión del jurado y la comunidad.
- [x] **Documento de Pitch listo:** [`docs/pitch.md`](docs/pitch.md) preparado para la sustentación presencial de 5 minutos en Microsoft.
