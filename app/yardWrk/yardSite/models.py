import datetime
from django.db import models
from accounts.models import CustomUser

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



class Job(models.Model):
    # Decided on three character codes for internal job representation
    # These are some that I came up with. Definitely add more as you
    # see fit!
    LAWN_CARE = 'LWN'
    SNOW_REMOVAL = 'SNW'
    PET_CARE = 'PET'
    LANDSCAPING = 'LND'
    AUTOMOTIVE = 'AUT'
    GARDENING = 'GAR'
    MOVING = 'MOV'
    DECORATION = 'CDN'
    JOB_TYPES = (
        (LAWN_CARE, 'Lawn Care'),
        (LANDSCAPING, 'Landscaping'),
        (GARDENING, 'Gardening/Plant Cultivation'),
        (SNOW_REMOVAL, 'Snow Removal'),
        (PET_CARE, 'Pet Care'),
        (AUTOMOTIVE, 'Automotive'),
        (MOVING, 'Moving Services'),
        (DECORATION, 'Decoration'),
    )

    name = models.CharField(max_length=20)

    description = models.CharField(max_length=100)

    # No id field needed, Django ORM handles this

    job_type = models.CharField(max_length=3, choices=JOB_TYPES)

    # Decide on whether this should be an integer or float field
    cash_reward = models.IntegerField()

    # Many to One Relation -- One Customer can have many jobs posted
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # Many to One Relation -- One Worker can be assigned many jobs
    worker = models.ForeignKey(Worker, null=True, on_delete=models.CASCADE)

    # Boolean field
    available = models.BooleanField(default=True)

    completed = models.BooleanField(default=False)

    date_to_be_finished_by = models.DateField(blank=True, null=True)

    zip_code = models.IntegerField()

    # GETTERS and SETTERS not needed. All Django model fields can be
    # accessed with the standard '.' syntax

    def __str__(self):
        return f"{self.name} - Zip Code: {self.zip_code} - Type: {self.job_type} Reward: {self.cash_reward} Available: {self.available} Completed: {self.completed} Should be finished by: {self.date_to_be_finished_by} Customer: {self.customer} Worker: {self.worker}"

class Review(models.Model):
    published_date = models.DateTimeField('date posted')
    review_text = models.CharField(max_length=400)
    rating_num = models.IntegerField(default=3)
    redList_bool = models.BooleanField()
    reviewerName_text = models.CharField(max_length = 40)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    reviewee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    isCustomer_bool = models.BooleanField()

    def __str__(self):
        return self.review_text
