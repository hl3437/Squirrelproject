from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .forms import SquirrelForm
from .models import Squirrel

def index(request):
    return render(request, 'sightings/index.html', {})

def stats(request):
    return render(request, 'sightings/stats.html', {})

def add_squirrel(request):
    context = {}
    form = SquirrelForm(request.POST)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request, 'sightings/add.html', context)
   
def update_suqirrel(request):
    context = {}
    
    form = SquirrelForm(request.POST)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request, 'sightings/update.html', context)

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels
        }
    return render(request, 'sightings/all.html', context)

# Create your views here.
