from django.shortcuts import render
from .models import movie
# Create your views here.

def list_movies(request):
    data=movie.objects.all()
    print(data)

    return render(request,'content.html',{'data':data})



def add_movies(request):
    return render(request,'addMovie.html')



def edit_movies(request):
    return render(request,'editeMovie.html')



def view_movies(request):
    return render(request,'contenView.html')