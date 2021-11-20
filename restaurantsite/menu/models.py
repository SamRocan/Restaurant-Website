from django.db import models
from django.core.validators import MinValueValidator
from autoslug import AutoSlugField

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255, default="Menu")
    displayImage = models.ImageField(upload_to='menu/', default='menu/default.jpg')
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

class MenuSection(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default="", related_name='sections')
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.name) + " ("+ str(self.menu.name) + ")"

class MenuItem(models.Model):
    section = models.ForeignKey(MenuSection, on_delete=models.CASCADE, default="",  related_name='items')
    name = models.CharField(max_length=255, default="")
    description = models.CharField(max_length=255, default="")
    price = models.FloatField(
        validators=[MinValueValidator(0.00)],
        default=1
    )

    def __str__(self):
        return str(self.name) + " ("+ str(self.section.name) + ")"

