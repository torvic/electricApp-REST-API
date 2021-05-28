from django.urls import path
from clients.views import SensorListAPIView, LecturaListAPIView, ClientListAPIView

urlpatterns = [
  path('sensors/', SensorListAPIView.as_view(), name='sensors'),
  path('clients/', ClientListAPIView.as_view(), name='clients'),
  path('lecturas/', LecturaListAPIView.as_view(), name='lecturas'),
]