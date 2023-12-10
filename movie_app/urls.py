from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/directors/', views.director_list_view, name='director_list_view'),
    path('api/v1/directors/<int:id>/', views.director_detail_view, name='director_detail_view'),
    path('api/v1/movies/', views.movie_list_view, name='movie_list_view'),
    path('api/v1/movies/<int:id>/', views.movie_detail_view, name='movie_detail_view'),
    path('api/v1/reviews/', views.review_list_view, name='review_list_view'),
    path('api/v1/reviews/<int:id>/', views.review_detail_view, name='review_detail_view'),
]