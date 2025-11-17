from django.db import models
from .game import Game
from .category import Category

class GameCategory(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game_categories")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="game_categories")

    class Meta:
        unique_together = ('game', 'category')
        verbose_name_plural = "Game Categories"

    def __str__(self):
        return f"{self.game.title} - {self.category.name}"
