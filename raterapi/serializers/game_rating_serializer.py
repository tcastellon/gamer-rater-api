from rest_framework import serializers
from raterapi.models import GameRating

class GameRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRating
        fields = ['id', 'game', 'rating', 'user', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
