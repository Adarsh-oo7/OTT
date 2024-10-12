from django.urls import path
from . import views
urlpatterns = [
    path('',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('resetPassword',views.rest_password,name="restPassword"),
    path('changepassword',views.change_password,name="changepassword"),
    # path('content',views.content,name="content")
    path('user',views.users,name="users"),
    path('watchHistory',views.watch_history,name="watchHistory"),
    path('subHistory',views.subscription_history,name="subhistory")


]
