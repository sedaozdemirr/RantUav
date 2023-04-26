from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from uav.models import Uav
from uav.api.serializers.uav_serializer import UavSerializer

class UavApiView(viewsets.ModelViewSet):

    queryset = Uav.objects.all()
    serializer_class = UavSerializer

    def delete(self, request, id=None):
        uavs = Uav.objects.filter(id=id)
        uavs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id=None):
        uavs = Uav.objects.filter(id=id)
        serializer = UavSerializer(uavs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
