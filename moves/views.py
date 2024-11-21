from django.shortcuts import render,redirect,get_object_or_404
from .models import movie
from rest_framework.response import Response
from django.contrib import messages
from django.utils.html import escape,mark_safe


from django.http import JsonResponse
# Create your views here.

def list_movies(request):
    data=movie.objects.all()
    # print(data)

    return render(request,'content.html',{'data':data})



def add_movies(request):
    if request.method == 'POST':
        movieNames = request.POST.get('movieName')
        movieThumbnail = request.FILES.get('thumbnail')  
        movieVideo = request.FILES.get('movieVideo')
        movieDescriptions = request.POST.get('movieDescription')
        
        movie.objects.create(
            title=movieNames,
            thumbnail=movieThumbnail,
            video=movieVideo,
            description=movieDescriptions,
            count=0
        )
        
        message_text = f'Successfully added {movieNames} movie'
        messages.success(request, mark_safe(message_text))
        
    return render(request, 'addMovie.html')

def edit_movies(request,id):
    movies=movie.objects.get(id=id)
    if request.POST:
        movies.title = request.POST.get('title')
        
    if request.FILES.get('thumbnail'): 
        movies.thumbnail = request.FILES.get('thumbnail')  
    if request.FILES.get('movieVideo'):
        movies.video = request.FILES.get('movieVideo')
        movies.description = request.POST.get('movieDescription')
    movies.save()




    return render(request,'editeMovie.html',{'move':movies})



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
    


def del_movie(request,id):
    print(id)
    movies=get_object_or_404(movie,id=id)
    print(movies)
    movies.delete()
    return redirect('listmovies')


