from django.contrib import admin
from .models import Category, Product, ProductSpecifications, Reviews, Brand


class ProductSpecificationsInline(admin.TabularInline):
    model = ProductSpecifications
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'brand', 'model', 'quantity')
    search_fields = ('name', 'brand', 'model')
    inlines = [ProductSpecificationsInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Brand)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



@admin.register(ProductSpecifications)
class ProductSpecificationsAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'value')
    search_fields = ('product__name', 'name', 'value')


admin.site.register(Reviews)