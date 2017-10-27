# -*- coding: utf-8 -*-
from django.contrib.gis import admin

# Register your models here.

from siting.models import County, SitingModel, ModelLayer

# regular geodjango admin
#admin.site.register(County, admin.GeoModelAdmin)

# open street map admin
admin.site.register(County, admin.OSMGeoAdmin)

admin.site.register(SitingModel)

admin.site.register(ModelLayer)

