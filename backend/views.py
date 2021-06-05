from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.

def test(request):
    qs = TestDB.objects.all()
    
    return JsonResponse(list(qs.values()), safe=False)



