from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import JobPostForm
from .forms import ReviewPostForm

# Responsible for creating the view a user sees when navigating to their customer page.

def empty(request):
    return redirect('/yardsite/home')

def home(request):
    qs = Job.objects.all().filter(available=True)
    filters = []
    checked = []
    for type,name in Job.JOB_TYPES:
        if request.GET.get(type) != 'on':
            filters.append(type)
        else:
            checked.append(type)
    if len(filters) > 0 and len(filters) < 7:
        for filter in filters:
            qs = qs.exclude(job_type=filter)

    return render(request, 'yardSite/home.html', { 'queryset': qs, 'checked': checked })

@login_required(login_url='/accounts/login')
def CustomerDashboard(request):
    # Grab the customer that is tied to the logged in user
    currentUserCustomerProfile = request.user.customer
    review_list = Review.objects.filter(reviewee=request.user).exclude(isCustomer_bool = False)

    
    pending_jobs = Job.objects.filter(customer=currentUserCustomerProfile).filter(available=True).filter(completed=False)
    progressing_jobs = Job.objects.filter(customer=currentUserCustomerProfile).filter(available=False).filter(completed=False)
    completed_jobs = Job.objects.filter(customer=currentUserCustomerProfile).filter(completed=True)

    context = {
        'pending_jobs': pending_jobs,
        'progressing_jobs': progressing_jobs,
        'completed_jobs': completed_jobs,
        'customerReviews': review_list
    }

    return render(request, 'yardSite/customerDashboard.html', context)

@login_required(login_url='/accounts/login')
def WorkerDashboard(request):
    w_user = request.user
    w_name = w_user.get_full_name()
    worker = w_user.worker
    # Gets available jobs that weren't posted by this user
    available_jobs = Job.objects.filter(available=True).filter(completed=False).exclude(customer=w_user.customer)
    review_list = Review.objects.filter(reviewee=w_user).exclude(isCustomer_bool = True)
    
    job_list = Job.objects.filter(worker=worker).filter(completed=False)
    completed_job_list = Job.objects.filter(worker=worker).filter(completed=True)
    context = {
        'name': w_name,
        'assigned': job_list,
        'available': available_jobs,
        'completed': completed_job_list,
        'workerReviews': review_list
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

def customer_create_review_post(request, job_id):
    requested_job = Job.objects.filter(id=job_id)[0]

    if request.method == 'POST':
        form = ReviewPostForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.reviewerName_text = request.user.get_full_name()
            instance.job = requested_job
            instance.published_date = datetime.datetime.now()
            instance.reviewee = requested_job.worker.user
            instance.isCustomer_bool = False
            instance.save()
            return redirect('/yardsite/home')
        else:
            print(form.errors)
    else: 
        form = ReviewPostForm(instance=requested_job)
    return render(request, 'yardsite/create-review-post.html', { 'form': form })

def create_review_post(request, job_id):
    requested_job = Job.objects.filter(id=job_id)[0]

    if request.method == 'POST':
        form = ReviewPostForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.reviewerName_text = request.user.get_full_name()
            instance.job = requested_job
            instance.published_date = datetime.datetime.now()
            instance.reviewee = requested_job.customer.user
            instance.isCustomer_bool = True
            instance.save()
            return redirect('/yardsite/home')
        else:
            print(form.errors)
    else: 
        form = ReviewPostForm(instance=requested_job)
    return render(request, 'yardsite/create-review-post.html', { 'form': form })

def editReview(request, review_id):
    requested_review = Job.objects.filter(id=job_id)[0]

    if request.method == 'POST':
        form = ReviewPostForm(request.POST, instance=requested_job)
        if form.is_valid():
            form.save()
            return redirect('/customer')
        else:
            print(form.errors)
    else:
        form = ReviewPostForm(instance=requested_review)

    context = {
        'review': requested_job,
        'form': form
    }

    return render(request, 'yardSite/editReview.html', context)

def OwnedReviewDetails(request, review_id):
    requested_review = Review.objects.filter(id=review_id)[0]

    can_assign_to_self = True
    context = {
        'review': requested_review
    }

    return render(request, 'yardSite/ownedReviewDetails.html', context)

def SentReviewDetails(request, review_id):
    requested_review = Review.objects.filter(id=review_id)[0]

    context = {
        'review': requested_review
    }

    return render(request, 'yardSite/sentReviewDetails.html', context)
