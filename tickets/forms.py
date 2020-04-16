from django import forms
from django.contrib.auth.models import User
from .models import Ticket
from django.core.exceptions import ValidationError

class AddTicketForm(forms.ModelForm):
    '''
    Ticket form that enables user to select ticket type, and type in ticket
    subject and description
    '''
    TYPE_CHOICES = [(i,i) for i in ["Feature", "Bug"] ]
    
    ticket_type = forms.ChoiceField(
        label='Ticket type',
        choices=TYPE_CHOICES, 
        required=False)
        
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
        model = Ticket
        fields = ["ticket_type", "subject", "description"]