from rest_framework import serializers
from uav.models import Uav
from django.conf import settings
class UavSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    class Meta:
        model = Uav
        fields = ('brand', 'model', 'weight', 'category', 'airtime', 'price','img')

    def get_img(self, obj):
        return  settings.STATIC_URL + obj.img.url if obj.img else ''