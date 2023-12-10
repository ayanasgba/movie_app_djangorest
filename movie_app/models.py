from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator

class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def movie_count(self):
        return self.movies.all().count()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def count_reviews(self):
        return self.reviews.all().count()
    @property
    def all_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return [{'id': i.id, 'text': i.text, 'stars': i.stars} for i in reviews]

    @property
    def average_rating(self):
        return self.reviews.aggregate(Avg('stars'))['stars__avg'] or 0

    # result:
    # {
    #     "id": 1,
    #     "title": "Astral",
    #     "description": "Awful",
    #     "duration": 2,
    #     "director": 4,
    #     "reviews": [
    #         {
    #             "id": 4,
    #             "text": "wiaskljcdns",
    #             "stars": 1,
    #             "movie": 1
    #         },
    #         {
    #             "id": 1,
    #             "text": "I like it",
    #             "stars": 5,
    #             "movie": 1
    #         },
    #         {
    #             "id": 5,
    #             "text": "hjgsdkofapdl",
    #             "stars": 2,
    #             "movie": 1
    #         }
    #     ],
    #     "count_reviews": 3,
    #     "average_rating": 2.6666666666666665
    # },

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='reviews')
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    #movieRev = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True)
    def __str__(self):
        return f"Review for {self.movie.title}"
