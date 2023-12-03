from rest_framework import serializers
from .models import Car
from rest_framework.renderers import JSONRenderer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


