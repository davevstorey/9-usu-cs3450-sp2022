from django.shortcuts import redirect, render

from yardSite.models import Job

# Create your views here.

def owner_dashboard(request):
    # Temporary Code for testing purposes (change when we have actual dashboard)
    return render(request, 'owner/owner-dash.html', {})


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