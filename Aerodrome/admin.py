from django.contrib import admin
from .models import Aerodrome

class AerodromeAdmin(admin.ModelAdmin):
    fields=['Name']

admin.site.register(Aerodrome,AerodromeAdmin)