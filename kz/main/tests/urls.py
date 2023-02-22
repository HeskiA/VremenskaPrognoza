from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *;



class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, homepage)

    def test_gradovi_url_is_resolved(self):
        url = reverse('gradovi')

        self.assertEquals(resolve(url).func.view_class, GradList)

    def test_lokacije_url_is_resolved(self):
        url = reverse('lokacije')

        self.assertEquals(resolve(url).func.view_class, LokacijaList)

    def test_korisnici_url_is_resolved(self):
        url = reverse('korisnici')

        self.assertEquals(resolve(url).func.view_class, KorisnikList)
