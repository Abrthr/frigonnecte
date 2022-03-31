from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import contient



def contenu3(request):
    Ingredients = contient.objects.values("ingredient").filter(ingredient__isnull=True).all() #requette qui garde la colonne ingredient, et ne garde que les valeurs non null de cette dernière
    Recettes = contient.objects.values("recette").filter(recette__isnull=True).all() #requette qui garde la colonne recette, et ne garde que les valeurs non null de cette dernière
    context = {
        'ingredient': Ingredients,
        'recette' : Recettes,
    }
    return render(request,'frigo/morecontenu.html',context)

def frigo(request):
    return HttpResponse("frigo")
