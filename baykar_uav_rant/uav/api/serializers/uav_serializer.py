from rest_framework import serializers
from uav.models import Uav
class UavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uav
        fields = ('brand', 'model', 'weight', 'category', 'airtime', 'price','img')