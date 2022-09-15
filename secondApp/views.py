from re import A
from django.shortcuts import render
from django.http import HttpResponse
from secondApp import views
# Create your views here.
def video(request):
    return HttpResponse ('<a href="https://youtu.be/pjj9newZBp0?t=19">huevo</a>')
