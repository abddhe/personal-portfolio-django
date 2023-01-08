from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def hello_world(request:HttpRequest):
    return render(request,template_name='hello_world.html')