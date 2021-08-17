from django.http import HttpResponse
from django.shortcuts import render
from prog1.forms import Person, ArtikelForm, DjangoForm, ModelsForm, TemplatesForm, AdminForm, ApiForm, FormsForm,\
    AppUrlForm, ViewsForm, SettingsForm, HauptUrlForm, GitHubForm, SonstigesForm, BefehleForm
from prog1.models import PersonModel, Artikel, DjangoModel, ModelsModel, TemplatesModel, AdminModel, ApiModel, FormsModel,\
    AppUrlModel, ViewsModel, SettingsModel, HauptUrlModel, GitHubModel, SonstigesModel, BefehleModel
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

def befehledok(request):
    context = {'name': 'otto'}
    context["befehleform"] = BefehleForm()
    return render(request, "prog1/dokumentation/befehle.html", context)



def djangopost(request):
    post_django = request.POST.get("djangoform")
    new_django = DjangoModel(djangoDok=post_django)
    new_django.save()
    return HttpResponse("Gespeichert")

def modelspost(request):
    post_models = request.POST.get("modelsform")
    new_models = ModelsModel(modelsDok=post_models)
    new_models.save()
    return HttpResponse("Gespeichert")

def templatespost(request):
    post_templates = request.POST.get("templatesform")
    new_templates = TemplatesModel(templatesDok=post_templates)
    new_templates.save()
    return HttpResponse("Gespeichert")

def adminpost(request):
    post_admin = request.POST.get("adminform")
    new_person = AdminModel(adminDok=post_admin)
    new_person.save()
    return HttpResponse("Gespeichert")

def apipost(request):
    post_api = request.POST.get("apiform")
    new_person = ApiModel(apiDok=post_api)
    new_person.save()
    return HttpResponse("Gespeichert")

def formspost(request):
    post_forms = request.POST.get("formsform")
    new_person = FormsModel(formsDok=post_forms)
    new_person.save()
    return HttpResponse("Gespeichert")

def appurlpost(request):
    post_appurl = request.POST.get("appurlform")
    new_person = AppUrlModel(appurlDok=post_appurl)
    new_person.save()
    return HttpResponse("Gespeichert")

def viewspost(request):
    post_views = request.POST.get("viewsform")
    new_person = ViewsModel(viewsDok=post_views)
    new_person.save()
    return HttpResponse("Gespeichert")

def settingspost(request):
    post_settings = request.POST.get("settingsform")
    new_person = SettingsModel(settingsDok=post_settings)
    new_person.save()
    return HttpResponse("Gespeichert")

def haupturlpost(request):
    post_haupturl = request.POST.get("haupturlform")
    new_person = HauptUrlModel(haupturlDok=post_haupturl)
    new_person.save()
    return HttpResponse("Gespeichert")

def githubpost(request):
    post_github = request.POST.get("githubform")
    new_person = GitHubModel(githubDok=post_github)
    new_person.save()
    return HttpResponse("Gespeichert")

def sonstigespost(request):
    post_sonstiges = request.POST.get("sonstigesform")
    new_person = SonstigesModel(sonstigesDok=post_sonstiges)
    new_person.save()
    return HttpResponse("Gespeichert")

def befehlepost(request):
    post_befehle = request.POST.get("befehleform")
    new_person = BefehleModel(befehleDok=post_befehle)
    new_person.save()
    return HttpResponse("Gespeichert")



def djangodoks(request):
    django = DjangoModel.objects.all()
    context = {"djangoform": django}
    return render(request, "prog1/dokumente/djangos.html", context)

def modelsdoks(request):
    models = ModelsModel.objects.all()
    context = {"modelsform": models}
    return render(request, "prog1/dokumente/modelss.html", context)

def templatesdoks(request):
    templates = TemplatesModel.objects.all()
    context = {"templatesform": templates}
    return render(request, "prog1/dokumente/templatess.html", context)

def admindoks(request):
    admin = AdminModel.objects.all()
    context = {"adminform": admin}
    return render(request, "prog1/dokumente/admins.html", context)

def apidoks(request):
    api = ApiModel.objects.all()
    context = {"apiform": api}
    return render(request, "prog1/dokumente/apis.html", context)

def formsdoks(request):
    forms = FormsModel.objects.all()
    context = {"formsform": forms}
    return render(request, "prog1/dokumente/formss.html", context)

def appurldoks(request):
    appurl = AppUrlModel.objects.all()
    context = {"appurlform": appurl}
    return render(request, "prog1/dokumente/appurls.html", context)

def viewsdoks(request):
    views = ViewsModel.objects.all()
    context = {"viewsform": views}
    return render(request, "prog1/dokumente/viewss.html", context)

def settingsdoks(request):
    settings = SettingsModel.objects.all()
    context = {"settingsform": settings}
    return render(request, "prog1/dokumente/settingss.html", context)

def haupturldoks(request):
    haupturl = HauptUrlModel.objects.all()
    context = {"haupturlform": haupturl}
    return render(request, "prog1/dokumente/haupturls.html", context)

def githubdoks(request):
    github = GitHubModel.objects.all()
    context = {"githubform": github}
    return render(request, "prog1/dokumente/githubs.html", context)

def sonstigesdoks(request):
    sonstiges = SonstigesModel.objects.all()
    context = {"sonstigesform": sonstiges}
    return render(request, "prog1/dokumente/sonstigess.html", context)

def befehledoks(request):
    sonstiges = BefehleModel.objects.all()
    context = {"befehleform": sonstiges}
    return render(request, "prog1/dokumente/befehles.html", context)


