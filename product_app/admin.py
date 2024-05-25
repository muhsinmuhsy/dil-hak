from django.contrib import admin
from .models import Category, Product, Size, ColorImage, Color, ProductVariant

# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    
@admin.register(ProductVariant)
class ProductVariantModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductVariant._meta.fields]
    
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    
@admin.register(Size)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Size._meta.fields]
    
@admin.register(ColorImage)
class ColorImageModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ColorImage._meta.fields]
    
@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Color._meta.fields]