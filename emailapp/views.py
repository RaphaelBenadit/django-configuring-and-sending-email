# emailapp/views.py
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Create a home.html template
def send_email(request):
    try:
        send_mail(
            'Django Ex4 - reg.',
            'Good Morning! Welcome to the department of information technology.',
            settings.EMAIL_HOST_USER,
            ['22uit097@kamarajengg.edu.in'],
            fail_silently=False,
        )
        return render(request, 'sendMail.html', {'message': 'Email sent successfully!'})
    except Exception as e:
        # Log the error and return an error message
        return render(request, 'sendMail.html', {'error': f'An error occurred: {e}'})
