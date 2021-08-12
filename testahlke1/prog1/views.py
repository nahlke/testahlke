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





def djangopost(request):
    post_django = request.POST.get("djangoDok")
    new_person = DjangoModel(djangoDok=post_django)
    new_person.save()
    return HttpResponse("Gespeichert")

def modelspost(request):
    post_models = request.POST.get("modelsDok")
    new_person = ModelsModel(modelsDok=post_models)
    new_person.save()
    return HttpResponse("Gespeichert")

def templatespost(request):
    post_templates = request.POST.get("templatesDok")
    new_person = TemplatesModel(templatesDok=post_templates)
    new_person.save()
    return HttpResponse("Gespeichert")

def adminpost(request):
    post_admin = request.POST.get("adminDok")
    new_person = AdminModel(adminDok=post_admin)
    new_person.save()
    return HttpResponse("Gespeichert")

def apipost(request):
    post_api = request.POST.get("apiDok")
    new_person = ApiModel(apiDok=post_api)
    new_person.save()
    return HttpResponse("Gespeichert")

def formspost(request):
    post_forms = request.POST.get("formsDok")
    new_person = FormsModel(formsDok=post_forms)
    new_person.save()
    return HttpResponse("Gespeichert")

def appurlpost(request):
    post_appurl = request.POST.get("appurlDok")
    new_person = AppUrlModel(appurlDok=post_appurl)
    new_person.save()
    return HttpResponse("Gespeichert")

def viewspost(request):
    post_views = request.POST.get("viewsDok")
    new_person = ViewsModel(viewsDok=post_views)
    new_person.save()
    return HttpResponse("Gespeichert")

def settingspost(request):
    post_settings = request.POST.get("settingsDok")
    new_person = SettingsModel(settingsDok=post_settings)
    new_person.save()
    return HttpResponse("Gespeichert")

def haupturlpost(request):
    post_haupturl = request.POST.get("haupturlDok")
    new_person = HauptUrlModel(haupturlDok=post_haupturl)
    new_person.save()
    return HttpResponse("Gespeichert")

def githubpost(request):
    post_github = request.POST.get("githubDok")
    new_person = GitHubModel(githubDok=post_github)
    new_person.save()
    return HttpResponse("Gespeichert")

def sonstigespost(request):
    post_sonstiges = request.POST.get("sonstigesDok")
    new_person = SonstigesModel(sonstigesDok=post_sonstiges)
    new_person.save()
    return HttpResponse("Gespeichert")



def djangodoks(request):
    django = DjangoModel.objects.all()
    context = {"djangoform": django}
    print(django)
    return render(request, "prog1/dokumente/djangos.html", context)

def modelsdoks(request):
    admin = DjangoModel.objects.all()
    context = {"modelsform": admin}
    return render(request, "prog1/dokumente/modelss.html", context)

def templatesdoks(request):
    admin = DjangoModel.objects.all()
    context = {"templatesform": admin}
    return render(request, "prog1/dokumente/templatess.html", context)

def admindoks(request):
    admin = DjangoModel.objects.all()
    context = {"adminform": admin}
    return render(request, "prog1/dokumente/admins.html", context)

def apidoks(request):
    admin = DjangoModel.objects.all()
    context = {"apiform": admin}
    return render(request, "prog1/dokumente/apis.html", context)

def formsdoks(request):
    admin = DjangoModel.objects.all()
    context = {"formsform": admin}
    return render(request, "prog1/dokumente/formss.html", context)

def appurldoks(request):
    admin = DjangoModel.objects.all()
    context = {"appurlform": admin}
    return render(request, "prog1/dokumente/appurls.html", context)

def viewsdoks(request):
    admin = DjangoModel.objects.all()
    context = {"viewsform": admin}
    return render(request, "prog1/dokumente/viewss.html", context)

def settingsdoks(request):
    admin = DjangoModel.objects.all()
    context = {"settingsform": admin}
    return render(request, "prog1/dokumente/settingss.html", context)

def haupturldoks(request):
    admin = DjangoModel.objects.all()
    context = {"haupturlform": admin}
    return render(request, "prog1/dokumente/haupturls.html", context)

def githubdoks(request):
    admin = DjangoModel.objects.all()
    context = {"githubform": admin}
    return render(request, "prog1/dokumente/githubs.html", context)

def sonstigesdoks(request):
    admin = DjangoModel.objects.all()
    context = {"sonstigesform": admin}
    return render(request, "prog1/dokumente/sonstigess.html", context)




