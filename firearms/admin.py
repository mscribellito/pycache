from django.contrib import admin

from .models import CaliberGauge
from .models import Firearm

admin.site.register(CaliberGauge)
admin.site.register(Firearm)