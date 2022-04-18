import decimal
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import JobPostForm
from .forms import ReviewPostForm

# Responsible for creating the view a user sees when navigating to their customer page.

def empty(request):
    return redirect('/yardWrk/home')

@login_required(login_url='/accounts/login')
def home(request):
    filters = []
    checked = []
    w_user = request.user
    redList = Review.objects.filter(reviewee = w_user).filter(redList_bool = True)
    returnRedList = Review.objects.filter(reviewer = w_user).filter(redList_bool = True)
    qs = Job.objects.all().filter(available=True)
    job_types = JobType.objects.all()

    for i in redList:
        wor = i.job.worker
        qs = qs.exclude(worker = wor)

        cus = i.job.customer
        qs = qs.exclude(customer = cus)

    for j in returnRedList:
        wor = j.job.worker
        qs = qs.exclude(worker = wor)

        cus = j.job.customer
        qs = qs.exclude(customer = cus)


    if request.GET.get('filter'):
        for type in job_types:
            if request.GET.get(type.name) != 'on':
                filters.append(type)
            else:
                checked.append(type.name)
        if len(checked) > 0:
            for filter in filters:
                qs = qs.exclude(job_type=filter)

        if request.GET.get('zip') == 'on':
            qs = qs.filter(zip_code=request.user.zip_code)
            checked.append('zip')
    
    return render(request, 'yardSite/home.html', { 'queryset': qs, 'job_types': job_types, 'checked': checked })

@login_required(login_url='/accounts/login')
def CustomerDashboard(request):

    # Grab the customer that is tied to the logged in user
    currentUserCustomerProfile = request.user.customer
    review_list = Review.objects.filter(reviewee=request.user).exclude(isCustomer_bool = False)
    yourReview_list = Review.objects.filter(reviewer=request.user)

    completed_job_list2 = Job.objects.filter(customer=request.user.customer).filter(completed=True)
    for i in yourReview_list:
        completed_job_list2 = completed_job_list2.exclude(review = i)

    
    pending_jobs = Job.objects.filter(customer=currentUserCustomerProfile).filter(available=True).filter(completed=False)
    progressing_jobs = Job.objects.filter(customer=currentUserCustomerProfile).filter(available=False).filter(completed=False)
    completed_jobs = Job.objects.filter(customer=currentUserCustomerProfile).filter(completed=True)

    context = {
        'pending_jobs': pending_jobs,
        'progressing_jobs': progressing_jobs,
        'c2': completed_job_list2,
        'completed_jobs': completed_jobs,
        'customerReviews': review_list,
        'currentCustomer' : currentUserCustomerProfile,
    }
    return render(request, 'yardSite/customerDashboard.html', context)

@login_required(login_url='/accounts/login')
def WorkerDashboard(request):
    w_user = request.user
    w_name = w_user.get_full_name()
    worker = w_user.worker
    wallet = w_user.wallet

    # Gets available jobs that weren't posted by this user
    review_list = Review.objects.filter(reviewee=w_user).exclude(isCustomer_bool = True)
    yourReview_list = Review.objects.filter(reviewer=w_user)
    available_jobs = Job.objects.filter(available=True).filter(completed=False).exclude(customer=w_user.customer)
    
    job_list = Job.objects.filter(worker=worker).filter(completed=False)
    completed_job_list = Job.objects.filter(worker=worker).filter(completed=True)
    completed_job_list2 = Job.objects.filter(worker=worker).filter(completed=True)
    for i in yourReview_list:
        completed_job_list2 = completed_job_list2.exclude(review = i)

    context = {
        'name': w_name,
        'assigned': job_list,
        'c2': completed_job_list2,
        'completed': completed_job_list,
        'workerReviews': review_list,
        'wallet' : wallet,
    }
    return render(request, 'yardSite/workerDashboard.html', context)

@login_required(login_url='/accounts/login')
def OwnedJobDetails(request, job_id):
    requested_job = Job.objects.filter(id=job_id)[0]
    currentUserCustomerProfile = request.user.customer

    can_assign_to_self = True
    if requested_job.customer == currentUserCustomerProfile:
        can_assign_to_self = False
    
    yourReviews =  Review.objects.filter(job = requested_job).filter(reviewer = request.user)
    receivedReviews =  Review.objects.filter(job = requested_job).exclude(reviewer = request.user)


    context = {
        'can_assign': can_assign_to_self,
        'receivedReview': receivedReviews,
        'yourReview': yourReviews,
        'job': requested_job
    }

    return render(request, 'yardSite/ownedJobDetails.html', context)

@login_required(login_url='/accounts/login')
def delete_job(request, job_id):
    requested_job = Job.objects.filter(id=job_id)[0]

    if request.method == 'POST':
        if request.POST.get("delete"): requested_job.delete()
        return redirect('/yardWrk/customer')
    
    return render(request, 'yardSite/delete-job.html', { 'job': requested_job })

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

    workerUser = CustomUser.objects.get(id=completed_job.worker.user.id)
    customerUser = CustomUser.objects.get(id=completed_job.customer.user.id)
    ownerUser = CustomUser.objects.get(is_superuser=True)

    # Calculate the different cuts
    totalReward = decimal.Decimal(completed_job.cash_reward)
    ownerCut = decimal.Decimal(totalReward * decimal.Decimal(0.1))
    workerCut = decimal.Decimal(totalReward - ownerCut)

    # Add or subtract cuts from the appropriate users
    workerUser.wallet += workerCut
    customerUser.wallet -= totalReward
    if(ownerUser):
        ownerUser.wallet += ownerCut

    # Save changes
    workerUser.save()
    customerUser.save()
    ownerUser.save()
    completed_job.save()

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
            return redirect('/yardWrk/customer')
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
            return redirect('/yardWrk/customer')
        else: 
            print(form.errors)
    else:
        form = JobPostForm(instance=requested_job)

    context = {
        'job': requested_job,
        'form': form
    }

    return render(request, 'yardSite/editJob.html', context)

@login_required(login_url='/accounts/login')
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
            instance.reviewer = requested_job.customer.user
            instance.save()
            return redirect('/yardWrk/home')
        else:
            print(form.errors)
    else: 
        form = ReviewPostForm(instance=requested_job)
    return render(request, 'yardsite/create-review-post.html', { 'form': form })

@login_required(login_url='/accounts/login')
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
            instance.reviewer = requested_job.worker.user
            instance.isCustomer_bool = True
            instance.save()
            return redirect('/yardWrk/home')
        else:
            print(form.errors)
    else: 
        form = ReviewPostForm(instance=requested_job)
    return render(request, 'yardsite/create-review-post.html', { 'form': form })

@login_required(login_url='/accounts/login')
def editReview(request, review_id):
    requested_review = Review.objects.filter(id=review_id)[0]

    if request.method == 'POST':
        form = ReviewPostForm(request.POST, instance=requested_review)
        if form.is_valid():
            form.save()
            return redirect('/yardWrk/sentReviews')
        else:
            print(form.errors)
    else:
        form = ReviewPostForm(instance=requested_review)

    context = {
        'review': requested_review,
        'form': form
    }

    return render(request, 'yardSite/editReview.html', context)

@login_required(login_url='/accounts/login')
def OwnedReviewDetails(request, review_id):
    requested_review = Review.objects.filter(id=review_id)[0]

    can_assign_to_self = True
    context = {
        'review': requested_review
    }

    return render(request, 'yardSite/ownedReviewDetails.html', context)

def SentReviews(request):
    r_reviews = Review.objects.filter(reviewer=request.user)

    context = {
        'reviews': r_reviews 
    }

    return render(request, 'yardSite/sentReviews.html', context)

def SentReviewDetails(request, review_id):
    requested_review = Review.objects.filter(id=review_id)[0]

    context = {
        'review': requested_review
    }

    return render(request, 'yardSite/sentReviewDetails.html', context)
