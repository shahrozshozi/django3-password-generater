from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters= list(' ')
    thepassword= ''
    length= int(request.GET.get('length', 0))
    if request.GET.get('uppercase'):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get('lowercase'):
        characters.extend("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get('special character'):
        characters.extend("!@#$%^&*()")
    if request.GET.get('number'):
        characters.extend("1234567890")
   
    for x in range(length):
        thepassword+=random.choice(characters)
    if thepassword=="":
        thepassword+="please select atleast one checkbox"
    

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')