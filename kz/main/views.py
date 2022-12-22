from django.shortcuts import render
from django.views.generic import ListView
from main.models import Grad, Lokacija, Korisnik, TrenutnoVrijeme, PrognoziranoVrijeme
# Create your views here.

def homepage(request):
    return render(request, 'pocetna.html')

class GradList(ListView):
    model = Grad

class LokacijaList(ListView):
    model = Lokacija

class KorisnikList(ListView):
    model = Korisnik

class TrenutnoVrijemeList(ListView):
    model = TrenutnoVrijeme

class PrognoziranoVrijemeList(ListView):
    model = PrognoziranoVrijeme


