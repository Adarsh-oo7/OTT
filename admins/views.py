from django.shortcuts import render,redirect,get_object_or_404
from API.forms import CustomUserCreationForm
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import authenticate
# Create your views here.

def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return render(request, "register.html")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return render(request, "register.html")

        user = CustomUser(email=email)
        user.set_password(password)
        user.save()

        messages.success(request, "Registration successful")
        return redirect('login')  
    return render(request, "register.html")


def login(request):
    if request.POST:
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= authenticate(email=email,password=password)
        if user:
            print("success")
            return redirect('listmovies')

        
        
    return render(request,'login.html')


def rest_password(request):
    return render(request,'restpassword.html')


def change_password(request):
    return render(request,'changepassword.html')



def users(request):
    user=CustomUser.objects.all()
    
    return render(request,'user/user.html',{"user":user})



def watch_history(request):
    return render(request,'user/watchHistory.html')



def subscription_history(request):
    return render(request,'user/subscriptionHistory.html')






def block_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.block = True
    user.save()
    return redirect('users')  


def unblock_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.block = False
    user.save()
    return redirect('users')