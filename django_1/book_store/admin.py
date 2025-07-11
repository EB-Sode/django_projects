from django.contrib import admin
from .models import Product, Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    search_fields = ('title', 'author')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category')
    search_fields = ('price', 'name')
    list_filter = ('category',)

admin.site.register(Book, BookAdmin)
admin.site.register(Product, ProductAdmin)