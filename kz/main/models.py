
from django.db import models
from django.utils import timezone


class Grad(models.Model):
	# General
    ime_grada = models.CharField("Ime grada", max_length=64)
    drzava = models.CharField("Drzava u kojoj se nalazi: ", max_length=64)
    
    def __str__(self):
        return self.ime_grada + ", " + self.drzava

class Lokacija(models.Model):
	# General
    ime = models.CharField("Ime", max_length=64)
    grad = models.ForeignKey(Grad, on_delete=models.CASCADE)
    zem_sirina = models.CharField("Zemljopisna sirina", max_length=64)
    zem_duzina = models.CharField("Zemljopisna duzina", max_length=64)
    

class Korisnik(models.Model):
	# General
    ime = models.CharField("Ime", max_length=64)
    prezime = models.CharField("Prezime", max_length=64)
    email = models.EmailField("Email", blank=True, null=True)
    fav_lokacije = models.ManyToManyField(Lokacija, blank=True)

    def __str__(self):
        return self.email


class TrenutnoVrijeme(models.Model):
    lokacija = models.OneToOneField(
        Lokacija,
        on_delete=models.CASCADE,
        primary_key=True,
    )
	#temperatura, vlaga, tlak
    temperatura = models.CharField(max_length=6)
    vlaga = models.CharField(max_length=3)
    tlak = models.CharField(max_length=5)
    

class PrognoziranoVrijeme(models.Model):
    temperatura = models.CharField(max_length=6)
    vlaga = models.CharField(max_length=3)
    tlak = models.CharField(max_length=5)
    datum_i_vrijeme = models.DateTimeField(default=timezone.now)
    lokacija = models.ForeignKey(Lokacija, on_delete=models.CASCADE)

    def __str__(self):
        return "Prognoza za " + self.lokacija.ime + " " + str(self.datum_i_vrijeme)



