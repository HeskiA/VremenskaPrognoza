from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('favoriti/<username>', views.Favoriti.as_view(), name='favoriti'),
    path('favoriti/<username>/dodaj', views.create_view_favorit, name='addfavorit'),
    path('favoriti/<username>/brisi/', views.delete_view_favorit, name='delfavorit'),
    path('gradovi', views.GradList.as_view(), name='gradovi'),
    path('gradovi/<grad>/', views.Grad1.as_view()),
    path('lokacije/<lokacija>/', views.Lokacija1.as_view()),
    path('lokacije', views.LokacijaList.as_view(), name='lokacije'),
    path('dodajlokaciju', views.create_view_lokacija, name='dodlokaciju'),
    path('brisilokaciju/<pk>', views.delete_view_lokacija, name='brisilokaciju'),
    path('korisnici', views.KorisnikList.as_view(), name='korisnici'),
    path('trenutnavremena', views.TrenutnoVrijemeList.as_view(), name='trenutnavremena'),
    path('trenutnovrijeme/<id>/', views.TrenutnoVrijeme1.as_view()),
    path('prognoze', views.PrognoziranoVrijemeList.as_view(), name='prognoze'),
    path('accounts/register', views.register, name='register'),
    path('odjava', views.logout_view, name='logout')
]
