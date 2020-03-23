from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def add_ticket(request):
    return render(request, 'add_ticket.html')
    
def all_tickets(request):
    return render(request, 'all_tickets.html')
    
def edit_ticket(request):
    return render(request, 'edit_ticket.html')

def view_ticket(request):
    return render(request, 'view_ticket.html')
'''
def delete_ticket(request):
'''