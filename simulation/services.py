from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import Campaign, Target, TrackingLog

def send_campaign_emails(campaign_id, request=None):
    """
    Sends simulated phishing emails to all targets in a campaign.
    """
    campaign = Campaign.objects.get(id=campaign_id)
    # En este prototipo, asumimos que enviamos a todos los targets registrados
    # En un sistema real, Campaign tendría una relación ManyToMany con Target
    targets = Target.objects.all()
    
    sent_count = 0
    
    for target in targets:
        # Get or create tracking log to ensure unique token exists
        log, created = TrackingLog.objects.get_or_create(
            campaign=campaign,
            target=target
        )
        
        # Build tracking URL
        # Assuming we are running on localhost:8000 for the demo
        base_url = "http://127.0.0.1:8000"
        if request:
             base_url = f"{request.scheme}://{request.get_host()}"
             
        tracking_link = f"{base_url}/track/{log.unique_token}/"
        
        # --- Theme Logic for Email Content ---
        if campaign.theme == 'MICROSOFT':
            # Simplified Microsoft Alert Template
            subject = "Alerta de Seguridad: Acción Requerida en su cuenta"
            message_body = f"""
            <div style="font-family: Arial, sans-serif; max-width: 600px; border: 1px solid #ddd;">
                <div style="padding: 20px;"><img src="https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE1Mu3b?ver=5c31" height="24"></div>
                <div style="padding: 20px;">
                    <h2 style="color: #333;">Actividad de inicio de sesión inusual</h2>
                    <p>Hola {target.first_name},</p>
                    <p>Hemos detectado algo inusual en un inicio de sesión reciente en la cuenta de Microsoft {target.email}.</p>
                    <p><strong>Por favor, verifique su actividad reciente para asegurar su cuenta.</strong></p>
                    <div style="text-align: center; margin: 30px 0;">
                        <a href="{tracking_link}" style="background-color: #0067b8; color: white; padding: 10px 20px; text-decoration: none; font-weight: bold;">Revisar actividad reciente</a>
                    </div>
                    <p style="font-size: 12px; color: #666;">Gracias, <br>El equipo de cuentas de Microsoft</p>
                </div>
            </div>
            """
        elif campaign.theme == 'GOOGLE':
            subject = "Alerta de seguridad crítica"
            message_body = f"""
            <div style="font-family: Arial, sans-serif; max-width: 600px; border: 1px solid #ddd; border-radius: 8px;">
                <div style="padding: 20px; text-align: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" height="24"></div>
                <div style="padding: 20px;">
                    <h2 style="color: #d93025; text-align: center;">Alerta de seguridad crítica</h2>
                    <div style="text-align: center;"><img src="https://ssl.gstatic.com/accounts/static/_/images/security_alert_red.png" height="64"></div>
                    <p>Hola, {target.first_name}:</p>
                    <p style="text-align: center;">Alguien conoce tu contraseña</p>
                    <div style="text-align: center; margin: 30px 0;">
                        <a href="{tracking_link}" style="background-color: #1a73e8; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px;">Comprobar actividad</a>
                    </div>
                </div>
            </div>
            """
        else: # GENERIC
            subject = f"IMPORTANTE: {campaign.name}"
            # Use the campaign's manually entered content or a default
            content = campaign.template_content if campaign.template_content else "Hola {{nombre}}, por favor haga clic en el siguiente enlace: {{link}}"
            message_body = content.replace("{{nombre}}", target.first_name)
            message_body = message_body.replace("{{link}}", tracking_link)
        
        # Send email (Console backend will print this to terminal)
        try:
            send_mail(
                subject=subject,
                message="Please enable HTML emails.", # Fallback text
                html_message=message_body, # Actual HTML content
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[target.email],
                fail_silently=False,
            )
            sent_count += 1
        except Exception as e:
            print(f"Error sending to {target.email}: {e}")
            
    return sent_count
