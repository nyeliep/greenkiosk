from django.contrib import admin

# Register your models here.
from.models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'customer_id', 'cart_status', 'total_cost')
    list_filter = ('cart_status',)
    search_fields = ('cart_id', 'customer_id')
    readonly_fields = ('total_cost',)

    filter_horizontal = ('items',)

    fieldsets = (
        ('Cart Information', {
            'fields': ('cart_id', 'customer_id', 'cart_status')
        }),
        ('Items in Cart', {
            'fields': ('items', 'quantity')
        }),
        ('Cost Details', {
            'fields': ('total_cost',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        if obj:  # Editing an existing object
            readonly_fields.extend(['cart_id', 'customer_id'])
        return readonly_fields
admin.site.register(Cart,CartAdmin)
