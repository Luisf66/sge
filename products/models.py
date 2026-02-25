from django.db import models

from brand.models import Brand
from categories.models import Categories

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(null=True, blank=True)
    serie_number = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    selling_price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title