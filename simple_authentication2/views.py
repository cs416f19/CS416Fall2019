from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    #Render the index page
    return render(request, 'simple_authentication2/index.html')

def login(request):
    #this is the method that authenticates the user based on username and password,
    #also renders the login page if the request method is not post
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        # Show the the index page if the user is authenticated, else give feedback saying nvalid credentials
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'simple_authentication2/login.html')

def logout(request):
    #This is the method to logout the user
    auth.logout(request)
    return redirect('index')

def register(request):
    #This is the method to render the registiration form page and create a new user based on the form data
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # More validation to make sure the above fields are not empty!

        # Validate password1 matched with password2
        # Validate the username and email address was not taken
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                print("Username is taken, must be unique")
                messages.info(request, 'Username is taken, must be unique')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                print("Email is taken, must be unique")
                messages.info(request, 'Email is taken, must be unique')
                return redirect('register')
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username, password=password1)
                print("A user has been created!")
        else:
            print("Passwords do not match!")
            messages.info(request, 'Passwords do not match!')
            return redirect('register')

        return redirect('index')

    else:
        return render(request, 'simple_authentication2/register.html')