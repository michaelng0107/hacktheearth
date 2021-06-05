from django.db import models
from math import pi
# Create your models here.

class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abundence = models.PositiveIntegerField()
    profits = models.IntegerField()

    def __str__(self):
        return f"{self.species}"
from django.db import models
from math import pi

# Create your models here.

class Tree(models.Model):
    tree_id = models.IntegerField(null=True, blank=True)
    species = models.ForeignKey(Species, related_name='Species', on_delete=models.CASCADE, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    radius = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    trunk_wounds = models.PositiveIntegerField(null=True, blank=True)
    mushrooms = models.PositiveIntegerField(null=True, blank=True)
    surface_roots = models.BooleanField()
    volume = models.PositiveIntegerField(default=(pi * (radius ** 2)  * height))
    value = models.PositiveIntegerField(default=(volume * species.profits))


    def __str__(self):
        return f"{self.id}"



class TestDB(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"{self.text}"