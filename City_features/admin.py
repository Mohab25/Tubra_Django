from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *

class CityFacilityAdmin(LeafletGeoAdmin):
    list_display = [field.name for field in City_Facility._meta.fields]

class CityBlocksAdmin(LeafletGeoAdmin):
    list_display = [field.name for field in City_Blocks._meta.fields]

class ObeidCityUrbanAreaAdmin(LeafletGeoAdmin):
    list_display = [field.name for field in Ob_urban_area._meta.fields]


admin.site.register(City_Facility,CityFacilityAdmin)
admin.site.register(City_Blocks,CityBlocksAdmin)
admin.site.register(Ob_urban_area,ObeidCityUrbanAreaAdmin)