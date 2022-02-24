# Generated by Django 3.2.8 on 2022-02-24 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0001_initial'),
        ('frigo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contient',
            name='ingredient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='recette.ingredient'),
        ),
        migrations.AlterField(
            model_name='contient',
            name='recette',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='recette.recette'),
        ),
    ]
