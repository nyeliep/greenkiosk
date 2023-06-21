from django.contrib import admin

# Register your models here.
from.models import Notification
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'date', 'status', 'notification_type', 'subject', 'sender_id', 'recipient_id')
    list_filter = ('status', 'notification_type')
    search_fields = ('message', 'subject')

admin.site.register(Notification, NotificationAdmin)