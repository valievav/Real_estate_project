from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User

from secrets import compare_digest


def register(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')
    else:
        # POST logic
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if compare_digest(password, password2):  # to reduce the risk of timing attacks
            # check username & email don't exist
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email already exists')
                    return redirect('register')
                else:
                    # create user
                    user = User.objects.create_user(first_name=first_name,
                                                    last_name=last_name,
                                                    username=username,
                                                    email=email,
                                                    password=password
                                                    )
                    # login user automatically after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')

                    # prompt user to log in manually
                    user.save()
                    messages.success(request, 'You have been registered, please log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')


def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    else:
        # POST logic
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:  # found in db
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')


def logout(request):  # redirect to home page
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are  logged out")
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
