from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tickets.models import Ticket, Upvote, Donation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tickets.forms import AddTicketForm, PaymentForm, DonationForm
from django.db.models import Count
from django.conf import settings
import stripe

# Create your views here.

# Import the Stripe secret API key
stripe.api_key = settings.STRIPE_SECRET

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
            return redirect('all_tickets')
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
    
    # Allows to retrive both forms inside the modal
    donation_form = DonationForm()
    payment_form = PaymentForm()
    
    # Check if user upvoted ticket
    try:
        has_voted = Upvote.objects.get(user=request.user, ticket=ticket)
    except Upvote.DoesNotExist:
        has_voted = None
    
    args = {
        'ticket': ticket, 
        'donation_form': donation_form, 
        'payment_form': payment_form,
        'has_voted': has_voted
    }
    
    return render(request, 'view_ticket.html', args)

@login_required
def delete_ticket(request, pk):
    
    ticket = get_object_or_404(Ticket, pk=pk)

    author= ticket.user
    if request.user.is_authenticated and request.user == author:
            ticket.delete()
            messages.success(request, "Ticket successfully deleted!")
            return redirect(reverse('all_tickets'))
          
@login_required
def upvote(request, pk):
    
    ticket = get_object_or_404(Ticket, pk=pk)
    
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        donation_form = DonationForm(request.POST)
        
        if payment_form.is_valid() and donation_form.is_valid():
            
            # Amount donated
            donation_amount = int(request.POST.get("donation_amount"))
            
            try:
                # Charge customer using Stripe API
                customer = stripe.Charge.create(
                    amount=int(donation_amount * 100),
                    currency="EUR",
                    description=request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                # If card is declined display the error message
                messages.error(request, "Your card was declined!")
            
            # Payment was successful
            if customer.paid:
                donation_form.instance.user = request.user
                donation_form.instance.donation_amount = donation_amount
                donation_form.instance.ticket = ticket
                donation_form.save()
                
                # Create an upvote for the feature
                Upvote.objects.create(ticket_id=ticket.pk,
                                      user_id=request.user.id)
                
                messages.error(request, "Your have successfully donated!")
                
            # If payment didn't go through
            else:
                messages.error(request, "Unable to process the payment.")
        else:
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = PaymentForm()
        donation_form = DonationForm()
    
    args = {
        'ticket': ticket,
        'donation_form': donation_form,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE
    }
    
    return render(request, 'view_ticket.html', args)
          