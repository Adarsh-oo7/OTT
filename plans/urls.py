from django.urls import path
from . import views

urlpatterns = [
    path("",views.plans,name="plans"),
    path("",views.view_plan,name="viewPlan"),
    path('createPlan',views.create_plan,name="createPlan")

]
