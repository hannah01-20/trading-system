from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=1, decimal_places=2, max_digits=9)

class Order(models.Model):
    stock_id = models.ForeignKey(Stock, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    quantity = models.PositiveBigIntegerField(default = 1)

    def total_amount(self):
        stocks = Stock.objects.filter(id = self.stock_id)
        total = sum(stock.price for stock in stocks)

        return total