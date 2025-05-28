from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models

class StockSerializer(ModelSerializer):
    class Meta:
        model = models.Stock
        fields = "__all__"

class OrderSerializer(ModelSerializer):
    stock = StockSerializer()
    total_price = SerializerMethodField()
    class Meta:
        model = models.Order
        fields = "__all__"
    
    def get_total_price(self, obj):
        return obj.stock.price * obj.quantity
    