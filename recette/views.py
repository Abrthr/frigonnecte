from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def recette(request):
    return HttpResponse("Recette chocolat : 1. 200g de chocolat  2. C'est prêt !!")