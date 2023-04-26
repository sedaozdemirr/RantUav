from rest_framework import serializers
from uav.models import Uav
from django.conf import settings
class UavSerializer(serializers.ModelSerializer):
    # img = serializers.SerializerMethodField()
    class Meta:
        model = Uav
        fields = ('id','brand', 'model', 'weight', 'category', 'airtime', 'price','img')

    # def get_img(self, obj):
    #     return  'http://127.0.0.1:8000/baykar_uav_rant' + obj.img.url if obj.img else ''

