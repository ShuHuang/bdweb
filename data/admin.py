from django.contrib import admin
from .models import BatteryProperty, BatteryDevice

admin.site.register(BatteryProperty)
admin.site.register(BatteryDevice)
