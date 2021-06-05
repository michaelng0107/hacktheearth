from django.db import models

# Create your models here.

class Tree(models.Model):
    species = models.ForiegnKey(Species, related_name='Species', on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    radius = models.PositiveIntegerField()
    trunk_wounds = models.PositiveIntegerField()
    mushrooms = models.PositiveIntegerField()
    surface_roots = models.CharField(max_length=20)
    leaf_colour = models.CharField(max_length=20)

class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abundence = models.PositiveIntegerField()
    profits = models.IntegerField()



    