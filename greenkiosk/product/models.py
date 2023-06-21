from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name