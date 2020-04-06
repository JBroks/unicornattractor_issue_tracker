from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tickets.models import Ticket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tickets.forms import AddTicketForm


# Create your views here.

@login_required
def add_ticket(request):
    if request.method == "POST":
        add_ticket_form = AddTicketForm(request.POST)

        if add_ticket_form.is_valid():
            add_ticket_form.instance.user = request.user
            add_ticket_form.instance.ticket_status = "Open"
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
    '''
    View all tickets in a form of paginated table.
    Enable user to filter tickets by type, status and / or user who added it
    '''
    
    tickets_list = Ticket.objects.all()
    page = request.GET.get('page', 1)
    
    # Paginate tickets
    paginator = Paginator(tickets_list, 1)
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)
        
    return render(request, 'all_tickets.html', {'tickets': tickets} )
    
def edit_ticket(request):
    return render(request, 'edit_ticket.html')

def view_ticket(request):
    return render(request, 'view_ticket.html')
'''
def delete_ticket(request):
'''