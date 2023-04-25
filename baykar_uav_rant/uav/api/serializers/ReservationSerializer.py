from rest_framework import serializers
from uav.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('customer','uav','issue_date','return_date')