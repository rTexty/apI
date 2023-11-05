from .serializers import CarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Car, Brand
from django.forms import model_to_dict

class CarsAPIView(APIView):
    def get(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car)
            return Response({'car': serializer.data})
        except Car.DoesNotExist:
            return Response({'error': 'Car does not exist'})
        
        
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        
        try:
            instance = Car.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = CarSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})



        # brands = request.data.get('brands')
        # year = request.data.get('year')
        # model = request.data.get('model')
        # cat_id = request.data.get('cat_id')  # Get the 'cat_id' value from the request data

        # car = Car.objects.create(brands=brands, year=year, cat_id=cat_id, model = model)  # Pass the 'cat_id' value to the create method

        # return Response({'post': model_to_dict(car)})