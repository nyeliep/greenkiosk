from django.db import models
from django.contrib.auth.models import User
from vendor.models import Vendor

# Create your models here.
class Product(models.Model):
    class Meta:
        verbose_name_plural = "inventories"

    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField()


  