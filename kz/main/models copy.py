
from django.db import models

class Driver(models.Model):
	# General
	first_name = models.CharField("Ime", max_length=64)
	last_name = models.CharField("Prezime", max_length=64)
	birth_date = models.DateField("Datum rođenja", blank=True, null=True)
	# Contact
	email = models.EmailField("Email", blank=True, null=True)
	phone = models.CharField("Telefon", max_length=15, blank=True, null=True)


class Car(models.Model):
	# General
	horse_power = models.IntegerField("Konjska snaga", null=True, blank=True)
	year = models.IntegerField("Godina proizvodnje")
	description = models.TextField("Detalji", null=True, blank=True)
	plates = models.CharField("Registracija", null=True, max_length=20)

	# Foreign keys
	model = models.ForeignKey(
		"Manufacturer", verbose_name="Manufacturer", on_delete=models.CASCADE)
	
	driver = models.ForeignKey(
		"Driver", verbose_name="Driver", on_delete=models.CASCADE)
		

class Manufacturer(models.Model):
	name = models.CharField("Naziv", max_length=128)

