from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.

def test(request):
    qs1 = Species.objects.all()
    qs2 = Tree.objects.all()
    lst = [list(qs1.values()), list(qs2.values())]

    
    return JsonResponse(lst, safe=False)

class TestView(View):
    test_class = Tree
    website = 'test.html'
    
def graph1(request, species):
    qs = Tree.objects.filter(species=species)
    data = []
    for tree in qs:
        data.append({'age': tree.age, 'volume': int(tree.volume)})

    return JsonResponse(data, safe=False)

def graph2(request, species):
    qs = Tree.objects.filter(species=species)
    rad_vol = []
    rad_height = []
    data = [rad_height, rad_vol]
    for tree in qs:
        rad_vol.append({'radius': tree.radius, 'volume': int(tree.volume)})
        rad_height.append({'radius': tree.radius, 'height': tree.height})

    return JsonResponse(data, safe=False)

def graph4(request, species):
    qs = Tree.objects.filter(species=species)
    data = []
    for tree in qs:
        data.append({'height': tree.age, 'volume': int(tree.volume), 'profit': int(tree.value)})
    return JsonResponse(data, safe=False)


def graph3(request, species):

    def calc(qs, lst1, lst2):
        for tree in qs:
            if tree.trunk_wounds >= 81:
                lst1[4]+=1
                lst2[4]+= tree.mushrooms
            elif tree.trunk_wounds >= 61:
                lst1[3]+=1
                lst2[3]+= tree.mushrooms
            elif tree.trunk_wounds >= 41:
                lst1[2]+=1
                lst2[2]+= tree.mushrooms
            elif tree.trunk_wounds >= 21:
                lst1[1]+=1
                lst2[1]+= tree.mushrooms
            else:
                lst1[0]+=1
                lst2[0]+= tree.mushrooms
        
    def divide_lst(lst1, lst2):
        lst = [0,0,0,0,0]
        for i in range(5):
            if lst2[i] == 0:
                pass
            else:
                lst[i] = lst2[i] / lst1[i]
        return lst

    qs1 = Tree.objects.filter(species=species, surface_roots=True)
    qs2 = Tree.objects.filter(species=species, surface_roots=False)
    tree1_wound_range = [0,0,0,0,0]
    tree1_mushroom = [0,0,0,0,0]
    tree2_wound_range = [0,0,0,0,0]
    tree2_mushroom = [0,0,0,0,0]
    calc(qs1, tree1_wound_range, tree1_mushroom)
    calc(qs2, tree2_wound_range, tree2_mushroom)
    data1 = [round(elem, 2) for elem in divide_lst(tree1_wound_range, tree1_mushroom)]
    data2 = [round(elem, 2) for elem in divide_lst(tree2_wound_range, tree2_mushroom)]

    print(data1)
    print(data2)

    lst = [data1, data2]
    return JsonResponse(lst, safe=False)

    