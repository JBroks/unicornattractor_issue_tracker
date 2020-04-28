from django import forms
from django.contrib.auth.models import User
from .models import Ticket, Donation, Upvote
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
        
class PaymentForm(forms.Form):
    '''
    Donation form that enables user to select the amount to donate in order to 
    prioritise the feature of their choice
    '''
    
    AMOUNT_CHOICES = [(i,i) for i in range (5,150,10)]
    MONTH_CHOICES = [(i,i) for i in range (1,12)]
    YEAR_CHOICES = [(i,i) for i in range (2020, 2040)]
    
    donation_amount = forms.ChoiceField(
        label="Amount",
        choices=AMOUNT_CHOICES,
        required=False
        )

    credit_card_number = forms.CharField(
        label="Credit card number",
        required=False)
        
    cvv = forms.CharField(
        label="Security code (CVV)",
        required=False)
        
    expiry_month = forms.ChoiceField(
        label="Month",
        choices=MONTH_CHOICES,
        required=False)
        
    expiry_year = forms.ChoiceField(
        label="Year",
        choices=YEAR_CHOICES,
        required=False)
        
    stripe_id = forms.CharField(
        widget=forms.HiddenInput)
        
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ('ticket', 'user', 'donation_amount')