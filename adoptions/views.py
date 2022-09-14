from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Pet


def home(request): 
    pets = Pet.objects.all()   
    context = {
        "pets":pets,
        "titre": "Premier Django"
    }
    print(pets)
    return render(request, 'home.html', context)