from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Stock
from ..serializers import StockSerializer

class StockView(APIView):
    def get(self, request):
        
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)

        return Response(serializer.data)