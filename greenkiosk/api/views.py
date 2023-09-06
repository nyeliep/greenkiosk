from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer, Product, Cart, Order
from .serializer import CustomerSerializer, CartSerializer,ProductSerializer,OrderSerializer



# Create your views here.

class CustomerListView(APIView):
      def get(self,request):
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers,many=True)
            return Response(serializer.data)

      def post(self,request):
            serializer = CustomerSerializer(data = request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
      def get(self,request,id, format=None):
            customer = Customer.objects.get(id=id)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)

      def put(self,request,id, format=None):
            customer = Customer.objects.get(id=id)
            serializer = CustomerSerializer(customer, request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)

      def delete(self,request,id, format=None):
            customer = Customer.objects.get(id=id)
            customer.delete()
            return Response("customer deleted", status = status.HTTP_204_NO_CONTENT)



# Product views
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response("Product deleted", status=status.HTTP_204_NO_CONTENT)



# Cart views
class CartListView(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartDetailView(APIView):
    def get(self, request, pk, format=None):
        cart = Cart.objects.get(pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cart = Cart.objects.get(pk=pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart = Cart.objects.get(pk=pk)
        cart.delete()
        return Response("Cart deleted", status=status.HTTP_204_NO_CONTENT)

    

# Order views
class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    def get(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response("Order deleted", status=status.HTTP_204_NO_CONTENT)
