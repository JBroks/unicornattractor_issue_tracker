from django.test import TestCase
from django.shortcuts import reverse, render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.test.client import Client
from .forms import UserRegistrationForm, UserLoginForm, UserChangeForm, UploadFileForm, UserDeleteForm
from accounts import forms


class TestRegistrationViews(TestCase):
    
    def setUp(self):
        '''
        Set up a client to be able to login users in order to test views
        using @login_required decorators
        '''
        self.client = Client()
        self.user = User.objects.create_user('joanna',
                                        'joanna@example.com',
                                        'secret')
    
    def test_registration_view_initial(self):
        '''
        Test registration view (get response) - if view redirects to the correct
        URL and a correct template is used
        '''
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page,'registration.html')
        self.failUnless(isinstance(page.context['form'],
                                   forms.UserRegistrationForm))
    
    def test_get_register_for_authenticated_user_page(self):
        '''
        Test if user already authenticated and tries to register
        they are redirected to homepage
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        page = self.client.get("/accounts/register/")
        self.assertRedirects(page, '/', status_code=302)
        
class TestLoginViews(TestCase):
    
    def setUp(self):
        '''
        Set up a client to be able to login users in order to test views
        using @login_required decorators
        '''
        self.client = Client()
        self.user = User.objects.create_user('joanna',
                                        'joanna@example.com',
                                        'secret')
                               
    def test_get_login_page(self):
        '''
        Test login view - if redirected to the correct URL and that
        a correct template is used
        '''
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
        self.failUnless(isinstance(page.context['form'],
                                   forms.UserLoginForm))
    
    def test_get_login_for_authenticated_user_page(self):
        '''
        Test if user already authenticated and tries to login
        they are redirected to homepage
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        page = self.client.get("/accounts/login/")
        self.assertRedirects(page, '/', status_code=302)
   
class TestProfileViews(TestCase):
    
    def setUp(self):
        '''
        Set up a client to be able to login users in order to test views
        using @login_required decorators
        '''
        self.client = Client()
        self.user = User.objects.create_user('joanna',
                                        'joanna@example.com',
                                        'secret')
    
    def test_get_user_profile_page(self):
        '''
        Test profile view - if redirected to the correct URL and that
        a correct template is used
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        page = self.client.get("/accounts/{0}/profile/".format(self.user.username))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")
    
    def test_get_user_profile_edit_page(self):
        '''
        Test edit profile view - if redirected to the correct URL and that
        a correct template is used
        '''
        # Login user
        self.client.login(username='joanna', password='secret')
        
        page = self.client.get("/accounts/{0}/profile-edit/".format(self.user.username))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_profile.html")

class TestLogoutViews(TestCase):
    
    def setUp(self):
        '''
        Set up a client to be able to login users in order to test views
        using @login_required decorators
        '''
        self.client = Client()
        self.user = User.objects.create_user('joanna',
                                        'joanna@example.com',
                                        'secret')
                                        
    def test_logout_view(self):
        '''
        Test logout view - if redirected to the correct URL and that
        a correct template is used
        '''
        self.client.login(username='joanna', password='secret')
        
        page = self.client.get("/accounts/logout/")
        self.assertEqual(page.status_code, 302)
        self.client.post(reverse('index'))