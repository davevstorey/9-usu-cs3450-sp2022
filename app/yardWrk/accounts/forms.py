from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField

from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=64)
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    phone = PhoneNumberField()

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "password1",
            "password2"
        ]

class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "phone",
        ]

class AddressForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            "address",
            "city",
            "state",
            "zip_code"
        ]