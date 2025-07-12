from django.contrib.auth.models import User
from django.shortcuts import render

def home(request):
    qs = User.objects.all()
    print(qs)
    context = {'qs':qs}
    return render(request, 'port/home.html')

def about(request):
    objects = User.objects.all()
    print(objects)
    context = {'objects':objects}
    return render(request, 'port/about.html')