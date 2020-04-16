from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tickets.models import Ticket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tickets.forms import AddTicketForm
from django.db.models import Count

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
    Enable user to filter tickets by type and / or status
    '''
    
    # Create type and status list for select option menu
    types_list = Ticket.objects.order_by().values_list('ticket_type',
                    flat=True).distinct()
    status_list = Ticket.objects.order_by().values_list('ticket_status',
                    flat=True).distinct()
    
    qs = Ticket.objects.all()
    
    # Queries
    type_filter_query = request.GET.get('ticket_type')
    status_filter_query = request.GET.get('ticket_status')
    
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
       
def edit_ticket(request):
    return render(request, 'edit_ticket.html')

def view_ticket(request):
    return render(request, 'view_ticket.html')
'''
def delete_ticket(request):
'''