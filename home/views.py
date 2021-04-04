from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from .models import snippet_table , Contact , codeforce_submission


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

def cp_solutions(request):
    return render(request , 'cp_solutions.html')

def codeforces_submissions(request):
    cf_submissions = codeforce_submission.objects.all().order_by('problem_name')
    context = {
        "variable1" : cf_submissions
    }
    return render(request , 'codeforces_submissions.html' , context)
