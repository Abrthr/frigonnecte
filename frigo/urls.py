from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('',views.frigo,name='frigo'),
    path('contenu/', views.contenu3, name='contenu'),
]