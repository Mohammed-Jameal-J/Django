from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import status
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


# Create your views here.

class CartViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_cart(self,user):
        cart, created = Cart.objects.get_or_create(user=user)
        return cart
