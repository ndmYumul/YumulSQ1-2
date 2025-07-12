from YumulSQ1.views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]