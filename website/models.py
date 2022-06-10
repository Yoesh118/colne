from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Booking(models.Model):

 name = models.TextField()
 phone_number = models.TextField(max_length=20)
 email = models.EmailField()
 wedding_date = models.DateField()
 wedding_colours = models.TextField()
 guests = models.BigIntegerField()
 visit_date = models.DateField()
 visit_time = models.TextField()

class Enquiry(models.Model):
    name = models.TextField()
    phone_number = models.TextField(max_length=20)
    email = models.EmailField(max_length=30)
    message = models.TextField()
