from django.shortcuts import render
from django.http import HttpResponse 
def home(request): 
    return HttpResponse("Welcome to the Hospital Management System")

# Create your views here.
