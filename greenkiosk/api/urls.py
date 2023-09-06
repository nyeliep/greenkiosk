from django.urls import path
from .views import CustomerListView,CustomerDetailView, ProductDetailView,ProductListView,CartListView,CartDetailView,OrderDetailView,OrderListView


urlpatterns = [
      path('customers/', CustomerListView.as_view(), name='customer_list_view'),

      path('customers/<int:id>/', CustomerDetailView.as_view(), name='customer_detail_view'),

      path('products/', ProductListView.as_view(), name='product_list'),
      path('products/<int:id>/', ProductDetailView.as_view(), name='product_detail'),

      path('carts/', CartListView.as_view(), name='cart_list'),
      path('carts/<int:id>/', CartDetailView.as_view(), name='cart_detail'),

      path('orders/', OrderListView.as_view(), name='order_list'),
      path('orders/<int:id>/', OrderDetailView.as_view(), name='order_detail'),



]