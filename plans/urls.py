from django.urls import path
from . import views

urlpatterns = [
    path("",views.plans,name="plans"),
    path("viewPlan",views.view_plan,name="viewPlan"),
    path('createPlan',views.create_plan,name="createPlan")

]
