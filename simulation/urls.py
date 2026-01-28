from django.urls import path
from . import views

urlpatterns = [
    path('track/<uuid:token>/', views.track_click, name='track_click'),
    path('login-submit/<uuid:token>/', views.handle_dummy_login, name='handle_dummy_login'),
    path('education/', views.education_page, name='education_page'),
]
