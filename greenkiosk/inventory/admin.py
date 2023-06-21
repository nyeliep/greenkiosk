from django.contrib import admin

# Register your models here.
from.models import Product
class Product_admin(admin.ModelAdmin):
    list_display = ("name", "stock","price","date_created","image","date_updated","description")
admin.site.register(Product,Product_admin)
