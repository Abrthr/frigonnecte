from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import contient

def contenu(request):
    contenu_frigo = contient.objects.all()
    output = ','.join([str(q.ingredient) for q in contenu_frigo])
    context = {'contenu': contenu_frigo}
    return HttpResponse(output)

#template.render(context, request)

def contenu2(request):
    contenu_frigo = contient.objects.all()
    context = {
        'contenu': contenu_frigo,
    }
    return render(request,'frigo/contenu.html',context)

def frigo(request):
    return HttpResponse("frigo")
