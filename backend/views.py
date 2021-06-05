from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .models import Test

# Create your views here.

class TestView(View):
    test_class = Test
    website = 'test.html'

    def get(self, request):
        return render(request, self.website, {})
