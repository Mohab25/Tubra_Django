from django.contrib import admin
from .models import City_Facility

class CityFacilityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in City_Facility._meta.fields]

admin.site.register(City_Facility,CityFacilityAdmin)