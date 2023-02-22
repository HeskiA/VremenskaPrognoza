from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from main.views import *
from main.models import *
from datetime import datetime


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('main:homepage')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, homepage)

    def test_gradovi_url_is_resolved(self):
        url = reverse('main:gradovi')

        self.assertEquals(resolve(url).func.view_class, GradList)

    def test_lokacije_url_is_resolved(self):
        url = reverse('main:lokacije')

        self.assertEquals(resolve(url).func.view_class, LokacijaList)

    def test_korisnici_url_is_resolved(self):
        url = reverse('main:korisnici')

        self.assertEquals(resolve(url).func.view_class, KorisnikList)

    def test_trenutnavremena_url_is_resolved(self):
        url = reverse('main:trenutnavremena')

        self.assertEquals(resolve(url).func.view_class, TrenutnoVrijemeList)


    def test_prognoze_url_is_resolved(self):
        url = reverse('main:prognoze')

        self.assertEquals(resolve(url).func.view_class, PrognoziranoVrijemeList)


    def test_register_url_is_resolved(self):
        url = reverse('main:register')

        self.assertEquals(resolve(url).func, register)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('main:homepage')
        self.gradovi_url = reverse('main:gradovi')
        self.lokacije_url = reverse('main:lokacije')
        self.korisnici_url = reverse('main:korisnici')
        self.trenutnavremena_url = reverse('main:trenutnavremena')
        self.prognoze_url = reverse('main:prognoze')
        self.register_url = reverse('main:register')
        self.logout_url = reverse('main:logout')



    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pocetna.html')

    def test_project_gradovi_GET(self):
        client = Client()

        response = client.get(self.gradovi_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/grad_list.html')
        
    def test_project_lokacije_GET(self):
        client = Client()

        response = client.get(self.lokacije_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/lokacija_list.html')

    def test_project_korisnici_GET(self):
        client = Client()

        response = client.get(self.korisnici_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/korisnik_list.html')

    def test_project_trenutnavremena_GET(self):
        client = Client()

        response = client.get(self.trenutnavremena_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/trenutnovrijeme_list.html')

    def test_project_prognoze_GET(self):
        client = Client()

        response = client.get(self.prognoze_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/prognoziranovrijeme_list.html')

    def test_project_register_GET(self):
        client = Client()

        response = client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_project_logout_GET(self):
        client = Client()

        response = client.get(self.logout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pocetna.html')
    

class Testmodels(TestCase):

    def setUp(self):
        self.grad1 = Grad.objects.create(
            ime_grada = "neki-grad",
            drzava = "neka-drzava",
        )

        self.lokacija1 = Lokacija.objects.create(
            ime = "neka-lokacija",
            grad = self.grad1,
            zem_sirina = "4.23121231",
            zem_duzina = "2.31252131"
        )

        self.korisnik1 = Korisnik.objects.create(
            ime = "neko-ime",
            prezime = "neko-prezime",
            email = "neki-email",
        )
        self.korisnik1.save()
        self.korisnik1.fav_lokacije.add(self.lokacija1)

        self.trenutnovrijeme1 = TrenutnoVrijeme.objects.create(
            temperatura = "22",
            vlaga = "33",
            tlak = "1011",
            lokacija = self.lokacija1
        )

        self.prognoziranovrijeme1 = PrognoziranoVrijeme.objects.create(
            temperatura = "22",
            vlaga = "33",
            tlak = "1011",
            lokacija = self.lokacija1
        )

    def test_grad(self):
        self.assertEquals(self.grad1.ime_grada, "neki-grad")

    def test_lokacija(self):
        self.assertEquals(self.lokacija1.ime, "neka-lokacija")
        self.assertEquals(self.lokacija1.grad, self.grad1)

    def test_korisnik(self):
        self.assertEquals(self.korisnik1.ime, "neko-ime")

    def test_trenutnovrijeme(self):
        self.assertEquals(self.trenutnovrijeme1.lokacija, self.lokacija1)

    def prognoziranovrijeme(self):
        self.assertEquals(self.prognoziranovrijeme1.lokacija, self.lokacija1)
