# Create your views here.
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import SightForm
from .models import Sight


# Create your views here.
def homepage_view(request):
    return render(request, 'sightings/homepage.html')


def map_view(request):
    sights = Sight.objects.all()[:200]
    context = {
        'sights': sights,
    }
    return render(request, 'sightings/map.html', context)


def list_sights(request):
    sights = Sight.objects.all()
    fields = ['Unique_Squirrel_Id', 'Longtitude', 'Latitude', 'Date', 'Shift']
    context = {
        'sights': sights,
        'fields': fields,
    }
    return render(request, 'sightings/list.html', context)


def update_sights(request, Unique_Squirrel_Id):
    sight = get_object_or_404(Sight, Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        form = SightForm(request.POST, instance=sight)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{Unique_Squirrel_Id}')
    else:
        form = SightForm(instance=sight)

    context = {
        'form': form,
    }
    return render(request, 'sightings/update.html', context)


def add_sights(request):
    if request.method == 'POST':
        form = SightForm.MMEditidStateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightForm()

    context = {
        'form': form,
    }

    return render(request, 'sightings/add.html', context)


def stats_view(request):
    return render(request, 'sightings/stats.html')


def index(request):
    return render(request, 'sightings/homepage.html')
