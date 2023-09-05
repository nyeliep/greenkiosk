from django.db import models
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

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    