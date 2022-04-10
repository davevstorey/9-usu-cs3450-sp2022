from django.urls import path
from . import views

app_name = 'owner'
urlpatterns = [
    path('dashboard', views.owner_dashboard, name='owner_dashboard'),
    path('dashboard/jobs', views.owner_add_delete_jobs, name='owner_add_delete_jobs'),
    path('dashboard/jobs/<int:job_id>', views.owner_job_details, name="owner_job_details"),
    path('dashboard/jobs/<int:job_id>/remove', views.owner_del_job, name="owner_del_job"),
    path('dashboard/editBalances', views.owner_edit_account_balances, name='owner_edit_account_ballances'),
]