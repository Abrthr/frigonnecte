from django.db import models
from django.conf import settings

from frigo.models import Frigo
from recette.models import Recette,Ingredient
# Create your models here.

class Personne(models.Model):
    nom = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    Omnivore = "OMni"
    Vegan = 'VeGa'
    Vegetarian = 'VeGe'

    regime_alimentaire = [(Omnivore, 'Omnivore'),(Vegan,"Vegan"),(Vegetarian, "Vegétarien")]
    Regime = models.CharField(max_length=100,choices = regime_alimentaire,default=Omnivore)

class Carnet(models.Model):
    Personne = models.ForeignKey(Personne,on_delete=models.CASCADE)
    Recette = models.ForeignKey(Recette,on_delete=models.CASCADE)
    Favori = models.BooleanField(default=False)

class aimepas(models.Model):
    personne = models.ForeignKey(Personne,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)

class Possede (models.Model):
    Personne  = models.ForeignKey(Personne,on_delete=models.CASCADE)
    frigo = models.ForeignKey(Frigo,on_delete=models.CASCADE)
