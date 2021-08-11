from django.db import models

class PersonModel(models.Model):
    name = models.CharField(max_length=30)
    alter = models.IntegerField()

class Artikel(models.Model):
    artikenummer = models.CharField(max_length=18, primary_key=True)
    artikelname = models.CharField(max_length=100)
    artikelbeschreibung = models.CharField(max_length=256)
    lieverantenummer = models.CharField(max_length=18)
    img = models.FileField(upload_to="uploads")


