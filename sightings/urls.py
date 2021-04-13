from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stats/', views.stats, name='stats'),
    path('add/', views.add_squirrel, name='add'),
]

