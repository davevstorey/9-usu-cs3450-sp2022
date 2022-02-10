from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=64)
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2"
        ]

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "first_name",
            "last_name"
        ]