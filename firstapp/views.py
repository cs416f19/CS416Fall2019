from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import People


def index(request):
    # get all the records in the people table in the database, and then reverse order them so that the last record appears first
    allPeople = People.objects.order_by('-id')

    # send allPeople object to the index.html where the fields of u (first_name, last_name and age) can be displayed
    context = {'people': allPeople}
    template = 'index.html'
    return render(request, template, context)

def addUser(request):
    # First check if the form has been sent by a post method
    # if so, then get the values
    if request.method == 'POST':

        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        age = request.POST.get("age")

        # Add a new record into the database
        People.objects.create(first_name = firstName, last_name = lastName, age = age)

        # Redirect to the index.html
        return redirect('index')
    else:
        return HttpResponse("Something went wrong!")


def register(request):
    #View/Render the register.html
    template = 'register.html'
    return render(request, template)


def test(request):
    # Add a record to the database
    p = People(first_name = "John", last_name = "Doe", age = 22)
    p.save()

    # Get the first row in the database and assign it to a variable called u
    u = People.objects.first()

    #Get the record whose id is 1
    #u = People.objects.get(id=1)

    # Print the values
    return HttpResponse("firstname = %s, lastname = %s, age=%s" %(u.first_name, u.last_name, u.age))