from django.shortcuts import redirect, render

from yardSite.models import Job
from accounts.models import CustomUser

# Create your views here.

def owner_dashboard(request):
    # Temporary Code for testing purposes (change when we have actual dashboard)
    user = request.user
    # Adding/Removing Funds for Owner
    if request.method == 'POST':
        if(request.POST.get("Add")):
            sumToAdd = int(request.POST.get("Add"))
            user.wallet += sumToAdd
        elif(request.POST.get("Withdraw")):
            sumToSub = int(request.POST.get("Withdraw"))
            if (user.wallet >= sumToSub):
                user.wallet -= sumToSub
        user.save()
        return redirect('/owner/dashboard')

    context = {
        'ownerUser' : user,
    }

    return render(request, 'owner/owner-dash.html', context)


def owner_add_delete_jobs(request):
    all_jobs = Job.objects.all()

    return render(request, 'owner/owner-add-del-jobs.html', { 'all_jobs': all_jobs })

def owner_job_details(request, job_id):
    requested_job = Job.objects.filter(id=job_id)[0]

    context = {
        'job': requested_job
    }

    return render(request, 'owner/owner-job-details.html', context)

def owner_del_job(request, job_id):
    # Delete Job
    Job.objects.filter(id=job_id)[0].delete()

    return redirect('/owner/dashboard/jobs')

def owner_edit_account_balances(request):
    # Grab all accounts besides owner.
    #TODO: Avoid grabbing owner.
    allAccounts = CustomUser.objects.all()

    context = {
        'allAccounts' : allAccounts
    }
    return render(request, 'owner/owner-edit-account-ballances.html', context)