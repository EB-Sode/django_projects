from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    