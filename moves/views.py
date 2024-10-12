from django.shortcuts import render

# Create your views here.

def list_movies(request):
    return render(request,'content.html')



def add_movies(request):
    return render(request,'addMovie.html')



def edit_movies(request):
    return render(request,'editeMovie.html')



def view_movies(request):
    return render(request,'contenView.html')