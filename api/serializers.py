from rest_framework.serializers import ModelSerializer
from . import models

class StockSerializer(ModelSerializer):
    class Meta:
        model = models.Stock
        fields = "__all__"