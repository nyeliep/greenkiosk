from django.urls import path
from .views import product_detail, product_list, product_upload_view, product_update_view
from . import views


urlpatterns = [
    path("products/upload/",product_upload_view,
    name="product_upload_views"),
    path("products/list",product_list, 
    name ="product_list_view"),
    path("products/<int:id>/",product_detail,
    name="product_detail_view"),
    path("products/edit/<int:id>/",product_update_view,
    name="product_update_view"),
    path('inventory/products/list', views.product_list, name='product_list'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

  
]


