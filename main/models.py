from django.db import models

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

    # respectedUser = models.CharField()
    # numberOfSuns = models.IntegerField(default=0)

    equipment = models.ManyToManyField(Equipment)
    ingredients = models.ManyToManyField(Ingredient)

    timeNeeded = models.IntegerField(default='0')
    timeNeededMeasuringUnit = models.CharField(max_length=8, default='minuta')
    preperation = models.TextField()

    def __str__(self):
        return self.name