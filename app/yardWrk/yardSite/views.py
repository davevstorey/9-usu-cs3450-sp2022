from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import JobPostForm

# Responsible for creating the view a user sees when navigating to their customer page.

def empty(request):
    return redirect('/yardsite/home')

def home(request):
    return render(request, 'yardSite/home.html')

@login_required(login_url='/accounts/login')
def CustomerDashboard(request):
    # Grab the customer that is tied to the logged in user
    currentUserCustomerProfile = request.user.customer
    
    pending_jobs = Job.objects.filter(customer=currentUserCustomerProfile).filter(available=True).filter(completed=False)
    progressing_jobs = Job.objects.filter(customer=currentUserCustomerProfile).filter(available=False).filter(completed=False)
    completed_jobs = Job.objects.filter(customer=currentUserCustomerProfile).filter(completed=True)

    context = {
        'pending_jobs': pending_jobs,
        'progressing_jobs': progressing_jobs,
        'completed_jobs': completed_jobs,
    }

    return render(request, 'yardSite/customerDashboard.html', context)

@login_required(login_url='/accounts/login')
def WorkerDashboard(request):
    w_user = request.user
    w_name = w_user.get_full_name()
    worker = w_user.worker
    # Gets available jobs that weren't posted by this user
    available_jobs = Job.objects.filter(available=True).filter(completed=False).exclude(customer=w_user.customer)
    
    job_list = Job.objects.filter(worker=worker).filter(completed=False)
    completed_job_list = Job.objects.filter(worker=worker).filter(completed=True)
    context = {
        'name': w_name,
        'assigned': job_list,
        'available': available_jobs,
        'completed': completed_job_list
    }
    return render(request, 'yardSite/workerDashboard.html', context)

@login_required(login_url='/accounts/login')
def OwnedJobDetails(request, job_id):
    requested_job = Job.objects.filter(id=job_id)[0]
    currentUserCustomerProfile = request.user.customer

    can_assign_to_self = True
    if requested_job.customer == currentUserCustomerProfile:
        can_assign_to_self = False
    
    context = {
        'can_assign': can_assign_to_self,
        'job': requested_job
    }

    return render(request, 'yardSite/ownedJobDetails.html', context)

@login_required(login_url='/accounts/login')
def accepted_job(request, job_id):
    accepted_job = Job.objects.filter(id=job_id)[0]
    currentUserWorkerProfile = request.user.worker

    accepted_job.available = False
    accepted_job.worker = currentUserWorkerProfile
    accepted_job.save()

    context = {
        'job': accepted_job
    }

    return render(request, 'yardSite/acceptedJob.html', context)

@login_required(login_url='/accounts/login')
def finish_job(request, job_id):
    completed_job = Job.objects.filter(id=job_id)[0]

    completed_job.completed = True
    completed_job.save()

    # Add logic for payment here

    context = {
        'job': completed_job
    }

    return render(request, 'yardSite/finishJob.html', context)

@login_required(login_url='/accounts/login')
def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user.get_full_name()
            instance.zip_code = request.user.zip_code
            instance.customer = request.user.customer
            instance.save()
            return redirect('/yardsite/customer')
        else: 
            print(form.errors)
    else:
        form = JobPostForm()
    return render(request, 'yardSite/create-job-post.html', { 'form': form })

@login_required(login_url='/accounts/login')
def editJob(request, job_id):
    requested_job = Job.objects.filter(id=job_id)[0]

    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=requested_job)
        if form.is_valid():
            form.save()
            return redirect('/yardsite/customer')
        else: 
            print(form.errors)
    else:
        form = JobPostForm(instance=requested_job)

    context = {
        'job': requested_job,
        'form': form
    }

    return render(request, 'yardSite/editJob.html', context)
