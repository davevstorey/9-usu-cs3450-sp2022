from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def CustomerDashboard(request):
    pending_jobs = Job.objects.filter(available=True).filter(completed=False)
    progressing_jobs = Job.objects.filter(available=False).filter(completed=False)
    completed_jobs = Job.objects.filter(completed=True)
    return HttpResponse("Welcome to the Customer Dashboard!")
