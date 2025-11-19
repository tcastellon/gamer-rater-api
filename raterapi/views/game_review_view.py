from rest_framework import viewsets, permissions
from raterapi.models import GameReview
from raterapi.serializers import GameReviewSerializer

class GameReviewViewSet(viewsets.ModelViewSet):
    """ ViewSet for creating and managing game reviews """
    queryset = GameReview.objects.all()
    serializer_class = GameReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """ Auto-set the user from the logged-in user """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """ Filter reviews by game """
        queryset = GameReview.objects.all()
        game_id = self.request.query_params.get('game')

        if game_id:
            queryset = queryset.filter(game_id=game_id)

        return queryset