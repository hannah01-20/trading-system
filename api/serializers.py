from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField, ValidationError
from django.contrib.auth.models import User
from . import models

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

class UserCreationSerializer(ModelSerializer):
    re_password = CharField(write_only = True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "re_password"]
    
    def validate(self, data):
        is_exist = User.objects.filter(username = data["username"])
        if is_exist:
            raise ValidationError("Username is taken")
        
        if data["password"] != data["re_password"]:
            raise ValidationError("Password and confirm password are not match.")
        
        return data
    
    def create(self, data):
        data.pop("re_password")

        user = User.objects.create_user(**data)

        return user

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
    