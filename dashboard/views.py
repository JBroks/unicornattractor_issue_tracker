from tickets.models import Ticket, Upvote
from django.shortcuts import render
from django.db.models import Count, Sum, Q

# Create your views here.


def dashboard(request):
    '''
     View gets data needed for the dashboard presenting general statistics.
     Statistics are displayed on dashboard.html
    '''
    # Variables for all tickets, bugs and features
    all_tickets = Ticket.objects.all()
    all_bugs = Ticket.objects.filter(ticket_type="Bug")
    all_features = Ticket.objects.filter(ticket_type="Feature")
    
    # Count all tickets and tickets by ticket_type
    total_tickets = all_tickets.count()
    total_bugs = all_bugs.count()
    total_features = all_features.count()
    
    # Total count of each ticket type grouped by ticket_status
    # Bugs
    total_open_bugs = all_bugs.filter(ticket_status="Open").count()
    total_in_progress_bugs = all_bugs.filter(
        ticket_status="In Progress").count()
    total_completed_bugs = all_bugs.filter(ticket_status="Completed").count()
    total_closed_bugs = all_bugs.filter(ticket_status="Closed").count()
    # Features
    total_open_features = all_features.filter(ticket_status="Open").count()
    total_in_progress_features = all_features.filter(
        ticket_status="In Progress").count()
    total_completed_features = all_features.filter(
        ticket_status="Completed").count()
    total_closed_features = all_features.filter(ticket_status="Closed").count()
    
    # Top 5 most upvoted tickets / bugs / features
    top_five_upvoted_tickets = all_tickets.annotate(
        num_likes=Count('upvote_ticket_key')).order_by('-num_likes')[:5]
    top_five_upvoted_bugs = all_bugs.annotate(
        num_likes=Count('upvote_ticket_key')).order_by('-num_likes')[:5]
    top_five_upvoted_features = all_features.annotate(
        num_likes=Count('upvote_ticket_key')).order_by('-num_likes')[:5]
    
    # Top 10 most donated features - only open features
    top_ten_donated_features = all_features.filter(
        Q(ticket_status__iexact="Open") | Q(
            ticket_status__iexact="In Progress")).annotate(
                sum_donation=Sum('donate_ticket_key')).order_by(
                    '-sum_donation')[:10]

    context = {
        'total_tickets': total_tickets,
        'total_bugs': total_bugs,
        'total_features': total_features,
        'total_open_bugs': total_open_bugs,
        'total_in_progress_bugs': total_in_progress_bugs,
        'total_completed_bugs': total_completed_bugs,
        'total_closed_bugs': total_closed_bugs,
        'total_open_features': total_open_features,
        'total_in_progress_features': total_in_progress_features,
        'total_completed_features': total_completed_features,
        'total_closed_features': total_closed_features,
        'top_five_upvoted_tickets': top_five_upvoted_tickets,
        'top_five_upvoted_bugs': top_five_upvoted_bugs,
        'top_five_upvoted_features': top_five_upvoted_features,
        'top_ten_donated_features': top_ten_donated_features,
    }
    
    return render(request, 'dashboard.html', context)
