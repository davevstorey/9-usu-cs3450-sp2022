from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit-profile'),
    path('profile/edit-address', views.edit_address, name='edit-address'),
    path('profile/change-password', views.change_password, name='change-password'),
    path('password-change-success', views.password_change_success, name='password-change-success')
]