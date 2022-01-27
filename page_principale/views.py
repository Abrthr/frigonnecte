from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def page_principale(request):
    return HttpResponse("Bienvenue dans ton frigo")