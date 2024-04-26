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

    preperation = models.TextField()

    def __str__(self):
        return self.name