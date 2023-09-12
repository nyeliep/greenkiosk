from rest_framework import serializers
from customer.models import Customer
from cart.models import Cart
from product.models import Product
from order.models import Order



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many = True)
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

