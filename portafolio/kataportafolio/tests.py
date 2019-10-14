import self as self
from django.test import TestCase


class PortafolioTestCase(TestCase):

    def test_lista_portafolio_estado(self):
        url = 'http://127.0.0.1:8000/kataportafolio/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
