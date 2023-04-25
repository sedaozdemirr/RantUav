from rest_framework import serializers
from uav.models import Customer

class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('brand', 'model', 'weight', 'category', 'airtime', 'price')
