from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class LatestProductsList(APIView):
     def get(self, request, format=None):
          products = Product.objects.all()[0:4]
          serializers = ProductSerializer(products, many=True)
          return Response(serializers.data)