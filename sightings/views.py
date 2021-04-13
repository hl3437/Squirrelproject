from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .forms import SquirrelForm
from .models import Squirrel
from django.shortcuts import get_object_or_404s

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
   
def update_squirrel(request, Unique_Squirrel_ID):
    squirrel = get_object_or_404(Squirrel, pk=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{Unique_Squirrel_ID}')
    else:
        form = SquirrelForm(instance=squirrel)
    return render(request, 'sightings/all.html', context)

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels
        }
    return render(request, 'sightings/all.html', context)

# Create your views here.
