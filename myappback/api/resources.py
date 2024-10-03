from rest_framework.viewsets import ModelViewSet
from myappback.models import CategoryActivity, Doctors
from myappback.api.serializers import  CategoryActivitySerializer, DoctorSerializer


class CategoryActivityModelViewSet(ModelViewSet):
    queryset = CategoryActivity.objects.all()
    serializer_class = CategoryActivitySerializer
    

class DoctorsModelViewSet(ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer