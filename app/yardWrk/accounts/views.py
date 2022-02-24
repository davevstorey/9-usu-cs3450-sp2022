from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, EditProfileForm

# Create your views here.

def home(request):
    return render(request, 'authentication/home.html', {})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/accounts/login')
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', { 'form': form })

@login_required(login_url='/accounts/login')
def profile(request):
    return render(request, 'authentication/profile.html', {})

@login_required(login_url='/accounts/login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'authentication/edit-profile.html', { 'form': form })

def logout_view(request):
    logout(request)
    return redirect('/accounts/home')

