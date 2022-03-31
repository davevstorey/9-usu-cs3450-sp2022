from django import forms

from .models import Job, Review


class JobPostForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = [
            "job_type",
            "description",
            "cash_reward",
            "date_to_be_finished_by"
        ]

class ReviewPostForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = [
            "rating_num",
            "review_text",
            "redList_bool"
        ]

