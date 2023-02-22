from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from main.models import Grad, Lokacija, Korisnik, TrenutnoVrijeme, PrognoziranoVrijeme
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from main.forms import *
# Create your views here.

def homepage(request):
    return render(request, 'pocetna.html')

class GradList(ListView):
    model = Grad

class Grad1(ListView):
    template_name = 'main/mjerne_lokacije.html'

    def get_queryset(self):
        self.grad = get_object_or_404(Grad, id=self.kwargs['grad'])
        return Lokacija.objects.filter(grad_id=self.grad.id)

class LokacijaList(ListView):
    model = Lokacija

class Lokacija1(ListView):
    template_name = 'main/trenutnovrijeme_list.html'

    def get_queryset(self):
        self.lokacija = get_object_or_404(Lokacija, id=self.kwargs['lokacija'])
        return TrenutnoVrijeme.objects.filter(lokacija_id=self.lokacija.id)

class KorisnikList(ListView):
    model = Korisnik

class TrenutnoVrijemeList(ListView):
    model = TrenutnoVrijeme

class TrenutnoVrijeme1(ListView):
    template_name = 'main/trenutnovrijeme.html'

    def get_queryset(self):
        self.lokacija = get_object_or_404(Lokacija, id=self.kwargs['id'])
        return TrenutnoVrijeme.objects.filter(lokacija_id=self.lokacija.id)


class PrognoziranoVrijemeList(ListView):
    model = PrognoziranoVrijeme

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            novi_korisnik = Korisnik(ime="nije", prezime="bitno", email=username+"@gmail.com")
            novi_korisnik.save()
            return redirect('main:homepage')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'pocetna.html')

class Favoriti(ListView):
    template_name = 'main/favoriti.html'

    def get_queryset(self):
        self.korisnik = get_object_or_404(Korisnik, email=self.kwargs['username'] + '@gmail.com')
        return Lokacija.objects.filter(korisnik__id=self.korisnik.id)
    

def create_view_lokacija(request):
    context ={}

    form = LokacijaForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "main/create_view.html", context)

def create_view_favorit(request, username):
    context ={}
 
    obj = get_object_or_404(Korisnik, email = (username + "@gmail.com"))
 
    form = FavoritForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/favoriti/" + username)
 
    context["form"] = form
 
    return render(request, "main/create_view.html", context)

def delete_view_favorit(request, username):
    context ={}
 
    obj = get_object_or_404(Korisnik, email = (username + "@gmail.com"))
 

    form = FavoritForm(request.POST or None, instance = obj)
    if form.is_valid():
        obj.fav_lokacije.clear()
        return HttpResponseRedirect("/favoriti/" + username)
 
    context["form"] = form
 
    return render(request, "main/create_view.html", context)

def delete_view_lokacija(request, pk):
    lokacija = Lokacija.objects.get(id=pk)

    if request.method == "GET":
        lokacija.delete()

    context = {'lokacija':lokacija}

    return redirect('main:lokacije')
