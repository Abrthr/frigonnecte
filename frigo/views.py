from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def frigo(request):
    return HttpResponse("frigo")