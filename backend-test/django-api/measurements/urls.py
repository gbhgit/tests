from django.urls import path
from measurements.views import MeasurementViewSet


urlpatterns = [
    path(
        "measurements/",
        MeasurementViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="measurement-list",
    ),
    path(
        "measurements/<int:pk>/",
        MeasurementViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="measurement-detail",
    ),
]
