from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, UserChangeForm


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
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
        
        args = {'login_form': login_form}
        
    return render(request, 'login.html', args)


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
        
        args = {"registration_form": registration_form}
        
    return render(request, 'registration.html', args)

def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    date_joined = User.objects.get(date_joined=request.user.date_joined)
    
    args = {"profile": user, "date_joined": date_joined}
    
    return render(request, 'profile.html', args)

def edit_profile(request):
    
    if request.method == 'POST':
        edit_form = UserChangeForm(request.POST, instance=request.user)
        
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, "Your profile has been successfully \
                              updated!")
            return redirect(reverse('profile'))
            
    else:
        edit_form = UserChangeForm(instance=request.user)
        args = {'edit_form': edit_form }
        
    return render(request, 'edit_profile.html', args)
    