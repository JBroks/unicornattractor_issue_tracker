from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe


class UserLoginForm(forms.Form):
    '''
    Form to be used to log users in.
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    '''
    Form used to register a new user.
    '''
    first_name = forms.CharField(
        label="First name",
        min_length=2,
        max_length=50,
        widget=forms.TextInput,
        required=True)
    last_name = forms.CharField(
        label="Last name",
        min_length=2,
        max_length=50,
        widget=forms.TextInput,
        required=True)
    email = forms.CharField(
        label="Email",
        min_length=2,
        max_length=50,
        widget=forms.EmailInput,
        required=True)
    username = forms.CharField(
        label="Username",
        min_length=5,
        max_length=25,
        widget=forms.TextInput,
        required=True)
    password1 = forms.CharField(
        label="Password",
        min_length=5,
        max_length=50,
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        min_length=5,
        max_length=50,
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'username',
                  'password1',
                  'password2']
        
    def clean_email(self):
        '''
        Check if email is already registered.
        '''
        email = self.cleaned_data.get('email')
        if User.objects.exclude(pk=self.instance.pk).filter(
                                email=email).exists():
            raise forms.ValidationError(u'Email "%s" is already in use.'
                                        % email)
        return email
        
    def clean_username(self):
        '''
        Check if username is already registered.
        '''
        username = self.cleaned_data.get('username')
        if User.objects.exclude(pk=self.instance.pk).filter(
                                username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.'
                                        % username)
        return username

    def clean_password2(self):
        '''
        Check that the two password entries match.
        '''
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

     
class UserChangeForm(forms.ModelForm):
    '''
    Form used to update user profile details.
    '''
    first_name = forms.CharField(
        label="First name",
        min_length=2,
        max_length=50,
        widget=forms.TextInput,
        required=True)
    last_name = forms.CharField(
        label="Last name",
        min_length=2,
        max_length=50,
        widget=forms.TextInput,
        required=True)
    email = forms.CharField(
        label="Email",
        min_length=2,
        max_length=50,
        widget=forms.EmailInput,
        required=True)
    username = forms.CharField(
        label="Username",
        min_length=5,
        max_length=25,
        widget=forms.TextInput,
        required=True)
        
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'username']


class UserDeleteForm(forms.ModelForm):
    '''
    Delete user form.
    '''
    class Meta:
        model = User
        fields = []


class UploadFileForm(forms.ModelForm):
    '''
    Form used to upload a user profile photo.
    '''
    image = forms.ImageField(label="Profile image",
                             widget=forms.FileInput(),
                             required=False)
    
    class Meta:
        model = UserProfile
        fields = ['image', ]
