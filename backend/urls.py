from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name="test"),
    path('graph1/<int:species>/', views.graph1, name='graph1'),
    path('graph2/<int:species>/', views.graph2, name='graph2'),
    path('graph3/<int:species>/', views.graph3, name="graph3"),
    path('graph4/<int:species>/', views.graph4, name='graph4'),
    path('species/', views.species, name='species'),
    path('species_test/', views.species_test, name='species_test'),
]
