from django.urls import path
from . import views
urlpatterns = [
    path("reg",views.Register,name="Register"),
    path('login',views.login,name="login")
    
]
