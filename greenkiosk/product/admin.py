from django.contrib import admin

# Register your models here.
from.models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'quantity', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    readonly_fields = ('product_id', 'date_created', 'date_updated')

    fieldsets = (
        ('Product Information', {
            'fields': ('product_id', 'name', 'category')
        }),
        ('Stock and Price', {
            'fields': ('quantity', 'price')
        }),
        ('Additional Details', {
            'fields': ('description', 'image_url')
        }),
        ('Date Information', {
            'fields': ('date_created', 'date_updated'),
            'classes': ('collapse',),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        if obj:  # Editing an existing object
            readonly_fields.append('date_created')
        return readonly_fields