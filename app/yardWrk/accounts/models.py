from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField

# Create your models here.

class CustomUser(AbstractUser):
    email = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    # phone = PhoneField(blank=True, help_text='Phone Number')

    # form of wallet/balance (Integer Representation)
    # balance = models.IntegerField()

