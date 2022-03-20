from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Responsible for creating the view a user sees when navigating to their customer page.
def CustomerDashboard(request):
    pending_jobs = Job.objects.filter(available=True).filter(completed=False)
    progressing_jobs = Job.objects.filter(available=False).filter(completed=False)
    completed_jobs = Job.objects.filter(completed=True)

    context = {
        'pending_jobs': pending_jobs,
        'progresesing_jobs': progressing_jobs,
        'completed_jobs': completed_jobs,
    }

    return render(request, 'yardSite/customerDashboard.html', context)

def OwnedJobDetails(request, job_id):
    requested_job = Job.objects.filter(id=job_id)

    context = {
        'job': requested_job[0],
    }

    return render(request, 'yardSite/ownedJobDetails.html', context)
