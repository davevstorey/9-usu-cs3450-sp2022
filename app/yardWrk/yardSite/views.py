from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import JobPostForm

# Responsible for creating the view a user sees when navigating to their customer page.

@login_required(login_url='/accounts/login')
def CustomerDashboard(request):
    # Grab the customer that is tied to the logged in user
    currentUser = Customer.objects.filter(user=request.user)[0]
    
    pending_jobs = Job.objects.filter(available=True).filter(completed=False).filter(customer=currentUser)
    progressing_jobs = Job.objects.filter(available=False).filter(completed=False).filter(customer=currentUser)
    completed_jobs = Job.objects.filter(completed=True).filter(customer=currentUser)

    context = {
        'pending_jobs': pending_jobs,
        'progresesing_jobs': progressing_jobs,
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
    
    #job_list = Job.objects.all()
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

    context = {
        'job': requested_job,
    }

    return render(request, 'yardSite/ownedJobDetails.html', context)

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
