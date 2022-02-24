from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def calendrier(request):
    return HttpResponse("Calendrier")