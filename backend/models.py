from django.db import models
from math import pi
# Create your models here.

class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abundence = models.PositiveIntegerField(null=True, blank=True)
    profits = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Tree(models.Model):
    species = models.ForeignKey(Species, related_name='Species', on_delete=models.CASCADE, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    radius = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    trunk_wounds = models.PositiveIntegerField(null=True, blank=True)
    mushrooms = models.PositiveIntegerField(null=True, blank=True)
    surface_roots = models.BooleanField(null=True, blank=True)

    @property
    def volume(self):
        return pi * (self.radius ** 2) * self.height

    @property
    def value(self):
        return self.volume * self.species.profits

    def __str__(self):
        return f"{self.id}"



class TestDB(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"{self.text}"