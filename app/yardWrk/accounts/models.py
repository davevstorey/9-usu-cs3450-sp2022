from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class CustomUser(AbstractUser):
    email = models.CharField(max_length=128, unique=True)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    state = models.CharField(max_length=4)
    phone = PhoneNumberField()

    # form of wallet/balance (Integer Representation)
    wallet = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def get_address(self):
        return f"{self.address}, {self.city}, {self.state}, {self.zip_code}"

