from django.contrib import admin

from employees.models import FederalManager, RegionalManager

admin.site.register(FederalManager)
admin.site.register(RegionalManager)
