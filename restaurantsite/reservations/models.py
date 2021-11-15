from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.
class Table(models.Model):
    table_number = models.PositiveIntegerField(default=1, primary_key=True)
    seats = models.PositiveIntegerField()
    booked = models.BooleanField(default=False)
    svg_path = models.CharField(default="", max_length=10000)

    def __str__(self):
        return "Table_"+ str(self.table_number)

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="")
    email = models.EmailField(default="")
    # make sure that people < seats
    # recommend for large bookings that they call/email to book
    people = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return str(self.date) +": " + self.name + " (" + str(self.people) + ")"

    class Meta:
        ordering = ["date"]
