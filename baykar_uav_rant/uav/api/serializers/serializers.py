from rest_framework import serializers
from uav.models import Uav,Customer,Reservation

class UavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uav
        fields = ('brand', 'model', 'weight', 'category', 'airtime', 'price','img')
class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('brand', 'model', 'weight', 'category', 'airtime', 'price')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('customer','uav','issue_date','return_date')