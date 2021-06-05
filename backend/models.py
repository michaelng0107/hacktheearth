from django.db import models

# Create your models here.

class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abundence = models.PositiveIntegerField()
    profits = models.IntegerField()

    def __str__(self):
        return f"{self.species}"


class Tree(models.Model):
    tree_id = models.IntegerField(null=True, blank=True)
    species = models.ForeignKey(Species, related_name='Species', on_delete=models.CASCADE, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    radius = models.PositiveIntegerField(null=True, blank=True)
    trunk_wounds = models.PositiveIntegerField(null=True, blank=True)
    mushrooms = models.PositiveIntegerField(null=True, blank=True)
    surface_roots = models.CharField(max_length=20, null=True, blank=True)
    leaf_colour = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"



class TestDB(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"{self.text}"