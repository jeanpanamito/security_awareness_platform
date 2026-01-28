from django.contrib import admin
from .models import Target, Campaign, TrackingLog

@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'department')
    search_fields = ('email', 'first_name', 'last_name')

from .services import send_campaign_emails
from django.contrib import messages

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    actions = ['launch_campaign']

    def launch_campaign(self, request, queryset):
        total_sent = 0
        for campaign in queryset:
            sent = send_campaign_emails(campaign.id, request)
            total_sent += sent
        self.message_user(request, f"Se enviaron {total_sent} correos simulados.", messages.SUCCESS)
    launch_campaign.short_description = "Lanzar Campaña (Enviar Correos)"

@admin.register(TrackingLog)
class TrackingLogAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'target', 'unique_token', 'clicked', 'data_submitted', 'clicked_at')
    list_filter = ('campaign', 'clicked', 'data_submitted')
    readonly_fields = ('unique_token',)
