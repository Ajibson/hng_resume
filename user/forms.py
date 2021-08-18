from django import forms
from .models import resume_details
from django.core.exceptions import ValidationError


class createResumeForm(forms.ModelForm):

    class Meta:
        model = resume_details
        exclude = ['refrence_id']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in [entry.email for entry in resume_details.objects.all()]:
            raise ValidationError("Email cannot be used")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number in [entry.phone_number for entry in resume_details.objects.all()]:
            raise ValidationError("phone number cannot be used")
        return phone_number


class updateResumeForm(forms.ModelForm):

    class Meta:
        model = resume_details
        fields = "__all__"
        # exclude = ['refrence_id']
