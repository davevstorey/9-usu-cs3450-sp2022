from django import forms

from accounts.models import CustomUser

from yardSite.models import JobType


class JobTypePostForm(forms.ModelForm):

    class Meta:
        model = JobType
        fields = [
            "name",
            "description",
        ]