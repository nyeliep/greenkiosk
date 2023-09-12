from django.db import models
from django.shortcuts import get_object_or_404, redirect
from refund.models import Refund
from django.contrib.auth.models import User
from inventory.models import Product


class Cart(models.Model):
    product_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    image = models.ImageField()
    price = models.IntegerField()
    date = models.DateTimeField()

    refund = models.ForeignKey(Refund, on_delete=models.CASCADE, null=True)

    products = models.ManyToManyField(Product)

    def add_product(self,product):
        self.products.add(product)
        self.save()
        return self

    def get_total(self):
        products = self.products.all()
        total = 0
        for product in products:
            total += product.price
            return total
     




class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
