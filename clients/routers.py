from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from clients.views import SensorViewSet, LecturaViewSet, ClientViewSet, ElectricMeterViewSet

router = DefaultRouter()

router.register(r'sensors', SensorViewSet, basename="sensors")
router.register(r'lecturas', LecturaViewSet, basename="lecturas")
router.register(r'clients', ClientViewSet, basename="clients")
router.register(r'electric_meter', ElectricMeterViewSet, basename="electric_meter")

urlpatterns = router.urls