from django.http import HttpResponse
from django.shortcuts import render
from prog1.forms import Person, ArtikelForm, DokumentForm
from prog1.models import PersonModel, Artikel, DokumentationModel
import requests
from prog1.api import CocktailApi
from django.views.generic.list import ListView


def test(request):
    context = {'name':'otto','alter':24}
    context["person_form"] = Person()
    context["artikel_form"] = ArtikelForm()
    context["dokumentation_form"] = DokumentForm()

    return render(request, "prog1/test.html", context)

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

def dokumentation(request):
    new_dokumentation = DokumentForm(request.POST)
    if new_dokumentation.is_valid():
        value = new_dokumentation.cleaned_data
        dok = Dokumentation(value)
        dok.save()
        return HttpResponse("Dokumentation wurde erstellt")
    else:
        return HttpResponse("Fehler" + str(new_dokumentation.errors))