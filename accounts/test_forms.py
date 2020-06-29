from django.test import TestCase
from django.core.exceptions import ValidationError
from django.shortcuts import reverse
from .forms import UserRegistrationForm
from django.contrib.auth.models import User


class TestUserRegistrationForm(TestCase):
    
    def test_user_can_register(self):
        '''
        Tests that the user registertration is completed by entering
        the required details.
        '''
        form = UserRegistrationForm({
            "username": "User123",
            "email": "test@test.com",
            "first_name": "John",
            "last_name": "Smith",
            "password1": "Password",
            "password2": "Password"
        })
        self.assertTrue(form.is_valid())
        
    def test_passwords_must_match_error(self):
        '''
        Tests if the correct error is displayed when passwords do not match.
        '''
        form = UserRegistrationForm({
            "password1": "Password1",
            "password2": "Password2"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["password2"],
                         [form.error_messages['password_mismatch']])
                  
    def test_registration_form_unique_email(self):
        '''
        Testing if error raised when trying to registered with an email
        that already exists in the database.
        '''
        # Create a user to verify that duplicate addresses can't be created.
        User.objects.create_user('joanna', 'joanna@example.com', 'secret')
        form = UserRegistrationForm({'username': 'foo',
                                     'email': 'joanna@example.com',
                                     'password1': 'foo',
                                     'password2': 'foo'})
        self.failIf(form.is_valid())
        self.assertEqual(form.errors['email'],
                         [u'Email "joanna@example.com" is already in use.'])
        
    def test_registration_form_unique_username(self):
        '''
        Testing if error raised when trying to registered with an username
        that already exists in the database.
        '''
        # Create a user to verify that duplicate usernames can't be created.
        User.objects.create_user('joanna', 'joanna@example.com', 'secret')
        form = UserRegistrationForm({'username': 'joanna',
                                     'email': 'foo@example.com',
                                     'password1': 'foo',
                                     'password2': 'foo'})
        self.failIf(form.is_valid())
        self.assertEqual(form.errors['username'],
                         [u'Username "joanna" is already in use.'])
