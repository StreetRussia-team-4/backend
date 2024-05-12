from django.contrib import admin

from regional_offices.models import Citi, Event, Region, Spot

admin.site.register(Region)
admin.site.register(Citi)
admin.site.register(Spot)
admin.site.register(Event)
