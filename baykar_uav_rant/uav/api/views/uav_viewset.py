from rest_framework import viewsets,filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from uav.models import Uav
from uav.api.serializers.uav_serializer import UavSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UavApiView(viewsets.ModelViewSet):

    queryset = Uav.objects.all()
    serializer_class = UavSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)

    filterset_fields = ['brand','model','weight','category','airtime','price']
    search_fields = ['brand',]
