from django.contrib import admin

from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug'
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'slug',
        'price',
        'is_stock',
        'is_active',
        'created',
        'updated',
    )
    list_filter = (
        'is_active',
        'is_stock',
    )
    list_editable = (
        'price',
        'is_stock'
    )
    prepopulated_fields = {'slug': ('title',)}
