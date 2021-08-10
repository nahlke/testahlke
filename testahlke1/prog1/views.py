from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hallo World")

def test(request):
    context = {'name':'otto','alter':24}
    return render(request, "prog1/test.html", context)

def createPerson(request):
    context = {'name': 'otto', 'alter': 24}
    return render(request, "prog1/test.html", context)