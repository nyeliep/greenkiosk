from django.db import models

# Create your models here.

class Notification(models.Model):
    message = models.CharField(max_length=255)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    notification_type = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    sender_id = models.IntegerField()
    recipient_id = models.IntegerField()

    def __str__(self):
        return f"Notification {self.id}"