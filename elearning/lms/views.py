from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
def forget(request):
    template = loader.get_template('forget.html')
    return HttpResponse(template.render())
def beranda(request):
    template = loader.get_template('beranda.html')
    return HttpResponse(template.render())