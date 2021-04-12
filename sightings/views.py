from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'sightings/index.html', {})

def stats(request):
    return render(request, 'sightings/stats.html', {})

# Create your views here.
