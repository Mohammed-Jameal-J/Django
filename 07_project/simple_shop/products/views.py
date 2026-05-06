from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Product
from .serializers import ProductSerializer  


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.filter(stock_quantity__gt=0)
    serializer_class = ProductSerializer
