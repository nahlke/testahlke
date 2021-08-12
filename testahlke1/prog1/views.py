from django.http import HttpResponse
from django.shortcuts import render
from prog1.forms import Person, ArtikelForm, DjangoForm, ModelsForm, TemplatesForm, AdminForm, ApiForm, FormsForm,\
    AppUrlForm, ViewsForm, SettingsForm, HauptUrlForm, GitHubForm, SonstigesForm
from prog1.models import PersonModel, Artikel, DjangoModel, ModelsModel, TemplatesModel, AdminModel, ApiModel, FormsModel,\
    AppUrlModel, ViewsModel, SettingsModel, HauptUrlModel, GitHubModel, SonstigesModel
import requests
from prog1.api import CocktailApi
from django.views.generic.list import ListView


def test(request):
    context = {'name':'otto','alter':24}
    context["person_form"] = Person()
    context["artikel_form"] = ArtikelForm()

    return render(request, "prog1/test.html", context)

def dok(request):
    return render(request, "prog1/dokumentieren.html")

def doks(request):
    return render(request, "prog1/dokumentationen.html")

def home(request):
    return render(request, "prog1/home.html")

def createPerson(request):
    post_name = request.POST.get("name")
    post_alter = request.POST.get("alter")
    new_person = PersonModel(name=post_name, alter=post_alter)
    new_person.save()
    return HttpResponse("{0} ist {1} Jahre alt".format(new_person.name, new_person.alter))

def user_list(request):
    users = PersonModel.objects.all()
    filter_users = PersonModel.objects.filter(alter=10)
    #cocktails = CocktailApi()
    context = {"users":users, "filtered":filter_users}
    return render(request, "prog1/db_table.html", context)

# API , "drink":cocktails.get_cocktails("margarita")

def artikel(request):
    new_artikel = ArtikelForm(request.POST, request.FILES)
    if new_artikel.is_valid():
        value = new_artikel.cleaned_data
        artikel = Artikel(value)
        artikel.save()
        return HttpResponse("Artikel wurde erstellt")
    else:
        print("Fehler")
        return HttpResponse("Fehler" + str(new_artikel.errors))

class ArtikelListView(ListView):
    model = Artikel


def djangodok(request):
    context = {'name': 'otto'}
    context["djangoform"] = DjangoForm()
    return render(request, "prog1/dokumentation/django.html", context)

def modelsdok(request):
    context = {'name': 'otto'}
    context["modelsform"] = ModelsForm()
    return render(request, "prog1/dokumentation/models.html", context)

def templatesdok(request):
    context = {'name': 'otto'}
    context["templatesform"] = TemplatesForm()
    return render(request, "prog1/dokumentation/templates.html", context)

def admindok(request):
    context = {'name': 'otto'}
    context["adminform"] = AdminForm()
    return render(request, "prog1/dokumentation/admin.html", context)

def apidok(request):
    context = {'name': 'otto'}
    context["apiform"] = ApiForm()
    return render(request, "prog1/dokumentation/api.html", context)

def formsdok(request):
    context = {'name': 'otto'}
    context["formsform"] = FormsForm()
    return render(request, "prog1/dokumentation/forms.html", context)

def appurldok(request):
    context = {'name': 'otto'}
    context["appurlform"] = AppUrlForm()
    return render(request, "prog1/dokumentation/appurl.html", context)

def viewsdok(request):
    context = {'name': 'otto'}
    context["viewsform"] = ViewsForm()
    return render(request, "prog1/dokumentation/views.html", context)

def settingsdok(request):
    context = {'name': 'otto'}
    context["settingsform"] = SettingsForm()
    return render(request, "prog1/dokumentation/settings.html", context)

def haupturldok(request):
    context = {'name': 'otto'}
    context["haupturlform"] = HauptUrlForm()
    return render(request, "prog1/dokumentation/haupturl.html", context)

def githubdok(request):
    context = {'name': 'otto'}
    context["githubform"] = GitHubForm()
    return render(request, "prog1/dokumentation/github.html", context)

def sonstigesdok(request):
    context = {'name': 'otto'}
    context["sonstigesform"] = SonstigesForm()
    return render(request, "prog1/dokumentation/sonstiges.html", context)




