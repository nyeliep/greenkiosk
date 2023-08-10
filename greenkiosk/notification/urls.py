from django.urls import path
from .views import create_notification, notification_list

urlpatterns = [
    path('notifications/create/', create_notification, name='create_notification'),
    path('notifications/', notification_list, name='notification_list'),
]
