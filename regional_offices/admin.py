from django.contrib import admin

from regional_offices.models import City, Event, Region, Spot

admin.site.register(Region)
admin.site.register(City)
admin.site.register(Spot)
admin.site.register(Event)
