from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from booker.settings import EMAIL_HOST_USER
from booker.forms import ContactForm

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def send_email(contact_form_data):
    email_message_format = 'name: %s\nemail: %s\nMessage: %s\n'
    name = contact_form_data.get('name', '')
    message = contact_form_data.get('message', '')
    email = contact_form_data.get('email')
    email_message_format = email_message_format % (name, email, message)
    send_mail('Booker WebApp', email_message_format, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently=False,)

def contact(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                send_email(form.cleaned_data)
                messages.success(request, 'Your response has been recorded')
        else:
            form = ContactForm()
    except:
        messages.error(request, 'Please configure your email settings.')

    return render(request, 'contact.html', {'form':form})

def clear(request):
	form = ContactForm()
	messages.error(request, 'Fields cleared successfully')
	return render(request, 'contact.html', {'form':form})