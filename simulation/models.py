from django.db import models
import uuid

class Target(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Campaign(models.Model):
    THEME_CHOICES = [
        ('GENERIC', 'Genérico (Rápido)'),
        ('MICROSOFT', 'Microsoft 365 (Seguridad)'),
        ('GOOGLE', 'Google Workspace (Alerta)'),
    ]
    name = models.CharField(max_length=200)
    theme = models.CharField(max_length=20, choices=THEME_CHOICES, default='GENERIC')
    template_content = models.TextField(help_text="HTML content of the email", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TrackingLog(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    unique_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    clicked = models.BooleanField(default=False)
    data_submitted = models.BooleanField(default=False)
    clicked_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ('campaign', 'target')

    def __str__(self):
        return f"{self.campaign.name} - {self.target.email}"
