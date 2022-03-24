from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def page_principale(request):
    return render(request,'page_principale/page_principale.html')