from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=1, decimal_places=2, max_digits=9)

class Order(models.Model):
    stock = models.ForeignKey(Stock, related_name = "order", verbose_name="stock", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = "order", verbose_name="user", on_delete = models.CASCADE)
    quantity = models.PositiveBigIntegerField(default = 1)
