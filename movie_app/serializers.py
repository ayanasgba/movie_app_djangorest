from rest_framework import serializers
from .models import *

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        # fields = '__all__'
        fields = 'id name movie_count'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        # fields = '__all__'
        fields = 'id title description duration director reviews count_reviews average_rating'.split()
    def get_reviews(self, movie):
        serializer = ReviewSerializer(Review.objects.filter(text__isnull=False, movie=movie),
                                          many=True)
        return serializer.data


