from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('',views.frigo,name='frigo'),
    path('contenu/', views.contenu2, name='contenu2'),
]