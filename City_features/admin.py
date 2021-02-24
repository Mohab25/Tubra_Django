from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import City_Facility, City_Blocks

class CityFacilityAdmin(LeafletGeoAdmin):
    list_display = [field.name for field in City_Facility._meta.fields]

class CityBlocksAdmin(LeafletGeoAdmin):
    list_display = [field.name for field in City_Blocks._meta.fields]

admin.site.register(City_Facility,CityFacilityAdmin)
admin.site.register(City_Blocks,CityBlocksAdmin)