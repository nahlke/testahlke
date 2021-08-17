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
    djangoDok = models.CharField(max_length = 500, null=True, blank=True)

class ModelsModel(models.Model):
    modelsDok = models.CharField(max_length = 500, null=True, blank=True)

class TemplatesModel(models.Model):
    templatesDok = models.CharField(max_length = 500, null=True, blank=True)

class AdminModel(models.Model):
    adminDok = models.CharField(max_length = 500, null=True, blank=True)

class ApiModel(models.Model):
    apiDok = models.CharField(max_length = 500, null=True, blank=True)

class FormsModel(models.Model):
    formsDok  = models.CharField(max_length = 500, null=True, blank=True)

class AppUrlModel(models.Model):
    appurlDok  = models.CharField(max_length = 500, null=True, blank=True)

class ViewsModel(models.Model):
    viewsDok  = models.CharField(max_length = 500, null=True, blank=True)

class SettingsModel(models.Model):
    settingsDok  = models.CharField(max_length = 500, null=True, blank=True)

class HauptUrlModel(models.Model):
    haupturlDok  = models.CharField(max_length = 500, null=True, blank=True)

class SonstigesModel(models.Model):
    sonstigesDok = models.CharField(max_length = 500, null=True, blank=True)

class GitHubModel(models.Model):
    githubDok = models.CharField(max_length = 500, null=True, blank=True)

class BefehleModel(models.Model):
    befehleDok = models.CharField(max_length = 500, null=True, blank=True)
