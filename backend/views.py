from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.

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
        data.append({'height': tree.age, 'volume': int(tree.volume), 'r': int((int(tree.value)/50000))})
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

def species_data(request, species):
    qs = Species.objects.filter(id=species)
    all_qs = Species.objects.all()

    specie = list(qs.values())

    profit = []
    for i in all_qs:
        profit.append({f'{i.name}':f'{i.profits}'})
    print(profit)

    tc = Tree.objects.all().count()
    s1_total = Tree.objects.filter(species=1).count()
    s2_total = Tree.objects.filter(species=2).count()
    s3_total = Tree.objects.filter(species=3).count()
    s4_total = Tree.objects.filter(species=4).count()
    s5_total = Tree.objects.filter(species=5).count()
    s6_total = Tree.objects.filter(species=6).count()
    s7_total = Tree.objects.filter(species=7).count()
    s8_total = Tree.objects.filter(species=8).count()
    
    total_trees = [s1_total/tc, s2_total/tc, s3_total/tc, s4_total/tc, s5_total/tc, s6_total/tc, s7_total/tc, s8_total/tc]
    pie_chart_data = [round(elem, 2)*100 for elem in total_trees]
    

    return JsonResponse([specie, profit, pie_chart_data], safe=False)  



def species(request):
    qs = Species.objects.all()
    data = []
    for spec in qs:
        data.append({f'{spec.id}': spec.name})
    return JsonResponse(data, safe=False)    

def all_trees(request):
    qs = Tree.objects.all()
    return JsonResponse(list(qs.values()), safe=False)