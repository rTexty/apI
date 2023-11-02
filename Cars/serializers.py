from rest_framework import serializers
from .models import Car
from rest_framework.renderers import JSONRenderer


class CarSerializer(serializers.ModelSerializer):
    brands = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    model = serializers.CharField(max_length=50, required=False)
    cat = serializers.CharField(default=1)


    class Meta:
        model = Car
        fields = [
            'brands',
            'year',
            'model',
            'cat',
        ]



    
    