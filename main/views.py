from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import get_template
from django.conf import settings


from .forms import Contact
from .models import Project, Skill, Location, Info


def home_view(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    location = Location.objects.first()
    info = Info.objects.first()

    form = Contact()
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('name')
            from_email = form.cleaned_data.get('email')
            to_email = getattr(settings, 'DEFAULT_FROM_EMAIL')
            phone_num = form.cleaned_data.get('phone_number')
            message = form.cleaned_data.get('message')
            context = {'name': subject, 'message': message, 'phone': phone_num}
            txt_ = get_template('main/snippets/message.txt').render(context)
            html_ = get_template(
                'main/snippets/html_message.html').render(context)

            send_mail(
                subject,
                txt_,
                from_email,
                ['masterbdxteam@gmail.com'],
                html_message=html_,
                fail_silently=False
            )
            messages.add_message(request, messages.SUCCESS,
                                 'your message has been sent')
            return redirect('/#contact')
    context = {'projects': projects,
               'form': form,
               'skills': skills,
               'location':location,
               'info':info,
               }

    return render(request, 'main/home.html', context)
