from backend.models import Tree, Species
from random import randint, choices
from numpy import random

SPECIES = ['American Beech', 'Bald Cypress', 'Black Willow', 'Canadian Hemlock',
            'Oak Tree', 'Olive Tree', 'Palm Tree', 'Red Maple Tree',]
# for i in range(8):
#     population = randint(10, 100) * 1000
#     profit = randint(11, 60) * 100
#     s = Species(i + 1, SPECIES[i], population, profit)
#     s.save()
#     # print(population, profit)

ages = random.normal(200, 50, 1000).astype(int)
radii = random.normal(10, 5, 1000).astype(int)
heights = {
    'American Beech': random.normal(22, 5, 1000).astype(int),
    'Bald Cypress': random.normal(25, 5, 1000).astype(int),
    'Black Willow': random.normal(11, 5, 1000).astype(int),
    'Canadian Hemlock': random.normal(18, 5, 1000).astype(int),
    'Oak Tree': random.normal(27, 5, 1000).astype(int), 
    'Olive Tree': random.normal(7, 5, 1000).astype(int), 
    'Palm Tree': random.normal(12, 5, 1000).astype(int), 
    'Red Maple Tree': random.normal(24, 5, 1000).astype(int),
}

# print(ages)
for i in range(0, 100):
    species = choices(SPECIES, [1, 1, 2, 1, 4, 3, 3, 4])[0]
    age = ages[i]
    radius = abs(radii[i]) if radii[i] < 0 else radii[i] + 1
    height = abs(heights[species][i]) if heights[species][i] < 0 else heights[species][i] + 1
    trunk_wounds = randint(0, 40)
    mushrooms = randint(0, 20)
    surface_roots = choices([True, False])[0]
    t = Tree(i + 1, Species.objects.get(name=species).id, age, radius, height, trunk_wounds, mushrooms, surface_roots)
    t.save()