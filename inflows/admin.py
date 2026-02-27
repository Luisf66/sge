from django.contrib import admin
from . import models

# Register your models here.
class InflowsAdmin(admin.ModelAdmin):
    model = models.Inflow
    list_display = ('product', 'supplier', 'quantity', 'description', 'created_at', 'updated_at')
    search_fields = ('product',)

admin.site.register(models.Inflow, InflowsAdmin)