from django.shortcuts import render
from django.db.models import Count, Q
from simulation.models import Campaign, TrackingLog

def dashboard(request):
    campaigns = Campaign.objects.all()
    stats = []

    for campaign in campaigns:
        total_targets = TrackingLog.objects.filter(campaign=campaign).count()
        clicked_count = TrackingLog.objects.filter(campaign=campaign, clicked=True).count()
        submitted_count = TrackingLog.objects.filter(campaign=campaign, data_submitted=True).count()
        
        click_rate = (clicked_count / total_targets * 100) if total_targets > 0 else 0
        submit_rate = (submitted_count / total_targets * 100) if total_targets > 0 else 0

        stats.append({
            'campaign': campaign,
            'total_targets': total_targets,
            'clicked_count': clicked_count,
            'submitted_count': submitted_count,
            'click_rate': round(click_rate, 1),
            'submit_rate': round(submit_rate, 1),
            # Data for Chart.js
            'chart_safe_count': total_targets - clicked_count,
            'chart_clicked_only_count': clicked_count - submitted_count,
            'chart_compromised_count': submitted_count
        })

    return render(request, 'analytics/dashboard.html', {'stats': stats})

def campaign_report(request, campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
    total_targets = TrackingLog.objects.filter(campaign=campaign).count()
    clicked_count = TrackingLog.objects.filter(campaign=campaign, clicked=True).count()
    submitted_count = TrackingLog.objects.filter(campaign=campaign, data_submitted=True).count()
    
    click_rate = (clicked_count / total_targets * 100) if total_targets > 0 else 0
    submit_rate = (submitted_count / total_targets * 100) if total_targets > 0 else 0
    
    context = {
        'campaign': campaign,
        'total_targets': total_targets,
        'clicked_count': clicked_count,
        'submitted_count': submitted_count,
        'click_rate': round(click_rate, 1),
        'submit_rate': round(submit_rate, 1),
        'chart_safe_count': total_targets - clicked_count,
        'chart_clicked_only_count': clicked_count - submitted_count,
        'chart_compromised_count': submitted_count
    }
    return render(request, 'analytics/report.html', context)
