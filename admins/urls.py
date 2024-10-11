from django.urls import path
from . import views
urlpatterns = [
    path('',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('resetPassword',views.rest_password,name="restPassword"),
    path('changepassword',views.change_password,name="changepassword")


]
