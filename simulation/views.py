from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import TrackingLog

def track_click(request, token):
    """
    Decodes the token, logs the click, and renders the dummy login page.
    """
    log_entry = get_object_or_404(TrackingLog, unique_token=token)
    
    if not log_entry.clicked:
        log_entry.clicked = True
        log_entry.clicked_at = timezone.now()
        log_entry.save()
    
    # Determine which template to render based on theme
    theme = log_entry.campaign.theme
    template_name = 'simulation/landing_generic.html'
    
    if theme == 'MICROSOFT':
        template_name = 'simulation/landing_microsoft.html'
    elif theme == 'GOOGLE':
        template_name = 'simulation/landing_google.html'
        
    return render(request, template_name, {'token': token})

def handle_dummy_login(request, token):
    """
    Handles the POST request from the dummy login page.
    Does NOT save any credentials.
    """
    if request.method == 'POST':
        log_entry = get_object_or_404(TrackingLog, unique_token=token)
        if not log_entry.data_submitted:
            log_entry.data_submitted = True
            log_entry.save()
        return redirect('education_page')
    
    # If not POST, redirect to tracking view (or education)
    return redirect('track_click', token=token)

def education_page(request):
    """
    The page shown after 'logging in' or if the user realizes it's a test.
    """
    return render(request, 'simulation/education.html')
