from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework import status

# Вывести список режиссеров
@api_view(['GET'])
def director_list_view(request):
    directors = Director.objects.all()
    data = DirectorSerializer(directors, many=True).data
    return Response(data)

# Вывести одного режиссера
@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Режиссер не найден"})
    data = DirectorSerializer(director).data
    return Response(data=data)

# Вывести список фильмов
@api_view(['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(movies, many=True).data
    return Response(data)

# Вывести один фильм
@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Фильм не найден"})
    data = MovieSerializer(movie).data
    return Response(data=data)

# Вывести список отзывов
@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data)

# Вывести один отзыв
@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': "Отзыв не найден"})
    data = ReviewSerializer(review).data
    return Response(data=data)