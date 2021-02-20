from django.contrib import admin
from .models import Document_Type, Document

class DocumentTypeAdmin(admin.ModelAdmin):
    fields = ('Doc_type',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Document._meta.fields]

admin.site.register(Document_Type,DocumentTypeAdmin)
admin.site.register(Document,DocumentAdmin)
