from django.contrib import admin

from about.models import Contact, Partner, PartnerType

admin.site.register(Partner)
admin.site.register(Contact)
admin.site.register(PartnerType)
