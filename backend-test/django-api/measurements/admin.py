from django.contrib import admin

from measurements.models import Measurement


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    search_fields = ('id', 'status')