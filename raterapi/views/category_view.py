from rest_framework import viewsets
from raterapi.models import Category
from raterapi.serializers import CategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for viewing categories """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer