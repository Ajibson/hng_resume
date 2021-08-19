from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone

class resume_details(models.Model):
    #Personal info
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField()
    gender = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 20)
    title = models.CharField(max_length = 100)
    city = models.CharField(max_length = 200)
    country = CountryField()
    bio = models.TextField()
    skills = models.TextField()

    #Education
    school = models.CharField(max_length = 250)
    course = models.CharField(max_length = 250)
    Degree = models.CharField(max_length = 100)
    edu_start_date = models.CharField(max_length = 30)
    edu_end_date = models.CharField(max_length = 30)

    #Work Experience
    work_title = models.CharField(max_length = 100)
    role = models.CharField(max_length = 250)
    work_start_date = models.CharField(max_length = 30)
    work_end_date = models.CharField(max_length = 30)

    #interest
    interest = models.TextField()

    #generated identification number
    reference_id = models.CharField(max_length = 20, blank=True)


    def __str__(self):
        return self.first_name

    # def save(self, *args, **kwargs):
    #     if self.refrence_id == "":
    #         self.refrence_id = uuid.uuid4().hex[:11]
    #     super().save(*args, **kwargs)

class message(models.Model):
    sender = models.CharField(max_length = 250)
    message_recieved = models.TextField()
    date_recieved = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.sender