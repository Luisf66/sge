from django.contrib import admin

from . import models
# Register your models here.

class OutflowsAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'description', 'created_at', 'updated_at')
    search_fields = ('product',)

admin.site.register(models.Outflow, OutflowsAdmin)