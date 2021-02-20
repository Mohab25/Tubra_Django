from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    fields=('Project_Name','Aerodrome')

class PhaseAdmin(admin.ModelAdmin):
    fields=('Phase_Name','Project')

class ActivityAdmin(admin.ModelAdmin):
    fields=('Activity_Name','Phase','Completion')

admin.site.register(Project,ProjectAdmin)
admin.site.register(Phase,PhaseAdmin)
admin.site.register(Activity,ActivityAdmin)
