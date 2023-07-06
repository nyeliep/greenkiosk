from django.db import models

class Refund(models.Model):
    # cart_id = models.IntegerField()
    reason = models.CharField(max_length=200)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    processed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Refund #{self.pk} "

