from django.shortcuts import render

# Create your views here.

def revenue_generated(request):
    return render(request,'reports/revenueGenerated.html')


def view_count(request):
    return render(request,'reports/viewCount.html')


def sub_history(request):
    return render(request,'reports/subHistory.html')


def movie_rating(request):
    return render(request,'reports/movieRating.html')