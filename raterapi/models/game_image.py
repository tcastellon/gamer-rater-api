from django.db import models
from django.contrib.auth.models import User
from .game import Game

class GameImage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="images")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_images")
    image_file = models.ImageField(upload_to='game_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.game.title} - uploaded by {self.user.username}"
