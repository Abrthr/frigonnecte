from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def accueil(request):
    return render(request,'accueil/accueil.html')
