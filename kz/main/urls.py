from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('gradovi', views.GradList.as_view()),
    path('lokacije', views.LokacijaList.as_view()),
    path('korisnici', views.KorisnikList.as_view()),
    path('trenutnavremena', views.TrenutnoVrijemeList.as_view()),
    path('prognoze', views.PrognoziranoVrijemeList.as_view()),
]
