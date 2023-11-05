from rest_framework import serializers
from .models import Car, Brand
from rest_framework.renderers import JSONRenderer


class CarSerializer(serializers.ModelSerializer):
    brands = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    model = serializers.CharField(max_length=50, required=False)
    cat = serializers.CharField(default=1)


    def create(self, validated_data):
        return Car.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.year = validated_data.get('year', instance.year)
        instance.cat = validated_data.get('cat', instance.cat)
        instance.save()
        return instance

    class Meta:
        model = Car
        fields = [
            'brands',
            'year',
            'model',
            'cat',
        ]



    
    