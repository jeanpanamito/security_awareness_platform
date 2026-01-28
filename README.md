# 🛡️ Security Awareness Platform

> **Plataforma de Simulación de Phishing y Concienciación de Seguridad**
> *Una herramienta de auditoría ética para medir y educar sobre riesgos de Ingeniería Social.*

![Status](https://img.shields.io/badge/Status-Educational_Prototype-orange)
![Tech](https://img.shields.io/badge/Backend-Django_Python-green)
![License](https://img.shields.io/badge/License-MIT-blue)

## 🚨 Descargo de Responsabilidad (Legal Disclaimer)

> [!CAUTION]
> **USO EXCLUSIVO PARA EDUCACIÓN Y AUDITORÍA AUTORIZADA**
> Este software ha sido desarrollado únicamente con fines académicos y de prueba de concepto. El uso de este código para lanzar campañas de phishing contra objetivos sin su consentimiento previo y por escrito es **ILEGAL** y puede constituir un delito grave bajo las leyes de ciberseguridad locales e internacionales.
>
> **Los autores no se hacen responsables del mal uso de esta herramienta.**

---

## 📖 Descripción del Proyecto

**Security Awareness Platform** es un sistema integral diseñado para simular ataques de *Credential Harvesting* de manera controlada. Su objetivo no es comprometer cuentas, sino evaluar la susceptibilidad de los usuarios ante técnicas de *Brand Spoofing* (suplantación de identidad de marcas como Microsoft 365 y Google Workspace) y proporcionar educación inmediata ("Teachable Moments").

El sistema permite a un administrador ("Red Team"):
1.  **Configurar campañas** temáticas (Microsoft, Google, Genérico).
2.  **Enviar correos masivos** simulados.
3.  **Monitorizar métricas** en tiempo real (Aperturas vs. Compromisos).
4.  **Educar** al usuario automáticamente si cae en la trampa.

---

## 🛠️ Stack Tecnológico

El proyecto está construido sobre una arquitectura robusta y modular:

| Componente | Tecnología | Descripción |
| :--- | :--- | :--- |
| **Backend** | **Django 5.0+** (Python) | Framework principal. Manejo de ORM, enrutamiento y lógica de negocio. |
| **Frontend** | **HTML5 / CSS3** | Clonación *pixel-perfect* de interfaces de login (sin frameworks pesados). |
| **Visualización** | **Chart.js** | Renderizado de gráficos interactivos en el Dashboard. |
| **Base de Datos** | **SQLite** (Dev) | Almacenamiento ligero de Targets, Campañas y Logs. |
| **Email** | **SMTP (Gmail)** | Envío real de correos electrónicos. |

---

## 📂 Arquitectura del Sistema

### Estructura de Directorios
```text
security_awareness_platform/
├── config/              # Configuración global (settings, urls)
├── simulation/          # Core de la simulación
│   ├── models.py        # Definición de datos (Target, Campaign)
│   ├── views.py         # Lógica de captura (track_click, dummy_login)
│   ├── services.py      # Servicio de envío de email (SMTP Logic)
│   └── templates/       # Clones visuales (Google, Microsoft)
├── analytics/           # Módulo de Reporte
│   ├── views.py         # Tablero de control y KPIs
│   └── templates/       # Dashboard y Reportes PDF
└── manage.py            # CLI de Django
```

### Mapa de Rutas (Endpoints)

| Zona | Endpoint | Descripción |
| :--- | :--- | :--- |
| **Admin** | `/admin/` | Panel de control para crear campañas y cargar usuarios. |
| **Admin** | `/analytics/dashboard/` | Dashboard con métricas en tiempo real. |
| **Admin** | `/analytics/report/<id>/` | Generación de reportes ejecutivos para impresión. |
| **Víctima** | `/track/<uuid>/` | **Vector de Ataque.** URL única para rastreo de clics. |
| **Víctima** | `/login-submit/<uuid>/` | Procesa el formulario falso (sin guardar password). |
| **Víctima** | `/education/` | Página educativa final. |

---

## ⚙️ Características Técnicas Clave

### 1. Ingeniería Visual (Clonación)
Las plantillas de phishing (`landing_microsoft.html`, `landing_google.html`) han sido desarrolladas con técnicas de ingeniería inversa visual:
*   **Hotlinking de Assets:** Se cargan imágenes y fondos directamente de los servidores oficiales (e.g., `akamaized.net`, `gstatic.com`) para garantizar realismo y evitar caché desactualizada.
*   **Tipografía Nativa:** Uso de fuentes propietarias (`Segoe UI`, `Roboto`) inyectadas vía CSS.
*   **Diseño Responsivo:** Adaptación fiel a dispositivos móviles.

### 2. Privacidad por Diseño (Ethical Safeguards)
El sistema está programado para **NO** persistir datos sensibles.
> En `simulation/views.py`:
> ```python
> # Se registra el evento de compromiso
> log_entry.data_submitted = True
> log_entry.save()
> # La contraseña NUNCA se lee del request.POST
> ```

### 3. Orquestación de Correo
Uso de un despachador SMTP personalizado en `simulation/services.py` que:
*   Genera UUIDs únicos por envío.
*   Inyecta el payload (enlace de rastreo) en la plantilla HTML seleccionada.
*   Gestiona errores de envío individualmente para no detener la campaña.

---

## � Manual de Despliegue (Quick Start)

### Prerrequisitos
*   Python 3.10 o superior.
*   Cuenta de Gmail con "App Password" generada (para envío SMTP).

### Pasos de Instalación

1.  **Clonar el Repositorio**
    ```bash
    git clone https://github.com/tu-repositorio/security-awareness.git
    cd security_awareness_platform
    ```

2.  **Crear y Activar Entorno Virtual**
    ```bash
    python -m venv venv
    # Windows:
    .\venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate
    ```

3.  **Instalar Dependencias**
    ```bash
    pip install django
    ```

4.  **Configurar Variables de Entorno**
    Modifica `config/settings.py` (o usa un archivo `.env`):
    ```python
    EMAIL_HOST_USER = 'tu-email@gmail.com'
    EMAIL_HOST_PASSWORD = 'tu-app-password-generado' # NO uses tu contraseña real
    ```

5.  **Inicializar Base de Datos**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser # Crea tu cuenta de Admin
    ```

6.  **Ejecutar Servidor**
    ```bash
    python manage.py runserver
    ```

---

## 🕹️ Guía de Uso (Flujo de Campaña)

1.  **Accede al Admin:** Ve a `http://127.0.0.1:8000/admin`.
2.  **Carga Objetivos:** En la sección **Targets**, añade los correos de prueba.
3.  **Crea una Campaña:**
    *   Ve a **Campaigns**.
    *   Elige un nombre y un **Tema** (Microsoft, Google, Genérico).
4.  **Lanza el Ataque:**
    *   En la lista de campañas, selecciona la que creaste.
    *   En el desplegable "Action", selecciona **"Launch Campaign (Enviar Correos)"**.
    *   Haz clic en **Go**.
5.  **Monitoriza:**
    *   Ve a `http://127.0.0.1:8000/analytics/dashboard/` para ver quién ha caído.

---

## 📚 Documentación Adicional

Para un análisis profundo sobre la teoría de la Ingeniería Social, los principios de psicología aplicados y el detalle académico de este proyecto, consulte:
👉 **[Informe Técnico / Wiki del Proyecto](WIKI.md)**

---

**© 2026 Security Awareness Platform Dev Team**
