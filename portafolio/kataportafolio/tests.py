import json
import time

import self as self
from django.contrib.auth.models import User
from django.test import TestCase

from kataportafolio.models import Portafolio


class PortafolioTestCase(TestCase):

    def test_lista_portafolio_estado(self):
        url = 'http://127.0.0.1:8000/kataportafolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_lista_portafolio_estado(self):
        url = 'http://127.0.0.1:8000/kataportafolio/'
        user_model = User.objects.create_user(username='test', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        Portafolio.objects.create(nombre='portafolioUno', publico=True, user=user_model,
                                  link_imagen="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEhUSEx",
                                  descripcion="foto de una serpiente", tipo_archivo='jpeg')
        Portafolio.objects.create(nombre='portafolioDos', publico=False, user=user_model,
                                  link_imagen="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEhUSExMVFRUXGBUVFxUXGBcXFxUXGBUXFxUWGBcYHSggGBolHR",
                                  descripcion="foto de otra una serpiente", tipo_archivo='jpeg')
        response = self.client.get(url, format='json')
        current_data = json.loads(response.content)
        self.assertEqual(len(current_data), 2)

    def test_add_user(self):
        response = self.client.post('http://127.0.0.1:8000/kataportafolio/addUser/', json.dumps(
            {"username": "usertdd", "first_name": "Test TDD", "last_name": "User TDD", "password": "usertdd123",
             "email": "testdd@test.com"}), content_type='application/json')
        current_data = json.loads(response.content)
        self.assertEqual(current_data[0]['fields']['username'], 'usertdd')

    def test_portafolio_publico_persona(self):
        user_model = User.objects.create_user(username='test123', password='kd8wke-DE34', first_name='test',
                                              last_name='test', email='test@test.com')
        Portafolio.objects.create(nombre='portafolioUno', publico=True, user=user_model,
                                  link_imagen="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEhUSEx",
                                  descripcion="foto de una serpiente", tipo_archivo='jpeg')
        Portafolio.objects.create(nombre='portafolioDos', publico=False, user=user_model,
                                  link_imagen="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEhUSExMVFRUXGBUVFxUXGBcXFxUXGBUXFxUWGBcYHSggGBolHR",
                                  descripcion="foto de otra una serpiente", tipo_archivo='jpeg')
        url = 'http://127.0.0.1:8000/kataportafolio/?id_persona=' + str(user_model.id)
        response = self.client.get(url, format='json')
        current_data = json.loads(response.content)
        print(current_data)
        self.assertEqual(len(current_data), 1)

    def test_login(self):
        url = 'http://127.0.0.1:8000/kataportafolio/login/'
        response = self.client.post(url, json.dumps(
            {"username": "usertdd", "password": "abcd123."}), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_editar_datos_persona(self):
       user_model = User.objects.create_user(username='test123', password='kd8wke-DE34', first_name='test',
                                             last_name='test', email='test@test.com')
       url = 'http://127.0.0.1:8000/kataportafolio/addUser/?id=1'
       response = self.client.post(url, json.dumps(
           {"first_name": "Test TDD", "last_name": "User TDD", "password": "newpass"}),
                                   content_type='application/json')
       current_data = json.loads(response.content)
       self.assertEqual(current_data[0]['fields']['first_name'], 'Test TDD')
       self.assertEqual(current_data[0]['fields']['last_name'], 'User TDD')
       self.assertEqual(current_data[0]['fields']['password'], 'newpass')
