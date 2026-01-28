from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/<int:campaign_id>/', views.campaign_report, name='campaign_report'),
]
