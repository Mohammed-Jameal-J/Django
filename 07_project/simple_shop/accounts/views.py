from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

class AuthViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
           customer = serializer.save()
           token = AccessToken.for_user(customer)
           return Response({'access_token': str(token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            