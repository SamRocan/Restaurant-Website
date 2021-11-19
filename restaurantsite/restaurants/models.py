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

    def __str__(self):
        return self.name + " - " + self.city

WEEKDAYS = [
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
]

class OpeningHours(models.Model):
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_time = models.TimeField()
    to_time = models.TimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.from_time) + " - " + str(self.to_time)

    class Meta:
        ordering = ('weekday', 'from_time')
        unique_together = ('weekday', 'from_time', 'to_time')
        verbose_name = "Opening Hour"