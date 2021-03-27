from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from .models import snippet_table , Contact


# Create your views here.
def index(request):
    messages.success(request, 'Your message has been sent!')
    return render(request , 'index.html')

def snippets(request):
    all_snippets = snippet_table.objects.all().order_by('name')
    context = {
        "variable1" : all_snippets
    }
    return render(request , 'snippets.html' , context)

def calulator(request):
    return render(request , 'calculator.html')

def contact(request):
    display_style = "none"
    if request.method == "POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(firstname=firstname , lastname=lastname , email = email , phone=phone , message = message, date=datetime.today())
        contact.save()
        display_style = "block"
    context = {
        "display_style" : display_style
    }
    return render(request , 'contact.html' , context)