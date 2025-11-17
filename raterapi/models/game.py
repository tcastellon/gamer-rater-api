from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    designer = models.CharField(max_length=100)
    year_released = models.IntegerField()
    num_of_players = models.IntegerField()
    est_play_time = models.IntegerField()
    age_recommendation = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games")

    @property
    def average_rating(self):
        """Calculate the average rating for this game."""
        result = self.ratings.aggregate(Avg('rating'))
        return round(result['rating__avg'], 2) if result['rating__avg'] is not None else 0

    def __str__(self):
        return self.title