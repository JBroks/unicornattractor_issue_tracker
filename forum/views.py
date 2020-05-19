from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, CommentPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AddPostForm, AddCommentPostForm
from django.db.models import Count, Sum

# Create your views here.
@login_required
def add_or_edit_post(request, pk=None):
    '''
    Allows user to add a new forum post or edit an existing one
    If user wants to add a new post they are redirected to a blank
    add_post_form where all details can be supplied and submitted
    If user wants to edit the post they are redirected to the post form
    that is pre-filled with the post details
    '''
    
    # Retrive the post if exists
    post = get_object_or_404(Post, pk=pk) if pk else None
    
    if request.method == "POST":
        add_post_form = AddPostForm(request.POST, request.FILES,
                                        instance=post)
        if add_post_form.is_valid():
            # Create post object without saving it to the database yet
            new_post = add_post_form.save(commit=False)
            # Assign the current user to the post
            add_post_form.instance.user = request.user
            # Save the post to the database
            new_post.save()
            messages.success(request, "You have successfully submitted your \
                                post!")
            return redirect('forum')
        else:
                messages.error(request, "Something went wrong. \
                                Please try again.")
    else:
        add_post_form = AddPostForm(instance=post)
    context = {
        'add_post_form': add_post_form
    }
    return render(request, 'add_post.html', context)

def forum(request):
    '''
    View all posts in a form of paginated table.
    Table is paginated to show only 10 records per page
    '''
    
    # Retrive all posts
    posts = Post.objects.all()
    
    page = request.GET.get('page', 1)
    
    # Paginate posts
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'forum.html', {'posts': posts})