from django.db import models
from django_countries.fields import CountryField
# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    country = CountryField()
    city = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    post_code = models.CharField(max_length=30)
