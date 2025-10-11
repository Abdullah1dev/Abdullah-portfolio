from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    
    def test_register_page_loads(self):
        response=self.client.get(reverse('register'))
        self.assertEqual(response.status_code,200)
        
        
    def test_login_page_loads(self):
        response=self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)
        
        
  
        