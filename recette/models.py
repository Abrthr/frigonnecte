from django.db import models

# Create your models here.

class Recette(models.Model):
    Est_Prive = models.BooleanField(default=True)

class Ingredient(models.Model):
    Poids = "g"
    Volume1 = "L"
    Volume2 = "mL"
    Nombre = "NBR"

    type = [(Poids,"gramme"),(Volume1,'Litre'),(Volume2, 'mL'),(Nombre, 'Nbre')]
    type_quantite = models.CharField(max_length = 3,choices = type,default = Nombre)

class Comporte(models.Model):
    Recette = models.ForeignKey(Recette,on_delete=models.CASCADE)
    Ingredient = models.ForeignKey(Ingredient,on_delete=models.PROTECT)
    quantite = models.FloatField()
    