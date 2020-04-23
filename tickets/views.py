from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tickets.models import Ticket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tickets.forms import AddTicketForm
from django.db.models import Count

# Create your views here.

@login_required
def add_or_edit_ticket(request, pk=None):
    '''
    Allows user to add a new ticket or edit an existing one
    If user wants to add a new ticket he or she is redirected to a blank
    add_ticket_form where all details can be supplied and submitted
    If user wants to edit the ticket they are redirected to the ticket form
    that is pre-filled with ticket details
    '''
    
    # Retrive the ticket if exists
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    
    if request.method == "POST":
        add_ticket_form = AddTicketForm(request.POST, request.FILES, instance=ticket)

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
        add_ticket_form = AddTicketForm(instance=ticket)
    
    return render(request, 'add_ticket.html', {'add_ticket_form': add_ticket_form} )
  
def all_tickets(request):
    '''
    View all tickets in a form of paginated table.
    Enable user to filter tickets by type and / or status
    Table is paginated to show only 10 records per page
    '''
    
    # Create type and status list for select option menu
    types_list = Ticket.objects.order_by().values_list('ticket_type',
                    flat=True).distinct()
    status_list = Ticket.objects.order_by().values_list('ticket_status',
                    flat=True).distinct()
    
    qs = Ticket.objects.all()
    
    # Queries
    type_filter_query = request.GET.get('ticket-type')
    status_filter_query = request.GET.get('ticket-status')
    
    # Filter queryset
    if type_filter_query and type_filter_query != "Select...":
        if status_filter_query and status_filter_query != "Select...":
           qs = qs.filter(ticket_type__iexact = type_filter_query, ticket_status__iexact = status_filter_query).order_by('ticket_type')
        else:
            qs = qs.filter(ticket_type__iexact = type_filter_query)
    elif status_filter_query and status_filter_query != "Select...":
        qs = qs.filter(ticket_status__iexact = status_filter_query)
    else:
        qs
        
    page = request.GET.get('page', 1)
    
    # Paginate tickets
    paginator = Paginator(qs, 10)
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)
        
    args = {'tickets': tickets, 
            'types_list': types_list, 
            'status_list': status_list }
        
    return render(request, 'all_tickets.html', args )

def view_ticket(request, pk):
    '''
    Enables user to view page containing all details regarding a selected ticket
    Function retrieves a single ticket based on its ID (pk) and renders it to 
    the view_ticket.html template
    If object is not found 404 error is being returned
    '''
    
    # Retrive the ticket
    ticket = get_object_or_404(Ticket, pk=pk)
    
    return render(request, 'view_ticket.html', {'ticket': ticket})
    

def delete_ticket(request, pk):
    
    ticket = get_object_or_404(Ticket, pk=pk)

    author= ticket.user
    if request.user.is_authenticated and request.user == author:
            ticket.delete()
            messages.success(request, "Ticket successfully deleted!")
            return redirect(reverse('all_tickets'))