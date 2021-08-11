from django.http import HttpResponse
from django.shortcuts import render
from prog1.forms import Person, ArtikelForm
from prog1.models import PersonModel, Artikel
import requests
from prog1.api import CocktailApi
from django.views.generic.list import ListView


def home(request):
    return HttpResponse("Hallo World")

def test(request):
    context = {'name':'otto','alter':24}
    context["person_form"] = Person()
    context["artikel_form"] = ArtikelForm()
    return render(request, "prog1/test.html", context)
#sdsdsd
def createPerson(request):
    post_name = request.POST.get("name")
    post_alter = request.POST.get("alter")
    new_person = PersonModel(name=post_name, alter=post_alter)
    new_person.save()
    return HttpResponse("{0} ist {1} Jahre alt".format(new_person.name, new_person.alter))

def user_list(request):
    users = PersonModel.objects.all()
    filter_users = PersonModel.objects.filter(alter=10)
    cocktails = CocktailApi()
    context = {"users":users, "filtered":filter_users, "drink":cocktails.get_cocktails("margarita")}
    return render(request, "prog1/db_table.html", context)

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