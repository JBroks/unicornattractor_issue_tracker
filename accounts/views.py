from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, UserChangeForm, UserDeleteForm
from .models import UserProfile
from tickets.models import Ticket, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
        
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
        
    return render(request, 'registration.html', {"registration_form": 
                    registration_form})

def user_profile(request, username):
    """The user's profile page"""

    user = User.objects.get(username=request.user.username)
    
    # Count all tickets / commments submited by the user
    ticket_count = Ticket.objects.filter(user=request.user).count()
    comment_count = Comment.objects.filter(user=request.user).count()
    
    # Retrive all user tickets / comments
    user_tickets = Ticket.objects.filter(user=request.user)
    user_comments = Comment.objects.filter(user=request.user)
    
    page = request.GET.get('page', 1)
    
    # Paginate tickets
    paginator = Paginator(user_tickets, 10)
    try:
        user_tickets = paginator.page(page)
    except PageNotAnInteger:
        user_tickets = paginator.page(1)
    except EmptyPage:
        user_tickets = paginator.page(paginator.num_pages)
    
    # Paginate comments
    paginator = Paginator(user_comments, 10)
    try:
        user_comments = paginator.page(page)
    except PageNotAnInteger:
        user_comments = paginator.page(1)
    except EmptyPage:
        user_comments = paginator.page(paginator.num_pages)
   
    context = {"user": user,
            "ticket_count": ticket_count,
            "comment_count": comment_count,
            "user_tickets": user_tickets,
            "user_comments": user_comments }
            
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request, username):
    
    username = User.objects.get(username=request.user.username)
    
    if request.method == 'POST':
        edit_form = UserChangeForm(request.POST, instance=request.user)
        
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, "Your profile has been successfully \
                              updated!")
            return redirect('profile', username)
            
    else:
        edit_form = UserChangeForm(instance=request.user)
        
    return render(request, 'edit_profile.html', {'edit_form': edit_form })

@login_required    
def delete_account(request):
    
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