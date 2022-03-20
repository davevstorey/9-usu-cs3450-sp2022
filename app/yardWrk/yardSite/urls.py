import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerDashboard, name="customerDashboard"),
    path('<int:job_id>/', views.OwnedJobDetails, name="ownedJobDetails"),
]