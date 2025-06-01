from measurements.models import Measurement
from rest_framework import serializers


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"
