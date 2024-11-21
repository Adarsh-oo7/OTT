from django.urls import path
from . import views
urlpatterns = [
    path("reg",views.Register,name="Register"),
    path('login',views.login,name="logins"),
    path('movie_list',views.movie_listing,name="moveListing"),
    path('movie/<int:id>',views.movie_detail,name="movie"),
    path("movieHistory",views.movie_history,name="MovieHistory"),
    path('addWatchList',views.add_watch_later,name="watchlist"),
    path("user/email", views.get_user_email, name="get_user_email"),
    path('watchlater',views.watch_later,name="watchlater")
    
]
 