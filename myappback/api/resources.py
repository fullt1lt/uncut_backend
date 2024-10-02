from rest_framework.viewsets import ModelViewSet
from myappback.models import CategoryActivity
from myappback.api.serializers import  CategoryActivitySerializer


class CategoryActivityModelViewSet(ModelViewSet):
    queryset = CategoryActivity.objects.all()
    serializer_class = CategoryActivitySerializer
    