from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, settings.EMAIL_HOST_USER, ['samclendenan@icloud.com'])
            except BadHeaderError:
                return render(request, "main/locations.html")
            return render(request, 'main/index.html')
    return render(request, "main/contact.html", {'form': form})

def successView(request):
    return render('Success! Thank you for your message.')

def locations(request):
    return render(request, 'main/locations.html')