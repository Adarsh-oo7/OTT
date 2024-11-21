from django.urls import path
from . import views
urlpatterns = [
    path('',views.list_movies,name="listmovies"),
    path('add',views.add_movies,name="addMove"),
    path('edite/<int:id>',views.edit_movies,name="editMovie"),
    path('moveView',views.view_movies,name="movieView"),
    path('search', views.search_movies, name='search_movies'),
    path('dele/<int:id>',views.del_movie,name="delete"),
    

]
