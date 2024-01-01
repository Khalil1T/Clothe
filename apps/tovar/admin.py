from django.contrib import admin
from .models import Category, Product, ProductSpecifications, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductSpecificationsInline(admin.TabularInline):
    model = ProductSpecifications
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'brand', 'model', 'quantity')
    search_fields = ('name', 'brand', 'model')
    inlines = [ProductImageInline, ProductSpecificationsInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ProductSpecifications)
class ProductSpecificationsAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'value')
    search_fields = ('product__name', 'name', 'value')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('product__name', 'image')


