from django import forms
from django.contrib.auth.models import User
from .models import Post, CommentPost
from django.core.exceptions import ValidationError
from itertools import chain

class AddPostForm(forms.ModelForm):
    '''
    Post form that enables user to type in the post subject and description
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
        model = Post
        fields = ["subject", "description"]
        
class AddCommentPostForm(forms.ModelForm):

    comment = forms.CharField(
        label="Leave a comment",
        min_length=20,
        max_length=8000,
        widget=forms.Textarea(attrs={'rows':3, 'cols':10, 'placeholder': 'Add a comment...'}),
        required=True)
    
    class Meta:
        model = CommentPost
        fields = ('comment',)
