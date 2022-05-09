from django.urls import path
from . import  views

urlpatterns = [
    path('', views.UpBank, name='UpBank'),
    path('bari/', views.bari, name='bari'),
    path('ole/', views.ole, name='ole'),
    path('refin/', views.refin, name='refin'),
    path('siape/', views.siape, name='siape'),
    path('bmg/', views.bmg, name='bmg'),
    path('loasBrasil/', views.loasBrasil, name='loasBrasil'),
    path('loasCidade/', views.loasCidade, name='loasCidade'),


    
]    