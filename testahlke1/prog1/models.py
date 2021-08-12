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

class DjangoModel(models.Model):
    djangoDok = models.TextField(max_length = 500, null=True, blank=True)

class ModelsModel(models.Model):
    modelsDok = models.TextField(max_length = 500, null=True, blank=True)

class TemplatesModel(models.Model):
    templatesDok = models.TextField(max_length = 500, null=True, blank=True)

class AdminModel(models.Model):
    adminDok = models.TextField(max_length = 500, null=True, blank=True)

class ApiModel(models.Model):
    apiDok = models.TextField(max_length = 500, null=True, blank=True)

class FormsModel(models.Model):
    formsDok  = models.TextField(max_length = 500, null=True, blank=True)

class AppUrlModel(models.Model):
    appUrlDok  = models.TextField(max_length = 500, null=True, blank=True)

class ViewsModel(models.Model):
    viewsDok  = models.TextField(max_length = 500, null=True, blank=True)

class SettingsModel(models.Model):
    settingsDok  = models.TextField(max_length = 500, null=True, blank=True)

class HauptUrlModel(models.Model):
    hauptUrlDok  = models.TextField(max_length = 500, null=True, blank=True)

class SonstigesModel(models.Model):
    sonstigesDok = models.TextField(max_length = 500, null=True, blank=True)

class GitHubModel(models.Model):
    githubDok = models.TextField(max_length = 500, null=True, blank=True)
