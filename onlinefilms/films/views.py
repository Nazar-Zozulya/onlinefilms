from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def main(request):
    films = Films.objects.all()
    # genres = Genre.objects.all()
    context={}
    context["films"] = films
    return render(request,'main.html', context=context)

def description(request,films_id):
    films = Films.objects.all()
    descriptions = get_object_or_404(Description, film=films_id)
    films = Films.objects.get(id=films_id)
    # films = Films.objects.get(id=films_id)

    context={"descriptions":descriptions,
             "films":films}
    # context["films"] = films

    return render(request,"description.html",context)