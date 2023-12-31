from django.urls import path
from .views import create_delivery, edit_delivery, delivery_list, delivery_detail, delivery_confirmation_view

urlpatterns = [
    path('deliveries/create/', create_delivery, name='create_delivery'),
    path('deliveries/<int:delivery_id>/edit/', edit_delivery, name='edit_delivery'),
    path('deliveries/', delivery_list, name='delivery_list'),
    path('deliveries/<int:delivery_id>/', delivery_detail, name='delivery_detail'),
    path('delivery_confirmation/', delivery_confirmation_view, name='delivery_confirmation_view'),
]

