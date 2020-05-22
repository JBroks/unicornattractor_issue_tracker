from django import forms
from django.contrib.auth.models import User
from .models import Thread, Post, ThreadVote
from django.core.exceptions import ValidationError
from itertools import chain

class AddThreadForm(forms.ModelForm):
    '''
    Thread form that enables user to type in the subject and description
    '''

    subject = forms.CharField(
        label="Subject",
        min_length=5,
        max_length=100,
        widget=forms.TextInput(),
        required=True)
        
    description = forms.CharField(
        label="Description",
        min_length=20,
        max_length=3000,
        widget=forms.Textarea(),
        required=True)
    
    class Meta:
        model = Thread
        fields = ["subject", "description"]
        
class AddPostForm(forms.ModelForm):

    post = forms.CharField(
        label="Submit your forum post",
        min_length=20,
        max_length=8000,
        widget=forms.Textarea(attrs={'rows':3, 'cols':10, 'placeholder': 'Add a comment...'}),
        required=True)
    
    class Meta:
        model = Post
        fields = ('post',)
