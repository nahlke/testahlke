from django import forms
from django.forms import ModelForm
from prog1.models import Artikel

class Person(forms.Form):
    name = forms.CharField(label='Dein Name', max_length = 30)
    alter = forms.IntegerField(label='Dein Alter')

class ArtikelForm(ModelForm):
    class Meta:
        model = Artikel
        fields=["artikenummer", "artikelname", "artikelbeschreibung", "lieverantenummer", "img"]