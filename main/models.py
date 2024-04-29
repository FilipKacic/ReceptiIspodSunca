from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=64, unique=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # numberOfSuns = models.IntegerField(default=0)

    equipment = models.ManyToManyField(Equipment)
    ingredients = models.ManyToManyField(Ingredient)
    time_needed = models.IntegerField()
    TIME_UNITS = (
        ('min', 'min'),
        ('ura', 'h'),
        ('dan', 'dan'),
    )
    time_measurement_unit = models.CharField(max_length=8, choices=TIME_UNITS, default=False)

    preperation = models.TextField()

    CATEGORIES = (
        ('drink', 'Piće'),
        ('food', 'Hrana'),
        ('medicine', 'Lijek'),
    )
    category = models.CharField(max_length=8, choices=CATEGORIES, default=False)

    def __str__(self):
        return self.name