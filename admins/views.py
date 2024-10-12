from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,"register.html")


def login(request):
    return render(request,'login.html')


def rest_password(request):
    return render(request,'restpassword.html')


def change_password(request):
    return render(request,'changepassword.html')

