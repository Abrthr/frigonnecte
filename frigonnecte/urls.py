"""frigonnecte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from accueil import views as viewsaccueil
from Calendrier import views as viewscalendrier
from LogIn import views as viewslogin
from creation_compte import views as viewscreation_compte
from frigo import views as viewsfrigo
from page_principale import views as viewspage_principale
from liste_courses import views as viewsliste_courses
from Paramètres import views as viewsparametres
from recette import views as viewsrecette


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('LogIn.urls')) ,#urls de l'application LogIn


    path('admin/', admin.site.urls),
    path('',viewsaccueil.accueil,name='accueil'),
    path('calendrier/',viewscalendrier.calendrier,name='calendrier'),
    path('creation_compte/',viewscreation_compte.creation_compte,name='creation_compte'),
    path('frigo/',viewsfrigo.frigo,name='frigo'),
    path('monfrigo/',viewspage_principale.page_principale,name='page_principale'),
    path('liste_courses/',viewsliste_courses.liste_courses,name='liste_courses'),
    path('parametres/',viewsparametres.parametres,name='parametres'),
    path('recette/',viewsrecette.recette,name='recette'),

]
