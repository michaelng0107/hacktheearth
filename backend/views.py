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

