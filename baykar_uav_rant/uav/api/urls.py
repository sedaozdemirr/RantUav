
from django.urls import path, include
from rest_framework import routers
from uav.api.views.uav_viewset import UavApiView

app_name = "api"
router = routers.DefaultRouter()
router.register(r'uav', UavApiView, basename="uav")


urlpatterns = [
    path('', include(router.urls)),
]