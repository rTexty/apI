from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Car, Brand
from django.forms import model_to_dict

class CarsAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        car_data = [model_to_dict(car) for car in cars]  # Convert each Car object to a dictionary
        return Response({'cars': car_data})
    def post(self, request):
        brands = request.data.get('brands')
        year = request.data.get('year')
        cat_id = request.data.get('cat_id')  # Get the 'cat_id' value from the request data

        try:
            brands = Brand.objects.get(name=brands)
        except Brand.DoesNotExist:
            brands = Brand.objects.create(name=brands)


        car = Car.objects.create(brands=brands, year=year, cat_id=cat_id)  # Pass the 'cat_id' value to the create method

        return Response({'post': model_to_dict(car)})