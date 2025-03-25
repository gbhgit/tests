from measurements.models import Measurement
from measurements.serializers import MeasurementSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request

class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [] # just for testing purposes

    def list(self, request: Request, *args, **kwargs) -> Response:
        return Response({'message': 'retrieve method is working'})