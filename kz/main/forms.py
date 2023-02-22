
from django import forms
from django.forms import ModelChoiceField
from .models import *
 
 
# creating a form
class LokacijaForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Lokacija
 
        # specify fields to be used
        fields = [
            "ime",
            "grad",
            "zem_sirina",
            "zem_duzina"
        ]

class FavoritForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Korisnik
 
        # specify fields to be used
        fields = [
            'fav_lokacije'
        ]

class DeleteLokacijaForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Lokacija
        fields = [
            'ime'
        ]
 