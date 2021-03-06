
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.mail import EmailMessage
from users.forms import ContactByMailForm, RegistrationDemandForm
from articles.models import Article
from events.models import Event
from users.models import CustomUser
# Create your views here.

# Display the foundation HomeScreen
def home(request):
    return render(request, 'index.html')

# Display the foundation about page
def about(request):
    return render(request, 'about.html')

# Display the User profile
def privacy_policy(request):
    return render(request, 'privacy-policy.html')


# Contact-Us form handling
def contact_us(request):
    sent = False
    if request.method == 'POST':
        form = ContactByMailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message_to_send = "Sender: <strong>{} ({})</strong>.<br>Content:<br><br> {}".format(cd['name'],cd['email'], cd['message'])
            email_subject = "[Fundation website] {}".format(cd['subject'])
            msg = EmailMessage(email_subject, message_to_send,cd['email'], ["{}".format(settings.EMAIL_HOST_USER),],reply_to=[cd['email']])
            msg.content_subtype = "html"
            msg.send()
            sent = True
    else:
        form = ContactByMailForm()

    return render(request, 'contact/contact-us.html', {'form': form,'sent': sent})

# Registration on Demain view
def registration_demand(request):
    sent = False
    if request.method == 'POST':
        form = RegistrationDemandForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd['first_name']
            last_name = cd['last_name']
            email = cd['email']
            speciality = cd['speciality']
            grade = cd['grade']
            message = cd['message']
            cv_file = request.FILES['cv_file']

            message_to_send = """
                New membership request from: <strong>{} {}</strong>.<br>
                Profile:<br><br>
                First name: <strong>{}</strong><br>
                Last name: <strong>{}</strong><br>
                Email: <strong>{}</strong><br>
                Speciality: <strong>{}</strong><br>
                Grade: <strong>{}</strong><br>
                Message:<br>{}""".format(first_name, last_name, first_name,
                                            last_name, email, speciality, grade,
                                            message)

            email_subject = "[Fundation website] Registration {}".format(cd['first_name'])
            msg = EmailMessage(email_subject, message_to_send,email, ["{}".format(settings.EMAIL_HOST_USER),],reply_to=[cd['email']])
            msg.content_subtype = "html"
            msg.attach(cv_file.name, cv_file.read(), cv_file.content_type)
            msg.send()
            sent = True

    else:
        form = RegistrationDemandForm()

    return render(request, 'contact/registration.html', {'form': form,'sent': sent})

# Render Error
def errors_view(request):
    return render(request, '404.html')
