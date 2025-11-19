from rest_framework import viewsets, permissions
from raterapi.models import Game
from raterapi.serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
    """ ViewSet for creating and managing games """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """ Auto-set the user from the logged-in user """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Filter games by category or year.
        Examples:
          - GET /games?category=1  (games in category 1)
          - GET /games?year_released=2015  (games from 2015)
        """
        queryset = Game.objects.all()

        # Filter by category
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(game_categories__category_id=category_id).distinct()

        # Filter by year
        year = self.request.query_params.get('year_released')
        if year:
            queryset = queryset.filter(year_released=year)

        return queryset