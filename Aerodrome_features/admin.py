from django.contrib import admin
from .models import *

class Aerodrome_Part_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Aerodrome_Part._meta.fields]

class Aerodrome_Entity_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Aerodrome_Entity._meta.fields]

class Pavement_Construction_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Pavement_Construction._meta.fields]

class Aerodrome_Utility_Pole_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Aerodrome_Utility_Pole._meta.fields]

class Aerodrome_Utility_Electric_Cable_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Aerodrome_Utility_Electric_Cable._meta.fields]

class Aerodrome_Utility_Water_Line_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Aerodrome_Utility_Water_Line._meta.fields]

class Aerodrome_Utility_Gas_Line_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Aerodrome_Utility_Gas_Line._meta.fields]

class Aerodrome_Utility_Sewage_Line_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Aerodrome_Utility_Sewage_Line._meta.fields]

class Aerodrome_Entity_Image_Admin(admin.ModelAdmin):
    list_display = [field.name for field in Aerodrome_Entity_Image._meta.fields]



admin.site.register(Aerodrome_Part,Aerodrome_Part_Admin)
admin.site.register(Aerodrome_Entity,Aerodrome_Entity_Admin)
admin.site.register(Pavement_Construction,Pavement_Construction_Admin)
admin.site.register(Aerodrome_Utility_Pole,Aerodrome_Utility_Pole_Admin)
admin.site.register(Aerodrome_Utility_Electric_Cable,Aerodrome_Utility_Electric_Cable_Admin)
admin.site.register(Aerodrome_Utility_Water_Line,Aerodrome_Utility_Water_Line_Admin)
admin.site.register(Aerodrome_Utility_Gas_Line,Aerodrome_Utility_Gas_Line_Admin)
admin.site.register(Aerodrome_Utility_Sewage_Line,Aerodrome_Utility_Sewage_Line_Admin)
admin.site.register(Aerodrome_Entity_Image,Aerodrome_Entity_Image_Admin)