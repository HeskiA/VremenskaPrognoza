import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from django.utils import timezone

from main.models import *

import random

class GradFactory(DjangoModelFactory):
	class Meta:
		model = Grad
	ime_grada = factory.Faker("city")
	drzava = factory.Faker("country")

class LokacijaFactory(DjangoModelFactory):
    class Meta:
        model = Lokacija

    ime = factory.Faker("first_name")
    grad = factory.Iterator(Grad.objects.all())
    zem_sirina = factory.Faker("latitude")
    zem_duzina = factory.Faker("latitude")

class KorisnikFactory(DjangoModelFactory):
    class Meta:
        model = Korisnik

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    email = factory.Faker("email")

class TrenutnoVrijemeFactory(DjangoModelFactory):
    class Meta:
        model = TrenutnoVrijeme

    temperatura = str(random.randint(-30, 45))
    vlaga = str(random.randint(0, 100))
    tlak = str(random.randint(950, 1050))
    lokacija = factory.SubFactory(LokacijaFactory)

class PrognoziranoVrijemeFactory(DjangoModelFactory):
    class Meta:
        model = PrognoziranoVrijeme

    temperatura = str(random.randint(-30, 45))
    vlaga = str(random.randint(0, 100))
    tlak = str(random.randint(950, 1050))
    datum_i_vrijeme = factory.fuzzy.FuzzyDateTime(timezone.now())
    lokacija = factory.Iterator(Lokacija.objects.all())



