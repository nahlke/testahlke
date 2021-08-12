from django import forms
from django.forms import ModelForm
from prog1.models import Artikel, DjangoModel, ModelsModel, TemplatesModel, AdminModel, ApiModel, FormsModel, AppUrlModel, ViewsModel, SettingsModel,\
    HauptUrlModel, GitHubModel, SonstigesModel

class Person(forms.Form):
    name = forms.CharField(label='Dein Name', max_length = 30)
    alter = forms.IntegerField(label='Dein Alter')

class ArtikelForm(ModelForm):
    class Meta:
        model = Artikel
        fields=["artikenummer", "artikelname", "artikelbeschreibung", "lieverantenummer", "img"]

class DjangoForm(forms.Form):
    djangoform = forms.CharField(label='DjangoDok', max_length = 500)

class ModelsForm(forms.Form):
    modelsform = forms.CharField(label='ModelsDok', max_length = 500)

class TemplatesForm(forms.Form):
    templatesform = forms.CharField(label='TemplatesDok', max_length = 500)

class AdminForm(forms.Form):
    adminform = forms.CharField(label='AdminDok', max_length = 500)

class ApiForm(forms.Form):
    apiform = forms.CharField(label='ApiDok', max_length = 500)

class FormsForm(forms.Form):
    formsform = forms.CharField(label='FormsDok', max_length = 500)

class AppUrlForm(forms.Form):
    appurlform = forms.CharField(label='AppUrlDok', max_length = 500)

class ViewsForm(forms.Form):
    viewsform = forms.CharField(label='ViewsDok', max_length = 500)

class SettingsForm(forms.Form):
    settingsform = forms.CharField(label='SettingsDok', max_length = 500)

class HauptUrlForm(forms.Form):
    haupturlform = forms.CharField(label='HauptUrlDok', max_length = 500)

class GitHubForm(forms.Form):
    githubform = forms.CharField(label='GitHubDok', max_length = 500)

class SonstigesForm(forms.Form):
    sonstigesform = forms.CharField(label='SonstigesDok', max_length = 500)