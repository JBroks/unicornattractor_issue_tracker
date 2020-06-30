from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tickets.models import Ticket, Upvote, Donation, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tickets.forms import AddTicketForm, PaymentForm, DonationForm, AddCommentForm
from django.db.models import Count, Sum
from django.conf import settings
import stripe
from itertools import chain

# Create your views here.

# Import the Stripe secret API key
stripe.api_key = settings.STRIPE_SECRET


def paginate(request, list):
    '''
    Helper function that will paginate any qiven queryset
    '''
    page = request.GET.get('page', 1)
    
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list

def record_exist_check(Model, user, ticket):
    '''
    Helper function that will check if record for a given user and ticket 
    already exist in a given model
    '''
    if user.is_authenticated:
        try:
            param = Model.objects.get(user=user, ticket=ticket)
        except Model.DoesNotExist:
            param = None
        return param
    else:
        param = None

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
        add_ticket_form = AddTicketForm(request.POST, request.FILES,
                                        instance=ticket)
        if add_ticket_form.is_valid():
            # Create ticket object without saving it to the database yet
            new_ticket = add_ticket_form.save(commit=False)
            # Assign the current user and ticket_status to the ticket
            add_ticket_form.instance.user = request.user
            add_ticket_form.instance.ticket_status = "Open"
            # Save the ticket to the database
            new_ticket.save()
            messages.success(request, "You have successfully submitted your \
                                ticket!")
            return redirect('all_tickets')
        else:
                messages.error(request, "Something went wrong. \
                                Please try again.")
    else:
        add_ticket_form = AddTicketForm(instance=ticket)
    context = {
        'add_ticket_form': add_ticket_form
    }
    return render(request, 'add_ticket.html', context)
  
def all_tickets(request):
    '''
    View all tickets in a form of paginated table.
    Enable user to filter tickets by type and / or status
    Table is paginated to show only 10 records per page
    '''
    
    # Create type and status list for select option menu
    types_list = list(chain(["Feature"], ["Bug"]))
    status_list = list(chain(["Open"], ["In Progress"], ["Completed"], ["Closed"]))
    
    # Set queryset to all tickets
    qs = Ticket.objects.all()
    
    # Query parameters
    type_filter_query = request.GET.get('ticket-type')
    status_filter_query = request.GET.get('ticket-status')
    
    # Filter queryset
    if type_filter_query and type_filter_query != "Select...":
        if status_filter_query and status_filter_query != "Select...":
           qs = qs.filter(ticket_type__iexact = type_filter_query,
           ticket_status__iexact = status_filter_query).order_by('ticket_type')
        else:
            qs = qs.filter(ticket_type__iexact = type_filter_query)
    elif status_filter_query and status_filter_query != "Select...":
        qs = qs.filter(ticket_status__iexact = status_filter_query)
    else:
        qs
    
    # Paginate tickets
    tickets = paginate(request, qs)
    
    context = {'tickets': tickets, 
            'types_list': types_list, 
            'status_list': status_list }
    return render(request, 'all_tickets.html', context)

def view_ticket(request, pk):
    '''
    Enables user to view page containing all details regarding a selected ticket
    Function retrieves a single ticket based on its ID (pk) and renders it to 
    the view_ticket.html template
    If object is not found 404 error is being returned
    '''
    
    # Retrive the ticket
    ticket = get_object_or_404(Ticket, pk=pk)
        
    # Allows to retrive forms on the view ticket page
    donation_form = DonationForm()
    payment_form = PaymentForm()
    comment_form = AddCommentForm()
    
    # Check if user upvoted ticket
    has_voted = record_exist_check(Upvote, request.user, ticket)
    
    # Check if user donated money for the feature
    has_donated = record_exist_check(Donation, request.user, ticket)
    
    # Count all upvotes / commments for a ticket
    upvote_count = Upvote.objects.filter(ticket=ticket).count()
    comment_count = Comment.objects.filter(ticket=ticket).count()
    
    # Count users involved in discussion around a given ticket
    user_commented_count = len(Comment.objects.filter(ticket=ticket
                            ).order_by().values_list('user', flat=True
                            ).distinct())
    
    # Get a sum of donations for a given ticket
    total_donations = Donation.objects.filter(ticket=ticket
                    ).aggregate(Sum('donation_amount'))['donation_amount__sum']
                    
    # Set donations to zero if no donations has been made
    if total_donations is None:
        total_donations = 0
    else:
        total_donations
    
    # Retrive all comments for a given ticket
    try:
        comments = Comment.objects.filter(ticket_id=ticket.pk)
    except Comment.DoesNotExist:
        comments = None
        
    # Paginate comments
    comments = paginate(request, comments)
    
    # Retrive last comment
    try:
        last_comment = Comment.objects.filter(ticket=ticket).latest('date_created')
    except Comment.DoesNotExist:
        last_comment = None
    
    context = {
        'ticket': ticket, 
        'donation_form': donation_form, 
        'payment_form': payment_form,
        'has_voted': has_voted,
        'has_donated': has_donated,
        'upvote_count': upvote_count,
        'total_donations': total_donations,
        'comments': comments,
        'comment_form': comment_form,
        'comment_count': comment_count,
        'user_commented_count': user_commented_count,
        'last_comment': last_comment
    }
    return render(request, 'view_ticket.html', context)

@login_required
def delete_ticket(request, pk):
    '''
    Allows user to delete their ticket
    '''
    
    # Retrive the ticket if exists
    ticket = get_object_or_404(Ticket, pk=pk)
    author= ticket.user
    
    if request.user.is_authenticated and request.user == author:
            ticket.delete()
            messages.success(request, "Ticket successfully deleted!")
            return redirect(reverse('all_tickets'))
    else:
        messages.error(request, "Error! You don't have a permission to \
                        delete this ticket.")
        return redirect('view_ticket', ticket.pk)

@login_required
def upvote(request, pk):
    '''
    Allows user to upvote the ticket and donate (for features only)
    If user upvoted already they won't be allowed to vote again
    Also if user upvoted and donated for the feature they won't be allowed to 
    downvote and upvote ticket again for the saem ticket, so function will check
    it by using has_voted and has_donated
    Stripe API used to charge a user's credit card
    '''
    
    # Retrive the comment and ticket if exists
    ticket = get_object_or_404(Ticket, pk=pk)
    
    # Check if user upvoted ticket
    has_voted = record_exist_check(Upvote, request.user, ticket)
    
    # Check if user donated money for the feature
    has_donated = record_exist_check(Donation, request.user, ticket)
    
    # Define comment form to avoid the error (so html can render it)
    comment_form = AddCommentForm()
    
    if has_voted is None and (ticket.ticket_type == "Bug" 
                                or has_donated is not None):
       Upvote.objects.create(ticket_id=ticket.pk, user_id=request.user.id) 
       messages.success(request, "Your have successfully upvoted the ticket!")
       return redirect('view_ticket', pk)
    
    if has_voted is None and has_donated is None and request.method == "POST":
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
                messages.success(request, "Your have successfully donated!")
                return redirect('view_ticket', pk)
            # If payment didn't go through
            else:
                messages.error(request, "Unable to process the payment.")
        # Forms not valid
        else:
            messages.error(request, "We were unable to take a payment \
                            with that card!")
    else:
        payment_form = PaymentForm()
        donation_form = DonationForm()
    
    context = {
        'ticket': ticket,
        'donation_form': donation_form,
        'payment_form': payment_form,
        'comment_form': comment_form,
        'publishable': settings.STRIPE_PUBLISHABLE
    }
    return render(request, 'view_ticket.html', context)

@login_required
def downvote(request, pk):
    '''
    View allows the user to downvote the ticket
    Downvote action will simply remove the user's upvote
    '''
    
    # Retrive the comment and ticket if exists
    ticket = get_object_or_404(Ticket, pk=pk)
    
    # Check if user upvoted ticket
    has_voted = record_exist_check(Upvote, request.user, ticket)
        
    if request.user.is_authenticated and has_voted is not None:
        upvote = Upvote.objects.get(ticket_id=ticket.pk,
                                        user_id=request.user.id)
        upvote.delete()
        messages.success(request, "Your upvote has been removed!")
        return redirect('view_ticket', pk)

@login_required
def add_or_edit_comment(request, ticket_pk, comment_pk=None):
    '''
    View allows the user to add a new comment
    or edit the  existing one
    '''
    
    # Retrive the comment and ticket if exists
    ticket = get_object_or_404(Ticket, pk=ticket_pk)
    comment = get_object_or_404(Comment, pk=comment_pk) if comment_pk else None
    
    if request.method == "POST":
        comment_form = AddCommentForm(request.POST, request.FILES,
                                        instance=comment)
        if comment_form.is_valid():
            # Create comment object without saving it to the database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current user and ticket to the comment
            comment_form.instance.user = request.user
            comment_form.instance.ticket = ticket
            # Save the comment to the database
            new_comment.save()
            messages.success(request, "Thanks for sharing your thoughts!")
            return redirect('view_ticket', ticket.pk)
        else:
            messages.error(request, "Something went wrong. Please try again.")
    else:
        comment_form = AddCommentForm(instance=comment)
    context = {
        'comment_form': comment_form
    }
    return render(request, 'view_ticket.html', context)

@login_required
def delete_comment(request, ticket_pk, comment_pk):
    
    # Retrive the comment and ticket if exists
    ticket = get_object_or_404(Ticket, pk=ticket_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    author= comment.user
    
    if request.user.is_authenticated and request.user == author:
            comment.delete()
            messages.success(request, "Comment successfully deleted!")
            return redirect('view_ticket', ticket.pk)
    else:
        messages.error(request, "Error! You don't have a permission to \
                        delete this comment.")
        return redirect('view_ticket', ticket.pk)