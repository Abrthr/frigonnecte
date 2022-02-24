from django.db import models

from recette.models import Recette
from frigo.models import Frigo

# Create your models here.


class cuisine(models.Model):
    frigo = models.ForeignKey(Frigo,on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette,on_delete=models.CASCADE)
    date = models.DateField()