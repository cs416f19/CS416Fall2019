from django.shortcuts import render
from django.http import HttpResponse
from .models import People

def addUser(request):

    # Add a record to the database
    p = People(first_name = "John", last_name = "Doe", age = 22)
    p.save()

    # Get the first row in the database and assign it to a variable called u
    u = People.objects.first()

    #Get the record whose id is 1
    #u = People.objects.get(id=1)

    # Print the values
    return HttpResponse("firstname = %s, lastname = %s, age=%s" %(u.first_name, u.last_name, u.age))


def register(request):
    #View the register.html
    template = 'register.html'
    return render(request, template)