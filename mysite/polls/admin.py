from django.contrib import admin

# Register your models here.
from .models import Product


class productview(admin.ModelAdmin):
    list_display = ('product_id', 'product_name',
                    'publish_date', 'product_price', 'product_available', 'product_quantity', 'product_price')
    list_filter = ('publish_date',)
    search_fields = ('product_name',)


admin.site.register(Product, productview)
