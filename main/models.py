from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
# class Equipment(models.Model):
#     name = models.CharField(max_length=64, unique=True)

#     def __str__(self):
#         return self.name
    
# class Ingredient(models.Model):
#     name = models.CharField(max_length=64, unique=True)

#     def __str__(self):
#         return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=64, unique=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # numberOfSaves = models.IntegerField(default=0)

    CATEGORIES = (
        ('food', 'Hrana'),
        ('drink', 'Piće'),
        ('medicine', 'Lijek'),
    )
    category = models.CharField(max_length=8, choices=CATEGORIES, default='food')

    equipment = models.TextField(default="")
    ingredients = models.TextField(default="")
    time_needed = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    TIME_UNITS = (
        ('min', 'min'),
        ('ura', 'h'),
        ('dan', 'dan'),
    )
    time_measurement_unit = models.CharField(max_length=8, choices=TIME_UNITS, default='min')

    preperation = models.TextField(default="")

    def __str__(self):
        return '„' + str(self.name) + '“' + ', autor: ' + str(self.author)