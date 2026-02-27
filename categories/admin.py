from django.contrib import admin
from . import models


# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)

admin.site.register(models.Categories, CategoriesAdmin)