from django.shortcuts import render, redirect
from django.apps import apps
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, EditProfileForm, EditAddressForm

# Create your views here.

def home(request):
    return redirect('/accounts/login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            instance = form.save()
            customer_model = apps.get_model('yardSite.Customer')
            worker_model = apps.get_model('yardSite.Worker')
            customer = customer_model(user=instance)
            customer.save()
            worker = worker_model(user=instance)
            worker.save()
            return redirect('/accounts/login')
        else: 
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/yardsite')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

@login_required(login_url='/accounts/login')
def profile(request):
    if request.method == 'POST':
        user = request.user
        if request.POST.get("add"):
            sumToAdd = int(request.POST.get("value"))
            user.wallet += sumToAdd
        elif request.POST.get("withdraw"):
            sumToSub = int(request.POST.get("value"))
            if (user.wallet >= sumToSub):
                user.wallet -= sumToSub
            else:
                user.wallet = 0
        user.save()

    return render(request, 'accounts/profile.html')

@login_required(login_url='/accounts/login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'accounts/edit-profile.html', { 'form': form })

@login_required(login_url='/accounts/login')
def edit_address(request):
    if request.method == 'POST':
        form = EditAddressForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditAddressForm(instance=request.user)
    return render(request, 'accounts/edit-address.html', { 'form': form })

@login_required(login_url='/accounts/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            print('valid form')
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/accounts/password-change-success')
        print('invalid form')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change-password.html', { 'form': form })

def password_change_success(request):
    return render(request, 'accounts/change-password-success.html', {})

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')

