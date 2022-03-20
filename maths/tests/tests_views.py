from django.test import TestCase, Client
from maths.models import Math

class MathViewsTest(TestCase):
    
    def setUp(self):
        Math.objects.create(operation="sub", a=10, b=30)
        self.client = Client()
    
    def test_math_list(self):
        response = self.client.get("/maths/histories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 1)
        self.assertIn('<li><a href="/maths/histories/1">id:1, a=10, b=30, op=sub, result=None</a></li>', response.content.decode())