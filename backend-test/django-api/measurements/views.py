from measurements.models import Measurement
from measurements.serializers import MeasurementSerializer
from rest_framework import viewsets


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = []
