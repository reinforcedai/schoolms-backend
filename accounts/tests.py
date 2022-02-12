from django.test import TestCase

from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('test@example.com', 'testing', 'password123')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def test_user_login(self):
        self.client.login(username='test@example.com', password='password123')
        self.client.login(username='test@example.com', password='password12')
        self.client.login(username='test@example.com', password='password1')