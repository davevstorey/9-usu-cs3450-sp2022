from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=64)


# class Customer(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


# class Worker(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


# class WorkerReview(models.Model):
#     worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
#     author = models.CharField(max_length=64)
#     comment = models.TextField()


# class CustomerReview(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     author = models.CharField(max_length=64)
#     comment = models.TextField()
