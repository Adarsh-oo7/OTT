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



def users(request):
    return render(request,'user/user.html')



def watch_history(request):
    return render(request,'user/watchHistory.html')



def subscription_history(request):
    return render(request,'user/subscriptionHistory.html')