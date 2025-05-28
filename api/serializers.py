from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.contrib.auth.models import User
from . import models

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class StockSerializer(ModelSerializer):
    class Meta:
        model = models.Stock
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"
    

class OrderDetailsSerializer(ModelSerializer):
    stock = StockSerializer()
    total_price = SerializerMethodField()
    user = UserSerializer()
    class Meta:
        model = models.Order
        fields = "__all__"
    
    def get_total_price(self, obj):
        return obj.stock.price * obj.quantity
    