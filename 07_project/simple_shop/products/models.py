from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price_in_paisa = models.IntegerField(default=0)
    stock_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.name}"