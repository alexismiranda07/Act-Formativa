from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def display(request):
    return HttpResponse ("<h1>tengo alergias</h1>") 
def displayDateTime(request):
    dt=datetime.datetime.now()
    s="<b>Nocion humana del tiempo </b>" +str(dt)
    return HttpResponse(s)
