# Red-Tinkuy

**Una plataforma web para que las organizaciones juveniles lideradas por mujeres se comuniquen, se financien y se organicen en un solo lugar.**

Warmi Innovathon 2026 · Reto de la ONG Ubuntu · Equipo: `[nombre del equipo]` · Demo: `[enlace pendiente]`

## El problema

Muchas organizaciones juveniles lideradas por mujeres trabajan con herramientas dispersas: chats, correos sueltos, hojas de cálculo y redes sociales. Les cuesta comunicarse con su comunidad, financiar sus eventos y mantener un calendario claro. Sin un espacio propio, pierden tiempo y alcance, y muchas iniciativas se apagan antes de crecer.

**Lo que escuchamos:** aplicamos una encuesta a 20 personas, sobre todo de Lima y Junín, para validar el problema. `[agregar 2 o 3 hallazgos clave cuando esté el informe]`

## Nuestra solución

Un sitio web con cuatro herramientas pensadas para organizaciones pequeñas y con poco presupuesto:

- **Comunicación comunitaria:** avisos y mensajes a sus integrantes y su comunidad.
- **Correos:** envío de comunicados sin depender de herramientas complicadas.
- **Micro recaudación:** financiar eventos con aportes pequeños de la comunidad.
- **Calendario de eventos:** todas las actividades en un solo lugar.

**¿Para quién es?** Lideresas y miembros de organizaciones juveniles del Perú, que entran desde el celular y no son personas técnicas.

**¿Qué la hace distinta?**

- Todo en un solo lugar, en lenguaje simple.
- Pensada para presupuestos mínimos.
- `[agregar 1 o 2 diferenciales propios]`

## Demo

`[enlace a la demo]`

Pruébala en 3 pasos:

1. `[paso 1]`
2. `[paso 2]`
3. `[paso 3]`

## Funcionalidades

Cada una con el requisito (RF) de la spec que cumple.

- [ ] Calendario de eventos (RF-`[n]`)
- [ ] Comunicación comunitaria (RF-`[n]`)
- [ ] Envío de correos (RF-`[n]`)
- [ ] Micro recaudación para eventos (RF-`[n]`)

El detalle está en `specs/001-[nombre]/spec.md`.

## Tecnologías

| Parte | Herramienta |
|---|---|
| Frontend | `[pendiente]` |
| Backend / datos | `[pendiente]` |
| Pruebas | `[pendiente]` |
| Despliegue | GitHub Pages con GitHub Actions |
| IA | GitHub Copilot + MCP de GitHub |

## Cómo ejecutarlo

```bash
git clone https://github.com/DayelinXiomaa/Red-Tinkuy.git
cd Red-Tinkuy
# [pendiente: comandos para ejecutar y probar]
```

¿Primera vez configurando Git, VS Code o el agente? Sigue la Parte 1 del README del kit.

## Cómo lo construimos

Usamos Spec-Driven Development: primero acordamos qué construir en una spec, y de ahí salen el plan, las tareas, el código y las pruebas.

| Fase | Dónde quedó |
|---|---|
| Reto | [docs/RETO.md](docs/RETO.md) |
| Principios | [docs/constitution.md](docs/constitution.md) |
| Requisitos | `specs/001-[nombre]/spec.md` |
| Plan y tareas | `plan.md` y `tasks.md` de la spec |
| Código | `[carpetas]` |
| Pruebas | `tests/` y la CI |
| Despliegue | `[workflow de Pages]` |
| Pitch | [docs/pitch.md](docs/pitch.md) |

## Equipo

| Nombre | Lidera | Tareas | GitHub |
|---|---|---|---|
| Dayelin Xiomaa | `[área]` | `[tareas]` | [@DayelinXiomaa](https://github.com/DayelinXiomaa) |
| `[nombre]` | `[área]` | `[tareas]` | `[usuario]` |
| `[nombre]` | `[área]` | `[tareas]` | `[usuario]` |

## Cómo trabajamos

- `main` siempre funciona, y todo entra por pull request revisado por una compañera.
- Una tarea = un issue = una rama. El tablero dice quién hace qué.
- La IA propone, una persona decide.

Reglas completas: [CONTRIBUTING.md](CONTRIBUTING.md) para personas y [AGENTS.md](AGENTS.md) para la IA.

## Checklist de entrega (domingo 15, 11:59 p. m.)

- [ ] README completo (problema, solución, demo, equipo)
- [ ] `main` funciona: se puede clonar y ejecutar con los pasos de arriba
- [ ] Cada requisito de la spec tiene su prueba y la CI está en verde
- [ ] Todas las integrantes tienen al menos un PR revisado y fusionado
- [ ] Enlace a la demo funcionando
- [ ] Sin contraseñas, claves ni datos personales reales en el repo
- [ ] Repositorio público
- [ ] `docs/pitch.md` listo para la final del lunes 16