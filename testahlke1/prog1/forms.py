from django import forms
from django.forms import ModelForm
from prog1.models import Artikel, DokumentationModel

class Person(forms.Form):
    name = forms.CharField(label='Dein Name', max_length = 30)
    alter = forms.IntegerField(label='Dein Alter')

class ArtikelForm(ModelForm):
    class Meta:
        model = Artikel
        fields=["artikenummer", "artikelname", "artikelbeschreibung", "lieverantenummer", "img"]

class DokumentForm(ModelForm):
    class Meta:
        model = DokumentationModel
        fields = ["djangodokumation", "modelsdokumation", "templatesdokumation", "admindokumation", "apidokumation",
                  "formsdokumation", "appUrldokumation", "viewsdokumation", "settingsdokumation",
                  "hauptUrldokumation", "sonstigesdokumation", "githubdokumation"]
