from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from .game import Game

class GameRating(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('game', 'user')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} rated {self.game.title}: {self.rating}/10"
