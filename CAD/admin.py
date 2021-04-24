from django.contrib import admin
from .models import Drawing, DrawingSeries

class DrawingSeriesAdmin(admin.ModelAdmin):
    fields = ('name','Aerodrome')

class DrawingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Drawing._meta.fields]

admin.site.register(DrawingSeries,DrawingSeriesAdmin)
admin.site.register(Drawing,DrawingAdmin)
