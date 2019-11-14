from django import forms
from django.forms import ModelForm
from .models import ContactMessage


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True,  max_length=60)
    last_name = forms.CharField(required=True, max_length=60)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'message']