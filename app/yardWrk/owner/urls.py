from django.urls import path
from . import views

app_name = 'owner'
urlpatterns = [
    path('dashboard', views.owner_dashboard, name='owner_dashboard')
]