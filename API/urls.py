from django.urls import path
from . import views
urlpatterns = [
    path("reg",views.Register,name="Register"),
    path('login',views.login,name="login"),
    path('movie_list',views.movie_listing,name="moveListing"),
    path('movie/<int:id>',views.movie_detail,name="movie")
    
]
