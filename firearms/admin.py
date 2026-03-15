from django.contrib import admin

from .models import Type
from .models import CaliberGauge
from .models import Firearm

class FirearmAdmin(admin.ModelAdmin):

    list_display = [
        "manufacturer_importer",
        "model",
        "type",
        "caliber_gauge",
        "date_acquired"
    ]

    list_filter = [
        "manufacturer_importer",
        "model",
        "type",
        "caliber_gauge",
        "date_acquired"
    ]

admin.site.register(Type)
admin.site.register(CaliberGauge)
admin.site.register(Firearm, FirearmAdmin)