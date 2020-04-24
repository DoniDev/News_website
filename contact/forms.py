# from django import forms
from django.forms import Form
from django import forms

class ContactForm(Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}),label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email Address'}),label='')
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message'}),label='')

