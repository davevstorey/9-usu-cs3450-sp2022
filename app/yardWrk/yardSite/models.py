import datetime
from django.db import models
from accounts.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Worker(models.Model):
	user = models.OneToOneField(
		CustomUser,
		on_delete=models.CASCADE,
		primary_key=True,
	)


class Customer(models.Model):
	user = models.OneToOneField(
		CustomUser,
		on_delete=models.CASCADE,
		primary_key=True,
	)

class JobType(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    # Decided on three character codes for internal job representation
    # These are some that I came up with. Definitely add more as you
    # see fit!
    
    name = models.CharField(max_length=24)

    description = models.CharField(max_length=200)

    # No id field needed, Django ORM handles this

    job_type = models.ForeignKey('JobType', on_delete=models.CASCADE)

    # Decide on whether this should be an integer or float field
    cash_reward = models.DecimalField(max_digits=10, decimal_places=2)

    # Many to One Relation -- One Customer can have many jobs posted
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # Many to One Relation -- One Worker can be assigned many jobs
    worker = models.ForeignKey(Worker, null=True, on_delete=models.CASCADE)

    # Boolean field
    available = models.BooleanField(default=True)

    completed = models.BooleanField(default=False)

    date_to_be_finished_by = models.DateField(blank=True, null=True)

    zip_code = models.CharField(max_length=12)

    # GETTERS and SETTERS not needed. All Django model fields can be
    # accessed with the standard '.' syntax

    def preview_description(self, length=150):
        if len(self.description) <= length:
            return self.description
        else:
            return ' '.join(self.description[:length+1].split(' ')[0:-1]) + '...'

    def __str__(self):
        return f"{self.name} - Zip Code: {self.zip_code} - Type: {self.job_type} Reward: {self.cash_reward} Available: {self.available} Completed: {self.completed} Should be finished by: {self.date_to_be_finished_by} Customer: {self.customer} Worker: {self.worker}"

class Review(models.Model):
    published_date = models.DateTimeField('date posted')
    review_text = models.CharField(max_length=400)
    rating_num = models.IntegerField(
            default=3,
            validators=[
                MinValueValidator(0),
                MaxValueValidator(5)
            ]
    )


    redList_bool = models.BooleanField(verbose_name="redlist")
    reviewerName_text = models.CharField(max_length = 40)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    reviewee = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviewee', default='110')
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviewer', default='1')
    isCustomer_bool = models.BooleanField()

    def __str__(self):
        return self.review_text


