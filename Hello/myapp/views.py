from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from myapp.admin import Contact
from django.contrib import  messages

# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    # messages.success(request,'Test message')
    return render(request,'index.html',context)

def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')

def summary(request):
    # return HttpResponse("this is summary page")
    return render(request,'summary.html')

def contact(request):
    # return HttpResponse("this is contact page")
    if request.method=="POST":
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(Name=Name,Email=Email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Form submitted successfully')
    return render(request,'contact.html')