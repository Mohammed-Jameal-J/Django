from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Customer
        fields = ['email', 'password']

    def create(self, validated_data):
        customer = Customer(email=validated_data['email'])
        customer.set_password(password)
        customer.save()
        return customer