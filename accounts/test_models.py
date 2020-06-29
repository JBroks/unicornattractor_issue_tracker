from django.test import TestCase
from .models import UserProfile
from django.contrib.auth.models import User


# Create your tests here.


class TestUserProfile(TestCase):
        
        def test_profile_creation(self):
            '''
            Test string displayed when for the user profile created.
            '''
            # Create a new user to test the profile string.
            new_user = User.objects.create_user({
                                'username': 'joanna',
                                'email': 'joanna@example.com',
                                'password': 'secret'
                                })
            # Retrive the user profile for the given user.
            profile = UserProfile.objects.get(id=1)
            displayed_object_name = f"{new_user.username}'s profile"
            self.assertEquals(displayed_object_name, str(profile))
