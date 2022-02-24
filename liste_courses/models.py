from django.db import models

from frigo.models import Frigo
from recette.models import Ingredient

# Create your models here.

class Liste_course(models.Model):
    frigo = models.ForeignKey(Frigo,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    date = models.DateField()
    quantité = models.FloatField()
