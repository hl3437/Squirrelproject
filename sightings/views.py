from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .forms import SquirrelForm

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
    #if request.method == 'POST':
    # form = SquirrelForm(request.POST)
    #   if form.is_valid():
     #       form.save()
    # else:
     #    form = SquirrelForm()
      #   context['form'] = form
    # return render(request, 'sightings/add.html', context) 
   

# Create your views here.
