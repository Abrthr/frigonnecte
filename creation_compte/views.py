from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def creation(request):
    return HttpResponse("Page de Création de compte")