from django.forms import ModelForm
from django import forms
import datetime
from .models import Contact

class ContactForm(ModelForm):
    phone = forms.CharField(required=False)

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message']
