from rest_framework import viewsets, permissions
from raterapi.models import GameImage
from raterapi.serializers import GameImageSerializer

class GameImageViewSet(viewsets.ModelViewSet):
    """ ViewSet for uploading and managing game images """
    queryset = GameImage.objects.all()
    serializer_class = GameImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """ Auto-set the user from the logged-in user """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """ Filter images by game """
        queryset = GameImage.objects.all()
        game_id = self.request.query_params.get('game')

        if game_id:
            queryset = queryset.filter(game_id=game_id)

        return queryset