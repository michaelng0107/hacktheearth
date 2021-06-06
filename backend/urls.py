from django.urls import path
from . import views

urlpatterns = [
    path('graph1/<int:species>/', views.graph1, name='graph1'),
    path('graph2/<int:species>/', views.graph2, name='graph2'),
    path('graph3/<int:species>/', views.graph3, name="graph3"),
    path('graph4/<int:species>/', views.graph4, name='graph4'),
    path('species/', views.species, name='species'),
    path('species_data/<int:species>/', views.species_data, name='species_data'),




    path('all_trees/', views.all_trees, name='all_trees'), # test
]
