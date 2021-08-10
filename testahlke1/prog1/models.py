from django.db import models

class PersonModel(models.Model):
    name = models.CharField(max_length=30)
    alter = models.IntegerField()
