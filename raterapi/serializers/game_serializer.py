from rest_framework import serializers
from raterapi.models import Game, Category, GameCategory
from .category_serializer import CategorySerializer

class GameSerializer(serializers.ModelSerializer):
    # Custom field for reading (output)
    categories = CategorySerializer(many=True, read_only=True, source='game_categories.category')

    # Custom field for writing (input)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Game
        fields = [
            'id', 'title', 'description', 'designer', 'year_released', 'num_of_players', 'est_play_time', 'age_recommendation', 'user', 'average_rating', 'categories', 'category_ids'
        ]
        read_only_fields = ['id', 'average_rating']

    def create(self, validated_data):
        #Extract category_ids from validated data
        category_ids = validated_data.pop('category_ids', [])

        #Create the game
        game = Game.objects.create(**validated_data)

        #Create GameCategory relationships
        for category in category_ids:
            GameCategory.objects.create(game=game, category=category)

        return game
    
    def update(self, instance, validated_data):
        #Extract category_ids if present
        category_ids = validated_data.pop('category_ids', None)

        #Update game fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        #Update categories if provided
        if category_ids is not None:
            #Remove old category relationships
            instance.game_categories.all().delete()

            #Create new category relationships
            for category in category_ids:
                GameCategory.objects.create(game=instance, category=category)

        return instance
    