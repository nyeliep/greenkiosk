from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['message', 'date', 'status', 'notification_type', 'subject', 'sender_id', 'recipient_id']
