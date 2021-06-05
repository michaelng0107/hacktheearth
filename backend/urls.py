from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name="test"),
    path('graph3/<int:species>', views.graph3, name="graph3"),
]
