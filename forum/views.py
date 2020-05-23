from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Thread, Post, ThreadVote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AddThreadForm, AddPostForm
from django.db.models import Count, Sum, F, Func, Value

# Create your views here.
@login_required
def add_or_edit_thread(request, pk=None):
    '''
    Allows user to add a new forum thread or edit an existing one
    If user wants to add a new thread they are redirected to a blank
    add_thread_form where all details can be supplied and submitted
    If user wants to edit the thread they are redirected to the thread form
    that is pre-filled with the thread details
    '''
    
    # Retrive the thread if exists
    thread = get_object_or_404(Thread, pk=pk) if pk else None
    
    if request.method == "POST":
        add_thread_form = AddThreadForm(request.POST, request.FILES,
                                        instance=thread)
        if add_thread_form.is_valid():
            # Create thread object without saving it to the database yet
            new_thread = add_thread_form.save(commit=False)
            # Assign the current user to the thread
            add_thread_form.instance.user = request.user
            # Save the thread to the database
            new_thread.save()
            messages.success(request, "You have successfully created a new \
                                thread!")
            return redirect('forum')
        else:
            messages.error(request, "Something went wrong. \
                                Please try again.")
    else:
        add_thread_form = AddThreadForm(instance=thread)
    context = {
        'add_thread_form': add_thread_form
    }
    return render(request, 'add_thread.html', context)

def forum(request):
    '''
    View all threads in a form of paginated table.
    Table is paginated to show only 10 records per page
    '''
    
    # Retrive all threads
    threads = Thread.objects.all()
    
    page = request.GET.get('page', 1)
    
    # Paginate threads
    paginator = Paginator(threads, 10)
    try:
        threads = paginator.page(page)
    except PageNotAnInteger:
        threads = paginator.page(1)
    except EmptyPage:
        threads = paginator.page(paginator.num_pages)
    
    return render(request, 'forum.html', {'threads': threads})

def view_thread(request, pk):
    '''
    Enables user to view page containing all details regarding a selected
    thread, including all posts
    Function retrieves a single thread based on its ID (pk) and renders it to 
    the view_thread.html template
    If object is not found 404 error is being returned
    '''
    
    # Retrive the thread
    thread = get_object_or_404(Thread, pk=pk)
    
    # Check if user voted and extract existing vote
    has_voted = record_exist_check(ThreadVote, request.user, thread)
    
    if has_voted is None:
        existing_vote_type = None
    else:
        existing_vote_type = has_voted.vote_type
        
    # Allows to retrive forms on the view thread page
    post_form = AddPostForm()
    
    # Count all posts for a thread
    posts_count = Post.objects.filter(thread=thread).count()
    
    # Retrive all posts for a given thread
    try:
        posts = Post.objects.filter(thread_id=thread.pk)
    except Post.DoesNotExist:
        posts = None
        
    # Paginate posts
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        'thread': thread,
        'posts': posts,
        'post_form': post_form,
        'posts_count': posts_count,
        'existing_vote_type': existing_vote_type
    }
    return render(request, 'view_thread.html', context)

@login_required
def delete_thread(request, pk):
    '''
    Allows user to delete their thread
    '''
    
    # Retrive the thread if exists
    thread = get_object_or_404(Thread, pk=pk)
    author= thread.user
    
    if request.user.is_authenticated and request.user == author:
            thread.delete()
            messages.success(request, "Thread successfully deleted!")
            return redirect(reverse('forum'))
    else:
        messages.error(request, "Error! You don't have a permission to \
                        delete this thread.")
        return redirect('view_thread', thread.pk)

@login_required
def add_or_edit_post(request, thread_pk, post_pk=None):
    '''
    View allows the user to add a new post
    or edit the  existing one
    '''
    
    # Retrive the post and thread if exists
    thread = get_object_or_404(Thread, pk=thread_pk)
    post = get_object_or_404(Post, pk=post_pk) if post_pk else None
    
    if request.method == "POST":
        post_form = AddPostForm(request.POST, request.FILES,
                                        instance=post)
        if post_form.is_valid():
            # Create post object without saving it to the database yet
            new_post = post_form.save(commit=False)
            # Assign the current user and thread to the post
            post_form.instance.user = request.user
            post_form.instance.thread = thread
            # Save the post to the database
            new_post.save()
            messages.success(request, "Thanks for sharing your thoughts!")
            return redirect('view_thread', thread.pk)
        else:
            messages.error(request, "Something went wrong. Please try again.")
    else:
        post_form = AddPostForm(instance=post)
    context = {
        'post_form': post_form
    }
    return render(request, 'view_thread.html', context)

@login_required
def delete_post(request, thread_pk, post_pk):
    
    # Retrive the post and thread if exists
    thread = get_object_or_404(Thread, pk=thread_pk)
    post = get_object_or_404(Post, pk=post_pk)
    author = post.user
    
    if request.user.is_authenticated and request.user == author:
            post.delete()
            messages.success(request, "Post successfully deleted!")
            return redirect('view_thread', thread.pk)
    else:
        messages.error(request, "Error! You don't have a permission to \
                        delete this post.")
        return redirect('view_thread', thread.pk)

def record_exist_check(Model, user, thread):
    '''
    Helper function that will check if record for a given user and thread 
    already exist in a given model
    '''
    if user.is_authenticated:
        try:
            param = Model.objects.get(user=user, thread=thread)
        except Model.DoesNotExist:
            param = None
        return param
    else:
        param = None

def vote_thread(request, thread_pk, vote_type):
    '''
    Enables authenticated users to like or dislike posted thread
    '''
    
    # Retrive the thread and votes if exists
    thread = get_object_or_404(Thread, pk=thread_pk)
    
    # Check if user voted already
    has_voted = record_exist_check(ThreadVote, request.user, thread)
   
    if request.user.is_authenticated:
        if has_voted is not None:
            existing_vote_type = has_voted.vote_type
            
            if existing_vote_type == vote_type:
                ThreadVote.objects.filter(thread_id=thread.pk, user_id=request.user.id, vote_type=vote_type).delete()
            else: 
                if has_voted.vote_type == "like":
                    ThreadVote.objects.filter(thread_id=thread.pk, user_id=request.user.id, vote_type="like").update(
                    vote_type=Func(F('vote_type'),Value('like'), Value('dislike'), function='replace',))
                elif has_voted.vote_type == "dislike":
                    ThreadVote.objects.filter(thread_id=thread.pk, user_id=request.user.id, vote_type="dislike").update(
                    vote_type=Func(F('vote_type'),Value('dislike'), Value('like'), function='replace',))
        else:
            ThreadVote.objects.create(thread_id=thread.pk, user_id=request.user.id, vote_type=vote_type)
    return redirect('view_thread', thread.pk)
