from django import forms
from django.contrib.auth.models import User
from .models import Ticket
from django.core.exceptions import ValidationError
from itertools import chain

class AddTicketForm(forms.ModelForm):
    '''
    Ticket form that enables user to select ticket type, and type in ticket
    subject and description
    '''
   
    TYPES = list(chain(["--- Please select type ---"],
                        Ticket.objects.order_by().values_list('ticket_type',
                        flat=True).distinct()
                        ))

    TYPE_CHOICES = [(i,i) for i in TYPES ]
    
    ticket_type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        label='Ticket type',
        required=True)
        
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