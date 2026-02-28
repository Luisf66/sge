from django.contrib import admin
from . import models
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'created_at', 'updated_at')
    search_fields = ('name', 'category', 'brand')

admin.site.register(models.Product, ProductsAdmin)