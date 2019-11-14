from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(request.POST)
            print (form.cleaned_data['email'])
            form.save()
            # redirect to a new URL:
            return render(request, 'simpleform/thanks.html')
    else:
        form = ContactForm()
        context = {'form' : form}
        template = 'simpleform/contact.html'
        return render(request, template, context)