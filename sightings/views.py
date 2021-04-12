from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .forms import SquirrelForm

def index(request):
    return render(request, 'sightings/index.html', {})

def stats(request):
    return render(request, 'sightings/stats.html', {})

def add_squirrel(request):
    if request.method == 'POST':
        form = SqurrielForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
   
    return JsonResponse({})

# Create your views here.
