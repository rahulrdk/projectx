from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexdef(request):
    return render(request,'user/index.html')

def aboutdef(request):
    return render(request,'user/about.html')
    
def contactsdef(request):
    return render(request,'user/contacts.html')

def homedef(request):
    return render(request,'user/home.html')
def logindef(request):
    return render(request,'user/login.html')

def baabtra(request):
    return render(request,'user/baabtra.html')