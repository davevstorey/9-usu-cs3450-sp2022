from django.urls import path
from . import views

app_name = 'yardSite'
urlpatterns = [
    path('', views.empty, name='empty'),
    path('home/', views.home, name='home'),
    path('customer/', views.CustomerDashboard, name="customerDashboard"),
    path('worker/', views.WorkerDashboard, name="workerDashboard"),
    path('<int:job_id>/', views.OwnedJobDetails, name="ownedJobDetails"),
    path('customer/create-job', views.create_job_post, name="createJob"),
    path('<int:job_id>/edit-job', views.editJob, name="editJob"),
    path('<int:job_id>/accepted', views.accepted_job, name="acceptedJob"),
    path('<int:job_id>/finished', views.finish_job, name="finishJob"),
]