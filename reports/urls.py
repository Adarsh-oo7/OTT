from django.urls import path
from . import views
urlpatterns = [
    path('',views.revenue_generated,name="revenueGenerated")
]
