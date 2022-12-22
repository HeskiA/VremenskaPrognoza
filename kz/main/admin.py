from django.contrib import admin
from main.models import *
# Register your models here.

model_list = [Grad, Lokacija, Korisnik, TrenutnoVrijeme, PrognoziranoVrijeme]
admin.site.register(model_list)