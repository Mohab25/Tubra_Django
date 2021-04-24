from django.contrib import admin
from .models import Reference

class ReferenceAdmin(admin.ModelAdmin):
    fields=('Name','Reference_File','Aerodrome_Entity')

admin.site.register(Reference,ReferenceAdmin)
