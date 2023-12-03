from rest_framework.generics import *
from .serializers import UserSerializer
from .models import User
# Create your views here.

class GetUserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserList(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer