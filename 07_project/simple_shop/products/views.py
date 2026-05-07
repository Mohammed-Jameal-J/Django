from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Product
from .serializers import ProductSerializer  
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.filter(stock_quantity__gt=0)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
