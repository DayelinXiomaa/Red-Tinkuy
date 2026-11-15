# Red Tinkuy — Arquitectura y Flujo de la Plataforma de ONGs del Perú

## 1. Visión y Propósito
**Red Tinkuy** (*"Tinkuy"* significa encuentro en quechua) es la plataforma digital concebida para articular, visibilizar y fortalecer a organizaciones sin fines de lucro, colectivos juveniles y organizaciones de base en el Perú. 

La plataforma resuelve el problema de la fragmentación del ecosistema civil:
- Las alianzas no dependen de la cercanía física sino del **impacto y la sinergia de propósitos**.
- La confianza institucional se construye con **validación formal (SUNARP / RENOJ-SENAJU / APCI)**.
- El financiamiento es transparente y auditable a través de la integración de **Juntta** (la plataforma peruana de donaciones con trazabilidad bancaria en tiempo real, sin que Red Tinkuy procese o retenga fondos).
- La articulación entre directivas se acelera con un **asistente de IA** que redacta propuestas y sincroniza agendas.

---

## 2. Flujo de Navegación del Usuario (UX Architecture)

```
[Visitante / No Registrada]
            │
            ▼
┌────────────────────────────────────────────────────────┐
│  Panel Informativo Público (Landing)                   │
│  - Hero con métricas nacionales (24 regiones, +180 ONGs)│
│  - Beneficios de incorporarse a la Red                 │
│  - Llamadas de Acción (CTAs): Explorar o Registrarse    │
└───────────────────────────┬────────────────────────────┘
                            │ Clic en "Registrar organización"
                            ▼
┌────────────────────────────────────────────────────────┐
│  Formulario de Registro Formal de ONG                  │
│  - Nombre de la ONG y Razón Social                     │
│  - RUC activo (11 dígitos) y Año de inicio             │
│  - Acreditación: SENAJU (RENOJ), SUNARP o APCI         │
│  - Número de beneficiados y Miembros activos           │
│  - Región, Enfoque temático y WhatsApp directo         │
│  - Misión (utilizada por el motor de IA para matches)  │
└───────────────────────────┬────────────────────────────┘
                            │ Envío validado y verificación automática
                            ▼
┌────────────────────────────────────────────────────────┐
│  Plataforma Integral Red Tinkuy (Dashboard 6 Módulos) │
│                                                        │
│  1. Mapa Interactivo & Perfil Verificado               │
│  2. Financiamiento Transparente con Juntta             │
│  3. Alianzas Estratégicas con Inteligencia Artificial  │
│  4. Calendarios y Disponibilidad Compartida            │
│  5. Tablón de Fondos y Convocatorias 2026-2027         │
│  6. Mi Organización y Rendición de Cuentas             │
└────────────────────────────────────────────────────────┘
```

---

## 3. Detalle de los 6 Módulos Interactivos

### Módulo 1: Mapa Interactivo con Perfil Verificado
* **Visualización Georreferenciada:** Mapa SVG del Perú con las 24 regiones debidamente coordinadas.
* **Filtros duales:** Por región geográfica y por eje temático (*Liderazgo Comunitario, Violencia de Género, Educación, Emprendimiento, Medio Ambiente, Derechos Humanos*).
* **Ficha de Organización:** Al hacer clic en cualquier ONG, se despliega su perfil con Razón Social, RUC, insignia de verificación, cantidad de beneficiados, enlaces directos a WhatsApp, Instagram y Facebook.
* **Datos incorporados:** Se integraron organizaciones históricas y territoriales del Perú como *Centro Flora Tristán (Lima/Cusco)*, *Movimiento Manuela Ramos (Lima)*, *DEMUS*, *Warmikuna Puririsun (Cusco)*, *Asociación Kallpa (Cusco/Loreto)*, *Warmi Junín (Huancayo)*, *Volcán Violeta (Arequipa)*, *Amazonas Vivas (Loreto)*, *Norte Solidario (Piura)*, *Altiplano Mujer (Puno)* y *Huaraz Activa (Áncash)*.

### Módulo 2: Financiamiento Transparente con Juntta
* **Modelo sin custodia:** Red Tinkuy **no procesa ni retiene dinero**, eliminando cualquier riesgo de desconfianza.
* **Conexión con Juntta:** Cada proyecto cuenta con barra de avance en tiempo real (Soles recaudados vs. Meta), días restantes y botón directo *"Apoyar este proyecto en Juntta"*.
* **Rendición de cuentas:** Al cerrar el proyecto, la organización publica en su perfil el reporte fotográfico y el balance de gastos.
* **Publicación ágil:** Las organizaciones registradas pueden crear una nueva campaña en segundos mediante el modal interactivo.

### Módulo 3: Alianzas con Apoyo de Inteligencia Artificial
* **Algoritmo de Compatibilidad:** Analiza la complementariedad temática, territorio y misión.
* **Redacción de Borrador Formal:** La IA genera una carta de intención formal lista para enviar a la otra organización con un clic.
* **Sincronizador de Horarios:** Cruza los calendarios de ambas directivas y detecta el primer horario disponible compartido, pasando de la propuesta a la reunión sin cadenas interminables de mensajes.

### Módulo 4: Calendario Propio y Agenda Nacional
* Publicación de talleres, ferias y asambleas comunitarias con fecha, hora y modalidad (Zoom o presencial).
* Configuración de la ventana de disponibilidad semanal del equipo de la ONG para reuniones de alianza.

### Módulo 5: Tablón de Convocatorias y Fondos
* Oportunidades activas 2026-2027: Fondo AECID / Red Tinkuy, Premio Nacional de Juventudes de la SENAJU, y Fondos de Innovación Juntta-Empresas con match funding *pari-passu*.

### Módulo 6: Mi Perfil y Reputación Formal
* Panel de administración de la organización con sello de formalidad (RENOJ-SENAJU / SUNARP / APCI).
* Indicadores clave de impacto: Beneficiados anuales, miembros activos del equipo y módulo de carga de balances y rendición de resultados.

---

## 4. Guía de Identidad Visual y UI/UX Aplicada
* **Tipografías:** `Outfit` (titulares expresivos y modernos) + `Plus Jakarta Sans` (cuerpo de texto nítido y legible).
* **Paleta de Colores:**
  - Primario: `#5a0e53` (Vino andino / Tinkuy).
  - Acento: `#9B3B91` y `#E8B8D9` (Tonos violetas y fucsias de empoderamiento social).
  - Oro Cálido: `#D97706` (Botones de acción de Juntta y financiamiento).
  - Verde Esmeralda: `#059669` (Insignia de organización verificada formal).
  - Fondo: `#FAF7F9` (Blanco cálido de alta legibilidad y confort visual).
