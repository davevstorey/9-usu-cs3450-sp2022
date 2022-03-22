from django import forms

from .models import Job


class JobPostForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = [
            "name",
            "job_type",
            "description",
            "cash_reward",
            "date_to_be_finished_by"
        ]