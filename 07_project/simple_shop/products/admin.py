from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price_in_paisa', 'stock_quantity', 'created_at']
    list_filter = ['created_at' , ]
    search_fields = ['name' , ]
    ordering = ['-created_at' , ]

admin.site.register(Product, ProductAdmin)
