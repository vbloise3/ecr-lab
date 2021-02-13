from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import loader, backends
from datetime import datetime

#TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',

ROOT_URLCONF = __name__

def index(request):
    title = 'AWS Certified Architect Associate course'
    app_type = 'an ECR repository'
    module = 'ECR fundamentals'
    author = 'Whiz Labs'
    date_run = datetime.now()
    html = render_to_string('index.html', {'title': title, 'app_type': app_type, 'module': module, 'author': author, 'date': date_run})
    return HttpResponse(html)

def dindex(request):
    return HttpResponse("<h1>You have successfully created an ECR repository!</H1><H2>Congratulations on learning the ECR fundamentals in the AWS Certified Architect Associate course!</H2>")

urlpatterns = [
    url(r'^$', index, name='homepage'),
    url(r'^about/$', dindex, name='aboutpage'),
]
