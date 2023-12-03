from rest_framework.generics import *
from .models import Car
from .serializers import CarSerializer




class CreateCarList(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class UpdateCarList(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    