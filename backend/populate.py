from backend.models import Tree, Species
from random import randint, choices
from numpy import random

SPECIES = [s.name for s in Species.objects.all()]
print(SPECIES)
# # for i in range(8):
# #     population = randint(10, 100) * 1000
# #     profit = randint(11, 60) * 100
# #     s = Species(i + 1, SPECIES[i], population, profit)
# #     s.save()
# #     # print(population, profit)

ages = random.normal(200, 50, 1000).astype(int)
radii = random.normal(10, 3, 1000).astype(int)
heights = {
    'Elm Tree': random.normal(22, 5, 1000).astype(int),
    'Birch Tree': random.normal(30, 5, 1000).astype(int),
    'Willow Tree': random.normal(11, 3, 1000).astype(int),
    'Fir Tree': random.normal(14, 4, 1000).astype(int),
    'Maple Tree': random.normal(27, 5, 1000).astype(int), 
    'Oak Tree': random.normal(23, 5, 1000).astype(int), 
    'Beech Tree': random.normal(25, 5, 1000).astype(int), 
    'Pine Tree': random.normal(54, 8, 1000).astype(int),
}

# print(ages)
# for i in range(0, 100):
#     species = choices(SPECIES, [1, 1, 2, 1, 4, 3, 3, 4])[0]
#     age = ages[i]
#     radius = abs(radii[i]) if radii[i] < 0 else radii[i] + 1
#     height = abs(heights[species][i]) if heights[species][i] < 0 else heights[species][i] + 1
#     trunk_wounds = randint(0, 40)
#     mushrooms = randint(0, 20)
#     surface_roots = choices([True, False])[0]
#     # t = Tree(i + 1, Species.objects.get(name=species).id, age, radius, height, trunk_wounds, mushrooms, surface_roots)
#     # t.save()