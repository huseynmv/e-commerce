from datetime import date
from django.template.loader import render_to_string
import datetime
from celery import shared_task
from django.core.mail import EmailMessage
from . models import Blog
from core import settings
from account.models import User
import time

@shared_task
def dump_database():
    print('Dump database started')
    time.sleep(10)
    print('Dump database finished')
    
@shared_task
def send_email_to_users():
    print('Mail sent')
    user_emails = User.objects.values_list('email', flat=True)
    yesterday_blog = datetime.date.today()-datetime.timedelta(days=1)
    today = datetime.date.today()
    
    from_email = settings.EMAIL_HOST_USER
    blogs = Blog.objects.filter(date__range=[yesterday_blog, today])
    subject = 'Latest Blogs'
    context={
        'blogs':blogs,
        'site_adress': settings.SITE_ADDRESS
    }
    body = render_to_string('email.html', context)
    mail = EmailMessage(subject, to = user_emails, from_email=from_email, body=body)
    mail.content_subtype = 'html'
    mail.send(fail_silently=True)