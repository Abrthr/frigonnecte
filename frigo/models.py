from django.db import models

from recette.models import Recette,Ingredient

# Create your models here.

class Frigo(models.Model):
    nom_frigo = models.CharField(max_length=50)

class contient (models.Model):
    frigo = models.ForeignKey(Frigo,on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette,on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient,on_delete=models.PROTECT)
    quantite = models.FloatField()
    date_achat = models.DateField(auto_now=True)
    date_de_peremption = models.DateField()

