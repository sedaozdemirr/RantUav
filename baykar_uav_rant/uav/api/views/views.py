from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from uav.models import Uav
from uav.api.serializers.uav_serializer import UavSerializer

class UavApiView(viewsets.ModelViewSet):

    queryset = Uav.objects.all()
    serializer_class = UavSerializer



