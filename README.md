# Security Awareness Platform (Phishing Simulation)

Plataforma de simulación de phishing con fines educativos y de auditoría de seguridad. Diseñada para evaluar la concienciación de los usuarios mediante campañas controladas de *Brand Spoofing* (Microsoft 365, Google Workspace).

## 🚀 Características
*   **Clonación Pixel-Perfect:** Plantillas visuales indistinguibles de Microsoft y Google.
*   **Orquestación de Campañas:** Envío masivo y monitorización en tiempo real desde el panel de administración.
*   **Privacidad por Diseño:** Las credenciales interceptadas se descartan automáticamente; **nunca se almacenan**.
*   **Educación Inmediata:** "Teachable Moments" al instante del compromiso, transformando el error en aprendizaje.
*   **Reportes Ejecutivos:** Generación de informes PDF con métricas de riesgo y gráficas analíticas.

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
