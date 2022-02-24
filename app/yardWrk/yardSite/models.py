import datetime
from django.db import models

class Review(models.Model):
    published_date = models.DateTimeField('date posted')
    review_text = models.CharField(max_length=400)
    rating_num = models.IntegerField(default=3)
    redList_bool = models.BooleanField()
    revieweeUserType = models.CharField(max_length=8)
    reviewerName_text = models.CharField(max_length = 40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.review_text
