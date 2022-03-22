import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerDashboard, name="customerDashboard"),
    path('worker/', views.WorkerDashboard, name="workerDashboard"),
    path('<int:job_id>/', views.OwnedJobDetails, name="ownedJobDetails"),
    path('job/create', views.create_job_post, name="job post creations"),
    path('<int:job_id>/edit_job', views.editJob, name="editJob"),
]