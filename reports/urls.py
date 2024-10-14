from django.urls import path
from . import views
urlpatterns = [
    path('',views.revenue_generated,name="revenueGenerated"),
    path("viewCount",views.view_count,name="viewCount"),
    path('subHistory',views.sub_history,name="subHistory"),
    path('moveRating',views.movie_rating,name='moveRating')

]
