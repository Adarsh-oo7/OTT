from django.urls import path
from . import views
urlpatterns = [
    path('',views.list_movies,name="listmovies"),
    path('add',views.add_movies,name="addMove"),
    path('edite',views.edit_movies,name="editMovie"),
    path('moveView',views.view_movies,name="movieView"),
    
]
