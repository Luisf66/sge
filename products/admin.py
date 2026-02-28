from django.contrib import admin
from . import models
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'cost_price', 'selling_price', 'quantity', 'created_at', 'updated_at')
    search_fields = ('title', 'category', 'brand')

admin.site.register(models.Product, ProductsAdmin)