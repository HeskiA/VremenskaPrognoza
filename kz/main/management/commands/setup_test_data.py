import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Grad, Lokacija, Korisnik, PrognoziranoVrijeme, TrenutnoVrijeme
from main.factories import (
    GradFactory,
    LokacijaFactory,
    KorisnikFactory,
    PrognoziranoVrijemeFactory,
    TrenutnoVrijemeFactory
)

NUM_GRADS = 50
NUM_LOKACIJAS = 150 
NUM_KORISNIKS = 300
NUM_TRENUTNO_VRIJEMES = NUM_LOKACIJAS
NUM_PROGNOZIRANO_VRIJEMES = NUM_LOKACIJAS * 3


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Grad, Lokacija, Korisnik, TrenutnoVrijeme]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_GRADS):
            grad = GradFactory()

        #for _ in range(NUM_LOKACIJAS):
        #    lokacija = LokacijaFactory()

        for _ in range(NUM_KORISNIKS):
            korisnik = KorisnikFactory()

        for _ in range(NUM_TRENUTNO_VRIJEMES):
            trenutno_vrijeme = TrenutnoVrijemeFactory()

        for _ in range(NUM_PROGNOZIRANO_VRIJEMES):
            prognozirano_vrijeme = PrognoziranoVrijemeFactory()