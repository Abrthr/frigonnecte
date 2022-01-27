from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def liste_courses(request):
    return HttpResponse("Liste de courses vide")