from django.shortcuts import render
from tickets.models import Ticket, Comment
from forum.models import Thread, Post
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

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
    
def search_results(request):
    
    # Query parameters
    search_term = request.GET.get('search')
    ticket_query = Q(subject__icontains=search_term
                            ) | Q(description__icontains=search_term )
    thread_query = Q(subject__icontains=search_term
                            ) | Q(description__icontains=search_term )
        
    if search_term and search_term != "":
        
        # Retrive results
        search_results_ticket = Ticket.objects.all().filter(ticket_query)
        search_results_comment = Comment.objects.all(
                                ).filter(comment__icontains=search_term
                                ).distinct()
        search_results_thread = Thread.objects.all().filter(thread_query)
        search_results_post = Post.objects.all(
                                ).filter(post__icontains=search_term
                                ).distinct()
        # Count results
        ticket_count = search_results_ticket.count()
        comment_count = search_results_comment.count()
        thread_count = search_results_thread.count()
        post_count = search_results_post.count()
        
        # Paginate results
        search_results_ticket = paginate(request, search_results_ticket)
        search_results_comment = paginate(request, search_results_comment)
        search_results_thread = paginate(request, search_results_thread)
        search_results_post = paginate(request, search_results_post)

    else:
        search_results_ticket = None
        search_results_comment = None
        search_results_thread = None
        search_results_post = None
        ticket_count = 0
        comment_count = 0
        thread_count = 0
        post_count = 0
    
    context = {
        "search_results_ticket": search_results_ticket,
        "search_results_comment": search_results_comment,
        "search_results_thread": search_results_thread,
        "search_results_post": search_results_post,
        "ticket_count": ticket_count,
        "comment_count": comment_count,
        "thread_count": thread_count,
        "post_count": post_count,
        "search_term": search_term
        }
    
    return render(request, 'search.html', context)   
        
    
            
