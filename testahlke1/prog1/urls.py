from django.urls import path
from prog1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test', views.test, name='test'),
    path('create-user', views.createPerson, name='user-create'),
    path('list', views.user_list, name='user_list'),
    path('artikel', views.artikel, name='artikel'),
    path('artikel-list', views.ArtikelListView.as_view(), name="artikel_list")
]