from django.urls import path
from measurements.views import MeasurementViewSet


urlpatterns = [
    path('measurements' , MeasurementViewSet.as_view({"get": "list"}), name='measurement'),
]