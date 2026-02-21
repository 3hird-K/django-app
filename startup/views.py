from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse("Hello, world! I'm the home page.")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("Hello, world! I'm the about page.") 
    return render(request, 'about.html')
