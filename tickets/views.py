from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tickets.forms import AddTicketForm

# Create your views here.

@login_required
def add_ticket(request):
    if request.method == "POST":
        add_ticket_form = AddTicketForm(request.POST)

        if add_ticket_form.is_valid():
            add_ticket_form.save()
            messages.success(request, "You have successfully submitted your \
                                ticket!")
            return redirect(all_tickets)
        else:
                messages.error(request, "Something went wrong. Please try again.")
            
    else:
        add_ticket_form = AddTicketForm()
    
    return render(request, 'add_ticket.html', {'add_ticket_form': add_ticket_form} )
   
def all_tickets(request):
    return render(request, 'all_tickets.html')
    
def edit_ticket(request):
    return render(request, 'edit_ticket.html')

def view_ticket(request):
    return render(request, 'view_ticket.html')
'''
def delete_ticket(request):
'''