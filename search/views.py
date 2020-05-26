from django.shortcuts import render
from tickets.models import Ticket, Comment
from forum.models import Thread, Post
from django.db.models import Q

# Create your views here.
def search_results(request):
    
    # Query parameters
    search_term = request.GET.get('search-term')
    
    if request.method == "GET" and search_term != '':
            ticket_query = Q(subject__icontains=search_term
                            ) | Q(description__icontains=search_term )
            search_results_ticket = Ticket.objects.all().filter(ticket_query)
            search_results_comment = Comment.objects.all().filter(
                                        comment__icontains=search_term)
            thread_query = Q(subject__icontains=search_term
                            ) | Q(description__icontains=search_term )
            search_results_thread = Thread.objects.all().filter(thread_query)
            search_results_post = Post.objects.all().filter(
                                        post__icontains=search_term)
    else:
        pass
    
    context = {
        "search_results_ticket": search_results_ticket,
        "search_results_comment": search_results_comment,
        "search_results_thread": search_results_thread,
        "search_results_post": search_results_post
    }
    return render(request, 'search.html', context)
            
