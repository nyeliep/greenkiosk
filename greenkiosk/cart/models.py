from django.db import models
# from product.models import Product

# Create your models here.

class Cart(models.Model):
    customer_id = models.IntegerField()
    cart_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    items = models.ManyToManyField('product.Product')
    cart_status = models.CharField(max_length=50)
    total_cost = models.IntegerField()

    def __str__(self):
        return f"Cart {self.cart_id} - Customer {self.customer_id}"
