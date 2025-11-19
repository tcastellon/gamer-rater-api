from rest_framework import viewsets, permissions
from raterapi.models import GameRating
from raterapi.serializers import GameRatingSerializer

class GameRatingViewSet(viewsets.ModelViewSet):
    """ ViewSet for creating and managing game ratings """
    queryset = GameRating.objects.all()
    serializer_class = GameRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """ Auto-set the user from the logged-in user """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """ Filter ratings by game """
        queryset = GameRating.objects.all()
        game_id = self.request.query_params.get('game')

        if game_id:
            queryset = queryset.filter(game_id=game_id)
        
        return queryset
    