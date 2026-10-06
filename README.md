# SIRAM - Sistema de Gestión de Denuncias y Casos de Maltrato Animal

> Repositorio oficial del proyecto **SIRAM**, diseñado para la gestión, validación, consolidación de denuncias y seguimiento de casos de maltrato animal, estructurado en base a un modelo conceptual robusto orientado a organismos de control y participación ciudadana.

---

## Descripción del Proyecto
**SIRAM** busca resolver el problema de la fragmentación de la información proveniente de múltiples fuentes de denuncias (municipales, provinciales, externas). Permite:
* Ingesta y validación de denuncias externas.
* Consolidación de múltiples denuncias en un **Caso** único para evitar duplicados.
* Gestión de estados diferenciados tanto para denuncias individuales como para casos en seguimiento.
* Trazabilidad y auditoría completa de todas las acciones realizadas sobre los casos.
* Control de acceso y permisos basados en usuarios y organismos participantes.

---

## Modelo Conceptual y Arquitectura de Información

El diseño del sistema se estructura en torno a las siguientes entidades principales y sus relaciones:

* **Usuario & Organismo:** Gestión de perfiles y pertenencia institucional para aplicar políticas de permisos y roles.
* **Denuncia:** Información cruda o preliminar que ingresa al sistema procedente de distintas fuentes. Posee estados de validación (*Pendiente, Validada, Rechazada, Incompleta, Consolidada*).
* **Caso:** Incidente consolidado que el sistema identifica y gestiona como unidad de investigación/seguimiento. Una o varias denuncias pueden asociarse a un mismo caso.
* **Víctima & Animal:** Entidades que registran la información de los involucrados en las denuncias y casos.
* **Historial_Auditoria:** Registro cronológico de cada modificación, cambio de estado, asociación o acción relevante sobre los casos para garantizar transparencia y trazabilidad.

---

## Tecnologías y Stack Tecnológico
* **Backend:** Python / Django (Modelos, ORM y API).
* **Base de Datos:** PostgreSQL (Diseño relacional a partir de cardinalidades validadas).
* **Control de Versiones:** Git & GitHub.
* **Entorno de Desarrollo:** Linux Mint / Entornos virtuales de Python.

---

## Instalación y Configuración Local

Sigue estos pasos para clonar y levantar el proyecto en tu entorno de desarrollo (Linux / Ubuntu / Mint):

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/UzumakiN314/SIRAM.git](https://github.com/UzumakiN314/SIRAM.git)

2. **Prueba de repositorio:**
