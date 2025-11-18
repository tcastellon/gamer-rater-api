from rest_framework import serializers
from raterapi.models import GameImage

class GameImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameImage
        fields = ['id', 'game', 'user', 'image_file', 'uploaded_at']
        read_only_fields = ['id', 'user', 'uploaded_at']
