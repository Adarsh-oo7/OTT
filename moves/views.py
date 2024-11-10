from django.shortcuts import render
from .models import movie
from rest_framework.response import Response
from django.http import JsonResponse
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


def search_movies(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.method == "GET":
        query = request.GET.get('query', '')
        if query:
            movies = movie.objects.filter(title__icontains=query)
            results = [{"id": movie.id, "title": movie.title, "description": movie.description} for movie in movies]
            return JsonResponse({"results": results})
        else:
            return JsonResponse({"results": []})  
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)