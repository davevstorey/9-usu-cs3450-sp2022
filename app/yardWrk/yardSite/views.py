from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import JobPostForm

# Create your views here.
def CustomerDashboard(request):
    pending_jobs = Job.objects.filter(available=True).filter(completed=False)
    progressing_jobs = Job.objects.filter(available=False).filter(completed=False)
    completed_jobs = Job.objects.filter(completed=True)
    return HttpResponse("Welcome to the Customer Dashboard!")

def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer')
        else: 
            print(form.errors)
    else:
        form = JobPostForm()
    return render(request, 'yardSite/create-job-post.html', { 'form': form })