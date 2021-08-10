from django.http import HttpResponse
from django.shortcuts import render
from prog1.forms import Person
from prog1.models import PersonModel
import requests
from prog1.api import CocktailApi


def home(request):
    return HttpResponse("Hallo World")

def test(request):
    context = {'name':'otto','alter':24}
    context["person_form"] = Person()
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
    cocktails = CocktailApi()
    context = {"users":users, "filtered":filter_users, "drink":cocktails.get_cocktails("margarita")}
    return render(request, "prog1/db_table.html", context)

