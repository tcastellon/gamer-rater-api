from rest_framework import serializers
from raterapi.models import GameReview

class GameReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameReview
        fields = ['id', 'game', 'user', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
