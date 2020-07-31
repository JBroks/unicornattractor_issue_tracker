from django.shortcuts import render, redirect, reverse
from django.db.models import Sum
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, \
    UserChangeForm, UserDeleteForm, UploadFileForm
from .models import UserProfile
from tickets.models import Ticket, Comment, Upvote, Donation
from forum.models import Thread, Post, ThreadVote, PostVote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(request, list):
    '''
    Helper function that will paginate any qiven queryset.
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


@login_required
def logout(request):
    '''
    Log the user out.
    '''
    auth.logout(request)
    messages.success(request, 'You have successfully been logged out')
    return redirect(reverse('index'))


def login(request):
    '''
    View that renders a login page.
    If user is authenticated he or she will be redirected to the index page.
    '''
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully logged in!')
                return redirect('profile', user.username)
            else:
                login_form.add_error(None, 'Your username or password is \
                                     incorrect')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    '''
    View that renders the registration page.
    If user is authenticated he or she will be redirected to the index page.
    '''
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered')
                return redirect('profile', user.username)
            else:
                messages.error(request, 'Unable to register your account at \
                               this time')
    else:
        registration_form = UserRegistrationForm()
        
    context = {'registration_form': registration_form}
    
    return render(request, 'registration.html', context)


def user_profile(request, username):
    '''
    The user's profile page
    '''
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
    else:
        return redirect('login')
        
    # Count all content submited by the user
    ticket_count = Ticket.objects.filter(user=request.user).count()
    comment_count = Comment.objects.filter(user=request.user).count()
    upvotes_count = Upvote.objects.filter(user=request.user).count()
    thread_count = Thread.objects.filter(user=request.user).count()
    post_count = Post.objects.filter(user=request.user).count()
    thread_votes_count = ThreadVote.objects.filter(user=request.user).count()
    post_votes_count = PostVote.objects.filter(user=request.user).count()
    
    # Get a sum of donations for a given user
    donations_total = Donation.objects.filter(user=request.user).aggregate(
                    Sum('donation_amount'))['donation_amount__sum']
    
    # Set donations to zero if no donations has been made
    if donations_total is None:
        donations_total = 0
    else:
        donations_total
    
    # Retrive all user content
    user_tickets = Ticket.objects.filter(user=request.user)
    user_comments = Comment.objects.filter(user=request.user)
    user_threads = Thread.objects.filter(user=request.user)
    user_posts = Post.objects.filter(user=request.user)
    user_thread_votes = ThreadVote.objects.filter(user=request.user)
    user_post_votes = PostVote.objects.filter(user=request.user)
    
    # Paginate pills content
    user_tickets = paginate(request, user_tickets)
    user_comments = paginate(request, user_comments)
    user_threads = paginate(request, user_threads)
    user_posts = paginate(request, user_posts)
    user_thread_votes = paginate(request, user_thread_votes)
    user_post_votes = paginate(request, user_post_votes)
    
    context = {
            'user': user,
            'ticket_count': ticket_count,
            'comment_count': comment_count,
            'upvotes_count': upvotes_count,
            'donations_total': donations_total,
            'thread_count': thread_count,
            'post_count': post_count,
            'thread_votes_count': thread_votes_count,
            'post_votes_count': post_votes_count,
            'user_tickets': user_tickets,
            'user_comments': user_comments,
            'user_threads': user_threads,
            'user_posts': user_posts,
            'user_thread_votes': user_thread_votes,
            'user_post_votes': user_post_votes
    }
    
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request, username):
    '''
    Allow user to edit their details as well as upload a new profile image
    '''
    username = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        edit_form = UserChangeForm(request.POST,
                                   instance=request.user)
        upload_img_form = UploadFileForm(request.POST,
                                         request.FILES,
                                         instance=request.user.userprofile)
        if edit_form.is_valid() and upload_img_form.is_valid():
            upload_img_form.save()
            edit_form.save()
            messages.success(request, 'Your profile has been successfully \
                              updated!')
            return redirect('profile', username)
    else:
        edit_form = UserChangeForm(instance=request.user)
        upload_img_form = UploadFileForm(instance=request.user.userprofile)
    
    context = {'edit_form': edit_form,
               'upload_img_form': upload_img_form}
               
    return render(request, 'edit_profile.html', context)


@login_required
def delete_account(request):
    '''
    Allow user to delete their account
    '''
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        if delete_form.is_valid():
            user = request.user
            user.delete()
            messages.info(request, 'Your account has been deleted.')
            return redirect('logout')
    else:
        delete_form = UserDeleteForm(instance=request.user)
    
    return render(request, 'delete_account.html', {'delete_form': delete_form})
