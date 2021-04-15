from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage_view),
    path('home', views.homepage_view),
    path('map/', views.map_view),
    path('list/', views.list_sights),
    path('stats/', views.stats_view),
    path('add/', views.add_sights),
    path('list/<Unique_Squirrel_Id>/', views.update_sights),
    path('index/', views.index),

]
