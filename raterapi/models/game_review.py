from django.db import models
from django.contrib.auth.models import User
from .game import Game

class GameReview(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('game', 'user')
        ordering = ['-created_at']
        verbose_name_plural = "Game Reviews"

    def __str__(self):
        return f"{self.user.username}'s review of {self.game.title}"
