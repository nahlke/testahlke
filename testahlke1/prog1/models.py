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

class DokumentationModel(models.Model):
    djangodokumation  = models.CharField(max_length = 500, null=True, blank=True)
    modelsdokumation  = models.CharField(max_length = 500, null=True, blank=True)
    templatesdokumation  = models.CharField(max_length = 500, null=True, blank=True)
    admindokumation  = models.CharField(max_length = 500, null=True, blank=True)
    apidokumation  = models.CharField(max_length = 500, null=True, blank=True)
    formsdokumation  = models.CharField(max_length = 500, null=True, blank=True)
    appUrldokumation  = models.CharField(max_length = 500, null=True, blank=True)
    viewsdokumation  = models.CharField(max_length = 500, null=True, blank=True)
    settingsdokumation  = models.CharField(max_length = 500, null=True, blank=True)
    hauptUrldokumation  = models.CharField(max_length = 500, null=True, blank=True)
    sonstigesdokumation  = models.CharField(max_length = 500, null=True, blank=True)
    githubdokumation = models.CharField(max_length = 500, null=True, blank=True)
