from django.test import TestCase
from django.test import SimpleTestCase 
from django.urls import reverse
from laboratorio.models import Laboratorio

# Create your tests here.

class InicioTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get('/crud/inicio/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
       response = self.client.get(reverse("inicio")) 
       self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):  
       response = self.client.get(reverse("inicio")) 
       self.assertTemplateUsed(response, "inicio.html")

    def test_template_content(self): 
       response = self.client.get(reverse("inicio")) 
       self.assertContains(response, "<h1 class='p-4'>Inicio</h1>") 
       self.assertNotContains(response, "No es la Página")

class LaboratorioTest(TestCase):
   
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre = 'Laboratorio TEST',
                                                    ciudad = 'Ciudad TEST',
                                                    pais = 'Pais TEST')
    def test_model_content(self): 
        self.assertEqual(self.laboratorio.nombre, "Laboratorio TEST") 
        self.assertEqual(self.laboratorio.ciudad, "Ciudad TEST") 
        self.assertEqual(self.laboratorio.pais, "Pais TEST")

    def test_url_exists_at_correct_location(self): 
        response = self.client.get("/crud/mostrar/") 
        self.assertEqual(response.status_code, 200)

    def test_homepage(self): 
        response = self.client.get(reverse("mostrar_lab")) 
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, "mostrar.html") 
        self.assertContains(response, "<h2 style='text-align: center'>Información de Laboratorios</h2>")