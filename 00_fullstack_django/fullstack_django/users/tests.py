from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class test_create_user(TestCase):
    def test_create_user(self):
        test_mail = "testuser@testuser.com"
        test_pass = "test123"
        
        User = get_user_model()
        user = User.objects.create(email=test_mail, password=test_pass)

        self.assertEqual(user.email, test_mail)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        # Ensure not using usernames
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")
    
    def test_create_superuser(self):
        test_mail = "super@testuser.com"
        test_pass = "testsuper123"

        User = get_user_model()
        admin_user = User.objects.create_superuser(email=test_mail, password=test_pass)
        self.assertEqual(admin_user.email, test_mail)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
     
        # Ensure not using usernames
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False)
