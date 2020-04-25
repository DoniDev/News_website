from django.shortcuts import render
from contact.forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from contact.models import Contact
import os


def contact(request):
    details = Contact.objects.first()


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(name,message,email,[str(os.environ.get('EMAIL_USER'))])
            messages.success(request,'Email sent successfuly')
        else:
            messages.error(request,'Something went wrong try again!')
    else:
        form = ContactForm()

    context={
        'form':form,
        'details':details,
    }


    return render(request,'contact/contact.html',context=context)