from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'description', 'price', 'category']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Product)
admin.site.register(Category)