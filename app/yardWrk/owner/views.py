from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import JobTypePostForm

from yardSite.models import Job, JobType
from accounts.models import CustomUser

# Create your views here.

@login_required(login_url='/accounts/login')
def owner_dashboard(request):
    job_types = JobType.objects.all()
    # Temporary Code for testing purposes (change when we have actual dashboard)
    user = request.user
    context = {
        'ownerUser' : user,
        'types' : job_types,
    }

    return render(request, 'owner/owner-dash.html', context)

@login_required(login_url='/accounts/login')
def owner_add_delete_jobs(request):
    all_jobs = Job.objects.all()

    return render(request, 'owner/owner-add-del-jobs.html', { 'all_jobs': all_jobs })

@login_required(login_url='/accounts/login')
def owner_job_details(request, job_id):
    requested_job = Job.objects.filter(id=job_id)[0]

    context = {
        'job': requested_job
    }

    return render(request, 'owner/owner-job-details.html', context)

@login_required(login_url='/accounts/login')
def owner_del_job(request, job_id):
    # Delete Job
    Job.objects.filter(id=job_id)[0].delete()

    return redirect('/owner/dashboard/jobs')

@login_required(login_url='/accounts/login')
def owner_edit_account_balances(request):
    # Grab all accounts besides owner.
    allAccounts = CustomUser.objects.filter(is_superuser=False)

    context = {
        'allAccounts' : allAccounts
    }
    return render(request, 'owner/owner-edit-account-balances.html', context)

@login_required(login_url='/accounts/login')
def owner_add_job_type(request):
    if request.method == 'POST':
        form = JobTypePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/owner/dashboard')
        else: 
            print(form.errors)
    else:
        form = JobTypePostForm()
    return render(request, 'owner/owner-add-job-type.html', { 'form': form })

@login_required(login_url='/accounts/login')
def owner_edit_specific_account(request, user_id):
    specificUser = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
            if(request.POST.get("Add")):
                sumToAdd = int(request.POST.get("Add"))
                specificUser.wallet += sumToAdd
            elif(request.POST.get("Withdraw")):
                sumToSub = int(request.POST.get("Withdraw"))
                if (specificUser.wallet >= sumToSub):
                    specificUser.wallet -= sumToSub
            specificUser.save()
            return redirect('owner:owner_edit_specific_account', user_id)

    context = {
        'account' : specificUser
    }
    return render(request, 'owner/owner-edit-specific-account.html', context)
