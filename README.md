# Security Awareness Platform (Phishing Simulation)

Plataforma de simulación de phishing con fines educativos y de auditoría de seguridad. Diseñada para evaluar la concienciación de los usuarios mediante campañas controladas de *Brand Spoofing* (Microsoft 365, Google Workspace).

## 2. Psicología Social Aplicada a la Ciberseguridad

Más allá del código, la efectividad de nuestra simulación se fundamenta en principios de psicología social. El diseño de las campañas explota sesgos cognitivos específicos para evadir el pensamiento crítico del usuario:

*   **Principio de Autoridad:** Al suplantar entidades reconocidas como Microsoft o Google, aprovechamos la tendencia natural de los usuarios a obedecer solicitudes "oficiales" o administrativas.
*   **Sentido de Urgencia:** Los correos simulan alertas de seguridad críticas (e.g., "Inicio de sesión inusual"), induciendo un estado de ansiedad que precipita la acción impulsiva (clic) antes de la verificación racional.
*   **Sesgo de Hábito:** Al clonar interfaces que el usuario utiliza diariamente, activamos su "piloto automático". La familiaridad visual reduce la carga cognitiva y baja las defensas de sospecha.

## 3. Definición del Escenario y Consideraciones Éticas

El ataque simulado se define como un ejercicio de "Clone Phishing". Para ello, utilizamos copias visualmente idénticas de sitios legítimos con el fin de inducir al usuario al error. Sin embargo, como desarrolladores comprometidos con el hacking ético, implementamos salvaguardas estrictas: el código valida que el usuario intentó enviar datos, pero deliberadamente se descarta cualquier contraseña ingresada antes de que toque la base de datos. De esta manera, garantizamos la privacidad total de los participantes mientras obtenemos las métricas necesarias para el análisis de riesgo.

## 4. Arquitectura y Tecnologías Seleccionadas

Para la construcción de la plataforma, seleccionamos **Django (Python)** como framework backend. Esta elección se fundamenta en su arquitectura MVT (Modelo-Vista-Template), que permite desacoplar la lógica de negocio de la presentación visual, facilitando la escalabilidad del proyecto.

En el frontend, se optó por un enfoque artesanal utilizando **HTML5 y CSS3 puros** para clonar las interfaces de Microsoft y Google, asegurando una fidelidad visual "pixel-perfect" que resulta crucial para el engaño. Para la visualización de datos en el dashboard, integramos la librería **Chart.js**, lo que permite presentar métricas complejas de manera intuitiva y ejecutiva.

Para la infraestructura de comunicaciones, se configuró un **backend SMTP conectado a Gmail**. Decidimos utilizar este proveedor real en lugar de una simulación de consola para enfrentar los desafíos reales de entregabilidad y evasión de filtros de spam básicos, acercando la simulación a un escenario de mundo real.

### 4.1 Estructura del Proyecto
El proyecto sigue una estructura modular de Django, dividiendo responsabilidades claramente:

```
security_awareness_platform/
├── config/              # Configuraciones globales (settings.py, urls.py)
├── simulation/          # Núcleo del ataque
│   ├── models.py        # Modelos (Campaign, Target, TrackingLog)
│   ├── views.py         # Lógica de engaño y captura (track_click, dummy_login)
│   ├── services.py      # Lógica de envío de correos (SMTP)
│   └── templates/       # Páginas clonadas (Google, Microsoft)
├── analytics/           # Motor de reporte
│   ├── views.py         # Cálculo de KPIs y Dashboard
│   └── templates/       # Vistas de gráficos y reportes PDF
└── db.sqlite3           # Base de datos (No almacena passwords)
```
### 4.2 Mapa de Rutas (Endpoints)
La arquitectura de direccionamiento se divide en dos zonas lógicas: la zona de administración (Atacante) y la zona de simulación (Víctima).

**Zona de Administración (Acceso Restringido):**
*   `/admin/` - Panel de Control central. Desde aquí se crean campañas y se lanzan los ataques.
*   `/analytics/dashboard/` - Centro de comando visual. Muestra gráficos y métricas en tiempo real.
*   `/analytics/report/<id>/` - Generador de Informes Ejecutivos en formato imprimible.

**Zona de Simulación (Acceso Público/Víctima):**
*   `/track/<uuid>/` - **El Vector de Ataque.** URL única generada para cada víctima. Al acceder, registra el clic y muestra el *Landing Page* (Microsoft/Google).
*   `/login-submit/<uuid>/` - Endpoint receptor de credenciales. Procesa el formulario POST, cuenta el compromiso y descarta la contraseña.
*   `/education/` - **The Teachable Moment.** Página final de aterrizaje que revela el simulacro.

## 5. Ingeniería Visual: Anatomía del Engaño del Login

La eficacia del phishing moderno reside en la calidad de la clonación. Para este proyecto, no utilizamos generadores automáticos, sino que reconstruimos las interfaces de autenticación "pixel-perfect" utilizando HTML5 y CSS3 nativos. A continuación, detallamos la ingeniería detrás de cada vector:

### 5.1 Vector Microsoft 365 (`landing_microsoft.html`)
Este vector está diseñado para interceptar credenciales corporativas.
*   **Fondo Dinámico:** Implementamos el background oficial de Microsoft (`https://img-prod-cms-rt-microsoft-com...`) mediante hotlinking para asegurar que la imagen de fondo esté siempre actualizada y sea indistinguible de la real.
*   **Caja de Login:** Se replicó el "Card" blanco con sombra suave (`box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2)`).
*   **Tipografía:** Uso forzado de la familia tipográfica `Segoe UI`, exclusiva del ecosistema Windows.
*   **Feedback Visual:** El botón "Siguiente" replica el color azul corporativo `#0067b8` y su estado `:hover` (`#005da6`).

### 5.2 Vector Google Workspace (`landing_google.html`)
Diseñado para comprometer cuentas de acceso a servicios en la nube (Drive, Docs).
*   **Diseño Material:** Se clonaron los principios de Material Design, incluyendo los bordes redondeados de 8px y el diseño centrado de tarjeta única.
*   **Logo Oficial:** Inyección del SVG oficial de Google desde Wikimedia Commons para evitar pixelación en pantallas Retina (`height: 24px`).
*   **Campos Flotantes:** Se imitó el estilo de input de Google con padding amplio (`13px 15px`) y bordes grises suaves (`#dadce0`).
*   **Call to Action:** El botón azul `#1a73e8` con sombra de elevación al pasar el mouse es idéntico al del flujo de autenticación OAuth 2.0 real.

## 📚 Documentación Completa
> Para acceder al **Informe Técnico Detallado**, metodología, y análisis de resultados, consulta la [Wiki del Proyecto](WIKI.md).

## 🛠️ Instalación Rápida
1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/security-awareness-platform.git
    cd security-awareness-platform
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install django
    ```

3.  **Configurar variables de entorno:**
    Edita `config/settings.py` y añade tus credenciales SMTP (Google App Password recomendado):
    ```python
    EMAIL_HOST_USER = 'tu-email@gmail.com'
    EMAIL_HOST_PASSWORD = 'tu-app-password'
    ```

4.  **Ejecutar el servidor:**
    ```bash
    python manage.py runserver
    ```

Accede al panel de administración en `http://127.0.0.1:8000/admin`.
